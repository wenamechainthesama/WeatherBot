from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


city_choice_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('Paris', callback_data='Paris'),
        InlineKeyboardButton('London', callback_data='London'),
        InlineKeyboardButton('Lisbon', callback_data='Lisbon')],

    [InlineKeyboardButton('Moscow', callback_data='Moscow'),
        InlineKeyboardButton('Madrid', callback_data='Madrid'),
        InlineKeyboardButton('San Francisco', callback_data='San Francisco')],

    [InlineKeyboardButton('Bangkok', callback_data='Bangkok'),
        InlineKeyboardButton('Hong Kong', callback_data='Hong Kong'),
        InlineKeyboardButton('Dubai', callback_data='Dubai')],     
], one_time_keyboard=True)