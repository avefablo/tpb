from telegram.ext import Updater, CommandHandler


def start(bot, update):
    update.message.reply_text('Приветик')


def help_(bot, update):
    update.message.reply_text('Я помогу. Но не сегодня.')


def add_public(bot, update):
    update.message.reply_text('Окей. Вставь ссылку на паблик в ответ.')


def ask_for_all_pics(bot, update):
    update.message.reply_text('Вот все твои пикчи.')


def ask_for_pics_from_one_public(bot, update):
    update.message.reply_text(
        'Окей. Из какого паблика ты хочешь получить пикчи?')


def get_pics():
    pass


updater = Updater('316772437:AAH0AbTWmNcb0OlsTFvfso4hE4AyhjJuS-8')
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help_))
updater.dispatcher.add_handler(CommandHandler('addpub', add_public))
updater.dispatcher.add_handler(CommandHandler('getall', ask_for_all_pics))
updater.dispatcher.add_handler(CommandHandler('getone',
                                              ask_for_pics_from_one_public))

updater.start_polling()
updater.idle()
