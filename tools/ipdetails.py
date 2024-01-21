import requests
import os
import sys
from tools import menu
from api import api


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def IPdetails():
    def ipmain():
        #Clear the screen using cls if windows else clear
        clear_screen()
        banner = '''

         ___________       _      _        _ _     
        |_   _| ___ \     | |    | |      (_) |    
          | | | |_/ /   __| | ___| |_ __ _ _| |___ 
          | | |  __/   / _` |/ _ \ __/ _` | | / __|
         _| |_| |     | (_| |  __/ || (_| | | \__ \\
         \___/\_|      \__,_|\___|\__\__,_|_|_|___/
        \n\n\n'''

        print(banner)
        while 1:
            selection = input("Please specify the IP Source.\n1. Own\t\t2. Other(input)\t\t0. Exit\n > ")
            
            # Ask the ip source and ahead accordingly.
            # Handle the exceptions and throw a friendly message.
            if selection == '1':
                try:
                    get_details(get_own_ip())

                except Exception as e:
                    print("An Error Occured. Please check your internet Connection and Try Again.")
                    return

            elif selection == '2':
                try:
                    ip = input("Enter the IP address to get details: ")
                    get_details(ip_address=ip)

                except Exception as e:
                    print(e)
                    print("An Error Occured. Please check your internet Connection and Try Again.")
                    return

            elif selection == '0':
                sys.exit()

            else:
                print("Invalid Choice. Choose Again.")


    # Get my own ip form ipify free api in json format
    def get_own_ip():
        response = requests.get('https://api64.ipify.org?format=json').json()
        
        #return just the ip form the response
        return response["ip"]


    # use ipapi for getting details of an ip in json format
    def get_details(ip_address):
        api_key = api.get_api_key("ip2location")

        response = requests.get(f'https://api.ip2location.io/?key={api_key}&ip={ip_address}').json()

        # store json response to variables for later use
        ip = response["ip"]
        city = response["city_name"]
        region = response["region_name"]
        country = response["country_name"]
        country_code = response["country_code"]
        post_code = response["zip_code"]
        latitude = response["latitude"]
        longitude = response["longitude"]
        timezone = response["time_zone"]
        asn = response["asn"]
        isp = response["as"]
        is_vpn = response["is_proxy"]

        print("\n\n============================================")
        print("                  IP INFO                 ")
        print("============================================\n")
        print(f"IP Address :\t{ip}")
        print(f"IP Version :\tIPv4")
        print(f"ASN        :\t{asn}")
        print(f"ISP        :\t{isp}\n\n")
        print(f"Proxy      :\t{is_vpn}")

        print("============================================")
        print("              Location INFO                 ")
        print("============================================\n")
        print(f"City               :\t{city}")
        print(f"Region             :\t{region}")
        print(f"Country            :\t{country}")
        print(f"Country Code       :\t{country_code}")
        print(f"Post Ccode         :\t{post_code}")
        print(f"Latitude, Longitude:\t{latitude}, {longitude}")
        print(f"TimeZone           :\t{timezone}")

        while 1:
            s = input("\n\n\n1.Search Again\t\t2. Main Menu\t\t0. Exit\n > ")

            if s == '1':
                ipmain()

            elif s == '2':
                menu.main()

            elif s == '0':
                sys.exit()

            else:
                print("Invalid Choice. Choose Again.")
                
    ipmain()