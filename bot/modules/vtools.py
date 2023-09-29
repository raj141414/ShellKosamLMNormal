from aiofiles.os import path as aiopath, makedirs
from aioshutil import move as aiomove
from os import path as ospath
from pyrogram.filters import command
from pyrogram.handlers import MessageHandler
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







bot.add_handler(MessageHandler(vtools, filters=command(BotCommands.vtoolsCommand) & CustomFilters.authorized))
