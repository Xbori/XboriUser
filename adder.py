from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest
import configparser
import os
import sys
import csv
import traceback
import time
import random

re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"

print (re+"██╗░░██╗██████╗░░█████╗░██████╗░██╗")
print (gr+"╚██╗██╔╝██╔══██╗██╔══██╗██╔══██╗██║")
print (re+"░╚███╔╝░██████╦╝██║░░██║██████╔╝██║")
print (gr+"░██╔██╗░██╔══██╗██║░░██║██╔══██╗██║")
print (re+"██╔╝╚██╗██████╦╝╚█████╔╝██║░░██║██║")
print (gr+"╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝")


print (cy+"version : 1.01")
print (cy+"Telegramda Xbori yə abunə olduğunuzdan əmin olun")
print (cy+"https://t.me/Xbori")

print (re+"QEYD :")
print ("1. Telegram yalnız bir istifadəçi tərəfindən qrupa 200 üzv əlavə etməyə icazə verir.")
print ("2. Daha çox üzv əlavə etmək üçün birdən çox Telegram hesabından istifadə edə bilərsiniz.")
print ("3. Hər dəfə qrupa yalnız 50 üzv əlavə edin, əks halda daşqın xətası alacaqsınız.")
print ("4. Sonra 15-30 dəqiqə gözləyin, sonra yenidən üzvləri əlavə edin.")
print ("5. Qrupunuzda İstifadəçi İcazəsininin Açığ olduğundan əmin olun")

cpass = configparser.RawConfigParser()
cpass.read('config.data')

try:
    api_id = cpass['cred']['id']
    api_hash = cpass['cred']['hash']
    phone = cpass['cred']['phone']
    client = TelegramClient(phone, api_id, api_hash)
except KeyError:
    os.system('clear')
    banner()
    print(re+"[!] run python setup.py first !!\n")
    sys.exit(1)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    os.system('clear')
    banner()
    client.sign_in(phone, input(gr+'[+] Kodu daxil edin: '+re))

users = []
with open(r"members.csv", encoding='UTF-8') as f:  #Enter your file name
    rows = csv.reader(f,delimiter=",",lineterminator="\n")
    next(rows, None)
    for row in rows:
        user = {}
        user['username'] = row[0]
        user['id'] = int(row[1])
        user['access_hash'] = int(row[2])
        user['name'] = row[3]
        users.append(user)

chats = []
last_date = None
chunk_size = 200
groups = []

result = client(GetDialogsRequest(
    offset_date=last_date,
    offset_id=0,
    offset_peer=InputPeerEmpty(),
    limit=chunk_size,
    hash=0
))
chats.extend(result.chats)

for chat in chats:
    try:
        if chat.megagroup == True:
            groups.append(chat)
    except:
        continue

print(gr+'İstifadəçiləri əlavə etmək üçün qrup seçin:'+cy)
i = 0
for group in groups:
    print(str(i) + '- ' + group.title)
    i += 1

g_index = input(gr+"Nömrə daxil edin: "+re)
target_group = groups[int(g_index)]

target_group_entity = InputPeerChannel(target_group.id, target_group.access_hash)

mode = int(input(gr+"İstifadəçi adı ilə əlavə etmək üçün 1 və ya ID ilə əlavə etmək üçün 2 daxil edin: "+cy))

n = 0

for user in users:
    n += 1
    if n % 80 == 0:
        sleep(60)
    try:
        print("Adding {}".format(user['id']))
        if mode == 1:
            if user['username'] == "":
                continue
            user_to_add = client.get_input_entity(user['username'])
        elif mode == 2:
            user_to_add = InputPeerUser(user['id'], user['access_hash'])
        else:
            sys.exit("Yanlış Rejim Seçildi. Zəhmət olmasa bir daha cəhd edin.")
        client(InviteToChannelRequest(target_group_entity, [user_to_add]))
        print("60-180 Saniyə Gözləyin...")
        time.sleep(random.randrange(0, 5))
    except PeerFloodError:
        print("Telegramdan Daşqın Xətası Alınır. Skript indi dayanır. Bir müddət sonra yenidən cəhd edin.")
        print("Waiting {} seconds".format(SLEEP_TIME_2))
        time.sleep(SLEEP_TIME_2)
    except UserPrivacyRestrictedError:
        print("İstifadəçinin məxfilik parametrləri bunu etməyə imkan vermir. Atlama.")
        print("5 saniyə gözləyin...")
        time.sleep(random.randrange(0, 5))
    except:
        traceback.print_exc()
        print("Gözlənilməz Xəta")
        continue
