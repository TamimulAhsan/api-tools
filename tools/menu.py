from tools import url,weather,ipdetails,whois
import os
import sys


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():

    banner = '''
             ____  __    __   __    ____  ____  ____ 
            (_  _)/  \  /  \ (  )  / ___)(  __)(_  _)
              )( (  O )(  O )/ (_/\\___ \ ) _)   )(  
             (__) \__/  \__/ \____/(____/(____) (__) 
                                        ---Tamimul Ahsan
            '''
    #Clears the screen
    clear_screen()
    print(f"{banner}\n\n")

    #Select from the available tools.
    selection = input('\nSelect Your Tool: \n1. IP details\t\t2. Url Shortner\n3. Weather Info\t\t4. Whois Data\n0. Exit\n > ')
    if selection == '1':
        ipdetails.IPdetails()

    elif selection == '2':
        url.urlShortner()
    
    elif selection == '3':
        weather.weather()
    
    elif selection == '4':
        whois.main()
    
    elif selection == '0':
        sys.exit()

    else:
        print("Invalid Selection.")

main()