from guizero import App, Box, PushButton, TextBox, Text

def calcular_sumatoria_pares():
    try:
        valor_max = int(textbox_valor_maximo.value)
        if valor_max > 0:
            suma = 0
            for i in range(2, valor_max + 1, 2):
                suma += i
            resultado.value = f"la suma de los valores pares hasta {valor_max} es de: {suma}"
        else:
            resultado.value = "ingresa un valor mayor que 0."
    except ValueError:
        resultado.value = "error"

app = App("sumatoria de pares con for")
main_box = Box(app, layout="grid")
Text(main_box, "valor máximo:", grid=[0, 0])
textbox_valor_maximo = TextBox(main_box, grid=[1, 0], width=20)
resultado = Text(main_box, text="", grid=[0, 1, 2, 1])
calcular_button = PushButton(main_box, calcular_sumatoria_pares, text="sumar", grid=[0, 2, 2, 1])

app.display()