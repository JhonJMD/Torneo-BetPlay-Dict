import os
import ui.menus as m
import funciones as fun

if __name__ == '__main__':
    isActive = True
    while isActive:
        os.system('cls')
        try:
            m.menuPrincipal()       
            op = int(input(': '))
        except ValueError:
            os.system('cls')
            print('Dato no valido')
            os.system('pause')
        else:
            if(op == 1):
                fun.regEquipos()
            elif(op == 2):
                fun.regFecha()
            elif(op == 3):
                fun.reporte()
            elif(op == 4):
                os.system('cls')
                print('Gracias por utilizar nuestro sistema')
                isActive = False
                os.system('pause')
            
