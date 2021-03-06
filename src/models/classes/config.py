# from configobj import ConfigObj


class Config:
    def __init__(self):
        # self.config = ConfigObj('config.ini', list_values=False, encoding='utf-8')
        self.token = '4e537bb43267d433-cd3515343b38db0-7ff05ffa6614bca8'
        self.tg_bot_token = '2139071493:AAG6zeE3FvrqyhKkP7xf_zi7UsrlR3pqajk'
        self.firebase_app_name = 'whitebit-bot1'
        self.firebase_db_name = 'whitebit-bot1-default-rtdb'
        self.firebase_db_region = 'europe-west1'
        self.assets_chat_id = -1001644782480
        self.admin_chat_id = -1001644782480
        self.papka_admin_id = 335676896
        self.bot_id = 108710344958762

        self.media_url = {
            'reg': {
                'ru': 'https://whitebot.xyz/assets/videos/reg.mov',
                'ua': 'https://whitebot.xyz/assets/videos/reg.mov',
                'en': 'https://whitebot.xyz/assets/videos/reg_en.mp4'
            },
            'kyc': {
                'ru': 'https://whitebot.xyz/assets/videos/kyc.mov',
                'ua': 'https://whitebot.xyz/assets/videos/kyc.mov',
                'en': 'https://whitebot.xyz/assets/videos/kyc_en.mp4'
            },
            'withdraw': {
                'ru': 'https://whitebot.xyz/assets/videos/withdraw_ru.mov',
                'ua': 'https://whitebot.xyz/assets/videos/withdraw_ru.mov',
                'en': 'https://whitebot.xyz/assets/videos/withdraw_ru.mov'
            },
            'ref': {
                'ru': 'https://whitebot.xyz/assets/images/ref_ru.jpg',
                'en': 'https://whitebot.xyz/assets/images/ref_en.jpg',
                'ua': 'https://whitebot.xyz/assets/images/ref_ua.jpg'
            },
            'activation': {
                'ru': [
                    'https://whitebot.xyz/assets/images/activation_ru_1.jpg',
                    'https://whitebot.xyz/assets/images/activation_ru_2.jpg'
                ],
                'en': [
                    'https://whitebot.xyz/assets/images/activation_en_1.jpg',
                    'https://whitebot.xyz/assets/images/activation_en_2.jpg'
                ],
                'ua': [
                    'https://whitebot.xyz/assets/images/activation_ua_1.jpg',
                    'https://whitebot.xyz/assets/images/activation_ua_2.jpg'
                ],
            }
        }

        self.messages = {
            'lang': 'Please, choose the language.\n???????????????? ????????, ????????????????????.\n?????????????? ????????, ???????? ??????????.',
            'yes': {
                'ru': '????',
                'en': 'Yes',
                'ua': '??????'
            },
            'no': {
                'ru': '??????',
                'en': 'No',
                'ua': '????'
            },
            'support': {
                'ru': '???????????????? ?????????????? ?????? ?????????? ????????????? ???????????? ?? ???????? ???????????? ?????????????????? support@whitebit.com ??? ???????????? ???????????? ?????????????? ?? ?????????????????????? ?????????? ?????????? ???????? ????????????.',
                'en': 'Do you have questions or need help? Write to our support service support@whitebit.com ??? the guys will quickly answer and solve your questions.',
                'ua': '?????????????? ?????????????? ?????? ???????????????? ????????????????? ???????????????? ???? ?????????? ???????????? ?????????????????? support@whitebit.com ??? ?????????????? ???????????? ???? ?????????????????????? ???????????????? ????????-?????? ??????????????.'
            },
            'hi': {
                'ru': '????????????!\n\n?? - WhiteBIT-??????, ???????????? ???????? ?????????????????????? ?? ?????? ??????????????????????. ???????????? ?????? ???????????????? ?????????? ?? ???????????? ?????????????????????????????? ???????????????????????????? ?? $2!\n\n?? ?????????? ???? ??????????????????????, ???????????? ?????????? ?????????????????????? ?? ????????????????????. ???????????????? ?????? ???????? ?????????????????? ???????????? ?? WhiteBIT! ???????????? ???????????????????? ?????????????????????????? ???????????? ?????? ???????????????????????????????????????? ???? WhiteBIT ??????????????????????????. ?? ????, ?????? ?????? ??????????????????????????????, ?????????? ?????????????????? ?????????????? ?? ???????????? ??????????????????????, ???????????????????? ?? ?????????????? ?????????? ?? ???????? ???????? ????',
                'en': 'Hey there!\n\nI???m your WhiteBIT bot. I will help you start off in the world of cryptocurrencies. Complete three main stages and get a guaranteed $2 reward!\n\nFollow our tips and instructions, so that you won???t get lost. Discover the world of cryptocurrencies with WhiteBIT! Participate in this activity if you are NOT registered on WhiteBIT. The registered users can take part in other activities, the information on which will be posted in this bot later ????',
                'ua': '????????????!\n\n?? - WhiteBIT-??????, ???????????????? ???????? ???????????????????? ?? ???????? ??????????????????????. ?????????????? ?????? ?????????????? ?????????? ???? ?????????????? ?????????????????????? ???????????????????? ?? $2!\n\n?????? ???? ??????????????????, ???????????????????? ?????????? ???????????????? ???? ????????????????????. ?????????????????? ?????? ???????? ???????????????????? ?????????? ?? WhiteBIT! ???? ???????????????????? ???????????????????? ???????????? ?????? ???????????????????????????????? ???? WhiteBIT ????????????????????????. ????, ?????? ?????? ??????????????????????????, ???????????? ?????????? ???????????? ?? ?????????? ??????????????????????, ???????????????????? ?????? ?????? ???????? ?? ?????????? ???????? ????'
            },
            'reg': {
                'ru': [
                    '?????????? ???????????????????????????????????? ???? ??????????, ???????????????????? ???? ???????? ???? ????????????:\n',
                    '???? ???????????? ?????????? ?? ?????????????????? ?????????????????????? ?? ???????????????? ?? ???????????????????? ????????.',
                ],
                'en': [
                    'Follow the link to sign up on the exchange:\n',
                    "???? Watch the registration process video guide and proceed to the next step",
                ],
                'ua': [
                    '?????? ?????????????????????????????? ???? ??????????, ?????????????????? ???? ????????????????????:\n',
                    '???? ???????????? ?????????? ?? ???????????????? ???????????????????? ???? ???????????????? ???? ???????????????????? ??????????.',
                ],
                'link': [
                    'https://whitebit.com/ru/auth/register?',
                    'https://whitebit.com/referral/referrer?',
                ],
                'ask_if_done': {
                    'ru': '?????????????? ?????????????????????? ???????????????',
                    'en': "Is it clear how to sign up now?",
                    'ua': '???????????? ???????????????????? ?????????????????????'
                },
                'motivashka': {
                    'ru': [
                        '?????????? ???????????????????????????????????? ???? ??????????, ???????????????????? ???? ???????? ???? ????????????:\nhttps://whitebit.com/ru/auth/register',
                        '?? ???????? ???????? ???????? ???????????????? $2! ?????? ??????????, ???????? ?????????? ???????????????????????????????????? ???? WhiteBIT. ???????????????? ?????????????????????? ??????????: ???????? ?????????? ?????????? ???? <a href="https://whitebit.com/ru">WhiteBIT</a>, ???????????? ???????????? ?????????????????????????? ?? ???????????? ??????????, ???? ?????????????? ???????????? ??????????????????. ?????????????? ???? ???????????? ?????????? ??????????????. ???? ???????????? ?????????????????????? ?????????????? ????????!\n\n?????????? ???????????????????????????????????? ???? ??????????, ???????????????????? ???? ???????? ???? ????????????:\nhttps://whitebit.com/ru/auth/register',
                        '?????????? ???????????????????????????????????? ???? ??????????, ???????????????????? ???? ???????? ???? ????????????:\nhttps://whitebit.com/ru/auth/register\n\n2$ ?????? ???????? ????????! ?????????? ???? ????????????????, ?????????? ???????????? ?????????????????????? ???? ?????????? ????????????. ?????????????? ???? ???????????? ???????????? 5 ??????????. ???????? ?????????? ????????????????????: #video'
                    ],
                    'en': [
                        'Follow the link to sign up on the exchange:\nhttps://whitebit.com/ru/auth/register',
                        "You have a chance to get $2! All you need to do is to sign up on WhiteBIT. The registration algorithm is simple: you need to go to WhiteBIT, click the \"Sign up\" button, and enter the e-mail to which the message will be sent. It will not take long. Don't miss the opportunity to get rewarded!\n\nFollow the link to sign up on the exchange:\nhttps://whitebit.com/ru/auth/register",
                        'Follow the link to sign up on the exchange:\nhttps://whitebit.com/ru/auth/register\n\n$2 are still waiting for you! Hurry up to sign up before the end of the week and get a reward! The process will not take more than 5 minutes. Here???s the tutorial: #video'
                    ],
                    'ua': [
                        '?????? ?????????????????????????????? ???? ??????????, ?????????????????? ???? ???????? ???? ????????????????????:\nhttps://whitebit.com/ru/auth/register',
                        '?? ???????? ?? ???????????????????? ???????????????? $2! ?????? ??????????, ???????? ???????????????? ?????????????????????????????? ???? WhiteBIT. ???????????????? ???????????????????? ??????????????: ???????? ???????????????? ?????????????? ???? WhiteBIT, ?????????????????? ???????????? ???????????????????????? ???? ???????????? email, ???????? ???????????? ????????????????????????. ???????????? ???? ?????????? ???????????? ????????. ???? ???????????? ???????????????????? ???????????????? ????????!\n\n?????? ?????????????????????????????? ???? ??????????, ?????????????????? ???? ???????? ???? ????????????????????:\nhttps://whitebit.com/ru/auth/register',
                        '?????? ?????????????????????????????? ???? ??????????, ?????????????????? ???? ???????? ???? ????????????????????:\nhttps://whitebit.com/ru/auth/register\n\n2$ ???? ?????????????? ???? ????????! ?????? ???? ????????????????, ?????????????? ???????????? ???????????????????? ???? ?????????? ??????????. ???????????? ???? ?????????? ???????????? ?????? 5 ????????????. ???????? ?????????? ????????????????????: #video'
                    ],
                }
            },
            'kyc': {
                'ru': '??????????????, ?????????????????????? ????????????????! ?????????????????? ???????? ???????????? ??????????, ?????????????????? ???????????????? ????????????????????????. KYC ??? ?????? ?????????????????????? ????????????????????????. ???? ?????????????????????? ?????????????? ???????????????????????? ???????????? ?? ???????????????? ?? ???????????? ???????????? ???????????? ?????? ?????????????? ?? ?????????????????????????? ????????????????????????????. ???????????? ?????????????????????? ?? ??????????, ?????????? ?????????????????????? ???????? ??????????????!',
                'en': "Great, you???ve signed up on WhiteBIT! The next step is extremely important as it concerns your safety. KYC means user verification. It can help restore access to your account in case you lose a password or a key to two-factor authentication. Follow the instructions in the video to keep your account safe!",
                'ua': "????????????????, ???????????????????? ????????????????! ?????????????????? ???????? ???????? ????????????????, ???????? ???????????????????? ??????????????. KYC ??? ???? ?????????????????????? ??????????????????????. ???? ?????????????????????? ???????????????? ?????????????????? ???????????? ???? ?????????????? ?? ???????? ???????????? ???????????? ?????? ?????????????? ???? ???????????????????????? ????????????????????????????. ?????????????? ?????????? ?? ??????????, ?????? ???????????????????? ???????? ????????????!",
                'ask_if_done': {
                    'ru': '?????????????????????? ?????????????????',
                    'en': "Did you pass KYC?",
                    'ua': "?????????????????????? ?????????????????"
                },
                'motivashka': {
                    'ru': [
                        '?????????????????????? KYC ?????????? ???????????????? ???????????????? ?? ??????????????????????????, ???? ???????????????????? ???? ??????????. ?????????????????????? ?????????????????????? ?????????? ?????????? ???????????? ???????????????????? ?? ????????????????????????, ??????????????, ?? ???????? ??????????????, ?????????????? ???????????? ???????????????????????? ?????? ????????????????. ???????????? ?????????????????????? ?? ???????????? ???????? ????????????????????????????!',
                        '?? KYC ???? ???????????? ?????????????????? ???????????? ???? ?????????? ?????? ???????????? ???????????????????? ??????????, ?????????? ???????????? ?????????????? ?????? ???????????? ????????????????????????. ???????????? ?????????????????????? ???????????? ?? ?????????????? ?????? ???????????? ???????????????????????? ?????? ????????????????!',
                        'KYC ????????! ?????????? ???????????????? $2 ?? ?????????????????????? ???????? ??????????????, ???????? ???????????????????? ???????????? ?????????????????????? ???? ?????????? ??????????. ?????????? ?? ?????????????????????? ????????, ?????? ?????? ??????????????, ???????????????????? ????????: #video'
                    ],
                    'en': [
                        'KYC often raises doubts among users, but there is no need to worry. Verification will provide the exchange with more accurate information about the user. The user, in turn, will receive more trading opportunities. Pass the verification and get your reward!',
                        'KYC will allow you to replenish your balance with a bank card, withdraw up to 100 BTC in crypto per day, and more! Pass verification now and get even more trading opportunities!',
                        'KYC is waiting! To get $2 and secure your account, you need to pass verification on our exchange. I attach a video explaining how to do this below: #video'
                    ],
                    'ua': [
                        '?????????????????????? KYC ?????????? ???????????????? ?????????????? ?? ????????????????????????, ?????????? ???? ?????????? ??????????????????????. ?????????????????????? ?????????????? ?????????? ?????????? ???????????????? ???????????????????? ?????? ??????????????????????, ????????, ?? ???????? ??????????, ?????????????? ???????????? ?????????????????????? ?????? ???????????????? ???? ??????????. ?????????????? ?????????????????????? ???? ?????????????? ???????? ????????????????????!',
                        'KYC ???? ?????????? ?????????????????????? ???????????? ???? ?????????????????? ?????????????????????? ????????????, ?????? ???????????????? ?????????????? ?????? ???????? ????????????????????????. ?????????????? ?????????????????????? ?????? ?????????? ???? ?????????????? ???? ???????????? ?????????????????????? ?????? ????????????????!',
                        'KYC ??????????! ?????? ???????????????? $2 ???? ???????????????????? ???????? ????????????, ???????? ?????????????????? ???????????? ?????????????????????? ???? WhiteBIT. ?????????? ?? ????????????????????, ???? ???? ?????????????? ??? ??????????: #video'
                    ]
                }
            },
            'email': {
                'ru': [
                    '??????????????????????, ???? ?????????????? ???????? ???????????? ?????? ?? ???????????????? ????????????????????. ???????????? ???? ???????????? ?????????????????? ?????? ?????????????????????? ?? ???????????????????????? ???????? ???????????????????? ??????????.\n\n?????????? ???????????????? ?????????? ?? ?????????????? 2$ ????????????????, ????????????????????, ???????? ?????????????????????? ??????????, ?????????????? ???? ???????????????????????? ?????? ??????????????????????:',
                    '????????????, ?????????????????????? ?????????? ?????????????? ??????????????. ???????????????????? ?????? ??????:',
                ],
                'en': [
                    "Congratulations, you???ve made your first step towards exploring the crypto world. Now, you can use the complete functionality of the exchange and trade without restrictions.\n\nTo get a $2 bonus, please send your registration e-mail:",
                    'It seems like email is invalid. Try again, please:'
                ],
                'ua': [
                    '??????????????, ???? ?????????????? ???????? ???????????? ???????? ?? ???????????????? ??????????????????????. ?????????? ???? ???????????? ?????????????????? ?????? ???????????????? ???? ?????????????????????? ???????? ???????????????????? ??????????.\n\n?????? ???????????????? ?????????? ?? ?????????????? 2$ ??????????????????, ???????? ??????????, ???????? ???????????????????? ??????????, ?????? ???? ?????????????????????????????? ?????? ????????????????????:',
                    '??????????, ???????????????????? ?????????? ?????????????? ??????????????. ?????????????????? ???? ??????:',
                ],
                'motivashka': {
                    'ru': [
                        '',
                        '',
                        ''
                    ],
                    'en': [
                        '',
                        '',
                        ''
                    ],
                    'ua': [
                        '',
                        '',
                        ''
                    ]
                }
            },
            'approve': {
                'ru': '??????????????! ???????????? ?????????????????? ???? ?????????? example@mail.ru ?? WhiteBIT-??????????, ?????????????? ???? ???????????? ????????????????????????, ?????????? ???????????????? ??????????????.\n???????????? ?????? ???????????????? 24 ????????, ???? ???????????????? ???????????????? ?????????????????? ???? 7 ????????.',
                'en': "Great! Expect an emil in example@mail.ru with a WhiteBIT Code which you can activate to get your reward.\nIt usually takes 24 hours, but you may have to wait for up to 7 days.",
                'ua': "????????????! ???????????? ???????????????????????? ???? ?????????? example@mail.ru ?? WhiteBIT-??????????, ???????? ???? ???????????? ???????????????????? ?????? ?????????????????? ????????????????????.\n???????????????? ???? ???????????? 24 ????????????, ?????? ?????????????? ?????????? ???????? ???????????????? ???? 7 ????????.",
                'btns': {
                    'ru': [
                        '?? ??????????????(??) ??????',
                        '?? ???????????? ?????? ?????????? 7 ????????'
                    ],
                    'en': [
                        'I received a code',
                        'I???ve been waiting more than 7 days'
                    ],
                    'ua': [
                        '?? ??????????????(????) ??????',
                        '?? ???????????? ?????? ???????????? ?????? 7 ????????'
                    ]
                },
                'motivashka': {
                    'ru': [
                        '?????????????? ???? ?????????????????????? ?? ?????????????????????? ??????????????????????! WhiteBIT-?????? ???? ?????????? $2  ?????? ???????? ???????? ?? ???????????? ???? ?????????????????? ?????? ?????????????????????? e-mail. ?????????????? ???? ?????????? ?? ???????????? ?????????? ????????????????????.',
                        '?????????? ????????????! ???? ???????? ?????????? ?????? ???????????? ???????????? ?? WhiteBIT-?????????? ???????????????????????? ?? $2, ?????? ???????????? ???????????????? ???? ???????????? ???????????????? ?????????????? ???? ??????????????????????. ?????????????? ???????????????? ???????????? ?? ???????????????? ?? ???????????????????? ????????!',
                        '?????? ???????? ??????, ?? ?????????????? ??? ?? ?????????? ??????????! ???????????????????? ???????? ???? ?????????????????????? ???? ?????????? ??????????. ?????????? ?????????????????????? ?????????????????????? ???????? ???? ?????????? ???????????? ???????????? ?? WhiteBIT-?????????? ???? ?????????? $2, ?????????????? ???????????????????? ???????????????????????? ?????? ?????????????????? ??????????. ???????????????? ?????? ?????????? ???? e-mail ?? ???????????????? ?? ???????????????????? ?????????? ??? ???????????? ??????????????!'
                    ],
                    'en': [
                        'Thank you for signing up and passing KYC! WhiteBIT Code and a $2 reward are waiting for you in the letter sent to your e-mail. Look into the mail and follow our instructions.',
                        'Almost ready! A letter with a WhiteBIT Code and a $2 reward has been sent to your e-mail. Use it to get a reward for the registration. Check your inbox and move on to the next step!',
                        'One more step and the reward is yours! Thank you for signing up on our exchange. After you passed KYC, you were supposed to receive an e-mail with a WhiteBIT Code and a $2 reward. Activate the code to receive the prize. Check all your e-mail folders and proceed to withdraw your funds!'
                    ],
                    'ua': [
                        '?????????????? ???? ???????????????????? ???? ??????????????????????! WhiteBIT-?????? ???? ???????? $2 ?????? ?????????? ???? ???????? ?? ?????????? ???? ?????????????????? ?????? ???????????????????? email. ?????????????? ???? ?????????? ???? ???????????? ?????????? ??????????????????.',
                        '?????????? ????????????! ???? ???????? ?????????? ?????? ?????????????? ???????? ?? WhiteBIT-?????????? ???? ???????? $2, ???? ?????????????????? ?????????? ???? ?????????? ???????????????? ???????????????????? ???? ????????????????????. ?????????????? ???????????? ?????????? ???? ???????????????? ???? ???????????????????? ??????????!',
                        '???? ???????? ????????, ?? ???????????????????? ??? ?? ???????? ?? ??????????! ?????????????? ???? ???????????????????? ???? ?????????? ??????????. ?????????? ?????????????????????? ?????????????????????? ???????? ???? ?????????? ?????????????? ???????? ?? WhiteBIT-?????????? ???? ???????? $2, ???????? ?????????????????? ???????????????????? ?????? ?????????????????? ??????????. ?????????????????? ?????? ?????????????????? ?????????? ???? ?????????? ???? ???????????????? ???? ???????????????????? ?????????? ??? ?????????????????? ????????????!'
                    ]
                }
            },
            'activation': {
                'ru': [
                    '?? WhiteBIT-?????????? ???? ???????????? ?????? ???????????????? ???????????????????? ???????????????? ???????????? ??????????, ?? ?????????? ???????????????????????? ???? ???? ???????????????????? ??????????????????, ?????????? ???????????????????? ???????????? ?????????? ????????????????????.\n?????????? ???????????????????????? WhiteBIT, ???????????? ??????????????????:\n\n1. ?????????????? ?? ????????????, ?????????????? ???? ?????????????????? ???? ?????????????????? ?????? ?????????????????????? email.\n2. ???????????????? ?????? ???? ???????????? ?? ?????????????? ?? ???????????? ???????????? ???? WhiteBIT: https://whitebit.com/ru/codes.\n3. ???????????? ?????????? ???? ???????????? ?????????????????????????? ????????.\n4. ???????????? ?????????????????????????? ?????? ?? ???????? ?? ?????????? ?????????????????????????? ????????.\n\n????????????! ?????????? ???????? ????????????????, ???????????????? ?????????? ?????????????????????? ?????????????????? ???? ???????? ???????????????? ????????????.',
                ],
                'en': [
                    'You can use WhiteBIT Codes to transfer funds within the exchange fee-free, as well as use them on partner platforms to transfer assets between wallets.\nTo activate a WhiteBIT Code, do the following:\n\n1. Open the letter that we sent to your e-mail.\n2. Copy the code from the letter and go to the "Codes" section on WhiteBIT: https://whitebit.com/ru/codes.\n3. Click on the "Activate Code" button.\n4. Paste the copied code into the field and click "Activate Code".\n\nReady! Now the funds will be instantly credited to your Main balance.',
                ],
                'ua': [
                    "?? WhiteBIT-?????????? ???? ?????????? ?????? ?????????????? ???????????????????????? ?????????? ???? ??????????, ?? ?????????? ?????????????????????????????? ???? ???? ???????????????????? ??????????????????, ?????? ???????????????????????? ?????????? ?????? ??????????????????.\n?????? ???????????????????? WhiteBIT-??????, ?????????????? ???????????????? ??????:\n\n1. ?????????????? ???? ??????????, ?????? ???? ???????????????????? ???? ???????????????? ?????? ???????????????????? email.\n2. ?????????????? ?????? ?? ?????????? ???? ?????????????? ???? ?????????????? ???????????? ???? WhiteBIT: https://whitebit.com/ru/codes.\n3. ?????????????? ???????????? ?????????????????????? ????????.\n4. ?????????? ???????????????????????? ?????? ?? ???????? ???? ?????????????? ?????????????????????? ????????.\n\n????????????! ?????????? ?????? ??????, ?????????? ???????????? ?????????????????????? ???????????????????? ???? ???????? ???????????????? ??????????????.",
                ],
                'ask_if_done': {
                    'ru': '???????????????????? ???????????????????????? WhiteBIT-???????',
                    'en': "Did you manage to activate a WhiteBIT Code?",
                    'ua': "???????????? ???????????????????? WhiteBIT-???????"
                },
                'motivashka': {
                    'ru': [
                        '?????????????????? WhiteBIT-???????? ???????????????? ???? ?????????? ???????? ??????????, ?? ?????? ?????????????? ?????????? ??????????. ???????????? ???????? ?????????????? ?????? ????????????!',
                        '???????? ?????????????? ?????? ????????????! ???????? ???????????????? ???????? ???????????????????????? WhiteBIT-?????? ?? ???????????????? $2 ?? ???????????????? ????????????????????????????.',
                        '??????-???? ?????????? ???? ??????? ???????? ?? ???????? ???????????????? ?????????????? ?????? ???? ???????????????????? ???????????????????????? WhiteBIT-??????, ???? ???????????? ???????????? ???????????????????? ?? ???????? ???????????? ??????????????????, ?????????????? ?????????????????????? ??????????????!\nsupport@whitebit.com'
                    ],
                    'en': [
                        'It takes not more than two minutes to activate the code, and the process is simple itself.',
                        'Your reward is very close! Activate the code and get your $2 reward!',
                        'Something???s wrong? If you have questions, or you could not activate your WhiteBIT Code, you can always turn to our support that will help you in no time!'
                    ],
                    'ua': [
                        '?????????????????? WhiteBIT-???????? ???????????? ???? ?????????? ?????? 2 ??????????????, ?????? ???????????? ??????????????. ?????????????? WhiteBIT-?????? ???? ?????????????? ???????? ???????????????????? ?????? ??????????!',
                        '???????? ???????????????????? ?????? ??????????????! ???????? ???????????????????? ???????? ???????????????????? WhiteBIT-?????? ???? ???????????????? ???????????????????? ?? $2.',
                        "???????? ???? ????????????? ???????? ?? ???????? ???????????????????? ?????????????? ?????? ???? ???????????? ???????????????????? WhiteBIT-??????, ???? ???????????? ?????????? ???????????????????? ?? ???????? ???????????? ??????????????????, ?????? ????????'???????????? ????????????????!"
                    ]
                }
            },
            'withdraw': {
                'ru': '?????????????????? ???????? ??? ?????????? ??????????????! ???????? ?????????? ???????????????????? ???? ???????????? ?????????????? ???? WhiteBIT.\n?????????? ?? ?????????????? ??????????????:',
                'en': "The final step is the withdrawal of funds! Here???s a video tutorial on how to withdraw funds on WhiteBIT.\nA video guide on withdrawals:",
                'ua': "?????????????????? ???????? ??? ?????????????????? ????????????! ???????????? ?????????? ????????????????????, ???? ???? ???????????????????????? ???? ?????????????? ?????????? ???? WhiteBIT.\n?????????? ?? ???????????????????? ????????????:"
            },
            'ref': {
                'ru': [
                    '??????????????, ???????????????? ?????? ???? ?????????? ??????????????! ???? ?????? ?????? ???? ?????? ????\n\n???????????? ?????? ???????? ?????????????????????? ???????????????? ??????????????? ?????????????? ?????????? ???????? ????????????????: ???????????????? ???????????? ???????????????????????????????????? ???? WhiteBIT ?? ???????????? $2 ?? ?????????????? ?????????????????????????????????????? ???? ?????????? ???????????? ????????????????????????.\n\n?????????? ?????? ???????? ?????????? ?????????? ?????????? ????????????, ???????????????? ?????? ???????? ?????????????????????? ????????????. ???? ???????????? ?????????? ????, ?????????????? ???? ????????????:\nhttps://whitebit.com/ru/referral.',
                    '????????????, ?????????????????????? ???????????? ?????????????? ??????????????. ???????????????????? ?????? ??????. ???? ???????????? ?????????? ???????? ?????????????????????? ???????????? ???? ???????? ????????????????:\nhttps://whitebit.com/ru/referral'
                ],
                'en': [
                    "Awesome! The balance is replenished! But there is more ????\n\nWould you like another opportunity to receive a reward? Take just one step: invite your friends to sign up on WhiteBIT through a referral link, get 40% from each of their transaction fees, and $2 for each friend with KYC! It's simple: they trade, and you receive passive income.\n\nIt will be easier for me to find your friends if you send me a referral link. You can find it here:\nhttps://whitebit.com/referral",
                    "It seems like referral link is invalid. Try again, please. You can find your referral link here:\nhttps://whitebit.com/referral"
                ],
                'ua': [
                    "????????????????, ?????????? ?????? ???? ???????????? ??????????????! ?????? ???? ???? ???? ?????? ????\n\n?????????? ???? ???????? ???????????????????? ???????????????? ????????????????????? ?????????????? ???????? ??????: ?????????????? ???????????? ???? WhiteBIT ???? ?????????????? $2 ???? ?????????????? ?????????????????????????????? ??????????????????????.\n\n?????? ???????? ???????? ???????????????? ???????????? ?????????? ????????????, ?????????????????? ???????? ???????? ???????????????????? ??????????????????. ???? ???????????? ???????????? ????, ???????????????????? ???? ????????????????????:\nhttps://whitebit.com/ru/referral.",
                    '??????????, ???????????????????? ?????????????????? ?????????????? ??????????????. ?????????????????? ???? ??????. ???? ???????????? ???????????? ???????? ???????????????????? ?????????????????? ???? ?????? ????????????????:\nhttps://whitebit.com/ru/referral'
                ],
                'motivashka': {
                    'ru': [
                        '???????????? ???????????????? ?????????????????? ??????????? ?????????????????? ???????????? ???? WhiteBIT ?? ?????????????? 2$ ???? ?????????????? ??????????, ?????????????? ?????????????????????????????????? ?? ???????????? ??????????????????????!',
                        '???????????????? ?????????? ???? ??????????, ???????????? ???? ??????????? ?????? ????????????????! ???????????? ???????????????? ?????????? ???? WhiteBIT ?? ?????????????? ???? ?????? ????????????????.',
                        '?????????????? ?????????????? ???? ?????????????? ?????????????????????????? ?????????? ???? WhiteBIT! ?????????????????? ?????????????? ?????????????????????? ???????????? ?? ?????????????? $2 ???? ?????????????? ?????????????????????????????????????? ????????????????????????.'
                    ],
                    'en': [
                        'Do you want to receive passive income? Invite your friends to WhiteBIT and get 40% of each of their transaction fees.',
                        'Want to get a prize for doing nothing? It is possible! Just invite a friend to WhiteBIT and get rewarded!',
                        'Enjoy our referral program. Invite friends and get 40% of every fee paid by them. Moreover, receive $2 for each friend with KYC!'
                    ],
                    'ua': [
                        '?????????? ???????????????????? ???????????????? ????????????????? ???????????????? ???????????? ???? WhiteBIT ???? ?????????????? $2 ???? ?????????????? ?????????????????????????????? ???? ?????????? ???????????????????? ??????????????????????.',
                        '???????????????????? ???????????????? ???? ??????????, ???????????? ???? ??????????????? ???? ??????????????! ???????????? ?????????????? ???????????? ???? WhiteBIT ???? ?????????????? ???? ???? ????????????????.',
                        '???????????????????? ???????????? ???????????????????? ?????????????????? ???? ?????????????? $2 ???? ?????????????? ?????????????????????????????? ??????????????????????. ???????????????? ???????????? ???? WhiteBIT ???? ?????????????? ???????????? ?????? ??????????!'
                    ]
                }
            },
            'ref_activate': {
                'ru': '?????? ???????????? ???? ?????? ???????????? ???????????????????? ??????????????. ?????????? ???????????????? ?????? ????????, ???? ?????? ???? ???????????????? $2 ???? ???????? ?????????????? ???? ?????????????? ??????????!',
                'en': "Send this link to your friends, so that they could go the same way you did. If they do, you will receive $2 to the Balance!",
                'ua': '???? ?????? ???????????? ?????????????????????? ???? ?????????????????? ????????????. ?????????? ?????????????????? ?????? ????????, ???? ???? ???? ?????????????????? $2 ???? ???????? ????????????????!',
            },
            'stats': {
                'ru': [
                    '????????????????????',
                    '???????????????????? ?????????? ??????????????????: '
                ],
                'en': [
                    'Statistics',
                    'Your referrals number: '
                ],
                'ua': [
                    '????????????????????',
                    '?????????????????? ?????????? ??????????????????: '
                ],
            }
        }

