from src.models.classes.config import Config
import firebase_admin
from firebase_admin import credentials, db
from google.cloud import storage
from google.oauth2 import service_account
import datetime
import re


class Db:
    def __init__(self):
        self.config = Config()

        try:
            cred = credentials.Certificate("./key.json")
            firebase_admin.initialize_app(cred, {'databaseURL': 'https://' + self.config.firebase_db_name + '.' + self.config.firebase_db_region + '.firebasedatabase.app/'})
        except ValueError:
            pass

    # Chats
    def add_chat(self, chat) -> str:
        return db.reference('chats').child(str(chat.id)).set(chat.to_dict())

    def get_chat(self, chat_id):
        return db.reference('chats/'+str(chat_id)).get()

    def get_all_chats(self):
        return db.reference('chats').get()

    def update_chat(self, chat):
        if chat.id:
            db.reference('chats/'+str(chat.id)).update(chat.to_dict())

    def set_chat_key_value(self, chat_id, key, value):
        if chat_id and len(key) > 0:
            db.reference('chats/'+str(chat_id)+'/'+key).set(value)

    def set_chat_id_by_email(self, chat_id, email):
        db.reference('chats_by_email/'+re.sub('[^a-zA-Z0-9]', '', email)).set(str(chat_id))

    def get_chat_id_by_email(self, email):
        if email and len(email) > 0:
            return db.reference('chats_by_email/'+re.sub('[^a-zA-Z0-9]', '', email)).get()

    def set_chat_id_by_referral_code(self, chat_id, referral_code):
        db.reference('chats_by_referral_code/'+referral_code).set(str(chat_id))

    def get_chat_id_by_referral_code(self, referral_code):
        if referral_code and len(referral_code) > 0:
            return db.reference('chats_by_referral_code/'+referral_code).get()

    def set_email_by_referral_code(self, email, referral_code):
        db.reference('emails_by_referral_code/'+referral_code).set(email)

    def get_email_by_referral_code(self, referral_code):
        if referral_code and len(referral_code) > 0:
            return db.reference('emails_by_referral_code/'+referral_code).get()

    def add_new_referral(self, referrer, referral):
        db.reference('users_refs/'+referrer).push({referral: referral})

    def get_user_referrals(self, user_referral_code):
        return db.reference('users_refs/'+user_referral_code).get()

    def set_utm_stats_by_date(self, date, utm, stats):
        db.reference('utm_stats_by_date/'+date.replace('/','-')+'/'+utm).set(stats)

    def get_utm_stats_by_date(self, date, utm):
        return db.reference('utm_stats_by_date/'+date.replace('/','-')+'/'+utm).get()

    def get_all_utm_stats_by_date(self, date):
        return db.reference('utm_stats_by_date/'+date.replace('/','-')).get()

    def get_all_utm_stats(self):
        return db.reference('utm_stats_by_date').get()

    def set_utm_stats(self, utm, stats):
        db.reference('utm_stats/'+utm).set(stats)

    def get_utm_stats(self, utm):
        return db.reference('utm_stats/'+utm).get()

    def get_all_utm_stats(self):
        return db.reference('utm_stats').get()

    def set_aff_stats(self, aff, stats):
        db.reference('aff_stats/'+aff).set(stats)

    def get_aff_stats(self, aff):
        return db.reference('aff_stats/'+aff).get()

    def get_all_aff_stats(self):
        return db.reference('aff_stats').get()

    def set_chat_aff(self, chat, aff):
        db.reference('aff_by_chat/'+str(chat)).set(aff)

    def get_chat_aff(self, chat):
        return db.reference('aff_by_chat/'+str(chat)).get()

    # ScheduledMessage
    def add_scheduled_message(self, sch_msg):
        return db.reference('scheduled_messages').child(sch_msg.id).set(sch_msg.to_dict())

    def remove_scheduled_message(self, sch_msg):
        return db.reference('scheduled_messages').child(sch_msg.id).delete()

    def get_scheduled_message(self, sch_msg_id):
        return db.reference('scheduled_messages/'+sch_msg_id).get()

    def get_all_scheduled_messages(self):
        return db.reference('scheduled_messages').get()

    # Storage
    # def upload_screenshot(self, file, prefix=None) -> str:
    #     name = '123.png'
    #     name = prefix+'_'+name if prefix else name
    #
    #     cred = service_account.Credentials.from_service_account_file('./key.json')
    #     storage_client = storage.Client(project=self.config.firebase_name, credentials=cred)
    #     bucket = storage_client.get_bucket(self.config.firebase_name+'.appspot.com')
    #     blob = bucket.blob(name)
    #     blob.upload_from_string(file, content_type='image/png')
    #
    #     return blob.public_url

    def get_media_url(self, file_name):
        cred = service_account.Credentials.from_service_account_file('./key.json')
        storage_client = storage.Client(project=self.config.firebase_app_name, credentials=cred)
        bucket = storage_client.get_bucket(self.config.firebase_app_name+'.appspot.com')
        blob = bucket.blob(file_name)
        return blob.generate_signed_url(datetime.timedelta(seconds=300), method='GET')

