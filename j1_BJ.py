from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.prompt import Prompt
from rich.align import Align
import imagenes_casino
import os
import random
import pygame

pygame.init()
pygame.mixer.init()

def valor_carta(carta, puntos_actuales):
    if carta in ['J', 'Q', 'K']:
        return 10
    elif carta == 'AS':
        return 11 if puntos_actuales <= 10 else 1
    else:
        return int(carta)

def generar_carta():
    carta = random.randint(1, 13)
    if carta == 1:
        return 'AS'
    elif carta == 11:
        return 'J'
    elif carta == 12:
        return 'Q'
    elif carta == 13:
        return 'K'
    else:
        return str(carta)

def carta_imprimir(carta):
    if carta == 'AS':
        return imagenes_casino.ass
    elif carta == '2':
        return imagenes_casino.dos
    elif carta == '3':
        return imagenes_casino.tres
    elif carta == '4':
        return imagenes_casino.cuatro
    elif carta == '5':
        return imagenes_casino.cinco
    elif carta == '6':
        return imagenes_casino.seis
    elif carta == '7':
        return imagenes_casino.siete
    elif carta == '8':
        return imagenes_casino.ocho
    elif carta == '9':
        return imagenes_casino.nueve
    elif carta == '10':
        return imagenes_casino.diez
    elif carta == 'J':
        return imagenes_casino.j
    elif carta == 'K':
        return imagenes_casino.k
    elif carta == 'Q':
        return imagenes_casino.q

def unir_cartas_ascii(cartas_ascii):
    lineas_por_carta = [carta.splitlines() for carta in cartas_ascii]
    cartas_unidas = ["  ".join(lineas) for lineas in zip(*lineas_por_carta)]
    return "\n".join(cartas_unidas)

def calcular_puntos(mano):
    puntos = 0
    ases = 0
    for carta in mano:
        valor = valor_carta(carta, puntos)
        puntos += valor
        if carta == 'AS':
            ases += 1
    while puntos > 21 and ases > 0:
        puntos -= 10
        ases -= 1
    return puntos

def Blackjack(saldo):
    pygame.mixer.music.stop()
    pygame.mixer_music.load('jazzblackjack.mp3')
    pygame.mixer_music.play(-1)
    console = Console()
    juego_activo = True

    while juego_activo:
        os.system('cls')
        console.print(Align.center(Panel("[bold magenta] BLACKJACK - MENU PRINCIPAL [/bold magenta]", border_style="magenta")))
        console.print(Panel(
            "[cyan]1.[/] Empezar juego\n"
            "[cyan]2.[/] Reglas\n"
            "[cyan]3.[/] Salir",
            border_style="cyan", title="Opciones", title_align="left"
        ))
        opcion = Prompt.ask("[bold green]Elija una opción[/bold green]")

        if opcion == '1':
            en_partida = True
            while en_partida:
                os.system('cls' if os.name == 'nt' else 'clear')
                console.print(Panel("[bold yellow]ESCRIBA SU APUESTA[/bold yellow]", border_style="yellow"))

                while True:
                    apuesta = Prompt.ask("Ingrese apuesta")
                    if apuesta.isdigit():
                        apuesta = float(apuesta)
                        if apuesta > saldo:
                            console.print("[red] Estás apostando más de tu saldo.[/red]")
                            input("Pulsa ENTER para volver.")
                        else:
                            saldo -= apuesta
                            break

                cartas_jugador = [generar_carta(), generar_carta()]
                cartas_crupier = [generar_carta(), generar_carta()]
                imprimir_jd = [carta_imprimir(cartas_jugador[0]), carta_imprimir(cartas_jugador[1])]
                imprimir_cp = [carta_imprimir(cartas_crupier[0]), imagenes_casino.vuelta]

                while True:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    console.print(Panel(unir_cartas_ascii(imprimir_jd), title="Tus cartas", border_style="blue"))
                    console.print(Panel(unir_cartas_ascii(imprimir_cp), title="Carta del Crupier", border_style="red"))

                    console.print(Panel(
                        "[cyan]1.[/] Plantarse\n"
                        "[cyan]2.[/] Pedir otra carta\n"
                        "[cyan]3.[/] Doblar Apuesta\n"
                        "[cyan]4.[/] Ver reglas de valor de cartas",
                        border_style="cyan", title="Opciones"
                    ))
                    opcion = Prompt.ask("Elija opción")

                    if opcion == '1':
                        break
                    elif opcion == '2':
                        nueva = generar_carta()
                        cartas_jugador.append(nueva)
                        imprimir_jd.append(carta_imprimir(nueva))
                    elif opcion == '3':
                        if (apuesta * 2) > saldo:
                            console.print("[red] No puedes doblar la apuesta sin saldo suficiente.[/red]")
                            input("Pulsa ENTER.")
                        else:
                            saldo -= apuesta
                            apuesta *= 2
                            nueva = generar_carta()
                            cartas_jugador.append(nueva)
                            imprimir_jd.append(carta_imprimir(nueva))
                            console.print(f"[green] Apuesta doblada a {apuesta}[/green]")
                            break
                    elif opcion == '4':
                        input("J, Q y K valen 10 puntos. AS vale 1 o 11 según convenga. Pulsa ENTER.")

                imprimir_cp[1] = carta_imprimir(cartas_crupier[1])
                os.system('cls' if os.name == 'nt' else 'clear')
                console.print(Panel(unir_cartas_ascii(imprimir_cp), title="Cartas del Crupier", border_style="red"))
                input("Pulsa ENTER para continuar...")

                while True:
                    puntos_crupier = calcular_puntos(cartas_crupier)
                    if puntos_crupier >= 17:
                        break
                    nueva_carta = generar_carta()
                    cartas_crupier.append(nueva_carta)
                    imprimir_cp.append(carta_imprimir(nueva_carta))
                    os.system('cls' if os.name == 'nt' else 'clear')
                    console.print(Panel(unir_cartas_ascii(imprimir_cp), title="Cartas del Crupier", border_style="red"))
                    input(f"El Crupier saca: {nueva_carta}. Pulsa ENTER...")

                puntos_jugador = calcular_puntos(cartas_jugador)
                os.system('cls' if os.name == 'nt' else 'clear')
                console.print(f"[blue]Puntos del Jugador:[/blue] {puntos_jugador}")
                console.print(f"[red]Puntos del Crupier:[/red] {puntos_crupier}")

                if puntos_jugador > 21:
                    console.print("[bold red] Has perdido por pasarte de 21.[/bold red]")
                elif puntos_crupier > 21:
                    console.print("[bold green] ¡El Crupier se pasó! Has ganado.[/bold green]")
                    saldo += apuesta * 2.5
                elif puntos_jugador > puntos_crupier:
                    console.print("[bold green] ¡Has ganado![/bold green]")
                    saldo += apuesta * 2.5
                elif puntos_jugador == puntos_crupier:
                    console.print("[yellow] Empate. Recuperas la apuesta.[/yellow]")
                    saldo += apuesta
                else:
                    console.print("[bold red] Has perdido contra el Crupier.[/bold red]")

                console.print(f"[bold cyan] Saldo actual: {saldo} €[/bold cyan]")

                while True:
                    opcion = Prompt.ask("¿Seguir jugando?", choices=["1", "2"], default="1")
                    if opcion == '1':
                        break
                    elif opcion == '2':
                        en_partida = False
                        break

        elif opcion == '2':
            reglas = [
                "- Se reparten 2 cartas a ti y al Crupier.",
                "- Las cartas J, Q y K valen 10 puntos.",
                "- El AS vale 1 o 11 según convenga.",
                "- Tu objetivo es acercarte a 21 sin pasarte.",
                "- Si ganas con 21 exactos-> ganas el doble.",
                "- Si ganas con menos-> apuestas + mitad.",
                "- Si pierdes, pierdes tu apuesta.",
                "- ¡Disfruta del juego!"
            ]
            for regla in reglas:
                console.print(regla)
                input("Pulsa ENTER para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
        elif opcion == '3':
            input('VUELVA PRONTO!')
            pygame.mixer.music.stop()
            pygame.quit()
            os.system('cls' if os.name == 'nt' else 'clear')
            return saldo


        





                    
            

            


