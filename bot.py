from telegram.ext import Updater, CommandHandler
import setting

def greet_user(bot, update):
    print('Вызван /start')

def main():
    #mybot = Updater(setting.API_KEY, request_kwargs=setting.PROXY)
    mybot = Updater(setting.API_KEY)
 
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    
    mybot.start_polling()
    mybot.idle()
    
main()