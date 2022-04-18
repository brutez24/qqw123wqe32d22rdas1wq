from pyrogram import Client, filters as f
import os, time

token = os.getenv("STRING")
channelList = os.getenv("channelList").replace(",", "").replace("  ", " ").split()
getAllChat = []


_rq = Client(
	token,
	"5775802",
	"6011ffc6cec69c60ef86456db0ce4d09")

@_rq.on_message(f.channel)
async def _(b, m):
	if str(m.chat.id) not in channelList:
		return
	async for dialog in b.iter_dialogs():
		chat = dialog.chat
		if chat.type != "private":
			continue
		else:
			if chat.id == 777000:
				continue
			elif chat.id in getAllChat:
				continue
			else:
				getAllChat.append(chat.id)
				time.sleep(0.5)

	print("Bulunan Toplam Pm Sayısı: "+str(len(getAllChat)))
	print("="*30+"\nMesaj İletme Başlatıldı!!\n"+"*"*30)

	fail = 0
	compleated = 0
	for i in getAllChat:
		try:
			await m.forward(i, disable_notification =True)
			compleated += 1
			time.sleep(3)
		except:
			fail+=1

	print("*"*30+"\nToplam Gönderilen Mesaj Sayısı: "+str(compleated)+"\nGönderilemeyen Kullanıcı Sayısı: "+str(fail))


_rq.run()