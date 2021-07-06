'''

BreachedSites modules found on mosint tools

Author : https://github.com/alpkeskin
Mosint Link : https://github.com/alpkeskin/mosint
License : https://github.com/alpkeskin/mosint/blob/master/LICENSE

'''
import requests, colorama, json
from colorama import Fore

def BreachedSites(email):
    url = "https://leak-lookup.com/api/search"
    payload = {"key": "6d0ac8fb1a3e1faecde871a4d0d2ca44", "type": "email_address", "query": email}
    res = requests.post(url, data=payload, timeout=30).json()
    
    if res['error'] == 'false' and isinstance(res['message'], dict):
        for i in res['message'].keys():
            print(f"[{Fore.YELLOW}!{Fore.RESET}] {i}")
