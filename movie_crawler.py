import requests
import telegram
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler

bot = telegram.Bot(token='716338105:AAH6hTeQ5YIR_xNWCz8vzKVgJp49MigcaDI')
url = "http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20190616"

def interval_job():
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    imax = soup.select_one('span.imax')

    if(imax):
        imax = imax.find_parent('div', class_="col-times")
        title = imax.select_one('div.info-movie > a > strong').text.strip()
        bot.sendMessage(chat_id=560721873, text=title + "의 IMAX 예매가 열렸습니다.")
        scheduler.pause()
    
    
scheduler = BlockingScheduler()
scheduler.add_job(interval_job, 'interval', seconds=30)
scheduler.start()