import requests
import random
import string
import threading
from colorama import init, Fore, Style
import time
import os

def generate_random_string(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def generate_account(password):
    url = 'https://v1.brain.fm/signup'

    headers = {
        'Origin': 'https://v1.brain.fm',
        'Referer': 'https://v1.brain.fm/redeem/gcp',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.0.0'
    }

    email = generate_random_string(10)

    payload = {
        "type": "SIGNUP",
        "email": f"{email}@yopmail.net",
        "password": f"{password}",
        "name": "DE3P4K",
        "token": "gcp",
        "consent": {},
    }

    try:
        response = requests.post(url=url, headers=headers, data=payload)
        if 'Signed up and logged in' in response.text:
            print(Fore.GREEN + f'   {email}@yopmail.net:{password}' + Style.RESET_ALL)
            with open('Brain.fm.txt', 'a') as f:
                f.write(f'{email}@yopmail.net:{password}\n')
        elif 'error' in response.text:
            print(Fore.RED + '   '+response.text + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f'Error : {e}' + Style.RESET_ALL)

def warning():
    os.system('cls')
    input('''
        ###############################################
        #          BRAIN.FM ACCOUNT GENERATOR         #
        ###############################################
        '''
        + Fore.YELLOW + '''
                       ⚠️  IMPORTANT ⚠️
          
         This service is intended for personal use only.
    To prevent abuse and ensure fair access for everyone, we
    have limited the number of accounts that can be generated
   to 10 per user. If you have already generated 10 accounts,
   please refrain from running this script multiple times or
                creating additional accounts.

   Creating multiple accounts for malicious purposes is
                      STRICTLY PROHIBITED.
        Thank you for your understanding and cooperation.\n
        ''' + Style.RESET_ALL +  
        '''            Enjoy using Brain.fm! ❣️

   Press ENTER to Continue.''')

def main():
    os.system('cls')
    print('''
    
      ██████╗ ██████╗  █████╗ ██╗███╗   ██╗   ███████╗███╗   ███╗
      ██╔══██╗██╔══██╗██╔══██╗██║████╗  ██║   ██╔════╝████╗ ████║
      ██████╔╝██████╔╝███████║██║██╔██╗ ██║   █████╗  ██╔████╔██║
      ██╔══██╗██╔══██╗██╔══██║██║██║╚██╗██║   ██╔══╝  ██║╚██╔╝██║
      ██████╔╝██║  ██║██║  ██║██║██║ ╚████║██╗██║     ██║ ╚═╝ ██║
      ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚═╝╚═╝     ╚═╝     ╚═╝
                          1 YEAR ACCOUNTS GEN

                      [+] DEVELOPED BY DE3P4K [+]
                   [+] linktr.ee/deepaksinghmalik [+]
    ''')
    try:
        num = int(input('   Enter Number of Accounts to Generate? '))
        if num <= 0:
            print(Fore.RED + '   Bad Input. :/' + Style.RESET_ALL + '\n\n   Provide a positive number!')
            time.sleep(3)
            os.system('Brain.fm.exe')
            exit()
        elif num > 10:
            print('\n   EXITING...')
            time.sleep(3)
            exit()
    except ValueError as e:
        print(Fore.RED + f'   Error : {e}.' + Style.RESET_ALL + "\n\n   Let's Try Again.")
        time.sleep(3)
        os.system('Brain.fm.exe')
        exit()
    password = input('\n   Set Password for all Accounts : ')
    if len(password) < 8:
        print(Fore.RED + '   The password must be at least 8 characters long!' + Style.RESET_ALL + "\n\n   Let's Try Again.")
        time.sleep(3)
        os.system('Brain.fm.exe')
        exit()
    print('\n')

    threads = []
    for _ in range(num):
        thread = threading.Thread(target=generate_account, args=[password,])
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    input('\n\n   Accounts saved in Brain.fm.txt. Press ENTER to EXIT.')
    # exit()

if __name__ == '__main__':
    warning()
    main()
