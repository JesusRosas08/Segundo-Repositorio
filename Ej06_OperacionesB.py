#Agrega los botones restar, multiplicar y dividir. Usa en el mismo mensaje el resultado.
import tkinter as tk
def sumar():

    num1 = float(entrada1.get())
    num2 = float(entrada2.get())
    

    suma = num1 + num2
    
    resultado.config(text=f"Resultado: {suma}")
def restar():
      num3 = float(entrada1.get())
      num4 = float(entrada2.get())
    

      suma2 = num3 - num4
    
      resultado.config(text=f"Resultado: {suma2}")
def multiplicar():
      num5 = float(entrada1.get())
      num6 = float(entrada2.get())
    

      suma3 = num5 * num6
    
      resultado.config(text=f"Resultado: {suma3}")
def dividir():
      num7 = float(entrada1.get())
      num8 = float(entrada2.get())
    

      suma4 = num7 / num8
    
      resultado.config(text=f"Resultado: {suma4}")
ventana = tk.Tk()
ventana.title("Suma de dos números")
ventana.geometry("350x230")
entrada1 = tk.Entry(ventana)
entrada2 = tk.Entry(ventana)
entrada1.pack(pady=5)
entrada2.pack(pady=5)
boton_sumar = tk.Button(ventana, text="Sumar", command=sumar)
boton_sumar.pack(pady=5)
boton_sumar = tk.Button(ventana, text="restar", command=restar)
boton_sumar.pack(pady=5)
boton_sumar = tk.Button(ventana, text="multiplicar", command=multiplicar)
boton_sumar.pack(pady=5)
boton_sumar = tk.Button(ventana, text="dividir", command=dividir)
boton_sumar.pack(pady=5)
resultado = tk.Label(ventana, text="Resultado:")
resultado.pack(pady=5)
ventana.mainloop()
