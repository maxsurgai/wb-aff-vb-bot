from src.models.firebase import Db
from datetime import datetime

class Chat:
    def __init__(self, chat=None, id=None, chat_data=None):
        self.db = Db()
        if chat_data and isinstance(chat_data, dict):
            self.id = chat_data['id'] if 'id' in chat_data else 0
            self.username = chat_data['username'] if 'username' in chat_data else ''
            self.start_date = chat_data['start_date'] if 'start_date' in chat_data else ''
            self.app = chat_data['app'] if chat_data.get('app') else 'viber'
            self.__step = chat_data['step'] if 'step' in chat_data else ''
            self.__email = chat_data['email'] if 'email' in chat_data else ''
            self.__language = chat_data['language'] if 'language' in chat_data else 'en'
            self.__referrer = chat_data['referrer'] if 'referrer' in chat_data else ''
            self.__referral_code = chat_data['referral_code'] if 'referral_code' in chat_data else ''
            self.__ref_activate_date = chat_data['ref_activate_date'] if 'ref_activate_date' in chat_data else ''
            self.__refs_num = chat_data['refs_num'] if 'refs_num' in chat_data else 0
            self.__utm_source = chat_data['utm_source'] if 'utm_source' in chat_data else ''
            self.__utm_medium = chat_data['utm_medium'] if 'utm_medium' in chat_data else ''
            self.__utm_campaign = chat_data['utm_campaign'] if 'utm_campaign' in chat_data else ''
            self.__utm_id = chat_data['utm_id'] if 'utm_id' in chat_data else ''
            self.__utm_creo = chat_data['utm_creo'] if 'utm_creo' in chat_data else ''
        else:
            self.id = chat.id if chat else id if id else 0
            self.username = chat.username if chat else ''
            self.start_date = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
            self.app = 'viber'
            self.__step = ''
            self.__email = ''
            self.__language = 'en'
            self.__referrer = ''
            self.__referral_code = ''
            self.__ref_activate_date = ''
            self.__refs_num = 0
            self.__utm_source = ''
            self.__utm_medium = ''
            self.__utm_campaign = ''
            self.__utm_id = ''
            self.__utm_creo = ''
            self.fetch()

    @property
    def step(self):
        return self.__step

    @step.setter
    def step(self, step):
        self.__step = step
        self.db.set_chat_key_value(self.id, 'step', step)

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email
        self.db.set_chat_key_value(self.id, 'email', email)
        self.db.set_chat_id_by_email(self.id, email)

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language):
        self.__language = language
        self.db.set_chat_key_value(self.id, 'language', language)

    @property
    def referrer(self):
        return self.__referrer

    @referrer.setter
    def referrer(self, referrer):
        self.__referrer = referrer
        self.db.set_chat_key_value(self.id, 'referrer', referrer)
        if referrer != '':
            self.db.add_new_referral(referrer, referral=str(self.id))
            referrer_chat = Chat(id=self.db.get_chat_id_by_referral_code(referrer))
            referrer_chat.refs_num += 1

    @property
    def referral_code(self):
        return self.__referral_code

    @referral_code.setter
    def referral_code(self, referral_code):
        self.__referral_code = referral_code
        self.db.set_chat_key_value(self.id, 'referral_code', referral_code)
        self.ref_activate_date = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        self.db.set_chat_id_by_referral_code(self.id, referral_code)
        self.db.set_email_by_referral_code(self.email, referral_code)

    @property
    def ref_activate_date(self):
        return self.__ref_activate_date

    @ref_activate_date.setter
    def ref_activate_date(self, ref_activate_date):
        self.__ref_activate_date = ref_activate_date
        self.db.set_chat_key_value(self.id, 'ref_activate_date', ref_activate_date)

    @property
    def refs_num(self):
        return self.__refs_num

    @refs_num.setter
    def refs_num(self, refs_num):
        self.__refs_num = refs_num
        self.db.set_chat_key_value(self.id, 'refs_num', refs_num)

    @property
    def utm_source(self):
        return self.__utm_source

    @utm_source.setter
    def utm_source(self, utm_source):
        self.__utm_source = utm_source
        self.db.set_chat_key_value(self.id, 'utm_source', utm_source)

    @property
    def utm_medium(self):
        return self.__utm_medium

    @utm_medium.setter
    def utm_medium(self, utm_medium):
        self.__utm_medium = utm_medium
        self.db.set_chat_key_value(self.id, 'utm_medium', utm_medium)

    @property
    def utm_campaign(self):
        return self.__utm_campaign

    @utm_campaign.setter
    def utm_campaign(self, utm_campaign):
        self.__utm_campaign = utm_campaign
        self.db.set_chat_key_value(self.id, 'utm_campaign', utm_campaign)

    @property
    def utm_id(self):
        return self.__utm_id

    @utm_id.setter
    def utm_id(self, utm_id):
        self.__utm_id = utm_id
        self.db.set_chat_key_value(self.id, 'utm_id', utm_id)

    @property
    def utm_creo(self):
        return self.__utm_creo

    @utm_creo.setter
    def utm_creo(self, utm_creo):
        self.__utm_creo = utm_creo
        self.db.set_chat_key_value(self.id, 'utm_creo', utm_creo)

    def fetch(self):
        chat_data = self.db.get_chat(self.id)
        if isinstance(chat_data, dict):
            self.username = chat_data['username'] if 'username' in chat_data else self.username
            self.start_date = chat_data['start_date'] if 'start_date' in chat_data else self.start_date
            self.__step = chat_data['step'] if 'step' in chat_data else self.__step
            self.__email = chat_data['email'] if 'email' in chat_data else self.__email
            self.__language = chat_data['language'] if 'language' in chat_data else self.__language
            self.__referrer = chat_data['referrer'] if 'referrer' in chat_data else self.__referrer
            self.__referral_code = chat_data['referral_code'] if 'referral_code' in chat_data else self.__referral_code
            self.__ref_activate_date = chat_data['ref_activate_date'] if 'ref_activate_date' in chat_data else self.__ref_activate_date
            self.__refs_num = chat_data['refs_num'] if 'refs_num' in chat_data else self.__refs_num
            self.__utm_source = chat_data['utm_source'] if 'utm_source' in chat_data else self.__utm_source
            self.__utm_medium = chat_data['utm_medium'] if 'utm_medium' in chat_data else self.__utm_medium
            self.__utm_campaign = chat_data['utm_campaign'] if 'utm_campaign' in chat_data else self.__utm_campaign
            self.__utm_id = chat_data['utm_id'] if 'utm_id' in chat_data else self.__utm_id
            self.__utm_creo = chat_data['utm_creo'] if 'utm_creo' in chat_data else self.__utm_creo
        else:
            self.db.add_chat(self)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'step': self.step,
            'app': self.app,
            'email': self.email,
            'start_date': self.start_date,
            'language': self.language,
            'referrer': self.referrer,
            'referral_code': self.referral_code,
            'ref_activate_date': self.ref_activate_date,
            'refs_num': self.refs_num,
            'utm_source': self.utm_source,
            'utm_medium': self.utm_medium,
            'utm_campaign': self.utm_campaign,
            'utm_id': self.utm_id,
            'utm_creo': self.utm_creo
        }

    def track_utm_stats(self):
        # date = self.start_date.split(',')[0]
        # utm = self.utm_source+'__'+self.utm_medium+'__'+self.utm_campaign
        # stats = self.db.get_utm_stats_by_date(date, utm)
        # self.db.set_utm_stats_by_date(date, utm, stats+1 if stats is not None and type(stats) is int else 1)
        stats = self.db.get_utm_stats(self.utm_campaign)
        self.db.set_utm_stats(self.utm_campaign, stats+1 if stats is not None and type(stats) is int else 1)

    def referrer_email(self) -> str:
        return self.db.get_email_by_referral_code(self.referrer) if self.referrer != '' else ''

    def step_num(self) -> int:
        if type(self.step) is int or self.start_date == '':
            return 8
        if self.refs_num > 0:
            return 7
        elif self.referral_code != '':
            return 6
        elif 'ref' in self.step or 'withdraw' in self.step:
            return 5
        elif self.email != '':
            return 4
        elif 'email' in self.step:
            return 3
        elif 'kyc' in self.step:
            return 2
        elif 'reg' in self.step or 'hi' in self.step:
            return 1
        else:
            return 8

