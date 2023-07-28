from time import sleep

from .color import color


def banner(interval):
    print("\n\n\n")
    print(
        "{}  ██████  ██▓███  ▒█████▄  ▒█████   █     █░███▄    █  ██▓     ▒█████   ▄▄▄      ▓█████▄ ▓█████  ██▀███  ".format(
            color.RED
        )
    )
    sleep(interval)
    print(
        "▒██    ▒ ▓██░  ██▒▒██    ▌▒██▒  ██▒▓█░ █ ░█░██ ▀█   █ ▓██▒    ▒██▒  ██▒▒████▄    ▒██▀ ██▌▓█   ▀ ▓██ ▒ ██▒"
    )
    sleep(interval)
    print(
        "░ ▓██▄   ▓██░ ██▓▒░██    ▌▒██░  ██▒▒█░ █ ░█▓██  ▀█ ██▒▒██░    ▒██░  ██▒▒██  ▀█▄  ░██   █▌▒███   ▓██ ░▄█ ▒"
    )
    sleep(interval)
    print(
        "  ▒   ██▒▒██▄█▓▒ ▒░▓█    ▌▒██   ██░░█░ █ ░█▓██▒  ▐▌██▒▒██░    ▒██   ██░░██▄▄▄▄██ ░▓█▄   ▌▒▓█  ▄ ▒██▀▀█▄  "
    )
    sleep(interval)
    print(
        "▒██████▒▒▒██▒ ░  ░░▓████▀ ░ ████▓▒░░░██▒██▓▒██░   ▓██░░██████▒░ ████▓▒░ ▓█   ▓██▒░▒████▓ ░▒████▒░██▓ ▒██▒"
    )
    sleep(interval)
    print(
        "▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▓░▒ ▒ ░ ▒░   ▒ ▒ ░ ▒░▓  ░░ ▒░▒░▒░  ▒▒   ▓▒█░ ▒▒▓  ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░"
    )
    sleep(interval)
    print(
        "░ ░▒  ░ ░░▒ ░      ░ ▒  ▒   ░ ▒ ▒░   ▒ ░ ░ ░ ░░   ░ ▒░░ ░ ▒  ░  ░ ▒ ▒░   ▒   ▒▒ ░ ░ ▒  ▒  ░ ░  ░  ░▒ ░ ▒░"
    )
    sleep(interval)
    print(
        "░  ░  ░  ░░        ░ ░  ░ ░ ░ ░ ▒    ░   ░    ░   ░ ░   ░ ░   ░ ░ ░ ▒    ░   ▒    ░ ░  ░    ░     ░░   ░ "
    )
    sleep(interval)
    print(
        "      ░              ░        ░ ░      ░            ░     ░  ░    ░ ░        ░  ░   ░       ░  ░   ░     "
    )
    sleep(interval)
    print(
        "                   ░                                                              ░                       {}".format(
            color.END
        )
    )
    sleep(interval)
    print("\n\n")
