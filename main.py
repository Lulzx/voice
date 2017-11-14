import telepot
import requests
import os
import time
import urllib2
from mutagen.mp3 import MP3

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
		audio = MP3(bot.getFile(file_id=fileid)['file_path'])
		length = audio.info.length * 0.33
		os.system("ffmpeg -ss " + str(length) + " -t 60 -y -i " + bot.getFile(file_id=fileid)['file_path'] + " -strict -2 -ac 1 -map 0:a -codec:a opus -b:a 128k -vbr off output.ogg")
		sendVoice(chat_id, "output.ogg")
	if msg["text"] == "/start":
		bot.sendMessage(chat_id,"Hello, please send me a MP3 file and I'll generate a preview")

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
