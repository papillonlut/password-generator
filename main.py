import time
import random
from rich.theme import Theme
from rich.prompt import Prompt
from rich.console import Console
from rich.progress import Progress

choice = Prompt.ask("Que voulez-vous faire ? ", choices=["generator", "gestion"]).strip()

if choice == "gestion":
    readFile = open("bdd", "r")
    password = readFile.read()
    readFile.close()

    userTyping = str(input("Entrer votre mot de passe : "))

    if userTyping == password:
        change = Prompt.ask("Voulez-vous changer de mot de passe ?", choices=["yes", "no"]).strip()
        if change == "yes":
            userTypingChange = str(input("Veuilez entrer votre ancien mot de passe : "))
            if userTypingChange == password:
                newPassword = str(input("Entrer votre nouveau mot de passe : "))

                file = open("bdd", "w")
                file.write(newPassword)
                file.close()
            else:
                print("ERROR")
        else:
            question = int(input("Quel mot de passe voulez-vous (1 à 99) ? "))
            
            readFile = open("password.csv", "r")
            lines = readFile.readlines()
            print(lines[question])
            readFile.close()
    else:
        print("ERROR")

elif choice == "generator":
    # Chaine de charactère
    chainNumber = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    chainChar = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    chainSpeChar = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "{", "}", "[", "]", "|", ":", ";", "'", ",", ".", "?", "/", "~", "`"]

    # Paramètre
    custom_theme = Theme({
        "info": "blue",
        "warning": "magenta"
    })
    console = Console(theme=custom_theme)

    size = int(input("Choisissez le nombre de charactères compris entre 8 et 16 : "))
    repeat = int(input("Combien de mot de passe voulez-vous (1 à 99) : "))

    if size < 8 or size > 16:
        console.print(f"[warning]Vous avez demandé un mot de passe de {size} caractères, malheureusement la taille n'est pas compris entre 8 et 16.[/warning]")
        exit()

    if repeat < 1 or repeat > 99:
        console.print(f"[warning]Vous avez demandé {repeat} n'étant pas compris entre 1 et 99.[/warning]")
        exit()
    elif repeat > 1:
        plur = "mots"
    else:
        plur = "mot"

    speChar = Prompt.ask("Voulez-vous des charactères spéciaux", choices=["yes", "no"]).strip()

    if speChar == "yes":
        loop = chainNumber + chainChar + chainSpeChar
        speCharMessage = "avec"
    else:
        loop = chainNumber + chainChar
        speCharMessage = "sans"

    console.print(f"Vous avez demandé {repeat} {plur} de passe de {size} caractères, {speCharMessage} caractères spéciaux.", style="info")

    with Progress() as progress:

        task1 = progress.add_task("[yellow]Reflection...", total=500)

        while not progress.finished:
            progress.update(task1, advance=1)
            time.sleep(0.02)

    with Progress() as progress2:

        task2 = progress2.add_task("[green]Creation...", total=100)

        while not progress2.finished:
            progress2.update(task2, advance=1)
            time.sleep(0.02)

    file = open("mdp-generator\password.csv", "w") 
    file.write("#;Mot de passe\n")
    i = 1
    for csvfile in range(repeat-1):
        password = ''.join(random.choices(loop, k=size))
        file.write(f"{i};\"{password}\"\n")
        i += 1
    file.write(f"{i};\"{password}\"")
    file.close()

    console.print("Votre mot de passe est disponible dans le fichier password.csv", style="info")
    time.sleep(5)
    console.clear()
