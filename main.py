import telebot

from services.valid_url import is_valid_url
from services.print_articles import print_articles
from config import (
    TOKEN_API,
    STARTING_RESPONSE,
    TAKING_LINK_RESPONSE,
    TAKING_LINK_BUT_NOTHING_RESPONSE,
    LINK_ALREADY_EXISTS,
    LINK_SAVED,
    LINK_INCORRECT,
    ACTION_NOT_FOUND,
)
from repository.database_manager import DatabaseManager


bot = telebot.TeleBot(TOKEN_API)
db_manager = DatabaseManager("links.db")
db_manager.create_table()


@bot.message_handler(commands=["start"])
def cmd_start(message) -> None:
    bot.send_message(message.chat.id, STARTING_RESPONSE)


@bot.message_handler(commands=["get_article"])
def cmd_get_article(message) -> None:
    id_chat = message.chat.id
    text = db_manager.get_random_article(id_chat)
    if bool(text):
        bot.send_message(id_chat, TAKING_LINK_RESPONSE.format(text))
    else:
        bot.send_message(id_chat, TAKING_LINK_BUT_NOTHING_RESPONSE)


@bot.message_handler(commands=["get_all_articles"])
def cmd_get_all_articles(message) -> None:
    id_chat = message.chat.id
    text = db_manager.get_all_articles(id_chat)
    text_for_print = print_articles(text)
    if bool(text):
        bot.send_message(id_chat, TAKING_LINK_RESPONSE.format(text_for_print))
    else:
        bot.send_message(id_chat, TAKING_LINK_BUT_NOTHING_RESPONSE)


@bot.message_handler(func=lambda message: True)
def handle_all_message(message) -> None:
    id_chat = message.chat.id
    text = message.text.strip()
    if text.startswith("http") or is_valid_url(text):
        if is_valid_url(text):
            if not db_manager.check_link_exists(text, id_chat):
                db_manager.insert_link(text, id_chat)
                bot.send_message(id_chat, LINK_SAVED)
            else:
                bot.send_message(id_chat, LINK_ALREADY_EXISTS)
        else:
            bot.send_message(id_chat, LINK_INCORRECT)
    else:
        bot.send_message(
            id_chat,
            ACTION_NOT_FOUND,
        )


try:
    bot.infinity_polling()
except Exception as ex:
    print(ex)
