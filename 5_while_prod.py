from guizero import App, Box, PushButton, TextBox, Text

def calcular_producto():
    try:
        num1 = int(textbox_num1.value)
        num2 = int(textbox_num2.value)

        if num1 > 0 and num2 > 0:
            producto = 0
            i = 0
            while i < num2:
                producto += num1
                i += 1
            resultado.value = f"el producto de {num1} y {num2} es: {producto}"
        else:
            resultado.value = "los numeros deben ser enteros positivos."
    except ValueError:
        resultado.value = "error"

app = App("producto de sumas sucesivas con while")
main_box = Box(app, layout="grid")
Text(main_box, "numero 1:", grid=[0, 0])
textbox_num1 = TextBox(main_box, grid=[1, 0])
Text(main_box, "numero 2:", grid=[0, 1])
textbox_num2 = TextBox(main_box, grid=[1, 1])
resultado = Text(main_box, text="", grid=[0, 2, 2, 1])
calcular_button = PushButton(main_box, calcular_producto, text="calcular", grid=[0, 3, 2, 1])

app.display()
