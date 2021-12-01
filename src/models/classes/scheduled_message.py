from src.models.firebase import Db
import time


class ScheduledMessage:
    def __init__(self, data=None, name='', text='', delay_sec=60, chat_id=0, step='', lang='en', timestamp=None):
        if data and isinstance(data, dict):
            self.name = data['name'] if 'name' in data else ''
            self.text = data['text'] if 'text' in data else ''
            self.timestamp = data['timestamp'] if 'timestamp' in data else str(0)
            self.delay_sec = data['delay_sec'] if 'delay_sec' in data else 60
            self.chat_id = data['chat_id'] if 'chat_id' in data else '0'
            self.step = str(data['step']) if 'step' in data else ''
            self.lang = data['lang'] if 'lang' in data else lang
            self.id = data['id'] if 'id' in data else str(self.chat_id) + self.name + str(self.step)
            self.app = 'viber'
        else:
            self.name = name
            self.text = text
            self.delay_sec = delay_sec
            self.chat_id = str(chat_id)
            self.step = str(step)
            self.lang = lang
            self.id = self.chat_id + self.name + str(self.step)
            self.timestamp = timestamp if timestamp else str(time.time_ns())
            self.app = 'viber'
        self.db = Db()

    def start(self):
        self.db.add_scheduled_message(self)

    def finish(self):
        self.db.remove_scheduled_message(self)

    def to_dict(self):
        return {
            'name': self.name,
            'timestamp': self.timestamp,
            'delay_sec': self.delay_sec,
            'chat_id': self.chat_id,
            'step': self.step,
            'text': self.text,
            'lang': self.lang,
            'app': self.app
        }

