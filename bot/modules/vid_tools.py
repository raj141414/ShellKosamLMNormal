from pyrogram.filters import command
from pyrogram.handlers import MessageHandler
from aiofiles.os import path as aiopath, makedirs
from aioshutil import move as aiomove
from os import path as ospath
from pyrogram.types import Message
from random import SystemRandom
from string import ascii_letters, digits

from bot import bot, config_dict, download_dict, download_dict_lock
from bot.helper.ext_utils.bot_utils import new_task
from bot.helper.ext_utils.fs_utils import get_path_size
from bot.helper.listeners.tasks_listener import MirrorLeechListener
from bot.helper.mirror_utils.status_utils.local_status import LocalStatus
from bot.helper.telegram_helper.bot_commands import BotCommands
from bot.helper.telegram_helper.filters import CustomFilters
from bot.helper.telegram_helper.message_utils import sendMessage, sendStatusMessage

def send_menu(message):
    # Create a custom keyboard (menu)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Option 1")
    item2 = types.KeyboardButton("Option 2")
    item3 = types.KeyboardButton("Option 3")
    markup.add(item1, item2, item3)

    # Send a welcome message with the menu
    bot.send_message(message.chat.id, "Welcome to the Bot Menu!", reply_markup=markup)

# Define handlers for each menu option
@bot.message_handler(func=lambda message: message.text == "Option 1")
def option1(message):
    bot.send_message(message.chat.id, "You selected Option 1!")

@bot.message_handler(func=lambda message: message.text == "Option 2")
def option2(message):
    bot.send_message(message.chat.id, "You selected Option 2!")

@bot.message_handler(func=lambda message: message.text == "Option 3")
def option3(message):
    bot.send_message(message.chat.id, "You selected Option 3!")

# Polling to continuously check for new messages
bot.polling()





bot.add_handler(MessageHandler(vtools, filters=command(BotCommands.vid_toolsCommand) & CustomFilters.authorized))
