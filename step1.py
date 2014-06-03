import requests
from BeautifulSoup import BeautifulSoup
from sqlalchemy import *
url= 'http://www.elcaribe.com.do/'
soup = BeautifulSoup(requests.get(url).text)

db = create_engine('sqlite:///ratexchange.db')
metadata = MetaData(db)
rtexch = Table('rates_exchanges', metadata,
		Column('currency', String(5), primary_key=True),
		Column('amount', String(16)))


def setup_db():
	rtexch.create()



def save_to_db(currency, amount):
	try:
	    i = rtexch.insert()
	    i.execute(currency=currency, amount=amount)
	except IntegrityError:
		u = rtexch.update().where(rtexch.c.currency==currency).values(amount=amount)
		u.execute()



def search_exchange():
	dolar = soup.find("div", {"class": "dolar"})
	for li in dolar.findAll('li'):
		currency, amount = li.text.split('RD$')
		save_to_db(currency, amount)


	

if __name__ == '__main__':
    setup_db()
    search_exchange()

