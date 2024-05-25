"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters



logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


#PROXY = {
    #'proxy_url': 'socks5://t1.learn.python.ru:1080',
    #'urllib3_proxy_kwargs': {
        #'username': 'learn',
        #'password': 'python'
    #}



def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(text)

def planet_choice(update, context):
    # Получаем текст команды и делим его на части
    user_input = update.message.text.split()
    
    if len(user_input) < 2:
        update.message.reply_text("Пожалуйста, предоставьте наименование планеты")
        return
    
    # Получаем название планеты из команды
    planet_name = user_input[1].capitalize()
    
    try:
        # Получаем объект планеты из модуля ephem
        planet = getattr(ephem, planet_name)()
        planet.compute(ephem.now())
        
        # Определяем созвездие, в котором находится планета
        constellation = ephem.constellation(planet)
        
        # Формируем ответное сообщение
        response = f"Планета {planet_name} сейчас находится в созвездии {constellation[1]}. RA: {planet.ra}, Dec: {planet.dec}"
    except AttributeError:
        response = f"Планеты под названием {planet_name} не существует!"

    update.message.reply_text(response)

def main():
    mybot = Updater("7133966741:AAF8tH51ZfWjoEs5nz8STG699MSNxr-oeJw", use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_choice))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
