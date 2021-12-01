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
            'lang': 'Please, choose the language.\nВыберите язык, пожалуйста.\nОберіть мову, будь ласка.',
            'yes': {
                'ru': 'Да',
                'en': 'Yes',
                'ua': 'Так'
            },
            'no': {
                'ru': 'Нет',
                'en': 'No',
                'ua': 'Ні'
            },
            'support': {
                'ru': 'Возникли вопросы или нужна помощь? Напиши в нашу службу поддержки support@whitebit.com – ребята быстро ответят и компетентно решат любой твой вопрос.',
                'en': 'Do you have questions or need help? Write to our support service support@whitebit.com — the guys will quickly answer and solve your questions.',
                'ua': 'Виникли питання або потрібна допомога? Звернись до нашої служби підтримки support@whitebit.com – команда швидко та компетентно вирішить будь-яке питання.'
            },
            'hi': {
                'ru': 'Привет!\n\nЯ - WhiteBIT-бот, помогу тебе погрузиться в мир криптовалют. Пройди три основных этапа и получи гарантированное вознаграждение в $2!\n\nА чтобы не заблудиться, следуй нашим инструкциям и подсказкам. Открывай для себя криптомир вместе с WhiteBIT! Данная активность предназначена только для незарегистрированных на WhiteBIT пользователей. А те, кто уже зарегистрирован, могут принимать участие в других активностях, информация о которых будет в этом боте 😉',
                'en': 'Hey there!\n\nI’m your WhiteBIT bot. I will help you start off in the world of cryptocurrencies. Complete three main stages and get a guaranteed $2 reward!\n\nFollow our tips and instructions, so that you won’t get lost. Discover the world of cryptocurrencies with WhiteBIT! Participate in this activity if you are NOT registered on WhiteBIT. The registered users can take part in other activities, the information on which will be posted in this bot later 😉',
                'ua': 'Привіт!\n\nЯ - WhiteBIT-бот, допоможу тобі зануритися у світ криптовалют. Виконай три основні умови та отримай гарантовану винагороду в $2!\n\nЩоб не заблукати, дотримуйся наших підказок та інструкцій. Відкривай для себе криптосвіт разом з WhiteBIT! Ця активність призначена тільки для незареєстрованих на WhiteBIT користувачів. Ті, хто вже зареєстровані, можуть брати участь в інших активностях, інформація про які буде в цьому боті 😉'
            },
            'reg': {
                'ru': [
                    'Чтобы зарегистрироваться на бирже, переходите на сайт по ссылке:\n',
                    '📺 Смотри видео с процессом регистрации и переходи к следующему шагу.',
                ],
                'en': [
                    'Follow the link to sign up on the exchange:\n',
                    "📺 Watch the registration process video guide and proceed to the next step",
                ],
                'ua': [
                    'Щоб зареєструватися на біржі, перейдіть за посиланням:\n',
                    '📺 Дивись відео з процесом реєстрації та переходь до наступного етапу.',
                ],
                'link': [
                    'https://whitebit.com/ru/auth/register?',
                    'https://whitebit.com/referral/referrer?',
                ],
                'ask_if_done': {
                    'ru': 'Процесс регистрации понятен?',
                    'en': "Is it clear how to sign up now?",
                    'ua': 'Процес реєстрації зрозумілий?'
                },
                'motivashka': {
                    'ru': [
                        'Чтобы зарегистрироваться на бирже, переходите на сайт по ссылке:\nhttps://whitebit.com/ru/auth/register',
                        'У тебя есть шанс получить $2! Для этого, тебе нужно зарегистрироваться на WhiteBIT. Алгоритм регистрации прост: тебе нужно зайти на <a href="https://whitebit.com/ru">WhiteBIT</a>, нажать кнопку «Регистрация» и ввести почту, на которую придет сообщение. Процесс не займет много времени. Не упусти возможность забрать приз!\n\nЧтобы зарегистрироваться на бирже, переходите на сайт по ссылке:\nhttps://whitebit.com/ru/auth/register',
                        'Чтобы зарегистрироваться на бирже, переходите на сайт по ссылке:\nhttps://whitebit.com/ru/auth/register\n\n2$ ещё ждут тебя! Чтобы их получить, успей пройти регистрацию до конца недели. Процесс не займет больше 5 минут. Лови видео инструкцию: #video'
                    ],
                    'en': [
                        'Follow the link to sign up on the exchange:\nhttps://whitebit.com/ru/auth/register',
                        "You have a chance to get $2! All you need to do is to sign up on WhiteBIT. The registration algorithm is simple: you need to go to WhiteBIT, click the \"Sign up\" button, and enter the e-mail to which the message will be sent. It will not take long. Don't miss the opportunity to get rewarded!\n\nFollow the link to sign up on the exchange:\nhttps://whitebit.com/ru/auth/register",
                        'Follow the link to sign up on the exchange:\nhttps://whitebit.com/ru/auth/register\n\n$2 are still waiting for you! Hurry up to sign up before the end of the week and get a reward! The process will not take more than 5 minutes. Here’s the tutorial: #video'
                    ],
                    'ua': [
                        'Щоб зареєструватися на біржі, перейдіть на сайт за посиланням:\nhttps://whitebit.com/ru/auth/register',
                        'У тебе є можливість отримати $2! Для цього, тобі потрібно зареєструватися на WhiteBIT. Алгоритм реєстрації простий: тобі потрібно перейти на WhiteBIT, натиснути кнопку «Реєстрація» та ввести email, куди прийде повідомлення. Процес не займе багато часу. Не проґав можливість отримати приз!\n\nЩоб зареєструватися на біржі, перейдіть на сайт за посиланням:\nhttps://whitebit.com/ru/auth/register',
                        'Щоб зареєструватися на біржі, перейдіть на сайт за посиланням:\nhttps://whitebit.com/ru/auth/register\n\n2$ ще чекають на тебе! Аби їх отримати, встигни пройти реєстрацію до кінця тижня. Процес не займе більше ніж 5 хвилин. Лови відео інструкцію: #video'
                    ],
                }
            },
            'kyc': {
                'ru': 'Отлично, регистрация пройдена! Следующий этап крайне важен, поскольку касается безопасности. KYC — это верификация пользователя. Ее прохождение поможет восстановить доступ к аккаунту в случае потери пароля или доступа к двухфакторной аутентификации. Следуй инструкциям в видео, чтобы обезопасить свой аккаунт!',
                'en': "Great, you’ve signed up on WhiteBIT! The next step is extremely important as it concerns your safety. KYC means user verification. It can help restore access to your account in case you lose a password or a key to two-factor authentication. Follow the instructions in the video to keep your account safe!",
                'ua': "Відмінно, реєстрація пройдена! Наступний етап дуже важливий, адже стосується безпеки. KYC – це верифікація користувача. Її проходження допоможе відновити доступ до акаунта у разі втрати паролю або доступу до двофакторної аутентифікації. Виконуй кроки у відео, аби убезпечити твій акаунт!",
                'ask_if_done': {
                    'ru': 'Верификация пройдена?',
                    'en': "Did you pass KYC?",
                    'ua': "Верификація пройдена?"
                },
                'motivashka': {
                    'ru': [
                        'Прохождение KYC часто вызывает сомнения у пользователей, но переживать не стоит. Верификация предоставит бирже более точную информацию о пользователе, который, в свою очередь, получит больше возможностей для торговли. Пройди верификацию и получи свое вознаграждение!',
                        'С KYC ты можешь пополнять баланс на бирже при помощи банковской карты, чтобы купить биткоин или другую криптовалюту. Пройди верификацию сейчас и получай еще больше возможностей для торговли!',
                        'KYC ждёт! Чтобы получить $2 и обезопасить свой аккаунт, тебе необходимо пройти верификацию на нашей бирже. Видео с объяснением того, как это сделать, прикрепляю ниже: #video'
                    ],
                    'en': [
                        'KYC often raises doubts among users, but there is no need to worry. Verification will provide the exchange with more accurate information about the user. The user, in turn, will receive more trading opportunities. Pass the verification and get your reward!',
                        'KYC will allow you to replenish your balance with a bank card, withdraw up to 100 BTC in crypto per day, and more! Pass verification now and get even more trading opportunities!',
                        'KYC is waiting! To get $2 and secure your account, you need to pass verification on our exchange. I attach a video explaining how to do this below: #video'
                    ],
                    'ua': [
                        'Проходження KYC часто викликає сумніви у користувачів, проте не варто перейматися. Верифікація надасть біржі більш детальну інформацію про користувача, який, в свою чергу, отримає більше можливостей для торгівлі на біржі. Проходь верифікацію та отримай свою винагороду!',
                        'KYC ти можеш поповнювати баланс за допомогою банківської картки, аби придбати біткоїн або іншу криптовалюту. Проходь верифікацію вже зараз та отримуй ще більше можливостей для торгівлі!',
                        'KYC чекає! Аби отримати $2 та убезпечити свій акаунт, тобі необхідно пройти верифікацію на WhiteBIT. Відео з поясненням, як це зробити – нижче: #video'
                    ]
                }
            },
            'email': {
                'ru': [
                    'Поздравляем, вы сделали свой первый шаг в изучении криптомира. Теперь вы можете торговать без ограничений и использовать весь функционал биржи.\n\nЧтобы получить бонус в размере 2$ пришлите, пожалуйста, свою электронную почту, которую вы использовали для регистрации:',
                    'Похоже, электронная почта введена неверно. Попробуйте еще раз:',
                ],
                'en': [
                    "Congratulations, you’ve made your first step towards exploring the crypto world. Now, you can use the complete functionality of the exchange and trade without restrictions.\n\nTo get a $2 bonus, please send your registration e-mail:",
                    'It seems like email is invalid. Try again, please:'
                ],
                'ua': [
                    'Вітаємо, ви зробили свій перший крок у вивченні криптовалют. Тепер ви можете торгувати без обмежень та використати весь функціонал біржі.\n\nЩоб отримати бонус у розмірі 2$ надішліть, будь ласка, свою електронну пошту, яку ви використовували для реєстрації:',
                    'Схоже, електронну пошту введено невірно. Спробуйте ще раз:',
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
                'ru': 'Отлично! Ожидай сообщение на почту example@mail.ru с WhiteBIT-кодом, который ты можешь активировать, чтобы получить награду.\nОбычно это занимает 24 часа, но возможно придется подождать до 7 дней.',
                'en': "Great! Expect an emil in example@mail.ru with a WhiteBIT Code which you can activate to get your reward.\nIt usually takes 24 hours, but you may have to wait for up to 7 days.",
                'ua': "Чудово! Очікуй повідомлення на пошту example@mail.ru з WhiteBIT-кодом, який ти зможеш активувати для отримання винагороди.\nЗазвичай це займає 24 години, але можливо треба буде зачекати до 7 днів.",
                'btns': {
                    'ru': [
                        'Я получил(а) код',
                        'Я ожидаю код более 7 дней'
                    ],
                    'en': [
                        'I received a code',
                        'I’ve been waiting more than 7 days'
                    ],
                    'ua': [
                        'Я отримав(ла) код',
                        'Я очікую код більше ніж 7 днів'
                    ]
                },
                'motivashka': {
                    'ru': [
                        'Спасибо за регистрацию и прохождение верификации! WhiteBIT-код на сумму $2  уже ждет тебя в письме на указанном при регистрации e-mail. Загляни на почту и следуй нашим подсказкам.',
                        'Почти готово! На твою почту уже пришло письмо с WhiteBIT-кодом эквивалентом в $2, при помощи которого ты можешь получить награду за регистрацию. Проверь входящие письма и переходи к следующему шагу!',
                        'Ещё один шаг, и награда – в твоих руках! Благодарим тебя за регистрацию на нашей бирже. После прохождения верификации тебе на почту пришло письмо с WhiteBIT-кодом на сумму $2, который необходимо активировать для получения приза. Проверяй все папки на e-mail и переходи к последнему этапу – выводу средств!'
                    ],
                    'en': [
                        'Thank you for signing up and passing KYC! WhiteBIT Code and a $2 reward are waiting for you in the letter sent to your e-mail. Look into the mail and follow our instructions.',
                        'Almost ready! A letter with a WhiteBIT Code and a $2 reward has been sent to your e-mail. Use it to get a reward for the registration. Check your inbox and move on to the next step!',
                        'One more step and the reward is yours! Thank you for signing up on our exchange. After you passed KYC, you were supposed to receive an e-mail with a WhiteBIT Code and a $2 reward. Activate the code to receive the prize. Check all your e-mail folders and proceed to withdraw your funds!'
                    ],
                    'ua': [
                        'Дякуємо за реєстрацію та верифікацію! WhiteBIT-код на суму $2 вже чекає на тебе у листі на вказаному при реєстрації email. Зазирни на пошту та слідуй нашим підказкам.',
                        'Майже готово! На твою пошту вже прийшов лист з WhiteBIT-кодом на суму $2, за допомогою якого ти можеш отримати винагороду за реєстрацію. Перевір вхідні листи та переходь до наступного кроку!',
                        'Ще один крок, і винагорода – у тебе в руках! Дякуємо за реєстрацію на нашій біржі. Після проходження верифікації тобі на пошту прийшов лист з WhiteBIT-кодом на суму $2, який необхідно активувати для отримання призу. Перевіряй всі нещодавні листи на пошті та переходь до останнього етапу – виведенню коштів!'
                    ]
                }
            },
            'activation': {
                'ru': [
                    'С WhiteBIT-кодом ты можешь без комиссии переводить средства внутри биржи, а также использовать их на платформах партнерах, чтобы переводить активы между кошельками.\nЧтобы активировать WhiteBIT, сделай следующее:\n\n1. Перейди в письмо, которое мы отправили на указанный при регистрации email.\n2. Скопируй код из письма и перейди в раздел «Коды» на WhiteBIT: https://whitebit.com/ru/codes.\n3. Теперь нажми на кнопку «Активировать код».\n4. Вставь скопированный код в поле и нажми «Активировать код».\n\nГотово! После этих действий, средства будут моментально начислены на твой Основной баланс.',
                ],
                'en': [
                    'You can use WhiteBIT Codes to transfer funds within the exchange fee-free, as well as use them on partner platforms to transfer assets between wallets.\nTo activate a WhiteBIT Code, do the following:\n\n1. Open the letter that we sent to your e-mail.\n2. Copy the code from the letter and go to the "Codes" section on WhiteBIT: https://whitebit.com/ru/codes.\n3. Click on the "Activate Code" button.\n4. Paste the copied code into the field and click "Activate Code".\n\nReady! Now the funds will be instantly credited to your Main balance.',
                ],
                'ua': [
                    "З WhiteBIT-кодом ти можеш без комісії переказувати кошти на біржі, а також використовувати їх на платформах партнерів, аби переказувати кошти між гаманцями.\nАби активувати WhiteBIT-код, виконай наступні дії:\n\n1. Перейди до листа, яке ми відправили на вказаний при реєстрації email.\n2. Скопіюй код з листа та перейди до розділу «Коди» на WhiteBIT: https://whitebit.com/ru/codes.\n3. Натисни кнопку «Активувати код».\n4. Встав скопійований код у поле та натисни «Активувати код».\n\nГотово! Після цих дій, кошти будуть моментально зараховані на твій Основний рахунок.",
                ],
                'ask_if_done': {
                    'ru': 'Получилось активировать WhiteBIT-код?',
                    'en': "Did you manage to activate a WhiteBIT Code?",
                    'ua': "Вийшло активувати WhiteBIT-код?"
                },
                'motivashka': {
                    'ru': [
                        'Активация WhiteBIT-кода занимает не более двух минут, а сам процесс очень прост. Получи свою награду уже сейчас!',
                        'Твоя награда уже близка! Тебе осталось лишь активировать WhiteBIT-код и получить $2 в качестве вознаграждения.',
                        'Что-то пошло не так? Если у тебя остались вопросы или не получилось активировать WhiteBIT-код, ты всегда можешь обратиться в нашу службу поддержки, которая обязательно поможет!\nsupport@whitebit.com'
                    ],
                    'en': [
                        'It takes not more than two minutes to activate the code, and the process is simple itself.',
                        'Your reward is very close! Activate the code and get your $2 reward!',
                        'Something’s wrong? If you have questions, or you could not activate your WhiteBIT Code, you can always turn to our support that will help you in no time!'
                    ],
                    'ua': [
                        'Активація WhiteBIT-коду займає не більш ніж 2 хвилини, сам процес простий. Активуй WhiteBIT-код та отримай свою винагороду вже зараз!',
                        'Твоя винагорода вже близько! Тобі залишилось лише активувати WhiteBIT-код та отримати винагороду в $2.',
                        "Щось не вийшло? Якщо у тебе залишились питання або не вийшло активувати WhiteBIT-код, ти завжди можеш звернутися в нашу службу підтримки, яка обов'язково допоможе!"
                    ]
                }
            },
            'withdraw': {
                'ru': 'Финальный этап – вывод средств! Лови видео инструкцию по выводу средств на WhiteBIT.\nВидео с выводом средств:',
                'en': "The final step is the withdrawal of funds! Here’s a video tutorial on how to withdraw funds on WhiteBIT.\nA video guide on withdrawals:",
                'ua': "Фінальний етап – виведення коштів! Тримай відео інструкцію, де ми розповідаємо як вивести кошти на WhiteBIT.\nВідео з виведенням коштів:"
            },
            'ref': {
                'ru': [
                    'Отлично, средства уже на твоём балансе! Но это еще не все 😜\n\nХочешь ещё одну возможность получить награду? Выполни всего одно действие: пригласи друзей зарегистрироваться на WhiteBIT и получи $2 с каждого зарегистрированного по твоей ссылке пользователя.\n\nЧтобы мне было проще найти ваших друзей, пришлите мне свою реферальную ссылку. Вы можете найти её, перейдя по ссылке:\nhttps://whitebit.com/ru/referral.',
                    'Похоже, реферальная ссылка введена неверно. Попробуйте еще раз. Вы можете найти свою реферальную ссылку на этой странице:\nhttps://whitebit.com/ru/referral'
                ],
                'en': [
                    "Awesome! The balance is replenished! But there is more 😜\n\nWould you like another opportunity to receive a reward? Take just one step: invite your friends to sign up on WhiteBIT through a referral link, get 40% from each of their transaction fees, and $2 for each friend with KYC! It's simple: they trade, and you receive passive income.\n\nIt will be easier for me to find your friends if you send me a referral link. You can find it here:\nhttps://whitebit.com/referral",
                    "It seems like referral link is invalid. Try again, please. You can find your referral link here:\nhttps://whitebit.com/referral"
                ],
                'ua': [
                    "Відмінно, кошти вже на твоєму балансі! Але це ще не все 😜\n\nХочеш ще одну можливість отримати винагороду? Виконай одну дію: запроси друзів на WhiteBIT та отримуй $2 за кожного зареєстрованого користувача.\n\nЩоб мені було простіше знайти ваших друзів, надішліть мені своє реферальне посилання. Ви можете знайти її, перейшовши за посиланням:\nhttps://whitebit.com/ru/referral.",
                    'Схоже, реферальне посилання введено невірно. Спробуйте ще раз. Ви можете знайти своє реферальне посилання на цій сторінці:\nhttps://whitebit.com/ru/referral'
                ],
                'motivashka': {
                    'ru': [
                        'Хочешь получать пассивный доход? Приглашай друзей на WhiteBIT и получай 2$ от каждого друга, который зарегистрировался и прошел верификацию!',
                        'Получать доход на бирже, ничего не делая? Это возможно! Просто пригласи друга на WhiteBIT и получай за это проценты.',
                        'Получай награду за каждого приглашенного друга на WhiteBIT! Отправляй друзьям реферальную ссылку и получай $2 за каждого зарегистрированного пользователя.'
                    ],
                    'en': [
                        'Do you want to receive passive income? Invite your friends to WhiteBIT and get 40% of each of their transaction fees.',
                        'Want to get a prize for doing nothing? It is possible! Just invite a friend to WhiteBIT and get rewarded!',
                        'Enjoy our referral program. Invite friends and get 40% of every fee paid by them. Moreover, receive $2 for each friend with KYC!'
                    ],
                    'ua': [
                        'Хочеш отримувати пасивний прибуток? Запрошуй друзів на WhiteBIT та отримуй $2 за кожного зареєстрованого за твоїм посиланням користувача.',
                        'Отримувати прибуток на біржі, нічого не роблячи? Це можливо! Просто запроси друзів на WhiteBIT та отримуй за це відсотки.',
                        'Відправляй друзям реферальне посилання та отримуй $2 за кожного зареєстрованого користувача. Запрошуй друзів на WhiteBIT та отримуй вигоду вже зараз!'
                    ]
                }
            },
            'ref_activate': {
                'ru': 'Эту ссылку вы уже можете отправлять друзьям. Пусть повторят ваш путь, за что вы получите $2 на свой кошелек за каждого друга!',
                'en': "Send this link to your friends, so that they could go the same way you did. If they do, you will receive $2 to the Balance!",
                'ua': 'Ви вже можете відправляти це посилання друзям. Нехай повторять ваш шлях, за що ви отримаєте $2 на свій гаманець!',
            },
            'stats': {
                'ru': [
                    'Статистика',
                    'Количество ваших рефералов: '
                ],
                'en': [
                    'Statistics',
                    'Your referrals number: '
                ],
                'ua': [
                    'Статистика',
                    'Кількість ваших рефералів: '
                ],
            }
        }

