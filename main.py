import requests
import os
import sys
import colorama
from colorama import Fore
import random
colorama.init()

os.system('cls')
os.system(f'mode con: cols=106 lines=30')
sys.stdout.write("\x1b]2;DiscBoost\x07")

class bot:

    def __init__ (self):

        print(f'''{Fore.LIGHTBLUE_EX}

██▄   ▄█    ▄▄▄▄▄   ▄█▄    ███   ████▄ ████▄    ▄▄▄▄▄      ▄▄▄▄▀ 
█  █  ██   █     ▀▄ █▀ ▀▄  █  █  █   █ █   █   █     ▀▄ ▀▀▀ █    
█   █ ██ ▄  ▀▀▀▀▄   █   ▀  █ ▀ ▄ █   █ █   █ ▄  ▀▀▀▀▄       █    
█  █  ▐█  ▀▄▄▄▄▀    █▄  ▄▀ █  ▄▀ ▀████ ▀████  ▀▄▄▄▄▀       █     
███▀   ▐            ▀███▀  ███                            ▀      
                                                                           
          ''')

        self.serverid = input("Enter The Server ID: ")
        self.limit = input('How Many Boosts: ')

        def gettokens(self):
            
            self.tokens = open('tokens.txt', 'r').read().splitlines()
            self.token = random.choice(self.tokens)

        def getid(self):

            try:

                gettokens(self)

                headers = {
                    'authority': 'discord.com',
                    'accept': '*/*',
                    'accept-language': 'en-US,en;q=0.9',
                    'authorization': self.token,
                    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
                    'sec-ch-ua-mobile': '?1',
                    'sec-ch-ua-platform': '"Android"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36',
                    'x-debug-options': 'bugReporterEnabled',
                    'x-discord-locale': 'en-US',
                    'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwNi4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTA2LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiJodHRwczovL3d3dy5nb29nbGUuY29tLyIsInJlZmVycmluZ19kb21haW4iOiJ3d3cuZ29vZ2xlLmNvbSIsInNlYXJjaF9lbmdpbmUiOiJnb29nbGUiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTUzMTMxLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
                }

                response = requests.get('https://discord.com/api/v9/users/@me/guilds/premium/subscription-slots', headers=headers)
                self.subscriptionid = str(response.json()[0]["id"])
                self.subscriptionid2 = str(response.json()[1]["id"])

                print(f'{Fore.BLUE}DISCORD{Fore.RESET}> Got Subscription IDS: [{Fore.BLUE}{self.subscriptionid} | {self.subscriptionid}{Fore.RESET}]')
            
            except:
                print('failed')

        def boost(self):

            for i in range(int(self.limit)):

                try:

                    gettokens(self)
                    getid(self)

                    headers = {

                        'authority': 'discord.com',
                        'accept': '*/*',
                        'accept-language': 'en-US,en;q=0.9',
                        'authorization': self.token,
                        'origin': 'https://discord.com',
                        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
                        'sec-ch-ua-mobile': '?1',
                        'sec-ch-ua-platform': '"Android"',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin',
                        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36',
                        'x-debug-options': 'bugReporterEnabled',
                        'x-discord-locale': 'en-US',
                        'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwNi4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTA2LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiJodHRwczovL3d3dy5nb29nbGUuY29tLyIsInJlZmVycmluZ19kb21haW4iOiJ3d3cuZ29vZ2xlLmNvbSIsInNlYXJjaF9lbmdpbmUiOiJnb29nbGUiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTUzMTMxLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
                    }

                    json_data = {

                        'user_premium_guild_subscription_slot_ids': [

                            self.subscriptionid,
                        ],
                    }

                    response = requests.put(f'https://discord.com/api/v9/guilds/{self.serverid}/premium/subscriptions', headers=headers, json=json_data)
                    getjson = response.json()['id']
                    print(f'{Fore.BLUE}DISCORD{Fore.RESET}> Attempted To Use First Boost | [{Fore.BLUE}{getjson}{Fore.RESET}]')
                        
                    responsee = requests.put(f'https://discord.com/api/v9/guilds/{self.serverid}/premium/subscriptions', headers=headers, json={

                        'user_premium_guild_subscription_slot_ids': [

                            self.subscriptionid2,

                            ],
                            })

                    getjsonn = responsee.json()['id']
                        
                    print(f'{Fore.BLUE}DISCORD{Fore.RESET}> Attempted To Use SecondBoost Boost | [{Fore.BLUE}{getjsonn}{Fore.RESET}]')

                except:
                    print(f'{Fore.YELLOW}ERROR{Fore.RESET} | JSON: {response.json()}]')
                    boost(self)
                       

        boost(self)


bot()
