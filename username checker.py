import requests
from colorama import Fore, Style

def recherche_pseudo(pseudo):
    sites = [
        "https://www.facebook.com/{}",
        "https://www.instagram.com/{}",
        "https://twitter.com/{}",
        "https://www.linkedin.com/in/{}",
        "https://github.com/{}",
        "https://www.root-me.org/{}",
        "https://www.youtube.com/{}",
        "https://www.tiktok.com/{}",
        "https://www.pinterest.com/{}",
        "https://soundcloud.com/{}",
        "https://steamcommunity.com/id/{}",
        "https://www.pornhub.com/users/{}",
        "https://www.twitch.tv/{}",
    ]

    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]

    color_index = 0

    for site in sites:
        url = site.format(pseudo)
        response = requests.get(url)
        if response.status_code == 200:
            print(colors[color_index] + f"J'ai pu trouvé une inscription sur : {url}" + Style.RESET_ALL)
        else:
            print(colors[color_index] + f"Je n'ai rien pu trouver sur : {url}" + Style.RESET_ALL)

        color_index = (color_index + 1) % len(colors)

if __name__ == "__main__":
    pseudo = input("Entrez le nom d'utilisateur à rechercher : ")
    recherche_pseudo(pseudo)