import telegram

bot = telegram.Bot(token=myToken)

# for i in bot.getUpdates():
#     print(i.message)

bot.sendMessage(chat_id=560721873, text="반갑다 나는 텔레그램이다")
