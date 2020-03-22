import telegram
token = '1080635812:AAH7lMSdM6i-aqMB3X0XI4RD0SNum207Ge0'
bot = telegram.Bot(token=token)

for i in bot.getUpdates():
    print(i.message)

bot.sendMessage(chat_id='993720824', text= 'test1')
