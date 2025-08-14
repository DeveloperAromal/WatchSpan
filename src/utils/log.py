from colorama import Fore, Style, init

def log(message, color=Fore.WHITE, symbol="[~]"):
    init(True)

    print(color + f"{symbol} {message}" + Style.RESET_ALL)