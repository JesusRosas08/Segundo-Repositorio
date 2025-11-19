import tkinter as tk

def sumar():

    num1 = float(entrada1.get())
    num2 = float(entrada2.get())
    

    suma = num1 + num2
    
    resultado.config(text=f"Resultado: {suma}")

ventana = tk.Tk()
ventana.title("Suma de dos números")
ventana.geometry("350x230")


entrada1 = tk.Entry(ventana)
entrada2 = tk.Entry(ventana)

entrada1.pack(pady=5)
entrada2.pack(pady=5)


boton_sumar = tk.Button(ventana, text="Sumar", command=sumar)
boton_sumar.pack(pady=5)

resultado = tk.Label(ventana, text="Resultado:")
resultado.pack(pady=5)

ventana.mainloop()
