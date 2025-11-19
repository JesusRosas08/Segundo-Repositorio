import tkinter as tk
def Dolares():
    cantidad = float(entrada1.get())
    divisa = cantidad/18.46
    resultado.config(text=f"Resultado: {divisa}")
def Euros():
      cantidad = float(entrada1.get())
      divisa = cantidad/21.48
      resultado.config(text=f"Resultado: {divisa}")
def Libras():
      cantidad = float(entrada1.get())
      divisa = cantidad/24.63
      resultado.config(text=f"Resultado: {divisa}")
def Yenes():
      cantidad = float(entrada1.get())
      divisa = cantidad/0.12
      resultado.config(text=f"Resultado: {divisa}")

ventana = tk.Tk()
ventana.title("Divisas")
ventana.geometry("350x230")
entrada1 = tk.Entry(ventana)
entrada1.pack(pady=5)
boton_sumar = tk.Button(ventana, text="Dolares", command=Dolares)
boton_sumar.pack(pady=5)
boton_sumar = tk.Button(ventana, text="Euros", command=Euros)
boton_sumar.pack(pady=5)
boton_sumar = tk.Button(ventana, text="Libras", command=Libras)
boton_sumar.pack(pady=5)
boton_sumar = tk.Button(ventana, text="Yenes", command=Yenes)
boton_sumar.pack(pady=5)
resultado = tk.Label(ventana, text="El cambio de tu divisa es:")
resultado.pack(pady=5)
ventana.mainloop()
