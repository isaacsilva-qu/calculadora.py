from tkinter import *

def limparDisplay() -> None:
    display.delete(0, END)

def inserir(valor: str) -> None:
    display.insert(END, valor)

def calcularResultado() -> None:
    textoDisplay = display.get()
    resultado = eval(textoDisplay)
    limparDisplay()
    inserir(resultado)


janela = Tk()
janela.title("Calculadora")
display = Entry(janela, background="white",font= "Tahoma 24", width=20,
                foreground="black")
display.pack()

frame = Frame(janela)
frame.pack()

# Variaves
silver = "#c0c0c0"
orange = "#ff9500"
gray = "#808080"

# Botões
btn0 = Button(frame, text="0", bg=silver, fg="white", font= "Tahoma 16 bold",
              height=3, width=6, command=lambda: inserir("0"))
btn1 = Button(frame, text="1", bg=silver, fg="white", font= "Tahoma 16 bold",
              height=3, width=6, command=lambda: inserir("1"))
btn2 = Button(frame, text="2", bg=silver, fg="white", font= "Tahoma 16 bold",
              height=3, width=6, command=lambda: inserir("2"))
btn3 = Button(frame, text="3", bg=silver, fg="white", font= "Tahoma 16 bold",
              height=3, width=6, command=lambda: inserir("3"))
btn4 = Button(frame, text="4", bg=silver, fg="white", font= "Tahoma 16 bold",
              height=3, width=6, command=lambda: inserir("4"))
btn5 = Button(frame, text="5", bg=silver, fg="white", font= "Tahoma 16 bold",
              height=3, width=6, command=lambda: inserir("5"))
btn6 = Button(frame, text="6", bg=silver, fg="white", font= "Tahoma 16 bold",
              height=3, width=6, command=lambda: inserir("6"))
btn7 = Button(frame, text="7", bg=silver, fg="white", font= "Tahoma 16 bold",
              height=3, width=6, command=lambda: inserir("7"))
btn8 = Button(frame, text="8", bg=silver, fg="white", font= "Tahoma 16 bold",
              height=3, width=6, command=lambda: inserir("8"))
btn9 = Button(frame, text="9", bg=silver, fg="white", font= "Tahoma 16 bold",
              height=3, width=6, command=lambda: inserir("9"))
btnSomar = Button(frame, text="+", bg=gray, fg="white", font= "Tahoma 16 bold",
              height=3, width=6, command=lambda: inserir("+"))
btnSubtrair = Button(frame, text="-", bg=gray, fg="white", font= "Tahoma 16 bold",
              height=3, width=6, command=lambda: inserir("-"))
btnMultiplicar = Button(frame, text="*", bg=gray, fg="white", font= "Tahoma 16 bold",
              height=3, width=6, command=lambda: inserir("*"))
btnDividir = Button(frame, text="/", bg=gray, fg="white", font= "Tahoma 16 bold",
              height=3, width=6, command=lambda: inserir("/"))
btnLimpar = Button(frame, text="C", bg=gray, fg="white", font= "Tahoma 16 bold",
              height=3, width=6, command=limparDisplay)
btnIgual = Button(frame, text="=", bg=gray, fg="white", font= "Tahoma 16 bold",
              height=3, width=6, command=calcularResultado)


# Primeira linha
btn7.grid(row=0, column=0)
btn8.grid(row=0, column=1)
btn9.grid(row=0, column=2)
btnSomar.grid(row=0, column=3)

# Segunda linha
btn4.grid(row=1, column=0)
btn5.grid(row=1, column=1)
btn6.grid(row=1, column=2)
btnSubtrair.grid(row=1, column=3)

# Terceira linha
btn1.grid(row=2, column=0)
btn2.grid(row=2, column=1)
btn3.grid(row=2, column=2)
btnMultiplicar.grid(row=2, column=3)

# Quarta linha
btnIgual.grid(row=3, column=0)
btn0.grid(row=3, column=1)
btnLimpar.grid(row=3, column=2)
btnDividir.grid(row=3, column=3)


janela.mainloop()