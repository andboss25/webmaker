
import colorama

def error(content:str):
    print(f"{colorama.Fore.RED}{content}{colorama.Fore.RESET}")
    return