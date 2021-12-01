from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from src.models.classes.config import Config
import json
import os


config = Config()
bot = Api(BotConfiguration(
    name='WhiteBIT Affiliate Bot',
    avatar='',
    auth_token=config.token
))


def get_ngrok_address():
    os.system("curl  http://localhost:4040/api/tunnels > tunnels.json")
    with open('tunnels.json') as data_file:
        datajson = json.load(data_file)
    return dict(zip(['https', 'http'], [i['public_url'] for i in datajson['tunnels']]))


bot.set_webhook(get_ngrok_address()['https'])
# bot.set_webhook('https://whitebot.xyz/viber')

