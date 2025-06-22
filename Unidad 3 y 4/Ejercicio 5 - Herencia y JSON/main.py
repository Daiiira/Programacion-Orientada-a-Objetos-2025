from ClaseGestorMedio import GestorMedio
from menu import Menu

if __name__=='__main__':
    unGestorMedio=GestorMedio()
    unGestorMedio.cargar()
    Menu(unGestorMedio)