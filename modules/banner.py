from time import sleep
from .color import color

def banner(interval):
    print("\n\n\n")
    print(u"{}  ██████  ██▓███  ▒█████▄  ▒█████   █     █░███▄    █  ██▓     ▒█████   ▄▄▄      ▓█████▄ ▓█████  ██▀███  ".format(color.RED));sleep(interval)
    print(  u"▒██    ▒ ▓██░  ██▒▒██    ▌▒██▒  ██▒▓█░ █ ░█░██ ▀█   █ ▓██▒    ▒██▒  ██▒▒████▄    ▒██▀ ██▌▓█   ▀ ▓██ ▒ ██▒");sleep(interval)
    print(  u"░ ▓██▄   ▓██░ ██▓▒░██    ▌▒██░  ██▒▒█░ █ ░█▓██  ▀█ ██▒▒██░    ▒██░  ██▒▒██  ▀█▄  ░██   █▌▒███   ▓██ ░▄█ ▒");sleep(interval)
    print(  u"  ▒   ██▒▒██▄█▓▒ ▒░▓█    ▌▒██   ██░░█░ █ ░█▓██▒  ▐▌██▒▒██░    ▒██   ██░░██▄▄▄▄██ ░▓█▄   ▌▒▓█  ▄ ▒██▀▀█▄  ");sleep(interval)
    print(  u"▒██████▒▒▒██▒ ░  ░░▓████▀ ░ ████▓▒░░░██▒██▓▒██░   ▓██░░██████▒░ ████▓▒░ ▓█   ▓██▒░▒████▓ ░▒████▒░██▓ ▒██▒");sleep(interval)
    print(  u"▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▓░▒ ▒ ░ ▒░   ▒ ▒ ░ ▒░▓  ░░ ▒░▒░▒░  ▒▒   ▓▒█░ ▒▒▓  ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░");sleep(interval)
    print(  u"░ ░▒  ░ ░░▒ ░      ░ ▒  ▒   ░ ▒ ▒░   ▒ ░ ░ ░ ░░   ░ ▒░░ ░ ▒  ░  ░ ▒ ▒░   ▒   ▒▒ ░ ░ ▒  ▒  ░ ░  ░  ░▒ ░ ▒░");sleep(interval)
    print(  u"░  ░  ░  ░░        ░ ░  ░ ░ ░ ░ ▒    ░   ░    ░   ░ ░   ░ ░   ░ ░ ░ ▒    ░   ▒    ░ ░  ░    ░     ░░   ░ ");sleep(interval)
    print(  u"      ░              ░        ░ ░      ░            ░     ░  ░    ░ ░        ░  ░   ░       ░  ░   ░     ");sleep(interval)
    print(  u"                   ░                                                              ░                       {}".format(color.END));sleep(interval)
    print("\n\n")
                                                                                                                                      
