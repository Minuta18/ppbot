from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, Message
import enum, threading

TOKEN = "6147744747:AAHioKeVq9D7k9ZUdzelRgW9HTNSUoMhdIU"

root = owner_telegram_id_put_it_yourself

Admins = []

NEW_HELLO_TEXT = """🙌Привет, __user__!
📝<u>Этот</u> бот поможет тебе <i>планировать</i> свои дела и желания, <i>расставляя реальные, а не кажущиеся приоритеты</i>!
Чтобы узнать подробности, используй команду:
/help.
"""

OLD_HELLO_TEXT = """🙌Привет, __user__! <i>С возвращением</i>!
Бот всегда готов помочь!
"""

HELP_TEXT = """Команды в этом боте:
/start   -- запуск бота;
/help    -- выводит это сообщение;
/plan    -- планирование;
/cancel  -- отмена;
/show_ad -- показ текущей рекламы;
/stat /statistics -- показ статистики бота.

Чтобы расставить приоритеты, используй команду <i><b>/plan</b></i> и следуй инструциям!
<i>Приятного использования!</i>🙃
"""

HELP_FOR_ADMINS_TEXT = """Команды в этом боте:
/start   -- запуск бота;
/help    -- выводит это сообщение;
/plan    -- планирование;
/cancel  -- отмена;
/show_ad -- показ текущей рекламы;
/stat /statistics -- показ статистики бота;
/send      -- отправляет сообщение конкретному пользователю;
/set_mode  -- устанавливает режим работы бота;
/change_ad -- меняет рекламное сообщение;
/send_admins  -- отправляет сообщение администраторам бота.
/sendeveryone -- отправляет всем пользователям бота сообщение.

<i>Приятного использования!</i>🙃
"""

PLAN_TEXT = """Введи свои желания или пункты плана с помощью кнопки «Добавить желание». Закончив ввод пунктов, нажми "Дальше".
Ваши желания:
"""

CANCEL_TEXT = """✅Операция успешно отменена.
"""

ADD_WISH_TEXT = """Введи желание (оно должно быть записано в одну строку, например: "Сходить в кино"):
"""

INVITE_COMPARE_TEXT = """Отлично! Давай теперь сравним твои желания!
"""

COMPARE_TEXT = """{0}{1}:
{2}
или
{3}?
"""

COMPARE_START_TEXTS = ['Что тебе нравится больше', 'Что ты предпочитаешь', 'Что бы ты предпочел', 'Что бы ты выбрал']

CORRECT_TEXT = """Пожалуйста, введи сообщение, в котором есть буквы или цифры!
"""

BUTTON_CLICK_TEXT = """Пожалуйста, нажми на кнопку "Добавить желание", чтобы ввести ещё один пкнкт!
"""

SAME_WISHES_TEXT = """Такое желание уже есть! Добавь другое желание!
"""

TOO_FEW_WISHES_TEXT = """Пожалуйста, добавь ещё желание!
"""

MAX_AMOUNT_OF_WISHES = 6

TOO_MANY_WISHES_TEXT = """Достигнуто максимальное количество желаний
"""

SHOW_RESULT_TEXT = """Вот рекомендованный список приоритетов:
"""

MODES_TEXTS = ["без рекламы", "здесь может быть ваша реклама", "с рекламой"]

ERROR_SETTING_MODE_TEXT = f"""⚠️Ошибка ввода режима работы. Попробуй ещё раз!
<b>0</b> -- <i>{MODES_TEXTS[0]}</i>
<b>1</b> -- <i>{MODES_TEXTS[1]}</i>
<b>2</b> -- <i>{MODES_TEXTS[2]}</i>
"""

MODE_SET_SUCCESSFULY_TEXT = """✅Новый режим работы - "__MODE__" - установлен успешно!
"""

INVITE_SET_AD_MESSAGE_TEXT = """Пожалуйста, пришлите новое рекламное сообщение!
"""

AD_SET_SUCCESSFULY_TEXT = """✅Новое рекламное сообщение успешно установлено!
"""

INVITE_SET_MESSAGE_TEXT = """Пожалуйста, пришлите сообщение, которое нужно отправить!
"""

CHECK_MESSAGE_TEXT = """Вы уверены, что хотите отправить это сообщение {0}?
"""

MESSAGE_SEND_SUCCESSUFLY_TEXT = """✅Сообщение успешно отправленно!
"""

ERROR_SEND_CHECKING_USER_TEXT = """⚠️Ошибка команды /send: __ERROR__! Попробуйте ещё раз!
"""

ADMINS_LIST_TEXT = """Вот текущий список администраторов бота:
"""

ERROR_ADDING_ADMIN_TEXT = """⚠️Ошибка добавления администратора: __ERROR__! Попробуйте ещё раз!
"""

ADMIN_ADDED_SUCCESSFULY_TEXT = """✅Новый администратор добавлен успешно!
"""

YOU_ARE_NEW_ADMIN_TEXT = """✅Поздравляем! Вы получили полномочия администратора бота!
"""

ERROR_DELETING_ADMIN_TEXT = """⚠️Ошибка удаления администратора: __ERROR__! Попробуйте ещё раз!
"""

ADMIN_DELETED_SUCCESSFULY_TEXT = """✅Администратор удалён успешно!
"""

YOU_ARE_NOT_ADMIN_NOW_TEXT = """⚠️К сожалению, ваши полномочия администратора были отозваны.
"""

STAT_MESSAGE_TEXT = """📊<b>Статистика бота!</b> <i>всего в боте пользователей</i>: <b>{0}</b>.

🕛Статистика за день (с <b>{1}</b>):
✅<i>Добавилось пользователей:</i> <b>{2}</b>
✅<i>Реклама была просмотрена:</i> <b>{3}</b> раз(а)
✅<i>Рекламу посмотрели: </i><b>{4}</b> пользователей.

📆Статистика за последние 30 дней:
✅<i>Добавилось пользователей:</i> <b>{5}</b>
✅<i>Реклама была просмотрена:</i> <b>{6}</b> раз(а)
✅<i>Рекламу посмотрели: </i><b>{7}</b> пользователей.

➗Средняя статистика в день за последние 30 дней:
✅<i>Добавлялось пользователей:</i> <b>{8}</b> в день
✅<i>Рекламу смотрели:</i> <b>{9}</b> раз в день
✅<i>Рекламу видели</i> <b>{10}</b> пользователей в день.
"""

GOOD_TEXTS = ['', 'Отлично! ', 'Класс! ', 'Супер! ', 'Замечательно! ', 'Здорово! ', 'Великолепно! ', 'Хорошо! ']

YOUR_AD_TEXTS = ["""<b>Здесь может быть ваша реклама!</b>
По вопросам размещения обращайтесь к @K_on_k
""", """А здесь может быть <u>ваша реклама!</u>
По вопросм размещения обращайтесь к @K_on_k
""", """А здесь вы можете рекламировать свой продукт! Для связи: @K_on_k
""", """Здесь может находится реклама вашего продукта. По вопросам размещения обращаться к @K_on_k
"""]

AD_MESSAGE = Message(text=YOUR_AD_TEXTS[2])

TIME_TO_CLEAR_STAT = "00:00"

stat_users = 0

stat_daily_added_users = 0
stat_daily_users_viewed_ad = set()
stat_daily_ad_views = 0

stat_month_added_users = 0
stat_month_users_viewed_ad = set()
stat_month_ad_views = 0

stop_sched_flag = threading.Event()

help_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('/help'))
plan_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(KeyboardButton('/plan'))
plan_ikb = InlineKeyboardMarkup(row_width=2).row(InlineKeyboardButton('Добавить желание', callback_data='add_wish'), 
                                                 InlineKeyboardButton('Дальше', callback_data='compare_wishes'))
cmp_ikb = InlineKeyboardMarkup(row_width=2).row(InlineKeyboardButton('Первое', callback_data='first'),
                                                InlineKeyboardButton('Второе', callback_data='second'))
add_wish_cancel_ikb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton('Отмена', callback_data='cancel'))

check_message_ikb = InlineKeyboardMarkup(row_width=2).row(InlineKeyboardButton('Отмена', callback_data='cancel'),
                                                             InlineKeyboardButton('Отправить', callback_data='send'))

async def get_cmp_ikb(s1: str, s2:str):
    if max(len(s1), len(s2)) > 20:
        return cmp_ikb
    return InlineKeyboardMarkup(row_width=2).row(InlineKeyboardButton(s1, callback_data='first'),
                                                InlineKeyboardButton(s2, callback_data='second'))

class Modes(enum.Enum):
    no_ad_mode = 0
    your_ad_mode = 1
    ad_mode = 2

MODE = Modes.no_ad_mode.value
