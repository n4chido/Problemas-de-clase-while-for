from guizero import App, Box, PushButton, TextBox, Text

def calcular_suma_cubos():
    try:
        valor_max = int(textbox_valor_maximo.value)
        if valor_max > 0:
            suma = 0
            for i in range(1, valor_max + 1):
                suma += i**3 
            resultado.value = f"la suma de los valores sucesivos hasta {valor_max} es: {suma}"
        else:
            resultado.value = "ingresa un valor mayor que 0."
    except ValueError:
        resultado.value = "error"

app = App("suma de cubos con for")
main_box = Box(app, layout="grid")
Text(main_box, "valor maximo:", grid=[0, 0])
textbox_valor_maximo = TextBox(main_box, grid=[1, 0], width=20)
resultado = Text(main_box, text="", grid=[0, 1, 2, 1])
calcular_button = PushButton(main_box, calcular_suma_cubos, text="sumarr", grid=[0, 2, 2, 1])

app.display()
