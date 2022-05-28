version = 1.0
try:
    import colorama
    from colorama import Fore
    from colorama import Style
    from simple_term_menu import TerminalMenu
    from ui import *
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
        try:
            from ui import *
        except:
            if colorama_check == True:
                print(f"{Fore.RED}[ERR]{Style.RESET_ALL}{Style.BRIGHT} GUI de la aplicación borrada! {Style.RESET_ALL}El archivo ui.py no debió ser borrado/movido!")

                import requests as req
                URL = "https://raw.githubusercontent.com/XtremeTHN/sortfiles-py/main/ui.py"
                print(f"{Style.BRIGHT}[INFO]{Style.RESET_ALL} Espera un momento, se esta descargando...")
                try:
                    file = req.get(URL, allow_redirects=True)
                    open('ui.py', 'wb').write(file.content)
                    print(f"{Style.BRIGHT}[INFO]{Style.RESET_ALL} Descargado!")
                except:
                    print(f"{Fore.RED}[ERR]{Style.RESET_ALL} No se pudo descargar el archivo")
                    fails.append("Ui de la aplicacion")
            else:
                print("[ERR] GUI de la aplicación borrada! El archivo ui.py no debió ser borrado/movido!")

                import requests as req
                URL = "https://raw.githubusercontent.com/XtremeTHN/sortfiles-py/main/ui.py"
                print("[INFO] Espera un momento, se esta descargando...")
                try:
                    file = req.get(URL, allow_redirects=True)
                    open('ui.py', 'wb').write(file.content)
                    print("}[INFO] Descargado!")
                except:
                    print("[ERR] No se pudo descargar el archivo")
                    fails.append("Ui de la aplicacion")
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
                    print("[INFO] Modulo faltante: {fails}")
                    sys.exit(1)
                else:
                    print("[INFO (BAD) El modulo necesario no se instalo correctamente, instalalo manualmente o ponte en contacto con el desarrollador de esta aplicacion")
                    print(f"[INFO] Modulo faltante: {fails}")
                    sys.exit(1)
import sys, os
if sys.platform == "win32":
    colorama.init()

print(Fore.GREEN + "[INFO]" + Style.RESET_ALL + " Todo esta instalado correctamente" + Style.RESET_ALL)
print(f"{Style.BRIGHT}[INFO]{Style.RESET_ALL} Cargando UI...")
try:
    from ui import *
except:
    print(f"{Fore.RED}[ERR]{Style.RESET_ALL} No se pudo cargar la ui, saliendo de la aplicacion...")
    sys.exit(1)

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        print(f"{Style.BRIGHT}[INFO]{Style.RESET_ALL} UI cargada con exito!")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

#print(Fore.GREEN + "[OK]" + Style.RESET_ALL + " Copiado correctamente" + Style.RESET_ALL)
#print(Fore.RED + "[BAD]" + Style.RESET_ALL + " La operacion de copiado falló" + Style.RESET_ALL)