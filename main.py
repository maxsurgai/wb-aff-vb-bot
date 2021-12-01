# -*- coding: utf-8 -*-

from flask import Flask, request, Response, jsonify
from telebot import TeleBot

from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
import logging

from viberbot.api.viber_requests import ViberConversationStartedRequest
from viberbot.api.viber_requests import ViberFailedRequest
from viberbot.api.viber_requests import ViberMessageRequest
from viberbot.api.viber_requests import ViberSubscribedRequest
from viberbot.api.viber_requests import ViberUnsubscribedRequest

from src.models.firebase import Db
from src.models.classes.config import Config
from src.scripts.script_bot_polling import ScriptBotPolling

app = Flask(__name__)
config = Config()
bot = Api(BotConfiguration(
    name='WhiteBIT Affiliate Bot',
    avatar='',
    auth_token=config.token
))

db = Db()
bot_controller = ScriptBotPolling(bot, db)
tg_bot = TeleBot(config.tg_bot_token)


@app.route('/', methods=['GET'])
def hello():
    return 'fakamazafaka'


@app.route('/', methods=['POST'])
def receive_message():
    if not bot.verify_signature(request.get_data(), request.headers.get('X-Viber-Content-Signature')):
        return Response(status=403)

    user_request = bot.parse_request(request.get_data())
    print(user_request)

    if isinstance(user_request, ViberMessageRequest):
        if user_request.message.tracking_data is not None or user_request.message.text == 'support' or 'step_' in user_request.message.text or 'stats' in user_request.message.text:
            bot_controller.postback(user_request)
        else:
            bot_controller.get_message(user_request)

    elif isinstance(user_request, ViberConversationStartedRequest):
        if bot_controller.start(user_request) == 'welcome':
            welcome_message_data = {
                "sender": {
                    "name": 'WhiteBIT Affiliate Bot',
                    "avatar": ""
                },
                "tracking_data": "start",
                "type": "text",
                "text": config.messages['lang'],
                "keyboard": {"Type": "keyboard", "DefaultHeight": True,
                        "Buttons": [
                            {"ActionType": "reply", "ActionBody": "lang_en", "Text": "English",
                             "TextSize": "regular"},
                            {"ActionType": "reply", "ActionBody": "lang_ru", "Text": "Русский",
                             "TextSize": "regular"},
                            {"ActionType": "reply", "ActionBody": "lang_ua", "Text": "Українська",
                             "TextSize": "regular"}
                        ]
                }
            }
            return jsonify(welcome_message_data)

    elif isinstance(user_request, ViberFailedRequest):
        tg_bot.send_message(config.papka_admin_id, text="client failed receiving message. failure: {0}".format(user_request))

    return Response(status=200)


if __name__ == '__main__':
    app.run()
