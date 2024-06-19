import time
import json
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
        change = Prompt.ask("Voulez-vous changer de mot de passe ?", choices=["oui", "non"]).strip()
        if change == "oui":
            userTypingChange = str(input("Veuilez entrer votre ancien mot de passe : "))
            if userTypingChange == password:
                newPassword = str(input("Entrer votre nouveau mot de passe : "))

                file = open("bdd", "w")
                file.write(newPassword)
                file.close()
            else:
                print("ERROR")
        else:
            print("""0. Avoir un mot de passe / identifiant
1. Ajouter un mot de passe / identifiant
2. Modifier un mot de passe / identifiant
3. Supprimer un mot de passe / identifiant
   ========================================
4. Lister tout les services
5. Ajouter un service
6. Supprimer un service""")
            
            question = int(input("Que souhaitez-vous faire ? "))

            if question == 0:
                question = str(input("Donnez le service dans lequel vous souhaitez le mot de passe et l'identifiant ? ")).lower()

                with open("service.json", "r") as source_file:
                    data = json.load(source_file)
                
                if question in data['data']:
                    print(f"Service: {question.capitalize()}")
                    for username, password in data['data'][question].items():
                        print(f"Username: {username}, Password: {password}")
                else:
                    print(f"Aucun service trouvé pour: {question}")
            elif question == 1:
                service = str(input("Donnez le service dans lequel vous souhaitez ajouter le mot de passe et l'identifiant ? ")).lower()

                with open("service.json", "r") as source_file:
                    data = json.load(source_file)
                
                if service in data['data']:
                    print(f"Service: {service.capitalize()}")
                    for username, password in data['data'][service].items():
                        print(f"Username: {username}, Password: {password}")
                else:
                    print(f"Aucun service trouvé pour: {service}")
                    add_new_service = str(input("Voulez-vous ajouter ce service ? (oui/non): ")).lower()
                    if add_new_service == 'oui':
                        data['data'][service] = {}

                new_username = str(input("Entrez le nouvel identifiant: "))
                new_password = str(input("Entrez le nouveau mot de passe: "))
                
                data['data'][service][new_username] = new_password

                with open("service.json", "w") as source_file:
                    json.dump(data, source_file, indent=4)
                
                print("Les données ont été ajoutées avec succès!")
            elif question == 2:
                service = str(input("Donnez le service dans lequel vous souhaitez modifier le mot de passe et l'identifiant ? ")).lower()

                with open("service.json", "r") as source_file:
                    data = json.load(source_file)
                
                if service in data['data']:
                    print(f"Service: {service.capitalize()}")
                    for username, password in data['data'][service].items():
                        print(f"Username: {username}, Password: {password}")

                    username_to_modify = str(input("Lequel voulez-vous modifier (ID requis) ? "))
                    
                    if username_to_modify in data['data'][service]:
                        new_username = str(input("Entrez le nouvel identifiant: "))
                        new_password = str(input("Entrez le nouveau mot de passe: "))
                        
                        del data['data'][service][username_to_modify]
                        data['data'][service][new_username] = new_password
                        
                        with open("service.json", "w") as source_file:
                            json.dump(data, source_file, indent=4)
                        
                        print("Les données ont été modifiées avec succès!")
            elif question == 3:
                service = str(input("Donnez le service dans lequel vous souhaitez supprimer le mot de passe et l'identifiant ? ")).lower()

                with open("service.json", "r") as source_file:
                    data = json.load(source_file)
                
                if service in data['data']:
                    print(f"Service: {service.capitalize()}")
                    for username, password in data['data'][service].items():
                        print(f"Username: {username}, Password: {password}")

                    username_to_delete = str(input("Lequel voulez-vous supprimer (ID requis) ? "))
                    
                    if username_to_delete in data['data'][service]:
                        del data['data'][service][username_to_delete]
                        
                        with open("service.json", "w") as source_file:
                            json.dump(data, source_file, indent=4)
                        
                        print("Les données ont été supprimées avec succès!")
            
            elif question == 4:
                with open("service.json", "r") as source_file:
                    data = json.load(source_file)

                services = list(data["data"].keys())

                print("4. Liste de tout les services")

                for service in services:
                    service = service.capitalize()
                    print(service)
            elif question == 5:
                with open("service.json", "r") as source_file:
                    data = json.load(source_file)

                def add_service(data, service_name):
                    if "data" not in data:
                        data["data"] = {}
                    data["data"][service_name] = {"admin": "admin", "password": "admin"}

                new_service_name = str(input("Entrer un nouveau service : ")).lower

                add_service(data, new_service_name)

                with open("service.json", "w") as source_file:
                    json.dump(data, source_file, indent=4)
            elif question == 6:
                with open("service.json", "r") as source_file:
                    data = json.load(source_file)

                def supprimer_service(data, service_name):
                    if service_name in data['data']:
                        del data['data'][service_name]
                    else:
                        print(f"Le service {service_name} n'existe pas dans les données.")
                    return data

                service_a_supprimer = "apple"
                data = supprimer_service(data, service_a_supprimer)

                with open("service.json", "w") as service_a_supprimer:
                    json.dump(data, service_a_supprimer, indent=4)

            else:
                print("ERROR")
    else:
        print("ERROR")

elif choice == "generator":
    chainNumber = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    chainChar = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    chainSpeChar = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "{", "}", "[", "]", "|", ":", ";", "'", ",", ".", "?", "/", "~", "`"]

    custom_theme = Theme({
        "info": "blue",
        "warning": "magenta"
    })
    console = Console(theme=custom_theme)

    size = int(input("Choisissez le nombre de charactères compris entre 8 et 16 : "))

    type = str(input("Voulez-vous générer un ou plusieurs mot de passe seul ou voulez-vous générer pour un service. (solo/service) "))

    if type == "solo":

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

        with Progress() as progress2:

            task2 = progress2.add_task("[green]Creation...", total=100)

            while not progress2.finished:
                progress2.update(task2, advance=1)
                time.sleep(0.01)

        file = open("password.csv", "w") 
        file.write("#;Mot de passe\n")
        i = 1
        for csvfile in range(repeat):
            password = ''.join(random.choices(loop, k=size))
            file.write(f"{i};\"{password}\"\n")
            i += 1
        file.close()

        console.print("Votre mot de passe est disponible dans le fichier password.csv", style="info")
        time.sleep(5)
        console.clear()
    elif type == "service":
        if size < 8 or size > 16:
            console.print(f"[warning]Vous avez demandé un mot de passe de {size} caractères, malheureusement la taille n'est pas compris entre 8 et 16.[/warning]")
            exit()
        
        else:
            service = str(input("Quel service voulez-vous ajouter un mot de passe ? "))

            speChar = Prompt.ask("Voulez-vous des charactères spéciaux", choices=["yes", "no"]).strip()

            if speChar == "yes":
                loop = chainNumber + chainChar + chainSpeChar
            else:
                loop = chainNumber + chainChar

            with Progress() as progress2:

                task2 = progress2.add_task("[green]Creation...", total=100)

                while not progress2.finished:
                    progress2.update(task2, advance=1)
                    time.sleep(0.01)

            password = ''.join(random.choices(loop, k=size))

            with open("service.json", "r") as source_file:
                data = json.load(source_file)
            
            if service in data['data']:
                print(f"Service: {service.capitalize()}")
                for username, pwd in data['data'][service].items():
                    print(f"Username: {username}, Password: {pwd}")
            else:
                print(f"Aucun service trouvé pour: {service}")
                add_new_service = str(input("Voulez-vous ajouter ce service ? (oui/non): ")).lower()
                if add_new_service == 'oui':
                    data['data'][service] = {}

            new_username = str(input("Entrez le nouvel identifiant: "))
            
            data['data'][service][new_username] = password

            with open("service.json", "w") as source_file:
                json.dump(data, source_file, indent=4)
            
            print("Les données ont été ajoutées avec succès!")
