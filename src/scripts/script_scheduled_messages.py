import telebot
from telebot import types
import time
from datetime import datetime, timedelta
import random
import csv
from src.models.classes.chat import Chat
from src.models.classes.config import Config
from src.models.firebase import Db
from src.models.classes.scheduled_message import ScheduledMessage

FETCH_DATA_DELAY_SEC = 5
LOOP_DELAY_SEC = 1


class ScriptScheduledMessages:
    def __init__(self, bot: telebot.TeleBot, db: Db):
        self.bot = bot
        self.db = db
        self.config = Config()
        self.loop()

    def ask_if_done(self, scheduled_message: ScheduledMessage):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(
            types.InlineKeyboardButton(text=self.config.messages['yes'][scheduled_message.lang], callback_data='step_'+scheduled_message.step+'_y'),
            types.InlineKeyboardButton(text=self.config.messages['no'][scheduled_message.lang], callback_data='support'))
        self.bot.send_message(scheduled_message.chat_id,
                              text=self.config.messages[scheduled_message.step]['ask_if_done'][scheduled_message.lang],
                              reply_markup=keyboard)
        ScheduledMessage(
            name='motivashka',
            delay_sec=60 * 30,
            chat_id=scheduled_message.chat_id,
            step=scheduled_message.step,
            lang=scheduled_message.lang,
            text='0'
        ).start()

    def send_step(self, scheduled_message: ScheduledMessage):
        step = scheduled_message.text
        self.db.set_chat_key_value(scheduled_message.chat_id, 'step', step)
        if step == 'ref':
            self.bot.forward_message(scheduled_message.chat_id,
                                     self.config.assets_chat_id,
                                     self.config.assets_message_id[step][scheduled_message.lang])
            self.bot.send_message(scheduled_message.chat_id,
                                  text=self.config.messages[step][scheduled_message.lang])
            ScheduledMessage(
                name='motivashka',
                delay_sec=60 * 30,
                chat_id=scheduled_message.chat_id,
                step=step,
                lang=scheduled_message.lang,
                text='0'
            ).start()

    def motivashka(self, scheduled_message: ScheduledMessage):
        msg_num = int(scheduled_message.text)
        msg = self.config.messages[scheduled_message.step]['motivashka'][scheduled_message.lang][msg_num]
        self.bot.send_message(scheduled_message.chat_id, text=msg.replace('#video', ''), parse_mode='HTML')
        if '#video' in msg:
            self.bot.forward_message(scheduled_message.chat_id,
                                     self.config.assets_chat_id,
                                     self.config.assets_message_id[scheduled_message.step][scheduled_message.lang])
        msg_num += 1
        if msg_num <= 2:
            ScheduledMessage(
                name='motivashka',
                delay_sec=60 * 60 * 2 * (1 if msg_num < 2 else 6),
                chat_id=scheduled_message.chat_id,
                step=scheduled_message.step,
                lang=scheduled_message.lang,
                text=str(msg_num)
            ).start()

    def table(self, scheduled_message: ScheduledMessage):
        chats = self.db.get_all_chats()
        stats_data = [
            ['tg id', 'Bot activate date', 'Date activate referral program', 'email', 'referral', 'user', 'referral activate bot']
        ]
        for chat_id in chats:
            user = Chat(chat_data=chats[chat_id])
            if user.step_num() == 8:
                continue
            ref_email = user.referrer_email()
            stats_data.append([
                user.id,
                user.start_date,
                user.ref_activate_date,
                user.email,
                ref_email if ref_email is not None else user.referrer,
                user.referral_code,
                user.refs_num
            ])
        stats_file = open('stats.csv', 'w')
        writer = csv.writer(stats_file)
        writer.writerows(stats_data)
        stats_file.close()
        stats_file = open('stats.csv', 'rb')
        self.bot.send_document(scheduled_message.chat_id, stats_file)
        stats_file.close()

    def stats(self, scheduled_message: ScheduledMessage):
        chats = self.db.get_all_chats()

        if scheduled_message.text == 'ютм':
            stats_msg_text = ''
            utm_stats_by_date = self.db.get_all_utm_stats()
            total_stats_by_utm = {}

            for date in utm_stats_by_date:
                need_daily_stats = False
                if date == (datetime.now() - timedelta(1)).strftime("%d-%m-%Y") or \
                        date == datetime.now().strftime("%d-%m-%Y"):
                    stats_msg_text += date + '\n\n'
                    need_daily_stats = True

                for utm in utm_stats_by_date[date]:
                    total_stats_by_utm[utm] = total_stats_by_utm[utm] + utm_stats_by_date[date][utm] if utm in total_stats_by_utm else utm_stats_by_date[date][utm]
                    if need_daily_stats:
                        stats_msg_text += utm + ': ' + str(utm_stats_by_date[date][utm]) + ' чел\n'

                if need_daily_stats:
                    stats_msg_text += '\n\n'

            stats_msg_text += 'Олтайм\n\n'
            for utm in total_stats_by_utm:
                stats_msg_text += utm + ': ' + str(total_stats_by_utm[utm]) + ' чел\n'
            return self.bot.send_message(scheduled_message.chat_id, text=stats_msg_text)

        chats_count_by_step = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for chat_id in chats:
            user_chat = Chat(chat_data=chats[chat_id])
            chats_count_by_step[user_chat.step_num()] += 1
            # if user_chat.step_num() == 4:
            #     self.bot.send_message(scheduled_message.chat_id, text=user_chat.id)
        self.bot.send_message(scheduled_message.chat_id,
                         "Шаг 0 (не выбрали язык): " + str(
                             chats_count_by_step[0]) + " чел\n" \
                                                       "Шаг 1 (не зарегались): " + str(
                             chats_count_by_step[1]) + " чел\n" \
                                                       "Шаг 2 (зарегались, ждём кус): " + str(
                             chats_count_by_step[2]) + " чел\n" \
                                                       "Шаг 3 (кус есть, ждём имейл): " + str(
                             chats_count_by_step[3]) + " чел\n" \
                                                       "Шаг 4 (имейл есть, ждут код): " + str(
                             chats_count_by_step[4]) + " чел\n" \
                                                       "Шаг 5 (код получили, ждём рефку): " + str(
                             chats_count_by_step[5]) + " чел\n" \
                                                       "Шаг 6 (рефка есть без рефов): " + str(
                             chats_count_by_step[6]) + " чел\n" \
                                                       "Шаг 7 (супермозг, есть рефы): " + str(
                             chats_count_by_step[7]) + " чел\n"
                         )

    def push(self, scheduled_message: ScheduledMessage):
        self.bot.send_message(chat_id=scheduled_message.chat_id, text=scheduled_message.text)

    def push_photo(self, scheduled_message: ScheduledMessage):
        photo = open('push.jpg', 'rb')
        self.bot.send_photo(chat_id=scheduled_message.chat_id, photo=photo, caption=scheduled_message.text)
        photo.close()

    def loop(self):
        sec = 0
        scheduled_messages = []

        while True:
            time.sleep(LOOP_DELAY_SEC)
            sec += LOOP_DELAY_SEC

            # fetch data each x sec
            if sec >= FETCH_DATA_DELAY_SEC:
                sec = 0
                scheduled_messages.clear()
                raw_scheduled_messages = self.db.get_all_scheduled_messages()
                if raw_scheduled_messages is None:
                    continue
                for idx in raw_scheduled_messages:
                    scheduled_messages.append(ScheduledMessage(data=raw_scheduled_messages[idx]))

            for idx, scheduled_message in enumerate(scheduled_messages):
                if int((time.time_ns() - float(
                        scheduled_message.timestamp)) / 1000000000) > scheduled_message.delay_sec:
                    try:
                        scheduled_message.finish()
                        scheduled_messages.pop(idx)
                        getattr(ScriptScheduledMessages, scheduled_message.name)(self, scheduled_message=scheduled_message)
                    except telebot.apihelper.ApiException:
                        pass


