import requests,time,random,string,argparse
from fake_useragent import UserAgent
from colorama import Fore, Back, Style

logo = """

 _____ _ _    _        _        ___ _               _             
/__   (_) | _| |_ ___ | | __   / __\ |__   ___  ___| | _____ _ __ 
  / /\/ | |/ / __/ _ \| |/ /  / /  | '_ \ / _ \/ __| |/ / _ \ '__|
 / /  | |   <| || (_) |   <  / /___| | | |  __/ (__|   <  __/ |   
 \/   |_|_|\_ \\__\___/|_|\_\ \____/|_| |_|\___|\___|_|\_\___|_|   
                                                                  


"""
print(Fore.RED,(logo),Fore.WHITE)

# initialize colorama to automatically reset colors after each print statement
#init(autoreset=True)

class UserCheckerTiktok:
    def __init__(self):
        self.run()
    
    def run(self):
        # create an argument parser
        parser = argparse.ArgumentParser(description="Check if a TikTok username exists.")
        parser.add_argument('-ur', metavar='-ur', help="The length of the username to generate (default: 10)", type=int)
        parser.add_argument('-s', metavar='-s', help="The number of seconds to wait between each check (default: 0.5)", type=float)
        args = parser.parse_args()

        ur = args.ur if args.ur else 10
        wait_time = args.s if args.s else 0.5
        
        user_gen_random = string.ascii_letters + string.digits
        headers = {
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
            'content-length': '3095',
            'content-type': 'text/plain;charset=UTF-8',
            'origin': 'https://www.tiktok.com',
            'referer': 'https://www.tiktok.com/',
            'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': "Windows",
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site'
        }
        
        while True:
            random_user = ''.join(random.choice(user_gen_random) for x in range(ur))
            url = f"https://www.tiktok.com/@{random_user}"
            user_agent = UserAgent().random
            headers['user-agent'] = user_agent
            
            try:
                req = requests.get(url, headers=headers, timeout=10)
                time.sleep(wait_time)
                url_conn = req.text
                req_sc = req.status_code

                if req_sc == 200:   
                    if random_user in url_conn:
                        print(f"User not found: {random_user}")
                    else:
                        print(f"{Fore.BLACK}Error Code: {req_sc, random_user}")
                elif req_sc == 404:
                    print(f"{Fore.GREEN}The user is found: {url}")
                elif req_sc == 403:
                    print(f"{Fore.RED}Page Not Found: {url}")
                else:
                    print(f"{Fore.LIGHTBLACK_EX}Unexpected status code: {req_sc}")
            
            except requests.exceptions.Timeout:
            
                print(f"{Fore.LIGHTRED_EX}Request timed out")
            
            except requests.exceptions.RequestException as e:
            
                print(f"{Fore.LIGHTYELLOW_EX}Request failed: {e}")
            

if __name__ == "__main__":
    run = UserCheckerTiktok()