import os
import ui.titles as t
import ui.menus as m
Equipos= {}

def regEquipos():
    os.system('cls')
    t.headerRegequipo()
    isAddEquipo = True
    while isAddEquipo:
        nombre = input('Ingrese el nombre del Equipo: ').capitalize()
        Equipos[nombre] = {
            'nombre': nombre,
            'partidosJugados': 0,
            'partidosGanados': 0,
            'partidosPerdidos': 0,
            'partidosEmpatados': 0,
            'golesAnotados': 0,
            'puntos': 0,
            'estado': ''
        }
        isAddEquipo = bool(input('¿Desea ingresar otro Equipo? (S si/Enter no): '))

def regFecha():
    estados = ['Local', 'Visitante']

    for i in range(2):
        is_equipo = True
        while is_equipo:
            try:
                os.system('cls')
                m.menuRegequipos(Equipos)
                nombre_equipo = input(f'Ingrese el nombre del equipo {i + 1}: ')
                if i == 0:
                    equipo_local = nombre_equipo
            except ValueError:
                print('Dato Erróneo')
            else:
                if nombre_equipo in Equipos:
                    equipo_data = Equipos[nombre_equipo]
                    is_equipo = False
                    is_estado = True
                    while is_estado:
                        try:
                            for idx, item in enumerate(estados):
                                print(f'{idx + 1}. {item}')
                            est = int(input(': '))
                        except ValueError:
                            print('Dato Erróneo')
                        else:
                            if est == 1:
                                estado = 'Local'
                                equipo_data['estado'] = estado
                                equipo_data['partidosJugados'] += 1
                                is_estado = False
                            elif est == 2:
                                estado = 'Visitante'
                                equipo_data['estado'] = estado
                                equipo_data['partidosJugados'] += 1
                                is_estado = False
                            else:
                                print('Dato ingresado no válido')
                    is_goles = True
                    while is_goles:
                        try:
                            goles = int(input(f'Cuantos goles hizo el equipo {equipo_data["nombre"]}: '))
                            if i == 0:
                                goles_equipo_local = goles
                        except ValueError:
                            print('Dato no válido')
                        else:
                            if goles >= 0:
                                if i == 0:
                                    equipo_data['golesAnotados'] += goles
                                if i == 1:
                                    Equipos[equipo_local]['golesAnotados'] += goles_equipo_local
                                    if goles > goles_equipo_local:
                                        equipo_data['partidosGanados'] += 1
                                        Equipos[equipo_local]['partidosPerdidos'] += 1
                                        equipo_data['puntos'] += 3
                                    elif goles < goles_equipo_local:
                                        equipo_data['partidosPerdidos'] += 1
                                        Equipos[equipo_local]['partidosGanados'] += 1
                                        Equipos[equipo_local]['puntos'] += 3
                                    else:
                                        equipo_data['partidosEmpatados'] += 1
                                        Equipos[equipo_local]['partidosEmpatados'] += 1
                                        equipo_data['puntos'] += 1
                                        Equipos[equipo_local]['puntos'] += 1
                                is_goles = False
                            else:
                                print('Los goles no pueden ser negativos')
                else:
                    print('El equipo ingresado no se encuentra registrado')
                    os.system('pause')
    os.system('pause')

def reporte():
    max_goles_anotados = {'equipo': '', 'goles': -1}
    max_puntos = {'equipo': '', 'puntos': -1}
    max_partidos_ganados = {'equipo': '', 'partidos_ganados': -1}
    total_goles_anotados = 0
    total_partidos_jugados = 0

    os.system('cls')
    t.headerReportes()

    for nombre_equipo, datos_equipo in Equipos.items():
        goles_anotados = datos_equipo['golesAnotados']
        partidos_ganados = datos_equipo['partidosGanados']
        puntos = datos_equipo['puntos']
        partidos_jugados = datos_equipo['partidosJugados']

        total_goles_anotados += goles_anotados
        total_partidos_jugados += partidos_jugados

        if goles_anotados > max_goles_anotados['goles']:
            max_goles_anotados['equipo'] = nombre_equipo
            max_goles_anotados['goles'] = goles_anotados

        if puntos > max_puntos['puntos']:
            max_puntos['equipo'] = nombre_equipo
            max_puntos['puntos'] = puntos

        if partidos_ganados > max_partidos_ganados['partidos_ganados']:
            max_partidos_ganados['equipo'] = nombre_equipo
            max_partidos_ganados['partidos_ganados'] = partidos_ganados

    promedio_goles_anotados = total_goles_anotados / total_partidos_jugados

    is_report = True
    while is_report:
        try:
            m.menuReport()
            op = input(': ').upper()
        except ValueError:
            print('Dato erroneo')
        else:
            if op == 'A':
                print(f'Equipo que más goles anotó: {max_goles_anotados["equipo"]}')
                os.system('pause')
            elif op == 'B':
                print(f'Equipo que más puntos tiene: {max_puntos["equipo"]}')
                os.system('pause')
            elif op == 'C':
                print(f'Equipo que más partidos ganó: {max_partidos_ganados["equipo"]}')
                os.system('pause')
            elif op == 'D':
                print(f'Total de goles anotados en el torneo: {total_goles_anotados}')
                os.system('pause')
            elif op == 'E':
                print(f'Promedio de goles anotados en el torneo: {promedio_goles_anotados}')
                os.system('pause')
            elif op == 'F':
                is_report = False
            else:
                print('Dato no válido')

    os.system('pause')
