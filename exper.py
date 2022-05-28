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
        exit_code = os.system('pip install colorama')
        exit_code = os.system('pip install simple_term_menu')
        print('[INFO] Comprobando...')
        fails = []
        try:
            import colorama
            from colorama import Fore
            from colorama import Style
            
            print(Fore.GREEN + "[OK]" + Style.RESET_ALL + " Modulo " + Fore.BLUE + "colorama " + Style.RESET_ALL + "instalado correctamente" + Style.RESET_ALL)
            colorama_check = True
        except:
            print('[ERR] Modulo no instalado')
            print('[INFO] El modulo no se ha instalado correctamente, intenta instalarlo manualmente, o comprueba que pip este instalado')
            fails.append("colorama")
        try:
            from simple_term_menu import TerminalMenu
            if colorama_check == True:
                print(f"{Fore.GREEN}[INFO]{Style.RESET_ALL} Modulo instalado correctamente")
        except:
            if colorama_check == True:
                print(f"{Fore.RED}[ERR]{Style.RESET_ALL} Modulo {Style.BRIGHT}simple_term_menu {Style.RESET_ALL}no instalado correctamente")
                fails.append("simple_term_menu")
            else:
                print("[ERR] Modulo simple_term_menu no instalado correctamente")
                fails.append("simple_term_menu")
        if str(fails) != "[]":
            if colorama_check == True:
                if len(fails) == 1:
                    print(f"{Fore.RED}[INFO (BAD)]{Style.RESET_ALL} El modulo necesario no se instalo correctamente, instalalo manualmente o ponte en contacto con el desarrollador de esta aplicacion")
                    print(f"{Fore.RED}[INFO] {Style.RESET_ALL}Modulo faltante: {fails}")
                    
                else:
                    print(f"{Fore.RED}[INFO (BAD)]{Style.RESET_ALL} El/Los modulos que faltaban no se han instalado correctamente, instalalos manualmente o ponte en contacto con el desarrollador de esta aplicacion")
                    print(f"{Fore.RED}[INFO] {Style.RESET_ALL}Modulos faltantes: {fails}")
            else:
                if len(fails) >= 1:
                    print("[INFO (BAD)] Los modulos que faltaban no se han instalado correctamente, instalalos manualmente o ponte en contacto con el desarrollador de esta aplicacion")
                else:
                    print("[INFO (BAD) El modulo necesario no se instalo correctamente, instalalo manualmente o ponte en contacto con el desarrollador de esta aplicacion")
                    print("[INFO] Modulo faltante:" + fails)
import sys, os
if sys.platform == "win32":
    colorama.init()

print(Fore.GREEN + "[INFO]" + Style.RESET_ALL + " Todo esta instalado correctamenteS" + Style.RESET_ALL)
#print(Fore.GREEN + "[OK]" + Style.RESET_ALL + " Copiado correctamente" + Style.RESET_ALL)
#print(Fore.RED + "[BAD]" + Style.RESET_ALL + " La operacion de copiado falló" + Style.RESET_ALL)