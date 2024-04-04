from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def generate_categories(lst: list):
    markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    category_buttons = []

    for category in lst:
        btn = KeyboardButton(text=category)
        category_buttons.append(btn)

    markup.add(*category_buttons)

    return markup
