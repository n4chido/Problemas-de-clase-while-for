from guizero import App, Box, PushButton, TextBox, Text

def calcular_producto():
    try:
        valor_maximo = int(textbox_valor_maximo.value)
        if valor_maximo > 0:
            producto = 1
            for i in range(1, valor_maximo + 1):
                producto *= i
            resultado.value = f"el producto de los valores desede 1 hasta {valor_maximo} es: {producto}"
        else:
            resultado.value = "tu un valor tiene que ser mayor que cero."
    except ValueError:
        resultado.value = "error"

app = App("calcular producto con for")
main_box = Box(app, layout="grid")
Text(main_box, "valor maximo:", grid=[0, 0])
textbox_valor_maximo = TextBox(main_box, grid=[1, 0])
resultado = Text(main_box, text="", grid=[0, 1, 2, 1])
calcular_button = PushButton(main_box, calcular_producto, text="calcular producto", grid=[0, 2, 2, 1])

app.display()
