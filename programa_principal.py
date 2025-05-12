import os
import imagenes_casino
import llamada_base_datos
import funci_extra
import j1_BJ
import j1_TRP
import j3_CAL
from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.prompt import Prompt
from rich.align import Align

console = Console()
casino = llamada_base_datos.gestCasino()
casino.conexionYcreacion()

mural = Align.center(imagenes_casino.mural_casino)

menu_texto = """
[bold cyan]1.[/bold cyan] Registrarse
[bold cyan]2.[/bold cyan] Jugar sin Registro
[bold cyan]3.[/bold cyan] Inicio de Sesión
[bold cyan]4.[/bold cyan] Cerrar Casino
"""

menu_juegos = """
[bold cyan]1.[/bold cyan] BlackJack
[bold cyan]2.[/bold cyan] Tragaperras
[bold cyan]3.[/bold cyan] Chuck-a-Luck
[bold cyan]----------------------------------------[/bold cyan]
[bold cyan]4.[/bold cyan] Volver al Menu Principal
[bold cyan]5.[/bold cyan] Ingresar Saldo
[bold cyan]6.[/bold cyan] Retirar Saldo
[bold cyan]7.[/bold cyan] Ver Saldo
[bold cyan]8.[/bold cyan] Salir del Casino
"""

menu_prin = True

while menu_prin:
    os.system('cls')
    console.print(mural, style="bold magenta")
    console.print(Panel(Align.center(menu_texto), title="[bold yellow]MENU PRINCIPAL[/bold yellow]", border_style="bright_blue"))

    opcion = Prompt.ask("[bold green]Elije una opción (ESCRIBA EL NÚMERO)[/bold green]->")

    match opcion:
        case '1':
            # Registro
            nombre = input('Escriba su nombre -> ')
            apellidos = input('Escriba sus apellidos -> ')
            dni = funci_extra.hacerdni()

            while True:
                edad = input('Escriba su edad -> ')
                if edad.isdigit() and int(edad) >= 18:
                    break
                console.print("[bold red]Edad no válida, necesita ser mayor de edad[/bold red]")

            while True:
                console.print(Panel.fit(
                    f"[bold white]Nombre:[/bold white] {nombre} {apellidos}\n[bold white]Edad:[/bold white] {edad}\n[bold white]DNI:[/bold white] {dni}",
                    title="[bold cyan]Verificación de Datos[/bold cyan]", border_style="bright_magenta")
                )
                satis = input('Estás satisfecho con los datos? (SI-> 1 | NO-> 2) -> ')
                if satis == '1':
                    casino.registro_usu(dni, nombre, apellidos, edad, 0)
                    console.print("[bold green]Registro completado con éxito.[/bold green]")
                    input()
                    break
                elif satis == '2':
                    console.print("[bold yellow]Volverá a introducir los datos...[/bold yellow]")
                    input()
                    os.system('cls')
                    break
                else:
                    console.print("[bold red]Opción no válida. Volverá al menú...[/bold red]")
                    input()
                    os.system('cls')
                    break

        case '2':
            # Jugar sin registro
            menu_noregistro = True
            saldo_noregistro = 0

            while menu_noregistro:
                os.system('cls')
                console.print(Panel(Align.center(menu_juegos), title="[bold magenta]JUEGOS[/bold magenta]", border_style="bright_yellow"))
                opcion = Prompt.ask("[bold green]Elije una opción (ESCRIBA EL NÚMERO)[/bold green] ->")

                match opcion:
                    case '1':
                        if saldo_noregistro <= 0:
                            console.print("[bold red]Sin SALDO no puede jugar.[/bold red]")
                        else:
                            saldo_noregistro = j1_BJ.Blackjack(saldo_noregistro)
                        input()
                    case '2':
                        if saldo_noregistro <= 0:
                            console.print("[bold red]Sin SALDO no puede jugar.[/bold red]")
                        else:
                            saldo_noregistro = j1_TRP.tragaperras(saldo_noregistro)
                        input()
                    case '3':
                        if saldo_noregistro <= 0:
                            console.print("[bold red]Sin SALDO no puede jugar.[/bold red]")
                        else:
                            saldo_noregistro = j3_CAL.Chuckaluck(saldo_noregistro)
                        input()
                    case '4':
                        menu_noregistro = False
                    case '5':
                        ingres = input('Escriba el dinero a ingresar -> ')
                        if ingres.isdigit() and float(ingres) > 0:
                            saldo_noregistro += float(ingres)
                            console.print(f"[bold green] Dinero ingresado con éxito\n[bold white]Saldo actual:[/bold white] {saldo_noregistro}")
                        else:
                            console.print("[bold red] Valor no válido o no numérico.[/bold red]")
                        input()
                    case '6':
                        ingres = input('Escriba el dinero a retirar -> ')
                        if ingres.isdigit() and float(ingres) > 0 and float(ingres) <= saldo_noregistro:
                            saldo_noregistro -= float(ingres)
                            console.print(f"[bold green] Retiro realizado\n[bold white]Saldo actual:[/bold white] {saldo_noregistro}")
                        else:
                            console.print("[bold red] No se pudo retirar. Verifique el monto.[/bold red]")
                        input()
                    case '7':
                        console.print(f"[bold cyan] Saldo disponible: {saldo_noregistro}[/bold cyan]")
                        input()
                    case '8':
                        input('Cerrando programa...')
                        casino.cerrarconexion()
                        menu_noregistro = False
                        menu_prin = False

        case '3':
            # Iniciar sesión
            verif = False
            while not verif:
                os.system('cls')
                console.print("[bold yellow]- INICIO DE SESIÓN -[/bold yellow]")
                dni_reg = funci_extra.hacerdni()
                nombre = input('Escriba su nombre -> ')
                if casino.revision_datos(dni_reg, nombre):
                    verif = True
                    menu_registro = True
                else:
                    console.print("[bold red]Usuario no registrado[/bold red]")
                    if input('¿Intentar de nuevo? (SI->1 | NO->2) -> ') == '2':
                        break

            while menu_registro:
                os.system('cls')
                saldo_registro = casino.dispo_saldo(dni_reg)
                console.print(Panel(Align.center(menu_juegos), title="[bold magenta]JUEGOS[/bold magenta]", border_style="bright_yellow"))
                opcion = Prompt.ask("[bold green]Elije una opción (ESCRIBA EL NÚMERO)[/bold green] ->")

                match opcion:
                    case '1':
                        if saldo_registro > 0:
                            saldo_registro = j1_BJ.Blackjack(saldo_registro)
                            casino.actualizar_saldo(dni_reg, saldo_registro)
                        else:
                            console.print("[bold red]Sin SALDO no puede jugar.[/bold red]")
                        input()
                    case '2':
                        if saldo_registro > 0:
                            saldo_registro = j1_TRP.tragaperras(saldo_registro)
                            casino.actualizar_saldo(dni_reg, saldo_registro)
                        else:
                            console.print("[bold red]Sin SALDO no puede jugar.[/bold red]")
                        input()
                    case '3':
                        if saldo_registro > 0:
                            saldo_registro = j3_CAL.Chuckaluck(saldo_registro)
                            casino.actualizar_saldo(dni_reg, saldo_registro)
                        else:
                            console.print("[bold red]Sin SALDO no puede jugar.[/bold red]")
                        input()
                    case '4':
                        menu_registro = False
                    case '5':
                        try:
                            saldo_ingreso = float(input('Cantidad a ingresar -> '))
                            casino.ingreso_saldo(saldo_ingreso, dni_reg)
                            console.print(f"[bold green]Ingreso realizado\nSALDO ACTUAL -> {casino.dispo_saldo(dni_reg)}[/bold green]")
                        except ValueError:
                            console.print("[bold red]Valor no válido[/bold red]")
                        input()
                    case '6':
                        try:
                            retiro = float(input('Cantidad a retirar -> '))
                            saldo_actual = casino.dispo_saldo(dni_reg)
                            if retiro <= saldo_actual:
                                casino.retiro_saldo(retiro, dni_reg)
                                console.print(f"[bold green]Retiro exitoso\nSALDO ACTUAL -> {casino.dispo_saldo(dni_reg)}[/bold green]")
                            else:
                                console.print("[bold red]Saldo insuficiente[/bold red]")
                        except ValueError:
                            console.print("[bold red]Valor inválido[/bold red]")
                        input()
                    case '7':
                        saldo = casino.dispo_saldo(dni_reg)
                        console.print(f"[bold cyan] Saldo disponible: {saldo} [/bold cyan]")
                        input()
                    case '8':
                        input('Cerrando programa...')
                        casino.cerrarconexion()
                        menu_registro = False
                        menu_prin = False

        case '4':
            casino.cerrarconexion()
            console.print("[bold yellow]¡VUELVA PRONTO![/bold yellow]")
            os.system('cls')
            menu_prin = False

        case '72':
            casino.conexionYcreacion()
            os.system('cls')

        case 'borradobbdd':
            casino.borrado()
