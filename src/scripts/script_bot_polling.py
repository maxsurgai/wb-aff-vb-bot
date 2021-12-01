import traceback
import urllib

from viberbot import Api
from viberbot.api.viber_requests import ViberMessageRequest
from viberbot.api.viber_requests import ViberConversationStartedRequest
from viberbot.api.messages.text_message import TextMessage
from viberbot.api.messages.picture_message import PictureMessage
from viberbot.api.messages.video_message import VideoMessage
from viberbot.api.messages.rich_media_message import RichMediaMessage

from src.models.classes.chat import Chat
from src.models.classes.config import Config
from src.models.firebase import Db
from src.models.classes.scheduled_message import ScheduledMessage

from telebot import TeleBot
import json

tg_bot = TeleBot(Config().tg_bot_token)


class ScriptBotPolling:
    def __init__(self, bot: Api, db: Db):
        self.bot = bot
        self.db = db
        self.config = Config()

    def start(self, request: ViberConversationStartedRequest):
        chat = Chat(id=request.user.id)
        if chat.step != '':
            return
        # param = request.event_type
        # if param is not None:
        #     if param.startswith('tgbot_'):
        #         chat.referrer = param.replace('tgbot_', '')
        #         chat.utm_source = 'messenger'
        #         chat.utm_medium = 'bot'
        #         chat.utm_campaign = 'referral'
        #     else:
        #         utms = param.split('__')
        #         for utm in utms:
        #             key = utm.split('-', maxsplit=1)[0]
        #             value = utm.split('-', maxsplit=1)[1]
        #             if 'src' in key or 'utm_source' in key:
        #                 chat.utm_source = value
        #             elif 'mdm' in key or 'utm_medium' in key:
        #                 chat.utm_medium = value
        #             elif 'cmpg' in key or 'utm_campaign' in key:
        #                 chat.utm_campaign = value
        #             elif 'id' in key:
        #                 chat.utm_id = value
        #             elif 'creo' in key:
        #                 chat.utm_creo = value
        #             else:
        #                 continue
        #         chat.track_utm_stats()
        self.send_step(chat, step='lang')
        return 'welcome'

    def postback(self, request: ViberMessageRequest):
        chat = Chat(id=request.sender.id)
        payload = request.message.text
        
        if payload == 'support':
            self.send_help(chat)
            self.clear_scheduled_message(chat.id, 'motivashka', chat.step)

        elif 'lang' in payload:
            chat.language = payload.split('_')[1]
            self.send_step(chat, step='hi')

        elif 'step' in payload:
            step = payload.split('_')[1]
            self.clear_scheduled_message(chat.id, 'motivashka', step)
            if step == 'reg':
                self.send_step(chat, 'kyc')
            elif step == 'kyc':
                self.send_step(chat, 'email')
            elif step == 'approve':
                self.send_step(chat, 'activation')
            elif step == 'activation':
                self.send_step(chat, 'withdraw')

        elif 'stats' in payload:
            return self.bot.send_messages(chat.id, TextMessage(text=self.config.messages['stats'][chat.language][1] + str(chat.refs_num)))

        return

    def get_message(self, request: ViberMessageRequest):
        chat = Chat(id=request.sender.id)
        message_text = request.message.text

        if chat.step == 'email':
            if '@' in message_text:
                email = message_text.translate({ord(c): "" for c in "!#$%^&*()[]{};:/<>?\|`~-=_+ "})
                if chat.email != email and self.db.get_chat_id_by_email(email) is not None:
                    self.bot.send_messages(chat.id, TextMessage(text=self.config.messages[chat.step][chat.language][1]))
                else:
                    # if chat.email != email:
                    #     self.bot.send_messages(self.config.admin_chat_id, email)
                    chat.email = email
                    return self.send_step(chat, 'approve')
            else:
                self.bot.send_messages(chat.id, TextMessage(text=self.config.messages[chat.step][chat.language][1]))

        elif chat.step == 'ref':
            if 'referral/' in message_text:
                self.clear_scheduled_message(chat.id, 'motivashka', chat.step)
                referral_code = message_text.strip('/').split('/')[-1]
                if (chat.referral_code != referral_code and self.db.get_user_referrals(referral_code) is not None) or \
                        chat.referrer == referral_code or \
                        len(referral_code) < 32:
                    self.bot.send_messages(chat.id, TextMessage(text=self.config.messages[chat.step][chat.language][1]))
                else:
                    # if chat.referral_code != referral_code:
                    #     self.bot.send_messages(self.config.admin_chat_id,
                    #                      "user " + referral_code + " activate referral program")
                    chat.referral_code = referral_code
                    return self.send_step(chat, step='ref_activate')
            else:
                self.bot.send_messages(chat.id, TextMessage(text=self.config.messages[chat.step][chat.language][1]))

        #  входящее сообщение на любом этапе
        self.send_help(chat)

    def send_step(self, chat: Chat, step):
        chat.step = step

        if step == 'lang':
            return
            # keyboard = {"Type": "keyboard", "DefaultHeight": True,
            #     "Buttons": [
            #         {"ActionType": "reply", "ActionBody": "lang_en", "Text": "English", "TextSize": "regular"},
            #         {"ActionType": "reply", "ActionBody": "lang_ru", "Text": "Русский", "TextSize": "regular"},
            #         {"ActionType": "reply", "ActionBody": "lang_ua", "Text": "Українська", "TextSize": "regular"}
            #     ]
            # }
            # self.bot.send_messages(chat.id, TextMessage(tracking_data=step, text=self.config.messages[step], keyboard=keyboard))

        elif step == 'hi':
            self.bot.send_messages(chat.id, TextMessage(text=self.config.messages[step][chat.language]))
            self.send_step(chat, step='reg')

        elif step == 'reg':
            self.bot.send_messages(chat.id, TextMessage(text=self.config.messages[step][chat.language][0] + self.config.messages[step]['link'][
                    0 if chat.referrer == '' else 1].replace('referrer', chat.referrer) + (
                        ('utm_source=' + chat.utm_source) if chat.utm_source != '' else '') + (('&utm_medium=' + chat.utm_medium) if chat.utm_medium != '' else '') + (('&utm_campaign=' + chat.utm_campaign) if chat.utm_campaign != '' else '') + (('&utm_id=' + chat.utm_id) if chat.utm_id != '' else '') + (('&utm_creo=' + chat.utm_creo) if chat.utm_creo != '' else '')))
            self.bot.send_messages(chat.id, VideoMessage(media=self.config.media_url[step][chat.language], text=self.config.messages[step][chat.language][1], size=1))
            ScheduledMessage(
                name='ask_if_done',
                chat_id=chat.id,
                delay_sec=30,
                step=step,
                lang=chat.language
            ).start()

        elif step == 'kyc':
            self.bot.send_messages(chat.id, VideoMessage(media=self.config.media_url[step][chat.language], text=self.config.messages[step][chat.language], size=1))
            ScheduledMessage(
                name='ask_if_done',
                chat_id=chat.id,
                delay_sec=30,
                step=step,
                lang=chat.language
            ).start()

        elif step == 'email':
            self.bot.send_messages(chat.id, TextMessage(text=self.config.messages[step][chat.language][0]))

        elif step == 'approve':
            self.bot.send_messages(chat.id, TextMessage(tracking_data=step, text=self.config.messages[step][chat.language].replace('example@mail.ru', chat.email)))
            self.bot.send_messages(chat.id, RichMediaMessage(tracking_data='stats',
                rich_media={
                    "Type": "rich_media",
                    "ButtonsGroupColumns": 3,
                    "ButtonsGroupRows": 1,
                    "Buttons": [
                        {"ActionType": "reply", "ActionBody": 'step_'+step+'_y', "Text": self.config.messages[step]['btns'][chat.language][0]},
                        {"ActionType": "reply", "ActionBody": "support", "Text": self.config.messages[step]['btns'][chat.language][1]}
                    ]}, min_api_version=2))

        elif step == 'activation':
            self.bot.send_messages(chat.id, [
                PictureMessage(media=self.config.media_url[step][chat.language][0]),
                PictureMessage(media=self.config.media_url[step][chat.language][1], text=self.config.messages[step][chat.language][0])
            ])
            ScheduledMessage(
                name='ask_if_done',
                chat_id=chat.id,
                delay_sec=60,
                step=step,
                lang=chat.language
            ).start()

        elif step == 'withdraw':
            self.bot.send_messages(chat.id, [
                VideoMessage(media=self.config.media_url[step][chat.language], text=self.config.messages[step][chat.language], size=1),
            ])
            # self.bot.send_messages(chat.id, TextMessage(text=self.config.messages[step][chat.language]))
            # self.send_step_attachment(chat)
            # ScheduledMessage(
            #     name='send_attachment',
            #     text=self.config.attachment_id[chat.step][chat.language],
            #     chat_id=chat.id,
            #     delay_sec=1).start()

            ScheduledMessage(
                name='send_step',
                text='ref',
                chat_id=chat.id,
                delay_sec=60,
                step=step,
                lang=chat.language
            ).start()

        # elif step == 'ref':
        #     if chat.referrer == '':
        #         self.bot.send_messages(chat.id, self.config.messages[step][chat.language][0])
        #     else:
        #         self.bot.send_messages(chat.id, self.config.messages[step][chat.language][1])
        #         # media
        #         self.bot.send_messages(chat.id, self.config.messages[step][chat.language][2])
        #     self.bot.forward_message(chat.id, self.config.assets_chat_id, self.config.ref_ua_msg_id if chat.language == 'ua' else self.config.ref_ru_msg_id if chat.language == 'ru' else self.config.ref_en_msg_id)

        elif step == 'ref_activate':
            self.bot.send_messages(chat.id, TextMessage(tracking_data=step, text='https://www.viber.com/whitebitaffiliatebot?ref=bot_' + chat.referral_code + '\n\n' +
                             self.config.messages[step][chat.language]))
            self.bot.send_messages(chat.id, RichMediaMessage(tracking_data='stats',
                rich_media={
                    "Type": "rich_media",
                    "ButtonsGroupColumns": 3,
                    "ButtonsGroupRows": 1,
                    "Buttons": [
                        {"ActionType": "reply", "ActionBody": "stats", "Text": self.config.messages['stats'][chat.language][0]}
                    ]}, min_api_version=2))

        return

    # def admin_command(self, chat, message):
    #     cmd = message.caption if message['photo'] else message['text']
    #     if 'пуш' in cmd.split()[0]:
    #         step = cmd.split()[0].replace('пуш', '').replace('ру', '').replace('юа', '').replace('ен', '')
    #         step = int(step) if step != '' else None
    #         language = 'ru' if 'ру' in cmd else 'ua' if 'юа' in cmd else 'en' if 'ен' in cmd else None
    #         text = cmd.replace(cmd.split()[0], '')
    #         # if len(message['photo']) > 0:
    #         #     f = open('push.jpg', 'wb')
    #         #     f.write(urllib.request.urlopen(
    #         #         self.bot.get_file_url(file_id=message['photo'][len(message.photo) - 1].file_id)).read())
    #         #     f.close()
    #
    #         chats = self.db.get_all_chats()
    #         for chat_id in chats:
    #             user_chat = Chat(chat_data=chats[chat_id])
    #             if user_chat.id == 0 or \
    #                     user_chat.id == self.config.admin_chat_id or \
    #                     (language is not None and language != user_chat.language) or \
    #                     (step is not None and step != user_chat.step_num()):
    #                 continue
    #             ScheduledMessage(
    #                 name='push_photo' if len(message.photo) > 0 else 'push',
    #                 delay_sec=1,
    #                 chat_id=user_chat.id,
    #                 text=text
    #             ).start()
    #
    #     elif 'таблица' in cmd.split()[0]:
    #         ScheduledMessage(
    #             name='table',
    #             delay_sec=1,
    #             chat_id=chat.id
    #         ).start()
    #
    #     elif 'стата' in cmd.split()[0]:
    #         ScheduledMessage(
    #             name='stats',
    #             delay_sec=1,
    #             chat_id=chat.id,
    #             text='ютм' if 'ютм' in cmd else ''
    #         ).start()
    #
    #     return

    def send_help(self, chat):
        self.bot.send_messages(chat.id, TextMessage(text=self.config.messages['support'][chat.language]))

    def clear_scheduled_message(self, chat_id, name, step):
        ScheduledMessage(data=self.db.get_scheduled_message(str(chat_id) + name + str(step))).finish()

