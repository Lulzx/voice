import telepot
import requests
import os

TOKEN = ""

def handle(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)
	if content_type == 'audio':
		audiofile = msg['audio']
		flavor = telepot.flavor(msg)
		summary = telepot.glance(msg, flavor=flavor)
		print(flavor, summary)

def sendVoice(chat_id,file_name):
	url = "https://api.telegram.org/bot%s/sendVoice"%(TOKEN)
	files = {'audio': open(file_name, 'rb')}
	data = {'chat_id' : chat_id}
	r= requests.post(url, files=files, data=data)
	print(r.status_code, r.reason, r.content)

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
print('Listening ...')

while 1:
	time.sleep(10)
