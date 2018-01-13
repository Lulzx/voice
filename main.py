import telepot
import requests
import os
import time
import urllib2
from mutagen.mp3 import MP3
from mutagen.mp4 import MP4

TOKEN = ""

def handle(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)
	if content_type == 'audio':
		audiofile = msg['audio']
		fileid = audiofile['file_id']
		flavor = telepot.flavor(msg)
		summary = telepot.glance(msg, flavor=flavor)
		print(flavor, summary)
		print(fileid)
		print(bot.getFile(file_id=fileid))
		filename = bot.getFile(file_id=fileid)['file_path']
		os.system("wget https://api.telegram.org/file/bot" + TOKEN + "/" + filename + " -O " + filename)
		if ".mp3" in filename:
			audio = MP3(filename)
			length = audio.info.length * 0.33
		if ".m4a" in filename:
			audio = MP4(filename)
			length = audio.info.length * 0.33
		if audio.info.length > l2:
			os.system("ffmpeg -ss " + str(length) + " -t 60 -y -i " + filename + " -strict -2 -ac 1 -map 0:a -codec:a opus -b:a 128k -vn output.ogg")
		else:
			os.system("ffmpeg -ss 0 -t 60 -y -i " + filename + " -strict -2 -ac 1 -map 0:a -codec:a opus -b:a 128k -vn output.ogg")
		sendVoice(chat_id, "output.ogg")

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
