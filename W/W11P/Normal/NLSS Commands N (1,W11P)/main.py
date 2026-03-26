from dependencies import idiomas
import re, sys, json, sys
from pathlib import Path
def code():
    def checking(file: Path):
        if file.exists() is False:
            file.touch()
        else:
            pass
    estado = True
    k = {}
    # Caminhos e criação
    pasta_nlss = Path(Path.home() / "Next Level Software Studio")
    ficheiros_temporários = Path(pasta_nlss / "Temporary Files" / "NLSS Commands" / "1,W11P")
    ficheiros_temporários.mkdir(parents=True, exist_ok=True)
    ficheiros_persistentes = Path(pasta_nlss / "Next Level Software Studio" / "Persistant Files" / "NLSS Commands" / "1,W11P")
    ficheiros_persistentes.mkdir(parents=True, exist_ok=True)
    pasta_de_programas = Path(pasta_nlss / "Programs")
    pasta_de_programas.mkdir(parents=True, exist_ok=True)
    pasta_de_idioma = Path(ficheiros_persistentes / "Language")
    pasta_de_idioma.mkdir(parents=True, exist_ok=True)
    ficheiro_de_idioma = Path(ficheiros_persistentes / "Language" / "Language.txt")
    ficheiro_de_verificador_de_idioma = Path(ficheiros_persistentes / "Language" / "Language Support File.json")
    pasta_de_alias = Path(ficheiros_persistentes / "Alias")
    pasta_de_alias.mkdir(parents=True, exist_ok=True)
    ficheiro_de_alias = Path(ficheiros_persistentes / "Alias" / "Alias.json")
    if ficheiro_de_alias.exists() is False or ficheiro_de_alias.read_text(encoding="utf-8").strip() == "":
        with open(file=ficheiro_de_alias, mode="r", ) as y:
            json.dump(k, y, indent=4, ensure_ascii=False)
    if ficheiro_de_verificador_de_idioma.exists() is False or ficheiro_de_verificador_de_idioma.read_text(encoding="utf-8").strip() == "":
        with open(file=ficheiro_de_verificador_de_idioma, mode="r", encoding="utf-8") as gg:
            json.dump(k, gg, indent=4, ensure_ascii=False)
    #

    # Conteúdos
    ficheiro_verificador_conteudo_false = {"Accepted": False}
    ficheiro_verificador_conteudo_true = {"Accepted": True}
    #

    # Listas
    idiomas_disponíveis = idiomas.idiomasAceites()
    #


    # Verificação do ficheiro de idioma
    with open(ficheiro_de_verificador_de_idioma, "r") as o:
        documento = json.load(o)
        estado_do_json = documento["Accepted"]
    try:
        if ficheiro_de_idioma.exists() is False:
            ficheiro_de_idioma.touch()
        elif ficheiro_de_idioma.exists() and estado_do_json is False:
            pergunta = input("It was found a language settings file, do you want to use it? (y/n)")
            if pergunta in ["yes", "y"]:
                with open(ficheiro_de_verificador_de_idioma, "w", encoding="utf-8") as file:
                    json.dump(ficheiro_verificador_conteudo_true, file, indent=4, ensure_ascii=False)
            elif pergunta in ["no", "n"]:
                with open(ficheiro_de_verificador_de_idioma, "w", encoding="utf-8") as ficheiro:
                    json.dump(ficheiro_verificador_conteudo_false, file, indent=4, ensure_ascii=False)
    except FileNotFoundError:
        print("The software could not find the language support file.")
        print("Exiting the program…")
        sys.exit(92)
    except PermissionError:
        print("The software could not open the language support file,\n because it didn't have enough permission.")
        print(f"INFO: The language support file is stored in {ficheiro_de_verificador_de_idioma}.")
        
    except Exception as e:
        print(f"Error\nPython error code: {e}.")

    try:
        with open(ficheiro_de_verificador_de_idioma, "r", encoding="utf-8") as arquivo:
            y = json.load(arquivo)
            estado_de_aceitação = y["Accepted"]
        if estado_de_aceitação is False:
            questão = input("What language do you want to setup, for default of this software?")
            if questão in idiomas_disponíveis:
                with open(ficheiro_de_idioma, "w") as a:
                    a.write(questão)
    except FileNotFoundError:
        print("The software could not find the language support file.")
        print("Exiting the program…")
        sys.exit(92)
    except PermissionError:
        print("The software could not open the language support file,\n because it didn't have enough permission.")
        print(f"INFO: The language support file is stored in {ficheiro_de_verificador_de_idioma}.")
        print("Exiting the program…")
        sys.exit(14)
    except Exception as e:
        print(f"Error\nPython error code: {e}.")
        print("Exiting the program…")
        sys.exit(1)

    with open(ficheiro_de_idioma) as f:
        idioma = f.read()

    if idioma.strip() in idiomas.buscador(idioma="Inglês"):
        print("Welcome to the NLSS Commands (1,W11P).")

        while estado is True:
            oi = input('> ')

            # Comandos
            install = re.match(r"'install (.+)", oi)
            uninstall = re.match(r"'uninstall (.+)", oi)
            metadataCheck = re.match(r"'check (.+) (.+)", oi)
            #

            if install:
                global estado_do_ficheiro_de_alias
                estado_do_ficheiro_de_alias = None
                with open(ficheiro_de_alias, "r") as d:
                    n = d.read()
                    if n in [r"{}", ""]:
                        estado_do_ficheiro_de_alias = False
                    else:
                        estado_do_ficheiro_de_alias = True
                print(f"Installing…")
                with open(install.group(1), "r") as file:
                    global conteúdo_do_instalador
                    conteúdo_do_instalador = json.load(file)
                    global guia_instalação
                    guia_instalação = Path(install.group(1))
                    pasta_pai = guia_instalação.parent
                    projeto = Path(pasta_pai / "main")
                    print("Informations \n(keep in mind that the information can be easily edited):")
                    print(f"Name: {conteúdo_do_instalador["Name"]}")
                    print(f"Version: {conteúdo_do_instalador["Version"]}")
                    print(f"Authors: {conteúdo_do_instalador["Authors"]}")
                    print(f"Website: {conteúdo_do_instalador["Website"]}")
                    print(f"Dependencies:\n    NLSS software: {conteúdo_do_instalador["Dependencies"]["NLSS software"]}\n    SNAIL software: {conteúdo_do_instalador["Dependencies"]["SNAIL software"]}")
                    try:
                        alias_final = []
                        if projeto.exists() is False:
                            print("The main folder off the project doesn't exists.")
                            while True:
                                g = input("Do you want to create it? (y/n)")
                                if g.lower() in ["y", "yes"]:
                                    print(f"Creating main folder ({projeto})…")
                                    projeto.mkdir(parents=True, exist_ok=False)
                                    print(f"The main folder ({projeto}), was created.")
                                    print("You need to restart the installation")
                                    break
                                elif g.lower() in ["n", "no"]:
                                    print("Cancelling installation…")
                                    break
                                else:
                                    print("Invalid input.")
                        elif projeto.exists():
                            for file in projeto.iterdir():
                                with open(file, "rb") as v:
                                    magicbytes = v.read(5)
                                    if magicbytes == b'alias' and Path(file).suffix == ".alias":
                                        with open(file, "rb") as a:
                                            a.seek(5)
                                            alias_file = a.read()
                                        alias_final.append(alias_file)
                                    elif magicbytes != b'alias' and Path(file).suffix == ".alias":
                                        while True:
                                            h = input(f"The file {file} is not valid.\nDo you want to ignore it,\nor stop the installation? (y/n)")
                                            if h.lower() in ["y", "yes"]:
                                                print("File was ignored.")
                                                break
                                            elif h.lower() in ["n", "no"]:
                                                print("Cancelling installation…")
                                                break
                                            else:
                                                print("Invalid input.")
                    except FileNotFoundError as e:
                        print("A file wasn't found.")
                        print(f"Python error code: {e}.")

                    lista_de_alias = {}

                    for alias_blob in alias_final:
                        linhas = alias_blob.decode('utf-8').splitlines()
                        for linha in linhas:
                            linha = linha.strip()
                            if "=" in linha is False:
                                print("A Command Line Alias file is corrupted.")
                                print("Stopping instalation…")
                                break
                            elif " = " in linha:
                                match = re.search(r"^(.+?)\s+=\s+\((.+)\)$", linha)
                                
                                if match:
                                    cmd_novo = match.group(1).strip()
                                    cmd_velho = match.group(2).strip()
                                    base_dados = {}
                                    if ficheiro_de_alias.exists():
                                        try:
                                            with open(ficheiro_de_alias, "r", encoding="utf-8") as f:
                                                conteudo = f.read().strip()
                                                base_dados = json.loads(conteudo) if conteudo else {}
                                        except json.JSONDecodeError:
                                            base_dados = {}
                                    nome_ext = conteúdo_do_instalador.get("Name", "Extension Unknown")
                                    if nome_ext in base_dados:
                                        print(f"\nErro: A extensão '{nome_ext}' já existe no sistema.")
                                        print("A interromper a instalação...")
                                        sys.exit(1)
                                    base_dados[nome_ext] = {
                                        "Version": conteúdo_do_instalador.get("Version", ""),
                                        "Authors": conteúdo_do_instalador.get("Authors", []),
                                        "Website": conteúdo_do_instalador.get("Website", ""),
                                        "Dependencies": {
                                            "NLSS software": conteúdo_do_instalador.get("Dependencies", {}).get("NLSS software", []),
                                            "SNAIL software": conteúdo_do_instalador.get("Dependencies", {}).get("SNAIL software", [])
                                        },
                                        "Alias": {} 
                                    }
                                    base_dados[nome_ext]["Alias"][cmd_novo] = cmd_velho
                                    with open(ficheiro_de_alias, "w", encoding="utf-8") as f:
                                        json.dump(base_dados, f, indent=4, ensure_ascii=False)
                print(f"Installing of {conteúdo_do_instalador["Name"]}, was complete.")
            elif uninstall:
                extensão = str(uninstall.group(1))
                with open(ficheiro_de_alias, "r", encoding="utf-8") as ficheiro:
                    conteúdo = json.load(ficheiro)
                a_eliminar = conteúdo.get(extensão)
                if a_eliminar in conteúdo:
                    del conteúdo[a_eliminar]
                    with open(ficheiro_de_alias, "w", encoding="utf-8") as ficheiro:
                        json.dump(conteúdo, ficheiro, indent=4, ensure_ascii=False)
                elif a_eliminar not in conteúdo:
                    print(f"The extension {a_eliminar}, ins't installed.")
                    print(f"Exiting the program…\nExit code 1.")
                    sys.exit(1)
            elif metadataCheck:
                extension = metadataCheck.group(1)
                data = metadataCheck.group(2)
                with open(ficheiro_de_alias, "r", encoding="utf-8") as database:
                    arquivoo = json.load(database)
                print(f"Requested metadata: {arquivoo[extension][data]}")
            elif oi == "exit" or oi == "shutdown":
                print("Exiting the program…")
                sys.exit(13)
            elif oi == "":
                continue
            else:
                print("An error occured.")
                print("Exiting the program…")
                sys.exit(1)
if __name__ == "__main__":
    code()
