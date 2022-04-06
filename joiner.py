from lib.GuildedWrapper import Guilded
from itertools import cycle
from colorama import init, Fore, Style
from concurrent.futures import ThreadPoolExecutor
import os, pyfiglet

class bcolors:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


os.system("cls")
proxies = open("./Data/Proxies.txt").read().splitlines()
accounts = open("./Data/Accounts.txt").read().splitlines()
print(pyfiglet.figlet_format(f"Clips Guilded Spammer"))
os.system(f'title CLIPS GUILDED.GG JOINER Accounts: {len(accounts)}  Proxies: {len(proxies)}')
invitecode=input(str("Server Invite Code: "))
TeamID=input(str("Team ID: "))
threadAmount=input("Amount of Threads: ")
os.system("cls")
def GetProxy():
    with open('./Data/Proxies.txt', 'r') as temp_file:
        proxies = [line.rstrip('\n') for line in temp_file]
    return proxies
proxies = GetProxy()
proxy_pool = cycle(proxies)
def GetProxies():
    proxy = next(proxy_pool)
    if len(proxy.split(':')) == 4:
        splitted = proxy.split(':')
        return f"{splitted[2]}:{splitted[3]}@{splitted[0]}:{splitted[1]}"
    return proxy

def GetAccountMail():
    with open('./Data/Accounts.txt', 'r') as temp_file:
        mails = [line.rstrip('\n') for line in temp_file]
    return mails
mails = GetAccountMail()
mail_pool = cycle(mails)
def GetMail():
    mail = next(mail_pool)
    splitted = mail.split(':')
    return f'{splitted[0]}'

def GetAccountPass():
    with open('./Data/Accounts.txt', 'r') as temp_file:
        passwords = [line.rstrip('\n') for line in temp_file]
    return passwords
password = GetAccountPass()
pass_pool = cycle(password)
def GetPass():
    Pass = next(pass_pool)
    splitted = Pass.split(':')
    return f'{splitted[1]}'

def Join():
    while True:
        try:
           Email=GetMail()
           Pass=GetPass()
           guilded = Guilded(proxy='http://'+GetProxies())
           success,response = guilded.login(Email, Pass)
           if success:
                #guilded.join_team(invitecode) #uncomment this when u want to join accounts to a server that requires mail verification or has a vanity invite (make sure to comment the one below when using this)
                guilded.join_server(invitecode, TeamID)
           else:
               print(f'Error: {response}')
        except Exception as e:
            print(e)
            Join()
if __name__ == "__main__":
    threadAmount = 1 if threadAmount == "" else int(threadAmount)
    threads = []
    print(f"{bcolors.GREEN}Joining...")
    with ThreadPoolExecutor(max_workers=threadAmount) as joiner:
        for x in range(threadAmount):
            joiner.submit(Join)