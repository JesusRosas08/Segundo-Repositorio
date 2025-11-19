#Realiza un programa con dos botones. Cada botón abrirá una ventana.
# La primera ventana contendrá etiquetas con tu nombre y apellidos y la segunda ventana tendrá el mensaje, «Programado con Python».

import tkinter as tk
from tkinter import Toplevel

ventana_principal = tk.Tk()
ventana_principal.title("Ventana Principal")
ventana_principal.geometry("300x200")

def abrir_ventana_hija():
    ventana_hija = Toplevel(ventana_principal)
    ventana_hija.title("Ventana Hija")
    ventana_hija.geometry("250x150")
    
    etiqueta = tk.Label(ventana_hija, text="Jesus Antonio Tadeo", font=("Arial", 12))
    etiqueta.pack(pady=10)
    
    boton_cerrar = tk.Button(ventana_hija, text="Cerrar", command=ventana_hija.destroy)
    boton_cerrar.pack(pady=10)

boton_abrir = tk.Button(ventana_principal, text="Nombre y Apellidos", command=abrir_ventana_hija)
boton_abrir.pack(pady=20)


def abrir_ventana_hija():
    ventana_hija2 = Toplevel(ventana_principal)
    ventana_hija2.title("Ventana Hija")
    ventana_hija2.geometry("250x150")
    
    etiqueta = tk.Label(ventana_hija2, text="Programando con python", font=("Arial", 12))
    etiqueta.pack(pady=10)
    
    boton_cerrar = tk.Button(ventana_hija2, text="Cerrar", command=ventana_hija2.destroy)
    boton_cerrar.pack(pady=10)
    
boton_abrir2 = tk.Button(ventana_principal, text="mensaje", command=abrir_ventana_hija)
boton_abrir2.pack(pady=20)


ventana_principal.mainloop()