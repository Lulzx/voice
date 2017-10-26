import telepot
import requests
import os
import time
import urllib2

TOKEN = ""

def handle(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)
	if content_type == 'audio':
		audiofile = msg['audio']
		fileid = msg['audio']['file_id']
		flavor = telepot.flavor(msg)
		summary = telepot.glance(msg, flavor=flavor)
		print(flavor, summary)
		print(fileid)
		print(bot.getFile(file_id=fileid))
		os.system("wget https://api.telegram.org/file/bot" + TOKEN + "/" + bot.getFile(file_id=fileid)['file_path'] + " -O " + bot.getFile(file_id=fileid)['file_path'])
		os.system("ffmpeg -ss 60 -t 60 -y -i " + bot.getFile(file_id=fileid)['file_path'] + " -acodec libvorbis output.ogg")
		sendVoice(chat_id, "output.ogg")
	if msg["text"] == "/start":
		bot.sendMessage(chat_id,"Hello, please send me an MP3 file and I'll generate a preview")

def sendVoice(chat_id,file_name):
	url = "https://api.telegram.org/bot%s/sendVoice"%(TOKEN)
	files = {'voice': open(file_name, 'rb')}
	data = {'chat_id' : chat_id}
	r= requests.post(url, files=files, data=data)
	print(r.status_code, r.reason, r.content)

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
print('Listening ...')

while 1:
	time.sleep(10)
