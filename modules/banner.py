from time import sleep

from .color import color


def banner(interval):
    print("\n\n\n")
    print(f"{color.RED}  ██████  ██▓███  ▒█████▄  ▒█████   █     █░███▄    █  ██▓     ▒█████   ▄▄▄      ▓█████▄ ▓█████  ██▀███"); sleep(interval)
    print(f"▒██    ▒ ▓██░  ██▒▒██    ▌▒██▒  ██▒▓█░ █ ░█░██ ▀█   █ ▓██▒    ▒██▒  ██▒▒████▄    ▒██▀ ██▌▓█   ▀ ▓██ ▒ ██▒"); sleep(interval)
    print(f"░ ▓██▄   ▓██░ ██▓▒░██    ▌▒██░  ██▒▒█░ █ ░█▓██  ▀█ ██▒▒██░    ▒██░  ██▒▒██  ▀█▄  ░██   █▌▒███   ▓██ ░▄█ ▒"); sleep(interval)
    print(f"  ▒   ██▒▒██▄█▓▒ ▒░▓█    ▌▒██   ██░░█░ █ ░█▓██▒  ▐▌██▒▒██░    ▒██   ██░░██▄▄▄▄██ ░▓█▄   ▌▒▓█  ▄ ▒██▀▀█▄  "); sleep(interval)
    print(f"▒██████▒▒▒██▒ ░  ░░▓████▀ ░ ████▓▒░░░██▒██▓▒██░   ▓██░░██████▒░ ████▓▒░ ▓█   ▓██▒░▒████▓ ░▒████▒░██▓ ▒██▒"); sleep(interval)
    print(f"▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▓░▒ ▒ ░ ▒░   ▒ ▒ ░ ▒░▓  ░░ ▒░▒░▒░  ▒▒   ▓▒█░ ▒▒▓  ▒  ░ ░  ░  ░▒ ░ ▒░"); sleep(interval)
    print(f"░ ░▒  ░ ░░▒ ░      ░ ▒  ▒   ░ ▒ ▒░   ▒ ░ ░ ░ ░░   ░ ▒░░ ░ ▒  ░  ░ ▒ ▒░   ▒   ▒▒ ░ ░ ▒  ▒  ░ ░  ░  ░▒ ░ ▒░"); sleep(interval)
    print(f"░  ░  ░  ░░        ░ ░  ░ ░ ░ ░ ▒    ░   ░    ░   ░ ░   ░ ░   ░ ░ ░ ▒    ░   ▒    ░ ░  ░    ░     ░░   ░ "); sleep(interval)
    print(f"      ░              ░        ░ ░      ░            ░     ░  ░    ░ ░        ░  ░   ░       ░  ░   ░     "); sleep(interval)
    print(f"                   ░                                                              ░                       {color.END}"); sleep(interval)
    print("\n\n")
