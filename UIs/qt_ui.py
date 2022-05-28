import colorama
from colorama import Fore
from colorama import Style
from simple_term_menu import TerminalMenu
from ui import *

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