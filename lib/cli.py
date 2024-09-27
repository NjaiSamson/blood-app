from helpers import print_bold, print_colored
from models import (add_donor, add_recipient, add_blood_type, delete_donor, delete_recipient, update_donor, update_recipient, update_donation, generate_reports, donate_blood, generate_donors_report, generate_recipients_report, generate_donations_report)
from colorama import Fore, Style, init
# # Initializing colorama for styling output colors
init()
 
# Main 
def main_menu():
    while True:
        print_bold(Fore.YELLOW + "\n    DONATE BLOOD MANAGEMENT SYSTEM")
        print()
        print_bold(Fore.CYAN + "    1. Generate Reports")
        print()
        print_bold(Fore.CYAN + "    2. Add Donor")
        print()
        print_bold(Fore.CYAN + "    3. Add Recipient")
        print()
        print_bold(Fore.CYAN + "    4. Add Blood Type")
        print()
        print_bold(Fore.CYAN + "    5. Delete Donor")
        print()
        print_bold(Fore.CYAN + "    6. Delete Recipient")
        print()
        print_bold(Fore.CYAN + "    7. Update Donor")
        print()
        print_bold(Fore.CYAN + "    8. Update Recipient")
        print()
        print_bold(Fore.CYAN + "    9. Update Donation")
        print()
        print_bold(Fore.CYAN + "    10. Donate Blood")
        print()
        print_bold(Fore.CYAN + "    11. Generate Donors Report")
        print()
        print_bold(Fore.CYAN + "    12. Generate recipients Report")
        print()
        print_bold(Fore.CYAN + "    0. Exit")
        print()
        
        
        choice = input(Fore.YELLOW + "    Enter your choice: " + Style.RESET_ALL)
        print()
        
        if choice == '1':
            generate_reports()
        elif choice == '2':
            add_donor()            
        elif choice == '3':
            add_recipient()
        elif choice == '4':
            add_blood_type()
        elif choice == '5':
            delete_donor()
        elif choice == '6':
            delete_recipient()
        elif choice == '7':
            update_donor()
        elif choice == '8':
            update_recipient()
        elif choice == '9':
            update_donation()
        elif choice == '10':
            donate_blood() 
        elif choice == '11':
            generate_donors_report()
        elif choice == '12':
            generate_recipients_report()              
                   
            
        elif choice == "0":
            print_colored("Thank you for using Donate Blood Management System", Fore.GREEN)
            print()
            exit()
        else:
            print_colored("    Invalid choice. Please try again.", Fore.RED)
            print()

if __name__ == "__main__":
    main_menu()