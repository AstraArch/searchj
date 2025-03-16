import subprocess
import os
from colorama import init, Fore
from colorama import init, Fore, Style
init(autoreset=True)
if not os.path.exists('base'):
    print(Fore.RED + "the system cannot find the folder 'base'.")
else:
    count = len(os.listdir('base'))
    data = input(Fore.WHITE + 'send info: ')
    print(Fore.GREEN + '\nsearch started\n')

    result = ''
    for label in os.listdir('base'):
        file_path = os.path.join('base', label)
        try:
            with open(file_path, 'r', encoding='UTF-8') as f:
                for line in f:
                    if data in line:
                        result += f"[{label}] - {line}".replace('.', '').replace('[', '').replace(']', '').replace('"',
                                                                                                                   '').replace(
                            'NULL', '')
                        break
        except Exception as e:
            print(Fore.RED + f"erorr {label}: {e}")

    print(Fore.PINK +'search is over')
    if result:
        print(Fore.GREEN + '\nsearch results:\n')
        print(result)
    else:
        print(Fore.RED + "nothing found.")

    f = input("press enter... ': " + Style.RESET_ALL)
    if f == "":
        subprocess.run(["python", "main.py"])
