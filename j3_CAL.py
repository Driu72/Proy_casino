from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.prompt import Prompt
from rich.align import Align
import imagenes_casino
import os
import random
import time

console = Console()

def num_dado():
    return random.randint(1, 6)

def unir_dados(lista_dados):
    lineas_por_dado = [dado.splitlines() for dado in lista_dados]
    dados_unidos = ["  ".join(lineas) for lineas in zip(*lineas_por_dado)]
    return "\n".join(dados_unidos)

def dado_imprimir(dado):
    return getattr(imagenes_casino, f"d{dado}")

def giro_dados():
    dados_ascii = [imagenes_casino.d1, imagenes_casino.d2, imagenes_casino.d3,
                   imagenes_casino.d4, imagenes_casino.d5, imagenes_casino.d6]

    pasos = 20
    for i in range(pasos):
        os.system('cls')
        cara1 = random.choice(dados_ascii)
        cara2 = random.choice(dados_ascii)
        cara3 = random.choice(dados_ascii)
        console.print(Panel(unir_dados([cara1, cara2, cara3]), title="Girando..."))
        time.sleep(0.05 + (0.15 * i / pasos))

  
    valores = [random.randint(1, 6) for _ in range(3)]
    caras_finales = [dado_imprimir(d) for d in valores]
    os.system('cls')
    console.print(Panel(unir_dados(caras_finales), title="Resultado Final"))
    return valores

def Chuckaluck(saldo):
    juego_activo = True

    while juego_activo:
        os.system('cls')
        console.print(Align.center(Panel("[bold magenta] CHUCK-A-LUCK - MENU PRINCIPAL [/bold magenta]", border_style="magenta")))
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
                os.system('cls')
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

                verif = False
                while not verif:
                    dado_jugador = input('Introduce el número que piensas que saldrá en los dados (1-6) -> ')
                    if dado_jugador.isdigit():
                        dado_jugador = int(dado_jugador)
                        if 1 <= dado_jugador <= 6:
                            verif = True
                        else:
                            print('Recuerda que los dados van del 1 al 6. No es un número válido.')
                    else:
                        print('Por favor, introduce un número')

                resultado = giro_dados()

                aciertos = resultado.count(dado_jugador)
                console.print(f"\nTu número fue [bold]{dado_jugador}[/bold]. Salió [bold]{aciertos}[/bold] vez/veces.", style="bold green" if aciertos else "bold red")

                if aciertos == 1:
                    ganancia = apuesta * 2
                    saldo += ganancia
                    console.print(f"¡Ganaste el doble! [+{ganancia}]")
                elif aciertos == 2:
                    ganancia = apuesta * 3
                    saldo += ganancia
                    console.print(f"¡Ganaste el triple! [+{ganancia}]")
                elif aciertos == 3:
                    ganancia = apuesta * 10
                    saldo += ganancia
                    console.print(f"¡TRIPLE! ¡Ganaste 10 veces tu apuesta! [+{ganancia}]")
                else:
                    console.print("No acertaste. Mejor suerte la próxima vez.")

                console.print(f"\nSaldo actual: [yellow]{saldo}[/yellow]")
                seguir = Prompt.ask("¿Deseas seguir jugando? (1/2)", choices=["1", "2"])
                if seguir == "n":
                    en_partida = False

        elif opcion == '2':
            os.system('cls')
            console.print(Panel("[bold cyan]Reglas del juego:[/bold cyan]\n\n"
                                "1. Elige un número del 1 al 6.\n"
                                "2. Se lanzan 3 dados.\n"
                                "3. Si tu número aparece:\n"
                                "   - Una vez: ganas el doble.\n"
                                "   - Dos veces: ganas el triple.\n"
                                "   - Tres veces: ganas 10 veces tu apuesta.\n"
                                "4. Si no aparece, pierdes tu apuesta.",
                                title="Reglas", border_style="cyan"))
            input("Presiona ENTER para volver al menú.")
        elif opcion == '3':
            juego_activo = False



