import os
import ui.titles as t
import funciones as fun

def menuPrincipal():
    os.system('cls')
    opciones = ['Registrar Equipo','Registrar fecha de juego','Reportes','Salir']
    t.headerPrincipal()
    for i, item in enumerate(opciones):
        print(f'{i+1}. {item}')

def menuRegequipos(Equipos : dict):
    t.headerRegfecha()
    print('Listado de Equipos: ')
    for key, valor in Equipos.items():
        print(f'- {valor['nombre']}')
    print('\n')
    
def menuReport():
    os.system('cls')
    opReport = ['A. NOMBRE DEL EQUIPO QUE MAS GOLES ANOTO','B. NOMBRE DEL EQUIPO QUE MAS PUNTOS TIENE','C. NOMBRE DEL EQUIPO QUE MAS PARTIDOS GANO','D. TOTAL DE GOLES ANOTADOS EN EL TORNEO','E. PROMEDIO DE GOLES ANOTADOS EN EL TORNEO','F. REGRESAR AL MENU PRINCIPAL']
    t.headerReportes()
    for idx, item in enumerate(opReport):
        print(item)
