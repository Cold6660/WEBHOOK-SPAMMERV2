import requests
import colorama
import asyncio
import time
import threading
import os
import ctypes
from colorama import Fore, Style
from threading import Thread
from sys import stdout
from requests import Session
from time import strftime, gmtime

sent = 0
session = Session()
b = Style.BRIGHT
os = os.system
os('cls')
ctypes.windll.kernel32.SetConsoleTitleW(f"[WEBHOOK SPAMMER] By Cold#6660 & never#6666 | Dont Skid Me ;) ")

print(f"""

{b+Fore.BLUE}
 $$$$$$\  $$$$$$\ $$\      $$$$$$$\        
$$  __$$\$$  __$$\$$ |     $$  __$$\       
$$ /  \__$$ /  $$ $$ |     $$ |  $$ |      
$$ |     $$ |  $$ $$ |     $$ |  $$ |      
$$ |     $$ |  $$ $$ |     $$ |  $$ |      
$$ |  $$\$$ |  $$ $$ |     $$ |  $$ |      
\$$$$$$  |$$$$$$  $$$$$$$$\$$$$$$$  |      
 \______/ \______/\________\_______/  
            | |                                   
            |_|                                   
{b+Fore.BLUE} > {Fore.RESET}Webhook Spammer
{b+Fore.BLUE} > {Fore.RESET}Creator: Cold#6660
""")

def sendtowebhook(webhook, message, username):
    data = {
        'content': message,
        'username': username
    }
    try:
        while True:
            requests.post(webhook, data=data)
    except KeyboardInterrupt:  # prevents error trace on keyboardinterrupt and exits cleanly
        exit()

print(f"[{Fore.GREEN}>{Fore.RESET}] Webhook link ")
webhook = input("#root~Cold~ ")
if webhook == '':  # script will not work without specifying a webhook link, so exit
    print('You need to specify a webhook link for this to work, exiting...')
    exit()
    
print(f"[{Fore.GREEN}>{Fore.RESET}] Message ")
message = input("#root~Cold~ ")
if message == '':  # no message will cause the webhook message not to send, so default to specified default
    message = defaultmessage
    print('Using default message...')

    
print(f"[{Fore.GREEN}>{Fore.RESET}] Username ")
username = input("#root~Cold~ ")
if username == '':  #  no username will default to a specified default
    username = defaultusername
    print('Using default username...')


try:
    print(f"[{Fore.GREEN}>{Fore.RESET}] Threads ")
    threads = int(input("#root~Cold~ "))
    if threads < 1: # prevent negative/0 threads from breaking the script
        print('Negative or no threads, defaulting to 1...')
        threads = 1
except ValueError:  # prevents ValueError if the result cannot be converted to a string
    threads = 1
    print('Invalid amount of threads, defaulting to 1...')

print('Webhook destroyer starting, press CTRL+C to stop.')

for x in range(threads):
    thread = threading.Thread(
        target=sendtowebhook(webhook, message, username), args=(1,))
    thread.start()
    # threading actually doesn't help very much due to discord's rate limiting
try:
    time.sleep(1)
    r = requests.post(webhoo, json=webhook_embed)
    
except:
     pass
