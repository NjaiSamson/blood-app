from colorama import Style, init
init()

# Styling functions
def print_bold(text):
    print(Style.BRIGHT + text + Style.RESET_ALL)

def print_colored(text, color):
    print(color + text + Style.RESET_ALL)