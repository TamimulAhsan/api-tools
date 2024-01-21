from tools import menu
from api import api
import os
import requests
import sys
import random
import urllib


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def urlShortner():
    # Clears the screen using cls if windows else clear
    clear_screen()
    banner = '''
    =====================================
    ==                                 ==
    ==                                 ==
    ==         Url Shortner            ==
    ==                   By Tamim      ==
    ==                                 ==
    =====================================
    \n\n'''
    print(banner)

    #Url to be shortened
    long_url = input("Enter the Url (eg: https://example.com):\n > ")

    # If there is no https:// or http:// present at the start of the url then add it.
    if not long_url.startswith("https://" or "http://"):
        long_url = f"https://{long_url}"
    

    # Dictionary of error code and their meaning for later use
    http_status_codes = {200:'Everything is Okay', 201:"Created Successfully", 202:'Accepted',204:'No Content',301:'Moved Permanently',400:'Bad Request',401:'Unauthorised',404:'Not Found',500:"Internal Server Error"}

    #Random number 1 or 2 for selecting bitly or cuttly
    random_number = random.randint(1,2)

    def bitLy(url):
        #API key of bitly
        bitly_access_token = api.get_api_key('bitly')
                 
        #Construction of request header
        header = {"Authorization": f"Bearer {bitly_access_token}"}

        #Get group UID for the acccount
        groups_req = requests.get("https://api-ssl.bitly.com/v4/groups", headers=header)

        #Get the guid if response is Okay
        if groups_req.status_code == 200:
            groups_data = groups_req.json()["groups"][0]
            guid = groups_data['guid']

        else:
            print("\n[!] Error. Can not get GUID. Exiting.")
            sys.exit()

        #Make the post request to shorten the url
        short_req = requests.post("https://api-ssl.bitly.com/v4/shorten/",json={"group_guid":guid, "domain":"bit.ly", "long_url":url}, headers=header)
        
        #Checkc if the link is generated. If yes print the link.
        if short_req.status_code == 201:
            short_link = short_req.json().get('link')
            print(f"\nshortened Link: {short_link}")

        else:
            #print the error code along with it's meaning form the dictionary
            print(f"{short_req.status_code}: {http_status_codes[short_req.status_code]}")
            print("\nError. Try again.")

        # ask if want to short another link or exit
        while 1:
            selection = input("\n\n1. Short another link\t\t2. Main Menu\t\t0. exit\n > ")

            if selection == '1':
                urlShortner()
            
            elif selection == '2':
                return

            elif selection == '0':
                sys.exit()

            else:
                print("Invaid Choice.")

            
    def cuttLy(url):
        #API key of cuttly
        cuttly_access_token = api.get_api_key("cuttly")

        #Parse the url through the urllib library
        parsed_url = urllib.parse.quote(url)

        # make a post request to the api for generating short link.
        #Include api key and the url(passed in the urllib library)
        short_req = requests.get('http://cutt.ly/api/api.php?key={}&short={}'.format(cuttly_access_token, parsed_url))


        # Check if the response code is okay or not.
        if short_req.status_code == 200:

            #Convert to json if the response is okay
            json_response = short_req.json()

            # Check the status code form the response and print messages accorddingly
            if json_response["url"]['status'] == 1:
                print("\nThe link is already been shortened.")

            elif json_response["url"]['status'] == 2:
                print("\nEntered Link is not a link.")

            elif json_response["url"]['status'] == 3:
                print("\nLink name is already taken.")

            elif json_response["url"]['status'] == 4:
                print("\n[!] Invalid API key.")

            elif json_response["url"]['status'] == 5:
                print("\n[!] Error. Link includes invalid Character.")

            elif json_response["url"]['status'] == 6:
                print("\n[!] Error. Link is from a blocked Domain.")

            # If the code is 7. Print the short link
            elif json_response["url"]['status'] == 7:
                print(f"\nShort Link: {json_response['url']['shortLink']}")

            elif json_response["url"]['status'] == 8:
                print("\nMonthly Limit Reached :(")

        elif short_req.status_code == 401:
            print("\n[!] Invalid API key")

        elif short_req.status_code == 404:
            print("\nCan not make POST request. Page not found.")

        else:
            print("\nUnknown Error Occured.")

        # ask if want to short another link or exit
        while 1:
            selection = input("\n\n1. Short another link \t\t2. Main Menu\t\t0. exit\n > ")

            if selection == '1':
                urlShortner()

            elif selection == '2':
                menu.main()

            elif selection == '0':
                sys.exit()

            else:
                print("Invaid Choice.")


    if random_number == 1:
        bitLy(long_url)

    elif random_number == 2:
        cuttLy(long_url)



