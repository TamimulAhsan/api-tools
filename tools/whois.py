import sys
import urllib
import requests
import os
from tools import menu
from api import api



def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def details(domain):
    clear_screen()

    api_key = api.get_api_key('ip2location')

    response = requests.get(f"https://api.ip2whois.com/v2?key={api_key}&domain={domain}").json()


    print("--------------------------------------------------")
    print("\t\tDomain Information")
    print("--------------------------------------------------\n")
    print(f"Domain Name   : {response['domain']}")
    print(f"Domain ID     : {response['domain_id']}")
    print(f"Status        : {response['status']}")
    print(f"Creation Date : {response['create_date']}")
    print(f"Update Date   : {response['update_date']}")
    print(f"Expiry Date   : {response['expire_date']}")
    print(f"Domain Age    : {response['domain_age']}")
    print(f"Whois Server  : {response['whois_server']}")

    print("\n\n--------------------------------------------------")
    print("\t\tRegistrar Information:")
    print("--------------------------------------------------")
    print(f"IANA ID = {response['registrar']['iana_id']}")
    print(f"Registrar Name = {response['registrar']['name']}")
    print(f"Registrar URL = {response['registrar']['url']}")

    print("\n\n--------------------------------------------------")
    print("\t\tRegistrant Information:")
    print("--------------------------------------------------")
    print("Data Redacted For Privacy\n")



    print("\n\n--------------------------------------------------")
    print("\t\tAdmininstrator Information:")
    print("--------------------------------------------------")
    print("Data Redacted For Privacy\n")


    print("\n\n--------------------------------------------------")
    print("\t\tBilling Information:")
    print("--------------------------------------------------")
    print("Data Redacted For Privacy\n")


    print("\n\n--------------------------------------------------")
    print("\t\tNameservers:")
    print("--------------------------------------------------")
    for ns in response['nameservers']:
        print(ns)

    while 1:
        sl = input(f"\n\nMake your Selection: \n1. Search Again\t2. Main Menu\t0. Exit\n > ")
        if sl == '1':
            main()
        elif sl == '2':
            menu.main()
        elif sl == '0':
            sys.exit()
        else:
            print("Invalid Selection..")



def main():
    clear_screen()
    banner = '''
                 _    _ _           _     
                | |  | | |         (_)    
                | |  | | |__   ___  _ ___ 
                | |/\| | '_ \ / _ \| / __|
                \  /\  / | | | (_) | \__ \\
                 \/  \/|_| |_|\___/|_|___/
                '''
    print(f"\t\t{banner}\n\n")


    details(input("Domain: "))
