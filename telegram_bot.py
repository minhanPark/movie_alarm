import telegram

bot = telegram.Bot(token='716338105:AAH6hTeQ5YIR_xNWCz8vzKVgJp49MigcaDI')

# for i in bot.getUpdates():
#     print(i.message)

bot.sendMessage(chat_id=560721873, text="반갑다 나는 텔레그램이다")