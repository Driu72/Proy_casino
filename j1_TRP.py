from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from rich.prompt import Prompt
from rich import box
import os
import random
import imagenes_casino
import time
import pygame

console = Console()

pygame.init()
pygame.mixer.init()
pygame.mixer.music.stop()



def generar_simbolos():
    simbolos = ['🍒', '🍋', '🔔', '7️⃣']
    return [random.choice(simbolos) for _ in range(3)]

def tragaperras(saldo):
    juegotp = True
    while juegotp:
        pygame.mixer_music.load('musictpr.mp3')
        pygame.mixer_music.play(-1)

        if saldo < 1:
            console.print("[bold red]No dispone de saldo suficiente, volverá al Menu de Juegos[/bold red]")
            input()
            os.system('cls')
            return saldo

        os.system('cls')
        console.print(Panel("[bold yellow]--- INICIO DEL JUEGO ---\n      1. Empezar juego\n      2. Reglas\n      3. Salir[/bold yellow]", title="[bold green]Tragaperras[/bold green]", style="bold blue", box=box.DOUBLE))
        opcion = Prompt.ask("[bold white]Elija una opción[/bold white]", choices=["1", "2", "3"])

        if opcion == '1':
            ingame = True
            while ingame:
                os.system('cls')
                console.print("\n[bold cyan]-- POR FAVOR ESCRIBA SU APUESTA --[/bold cyan]")
                verif = False
                while not verif:
                    apuesta = Prompt.ask("[bold white]Introduce sin decimales[/bold white]")
                    if apuesta.isdigit():
                        apuesta = int(apuesta)
                        if apuesta > saldo:
                            console.print("[red]Estás apostando más dinero del que posees. Cambia la apuesta.[/red]")
                            input()
                        else:
                            saldo -= apuesta
                            verif = True
                    else:
                        console.print("[red]Introduce una cantidad válida[/red]")

                console.print("\n[italic yellow]Tendrás tantos giros como el número apostado[/italic yellow]")
                console.print("[dim]No pulses nada por favor hasta que se te indique[/dim]")
                time.sleep(5)
                premio = 0

                for giro in range(apuesta):
                    apuesta -= 1
                    slots = generar_simbolos()

                    for i in range(7):
                        os.system('cls')
                        console.print(Align.center(imagenes_casino.ani1))
                        time.sleep(0.2)
                        os.system('cls')
                        console.print(Align.center(imagenes_casino.ani2))
                        time.sleep(0.2)
                        os.system('cls')


                    if slots == ["🍒", "🍒", "🍒"]: 
                        console.print(Align.center(imagenes_casino.cercercer1))
                        print('Enhorabuena Obtuviste 2€')
                        premio+=2
                        time.sleep(3)
                        os.system('cls')
                    elif slots == ["🍒", "🍒", "🍋"]:
                        console.print(Align.center(imagenes_casino.cercerlim2))
                        print('Enhorabuena Obtuviste un Premio')
                        premio+=0.2
                        time.sleep(5)
                        os.system('cls')
                    elif slots == ["🍒", "🍒", "🔔"]:
                        console.print(Align.center(imagenes_casino.cercerbel3))
                        print('Enhorabuena Obtuviste un Premio')
                        premio+=0.2
                        time.sleep(5)
                        os.system('cls')
                    elif slots == ["🍒", "🍒", "7️⃣"]:
                        console.print(Align.center(imagenes_casino.cercer74))
                        print('Enhorabuena Obtuviste un Premio')
                        premio+=0.2
                        time.sleep(5)
                        os.system('cls')
                    elif slots == ["🍒", "🍋", "🍒"]:
                        console.print(Align.center(imagenes_casino.cerlimcer5))
                        time.sleep(3)
                    elif slots == ["🍒", "🍋", "🍋"]:
                        console.print(Align.center(imagenes_casino.cerlimlim6))
                        print('Enhorabuena Obtuviste un Premio')
                        premio+=0.5
                        time.sleep(5)
                        os.system('cls')
                    elif slots == ["🍒", "🍋", "🔔"]:
                        console.print(Align.center(imagenes_casino.cerlimbel7))
                        time.sleep(3)
                    elif slots == ["🍒", "🍋", "7️⃣"]:
                        console.print(Align.center(imagenes_casino.cerlim78))
                        time.sleep(3)
                    elif slots == ["🍒", "🔔", "🍒"]:
                        console.print(Align.center(imagenes_casino.cerbelcer9))
                        time.sleep(3)
                    elif slots == ["🍒", "🔔", "🍋"]:
                        console.print(Align.center(imagenes_casino.cerbellim10))
                        time.sleep(3)
                    elif slots == ["🍒", "🔔", "🔔"]:
                        console.print(Align.center(imagenes_casino.cerbelbel11))
                        print('Enhorabuena Obtuviste un Premio')
                        premio+=1
                        time.sleep(5)
                        os.system('cls')
                    elif slots == ["🍒", "🔔", "7️⃣"]:
                        console.print(Align.center(imagenes_casino.cerbel712))
                        time.sleep(3)
                    elif slots == ["🍒", "7️⃣", "🍒"]:
                        console.print(Align.center(imagenes_casino.cer7cer13))
                        time.sleep(3)
                    elif slots == ["🍒", "7️⃣", "🍋"]:
                        console.print(Align.center(imagenes_casino.cer7lim14))
                        time.sleep(3)
                    elif slots == ["🍒", "7️⃣", "🔔"]:
                        console.print(Align.center(imagenes_casino.cer7bel15))
                        time.sleep(3)
                    elif slots == ["🍒", "7️⃣", "7️⃣"]:
                        console.print(Align.center(imagenes_casino.cer7716))
                        print('Enhorabuena Obtuviste 15€')
                        premio+=15
                        time.sleep(5)
                        os.system('cls')
                    elif slots == ["🍋", "🍒", "🍒"]:
                        console.print(Align.center(imagenes_casino.limcercer17))
                        print('Enhorabuena Obtuviste un Premio')
                        premio+=0.2
                        time.sleep(5)
                        os.system('cls')
                    elif slots == ["🍋", "🍒", "🍋"]:
                        console.print(Align.center(imagenes_casino.limcerlim18))
                        time.sleep(3)
                    elif slots == ["🍋", "🍒", "🔔"]:
                        console.print(Align.center(imagenes_casino.limcerbel19))
                        time.sleep(3)
                    elif slots == ["🍋", "🍒", "7️⃣"]:
                        console.print(Align.center(imagenes_casino.limcer720))
                        time.sleep(3)
                    elif slots == ["🍋", "🍋", "🍒"]:
                        console.print(Align.center(imagenes_casino.limlimcer21))
                        print('Enhorabuena Obtuviste un Premio')
                        premio+=0.5
                        time.sleep(5)
                        os.system('cls')
                    elif slots == ["🍋", "🍋", "🍋"]:
                        console.print(Align.center(imagenes_casino.limlimlim22))
                        print('Enhorabuena Obtuviste 10€')
                        premio+=10
                        time.sleep(5)
                        os.system('cls')
                    elif slots == ["🍋", "🍋", "🔔"]:
                        console.print(Align.center(imagenes_casino.limlimbel23))
                        time.sleep(3)
                    elif slots == ["🍋", "🍋", "7️⃣"]:
                        console.print(Align.center(imagenes_casino.limlim724))
                        print('Enhorabuena Obtuviste un Premio')
                        premio+=0.5
                        time.sleep(5)
                        os.system('cls')
                    elif slots == ["🍋", "🔔", "🍒"]:
                        console.print(Align.center(imagenes_casino.limbelcer25))
                        time.sleep(3)
                    elif slots == ["🍋", "🔔", "🍋"]:
                        console.print(Align.center(imagenes_casino.limbellim26))
                        time.sleep(3)
                    elif slots == ["🍋", "🔔", "🔔"]:
                        console.print(Align.center(imagenes_casino.limbelbel27))
                        print('Enhorabuena Obtuviste un Premio')
                        premio+=1
                        time.sleep(5)
                        os.system('cls')
                    elif slots == ["🍋", "🔔", "7️⃣"]:
                        console.print(Align.center(imagenes_casino.limbel728))
                        time.sleep(3)
                    elif slots == ["🍋", "7️⃣", "🍒"]:
                        console.print(Align.center(imagenes_casino.lim7cer29))
                        time.sleep(3)
                    elif slots == ["🍋", "7️⃣", "🍋"]:
                        console.print(Align.center(imagenes_casino.lim7lim30))
                        time.sleep(3)
                    elif slots == ["🍋", "7️⃣", "🔔"]:
                        console.print(Align.center(imagenes_casino.lim7bel31))
                        time.sleep(3)
                    elif slots == ["🍋", "7️⃣", "7️⃣"]:
                        console.print(Align.center(imagenes_casino.lim7732))
                        print('Enhorabuena Obtuviste 15€')
                        premio+=15
                        time.sleep(5)
                        os.system('cls')
                    elif slots == ["🔔", "🍒", "🍒"]:
                        console.print(Align.center(imagenes_casino.belcercer33))
                        print('Enhorabuena Obtuviste un Premio')
                        premio+=0.2
                        time.sleep(5)
                        os.system('cls')
                    elif slots == ["🔔", "🍒", "🍋"]:
                        console.print(Align.center(imagenes_casino.belcerlim34))
                        time.sleep(3)
                    elif slots == ["🔔", "🍒", "🔔"]:
                        console.print(Align.center(imagenes_casino.belcerbel35))
                        time.sleep(3)
                    elif slots == ["🔔", "🍒", "7️⃣"]:
                        console.print(Align.center(imagenes_casino.belcer736))
                        time.sleep(3)
                    elif slots == ["🔔", "🍋", "🍒"]:
                        console.print(Align.center(imagenes_casino.bellimcer37))
                        time.sleep(3)
                    elif slots == ["🔔", "🍋", "🍋"]:
                        console.print(Align.center(imagenes_casino.bellimlim38))
                        print('Enhorabuena Obtuviste un Premio')
                        premio+=0.5
                        time.sleep(5)
                        os.system('cls')
                    elif slots == ["🔔", "🍋", "🔔"]:
                        console.print(Align.center(imagenes_casino.bellimbel39))
                        time.sleep(3)
                    elif slots == ["🔔", "🍋", "7️⃣"]:
                        console.print(Align.center(imagenes_casino.bellim740))
                        time.sleep(3)
                    elif slots == ["🔔", "🔔", "🍒"]:
                        console.print(Align.center(imagenes_casino.belbelcer41))
                        print('Enhorabuena Obtuviste un Premio')
                        premio+=1
                        time.sleep(5)
                        os.system('cls')
                    elif slots == ["🔔", "🔔", "🍋"]:
                        console.print(Align.center(imagenes_casino.belbellim42))
                        print('Enhorabuena Obtuviste un Premio')
                        premio+=1
                        time.sleep(5)
                        os.system('cls')
                    elif slots == ["🔔", "🔔", "🔔"]:
                        console.print(Align.center(imagenes_casino.belbelbel43))
                        print('Enhorabuena Obtuviste 20€')
                        premio+=20
                        time.sleep(5)
                        os.system('cls')
                    elif slots == ["🔔", "🔔", "7️⃣"]:
                        console.print(Align.center(imagenes_casino.belbel744))
                        print('Enhorabuena Obtuviste un Premio')
                        premio+=1
                        time.sleep(5)
                        os.system('cls')
                    elif slots == ["🔔", "7️⃣", "🍒"]:
                        console.print(Align.center(imagenes_casino.bel7cer45))
                        time.sleep(3)
                    elif slots == ["🔔", "7️⃣", "🍋"]:
                        console.print(Align.center(imagenes_casino.bel7lim46))
                        time.sleep(3)
                    elif slots == ["🔔", "7️⃣", "🔔"]:
                        console.print(Align.center(imagenes_casino.bel7bel47))
                        time.sleep(3)
                    elif slots == ["🔔", "7️⃣", "7️⃣"]:
                        console.print(Align.center(imagenes_casino.bel7748))
                        
                        print('Enhorabuena Obtuviste 15€')
                        premio+=15
                        time.sleep(5)
                        os.system('cls')
                    elif slots == ["7️⃣", "🍒", "🍒"]:
                        console.print(Align.center(imagenes_casino.a7cercer49))
                        print('Enhorabuena Obtuviste un Premio')
                        premio+=0.2
                        time.sleep(5)
                        os.system('cls')
                    elif slots == ["7️⃣", "🍒", "🍋"]:
                        console.print(Align.center(imagenes_casino.a7cerlim50))
                        time.sleep(3)
                    elif slots == ["7️⃣", "🍒", "🔔"]:
                        console.print(Align.center(imagenes_casino.a7cerbel51))
                        time.sleep(3)
                    elif slots == ["7️⃣", "🍒", "7️⃣"]:
                        console.print(Align.center(imagenes_casino.a7cer752))
                        time.sleep(3)
                    elif slots == ["7️⃣", "🍋", "🍒"]:
                        console.print(Align.center(imagenes_casino.a7limcer53))
                        time.sleep(3)
                    elif slots == ["7️⃣", "🍋", "🍋"]:
                        console.print(Align.center(imagenes_casino.a7limlim54))
                        print('Enhorabuena Obtuviste un Premio')
                        premio+=0.5
                        time.sleep(5)
                        os.system('cls')
                    elif slots == ["7️⃣", "🍋", "🔔"]:
                        console.print(Align.center(imagenes_casino.a7limbel55))
                        time.sleep(3)
                    elif slots == ["7️⃣", "🍋", "7️⃣"]:
                        console.print(Align.center(imagenes_casino.a7lim756))
                        time.sleep(3)
                    elif slots == ["7️⃣", "🔔", "🍒"]:
                        console.print(Align.center(imagenes_casino.a7belcer57))
                        time.sleep(3)
                    elif slots == ["7️⃣", "🔔", "🍋"]:
                        console.print(Align.center(imagenes_casino.a7bellim58))
                        time.sleep(3)
                    elif slots == ["7️⃣", "🔔", "🔔"]:
                        console.print(Align.center(imagenes_casino.a7belbel59))
                        print('Enhorabuena Obtuviste un Premio')
                        premio+=1
                        time.sleep(5)
                        os.system('cls')
                    elif slots == ["7️⃣", "🔔", "7️⃣"]:
                        console.print(Align.center(imagenes_casino.a7bel760))
                        time.sleep(3)
                    elif slots == ["7️⃣", "7️⃣", "🍒"]:
                        console.print(Align.center(imagenes_casino.a77cer61))
                        print('Enhorabuena Obtuviste 25€')
                        premio+=25
                        time.sleep(5)
                        os.system('cls')
                    elif slots == ["7️⃣", "7️⃣", "🍋"]:
                        console.print(Align.center(imagenes_casino.a77lim62))
                        print('Enhorabuena Obtuviste un Premio')
                        premio+=(apuesta +(apuesta/2))
                        time.sleep(5)
                        os.system('cls')
                    elif slots == ["7️⃣", "7️⃣", "🔔"]:
                        console.print(Align.center(imagenes_casino.a77bel63))
                        print('Enhorabuena doblaste tu apuesta, tendras más giros')
                        apuesta*=2
                        time.sleep(5)
                        os.system('cls')
                    elif slots == ["7️⃣", "7️⃣", "7️⃣"]:
                        console.print(Align.center(imagenes_casino.a77764))
                        print('Enhorabuena Obtuviste 50€')
                        premio+=50
                        time.sleep(5)
                        os.system('cls')
                console.print(Panel(f"[bold green]Has conseguido {premio:.2f}€[/bold green]", title="[bold cyan]Ganancias[/bold cyan]"))
                saldo += premio
                time.sleep(5)
                seguir = Prompt.ask("[bold white]¿Seguir jugando?[/bold white]", choices=["1", "2"], default="1")
                if seguir != '1':
                    ingame = False

        elif opcion == '2':
            reglas = """
Consiste en apostar dinero para hacer girar unos carretes que contienen símbolos.
El objetivo es obtener combinaciones específicas de esos símbolos que otorgan premios.

[bold yellow]-- PREMIOS PRINCIPALES --[/bold yellow]
[green]🍒🍒🍒[/green] - 2€
[green]🍋🍋🍋[/green] - 10€
[green]🔔🔔🔔[/green] - 20€
[green]7️⃣7️⃣🍒[/green] - 25€
[green]7️⃣7️⃣🍋[/green] - Apuesta + (Apuesta / 2)
[green]7️⃣7️⃣🔔[/green] - Más giros
[green]7️⃣7️⃣7️⃣[/green] - 50€
"""
            console.print(Panel(reglas, title="[bold blue]Reglas del Juego[/bold blue]", style="bold white"))
            input("Presiona Enter para continuar...")

        elif opcion == '3':
            console.print("[bold red]¡Vuelva pronto![/bold red]")
            pygame.mixer.music.stop()
            pygame.quit()
            os.system('cls')
            juegotp = False
            return saldo
