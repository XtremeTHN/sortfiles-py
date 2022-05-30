version = 1.0
try:
    import colorama
    from colorama import Fore
    from colorama import Style
    from simple_term_menu import TerminalMenu
except:
    print('[ERR] Modulos requeridos no instalados')
    print('[INFO] Deseas instalarlos?')
    choice = input('[S] Si    [N] No  :')
    if choice == 'S':
        import sys, os
        print('[INFO] Ejecutando pip...')
        exit_code = os.system('pip install colorama simple_term_menu PyQt5')
        print('[INFO] Comprobando...')
        fails = []
        try:
            import colorama
            from colorama import Fore
            from colorama import Style
            
            print(Fore.GREEN + "[OK]" + Style.RESET_ALL + " Modulo " + Fore.BLUE + "colorama " + Style.RESET_ALL + "comprobado")
            colorama_check = True
        except:
            print('[ERR] Modulo colorama no instalado')
            fails.append("colorama")
        try:
            from simple_term_menu import TerminalMenu
            if colorama_check == True:
                print(f"{Fore.GREEN}[OK]{Style.RESET_ALL} Modulo {Fore.LIGHTRED_EX}simple_term_menu{Style.RESET_ALL} comprobado!")
        except:
            if colorama_check == True:
                print(f"{Fore.RED}[ERR]{Style.RESET_ALL} Modulo {Style.BRIGHT}simple_term_menu {Style.RESET_ALL}no instalado")
                fails.append("simple_term_menu")
            else:
                print("[ERR] Modulo simple_term_menu no instalado")
                fails.append("simple_term_menu")
        try:
            from PyQt5 import QtCore, QtGui, QtWidgets
            from PyQt5.QtWidgets import *
            from PyQt5.QtCore import QDir, QUrl
            print(f"{Fore.GREEN}[OK]{Style.RESET_ALL} Modulo {Fore.LIGHTWHITE_EX}PyQt5{Style.RESET_ALL} comprobado!")
        except:
            if colorama_check == True:
                print(f"{Fore.RED}[ERR]{Style.RESET_ALL} Modulo PyQt5 no instalado")
                fails.append("PyQt5 (GUI)")
            else:
                print("[ERR] Modulo PyQt5 no instalado")
                fails.append("PyQt5 (GUI)")

        if str(fails) != "[]":
            if colorama_check == True:
                if len(fails) == 1:
                    print(f"{Fore.RED}[INFO (BAD)]{Style.RESET_ALL} El modulo necesario no se instalo correctamente, instalalo manualmente o ponte en contacto con el desarrollador de esta aplicacion")
                    print(f"{Fore.RED}[INFO] {Style.RESET_ALL}Modulo faltante: {fails}")
                    sys.exit(1)
                else:
                    print(f"{Fore.RED}[INFO (BAD)]{Style.RESET_ALL} El/Los modulos que faltaban no se han instalado correctamente, instalalos manualmente o ponte en contacto con el desarrollador de esta aplicacion")
                    print(f"{Fore.RED}[INFO] {Style.RESET_ALL}Modulos faltantes: {fails}")
                    sys.exit(1)
            else:
                if len(fails) >= 1:
                    print("[INFO (BAD)] Los modulos que faltaban no se han instalado correctamente, instalalos manualmente o ponte en contacto con el desarrollador de esta aplicacion")
                    print(f"[INFO] Modulo faltante: {fails}")
                    sys.exit(1)
                else:
                    print("[INFO (BAD) El modulo necesario no se instalo correctamente, instalalo manualmente o ponte en contacto con el desarrollador de esta aplicacion")
                    print(f"[INFO] Modulo faltante: {fails}")
                    sys.exit(1)
    else:
        sys.exit(1)
import sys, os
if sys.platform == "win32":
    colorama.init()

print(Fore.GREEN + "[INFO]" + Style.RESET_ALL + " Todo esta instalado correctamente" + Style.RESET_ALL)
print(f"{Style.BRIGHT}[INFO]{Style.RESET_ALL} Comenzando configuracion...")
print(f"{Style.BRIGHT}[INFO]{Style.RESET_ALL} Hay dos UI que puedes utilizar, Qt5 y GTK.  Qt se puede utilizar tanto en Windows, como en Linux, recomiendo mas GTK si estas en linux. ¿Qué eliges?")
sub_menu = ["[a] Qt5", "[b] GTK"]
choice = sub_menu[TerminalMenu(sub_menu).show()]
if choice == "[a] Qt5":
    print(f"{Style.BRIGHT}[INFO]{Style.RESET_ALL} Descargando... (0/2)", end="\r")
    import requests as req
    download_fails = []
    URL = ["https://raw.githubusercontent.com/XtremeTHN/sortfiles-py/main/ui.py", "https://raw.githubusercontent.com/XtremeTHN/sortfiles-py/main/UIs/qt_ui.py"]
    try:
        file = req.get(URL[0], allow_redirects=True)
        open('qt_ui.py', 'wb').write(file.content)
        print(f"{Style.BRIGHT}[INFO]{Style.RESET_ALL} Descargado! (1/2)", end="\r")
    except:
        print(f"{Fore.RED}[ERR]{Style.RESET_ALL} No se pudo descargar el archivo")
        download_fails.append(1)
    print(f"{Style.BRIGHT}[INFO]{Style.RESET_ALL} Descargando... (1/2)", end="\r")
    try:
        file = req.get(URL[1], allow_redirects=True)
        open('qt_ui.py', 'wb').write(file.content)
        print(f"{Style.BRIGHT}[INFO]{Style.RESET_ALL} Descargado! (2/2)", end="\r")
    except:
        print(f"{Fore.RED}[ERR]{Style.RESET_ALL} No se pudo descargar el archivo")
        download_fails.append(2)
    if len(download_fails) == 2:
        print(f"{Fore.RED}[ERR]{Style.RESET_ALL} Ninguno de los dos archivos pudieron ser descargados, asegurate que tienes una conexion a internet o que el repositorio del proyecto siga disponible")
        print(F"{Style.BRIGHT}[INFO]{Style.RESET_ALL} Intentalo de nuevo mas tarde")
        sys.exit(1)
    elif download_fails[1] == 2:
        print(f"{Fore.RED}[ERR]{Style.RESET_ALL} El archivo que contenia el UI del programa no pudo ser descargado, asegurate que tienes una conexion a internet o que el repositorio del proyecto siga disponible")
        print(F"{Style.BRIGHT}[INFO]{Style.RESET_ALL} Solo el archivo que contenia el codigo pudo ser descargado, intenta descargar el UI mas tarde")
    elif download_fails[0] == 1:
        print(f"{Fore.RED}[ERR]{Style.RESET_ALL} El archivo que contenia el codigo que inicializaba el UI del programa no pudo ser descargado, asegurate que tienes una conexion a internet o que el repositorio del proyecto siga disponible")
        print(f"{Style.BRIGHT}[INFO]{Style.RESET_ALL} Solo el archivo que contenia el UI pudo ser descargado, intenta descargar el codigo mas tarde")
    else:
        print(f"{Style.BRIGHT}[INFO]{Style.RESET_ALL} ¿Quieres hacer la GUI Qt5 como predeterminada? Si deseas cambiar de opinion, ejecuta este programa con ""-rg""")
        sub_menu = ["Si", "No"]
        choice = sub_menu[TerminalMenu(sub_menu).show()]
#print(Fore.GREEN + "[OK]" + Style.RESET_ALL + " Copiado correctamente" + Style.RESET_ALL)
#print(Fore.RED + "[BAD]" + Style.RESET_ALL + " La operacion de copiado falló" + Style.RESET_ALL)