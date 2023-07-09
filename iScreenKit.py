import requests
import json
import time
import re
import threading

print('''
   ▄▄                                                                 ▄▄        
   ██  ▄█▀▀▀█▄█                                         ▀████▀ ▀███▀  ██   ██   
      ▄██    ▀█                                           ██   ▄█▀         ██   
 ▀███ ▀███▄    ▄██▀██▀███▄███  ▄▄█▀██  ▄▄█▀██▀████████▄   ██ ▄█▀    ▀███ ██████ 
   ██   ▀█████▄█▀  ██  ██▀ ▀▀ ▄█▀   ██▄█▀   ██ ██    ██   █████▄      ██   ██   
   ██ ▄     ▀███       ██     ██▀▀▀▀▀▀██▀▀▀▀▀▀ ██    ██   ██  ███     ██   ██   
   ██ ██     ███▄    ▄ ██     ██▄    ▄██▄    ▄ ██    ██   ██   ▀██▄   ██   ██   
 ▄████▄▀█████▀ █████▀▄████▄    ▀█████▀ ▀█████▀████  ████▄████▄   ███▄████▄ ▀████
 
                           1 YEAR LICENSE GEN

                       [+] DEVELOPED BY DE3P4K [+]
                    [+] linktr.ee/deepaksinghmalik [+]
''')

generated_codes = 0
num_codes = 0
stop_generation = False
lock = threading.Lock()

def process_email():
    global generated_codes
    global stop_generation
    while True:
        try:
            mailurl = 'https://www.developermail.com/api/v1/mailbox'
            mailheaders = {
                'accept': 'application/json'
            }

            mailresponse = requests.put(mailurl, headers=mailheaders)
            mailjson = json.loads(mailresponse.text)
            name = mailjson['result']['name']

            token = mailjson['result']['token']

            url = 'https://www.iscreenkit.com/giveaway/tickcoupon'

            headers = {
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-US,en;q=0.9,en-IN;q=0.8',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Origin': 'https://www.iscreenkit.com',
                'Referer': 'https://www.iscreenkit.com/giveaway/tickcoupon',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36 Edg/116.0.0.0',
                'X-October-Request-Flash': '1',
                'X-October-Request-Handler': 'onGiveaway',
                'X-Requested-With': 'XMLHttpRequest'
            }

            data = f'email={name}%40developermail.com'

            response = requests.post(url=url, headers=headers, data=data)

            inboxurl = f'https://www.developermail.com/api/v1/mailbox/{name}'
            inboxheaders = {
                'accept': 'application/json',
                'X-MailboxToken': f'{token}',
                'Content-Type': 'application/json'
            }

            time.sleep(10)

            response = requests.get(inboxurl, headers=inboxheaders)

            jsonresponse = json.loads(response.text)
            if jsonresponse['result'] == []:
                time.sleep(5)
                response = requests.get(inboxurl, headers=inboxheaders)

                jsonresponse = json.loads(response.text)
                if jsonresponse['result'] == []:
                    pass
                else:
                    msgid = jsonresponse['result'][0]

            else:
                msgid = jsonresponse['result'][0]

            msgurl = f'https://www.developermail.com/api/v1/mailbox/{name}/messages'
            msgheaders = {
                'accept': 'application/json',
                'X-MailboxToken': f'{token}',
                'Content-Type': 'application/json'
            }

            msgdata = [msgid]
            msgres = requests.post(msgurl, headers=msgheaders, data=json.dumps(msgdata))
            msgres = json.dumps(msgres.text)

            activation_code = re.search(r'<strong>([\w-]+)=', msgres).group(1)
            if activation_code is not None:
                with lock:
                    generated_codes += 1
                    if generated_codes > num_codes:
                        stop_generation = True
                        break
                    
                    output = name + '@developermail.com : ' + activation_code
                    print(' '+output)
                    with open('iScreenKit 1 Year.txt', 'a') as f:
                        f.write(output + '\n')

        except:
            pass

        if stop_generation:
            break


# Get the number of codes to generate from the user
num_codes = int(input(" Enter the number of codes to generate: "))
print('\n')
# Create and start 10 threads
threads = []
for _ in range(num_codes):
    thread = threading.Thread(target=process_email)
    thread.start()
    threads.append(thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()

# Wait for user to press Enter to exit
input("\n Done. Press Enter to Exit... ")
