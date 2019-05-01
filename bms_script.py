import json
import requests
import time
from bs4 import BeautifulSoup
import smtplib
import datetime
import os


def send_email(TO, T_NAME):
    TIME = datetime.datetime.now()
    GMAIL_USER = 'YOUR_GMAIL_USERNAME'
    GMAIL_PASS = 'YOUR_GMAIL_PASSWORD'
    SUBJECT = 'BMS: '+T_NAME +' '+ str(TIME)
    TEXT = T_NAME + ' Appears to be online!!!!-CHECK BookMYShow NOW! ' 
    print("Sending Email")
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(GMAIL_USER, GMAIL_PASS)
    header = 'To:' + TO + '\n' + 'From: ' + GMAIL_USER
    header = header + '\n' + 'Subject:' + SUBJECT + '\n'
    print header
    msg = header + '\n' + TEXT + ' \n\n'
    smtpserver.sendmail(GMAIL_USER, TO, msg)
    smtpserver.close()

def main():
	while True:
		#emails of all the people you want the notification to be sent. Should be atleat 2 emails.
		emails = ('email1@gmail.com','email2@gmail.com')
		os.system('curl -s https://in.bookmyshow.com/buytickets/avengers-endgame-hyderabad/movie-hyd-ET00100559-MT/20190426 | grep "JSON.parse" | grep "showDates" | cut -d " " -f12- > /tmp/tdata')
		os.system('''python -c "s = open('/tmp/tdata','r').read()[28:-5:]; file =open('/tmp/sorteddata', 'w'); file.write(s) "''')
		s = open('/tmp/sorteddata','r').read()
		data = s.replace('\\', '')
		obj = json.loads(data)
		print str(datetime.datetime.now())+' Checking For IMAX LARGE SCREEN ON 26 APRIL 2019 '
		for i in obj['aiSD']:
			if (i['VenueCode']=='PRHY' and i['DateCode']=='20190426'):
				for x in emails:
		                        T_NAME = "LARGE SCREEN - 26 APRIL 2019"
                        		send_email(x,T_NAME)
			else:
                		continue
		time.sleep(150)


if __name__ == '__main__':
    main()
