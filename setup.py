#!/bin/env python3
# code by : Termux Professor

"""

you can re run setup.py 
if you have added some wrong value

"""
import os, sys
import configparser
re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"
def banner():
	os.system('clear')
	print(f"""
{gr}██╗░░██╗██████╗░░█████╗░██████╗░██╗
{re}╚██╗██╔╝██╔══██╗██╔══██╗██╔══██╗██║
{gr}░╚███╔╝░██████╦╝██║░░██║██████╔╝██║
{re}░██╔██╗░██╔══██╗██║░░██║██╔══██╗██║
{gr}██╔╝╚██╗██████╦╝╚█████╔╝██║░░██║██║
{re}╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝
	
	           Version : 2.02
 {re}Telegramda Xbori yə abunə olduğunuzdan əmin olun
   {cy}https://t.me/Xbori
	""")
banner()
print(gr+"[+] Tələblər quraşdırılır...")
os.system('python3 -m pip install telethon')
os.system('pip3 install telethon')
banner()
os.system("config.data-ya toxunun")
cpass = configparser.RawConfigParser()
cpass.add_section('cred')
xid = input(gr+"[+] APİ ID daxil edin: "+re)
cpass.set('cred', 'id', xid)
xhash = input(gr+"[+] APİ HASH daxil edin : "+re)
cpass.set('cred', 'hash', xhash)
xphone = input(gr+"[+] telefon nömrəsini daxil edin: "+re)
cpass.set('cred', 'phone', xphone)
setup = open('config.data', 'w')
cpass.write(setup)
setup.close()
print(gr+"[+] quraşdırma tamamlandı!")
print(gr+"[+] indi istənilən aləti işlədə bilərsiniz!")
print(gr+"[+] docs 4 quraşdırma və api quraşdırmasını oxumağınızdan əmin olun")
print(gr+"[+] Telegram - https://t.me/Xbori")
