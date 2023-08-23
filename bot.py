# import telebot
# from telebot import types
#
# botTimeWeb = telebot.TeleBot('6447698709:AAFj-anF1rSSSdoMrCDt97AK6Wzyn83zvZQ')
#
#
# @botTimeWeb.message_handler(commands=['start'])
# def startBot(message):
#     first_mess = f"<b>{message.from_user.first_name}</b>, привет!\nХочешь получать ежедневную порцию лучших бизнес идей??"
#     markup = types.InlineKeyboardMarkup()
#     button_yes = types.InlineKeyboardButton(text='Да, прям!', callback_data='yes')
#     markup.add(button_yes)
#     button_why = types.InlineKeyboardButton(text='Зачем мне это?', callback_data='why')
#     markup.add(button_why)
#     button_no = types.InlineKeyboardButton(text='Мне не интересно', callback_data='no')
#     markup.add(button_no)
#     botTimeWeb.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)
#
#
# @botTimeWeb.callback_query_handler(func=lambda call: True)
# def response(function_call):
#     if function_call.message:
#         if function_call.data == "yes":
#             second_mess = "Я Ади Азаматов!!!"
#             markup = types.InlineKeyboardMarkup()
#             markup.add(types.InlineKeyboardButton("Перейти на сайт", url="https://t.me/dariga69"))
#             botTimeWeb.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
#             botTimeWeb.answer_callback_query(function_call.id)
#         elif function_call.data == 'why':
#             second_mess = "по работе)"
#             markup = types.InlineKeyboardMarkup()
#             markup.add(types.InlineKeyboardButton("Тормоз", url="https://avtokafe.ru/tormoza/"))
#             botTimeWeb.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
#             botTimeWeb.answer_callback_query(function_call.id)
#         elif function_call.data == 'no':
#             second_mess = "интересует"
#             markup = types.InlineKeyboardMarkup()
#             markup.add(types.InlineKeyboardButton("Можешь нажать", url="https://www.youtube.com/watch?v=G2huGX6z-RU"))
#             botTimeWeb.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
#             botTimeWeb.answer_callback_query(function_call.id)
#
#
# botTimeWeb.infinity_polling()