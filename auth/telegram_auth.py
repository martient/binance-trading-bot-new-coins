import yaml
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


def load_telegram_creds(file) -> Updater:
    with open(file) as file:
        auth = yaml.load(file, Loader=yaml.FullLoader)
    updater = Updater(token=auth['telegram_token'])
    updater.start_polling()
    return updater, auth['telegram_tchat_id']
