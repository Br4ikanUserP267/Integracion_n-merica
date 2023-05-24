import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import simpledialog

def interpolar(tiempo, tasa_autos, x):
    # Interpolación lineal
    for i in range(len(tiempo)-1):
        if tiempo[i] <= x <= tiempo[i+1]:
            t = (x - tiempo[i]) / (tiempo[i+1] - tiempo[i])
            y = (1 - t) * tasa_autos[i] + t * tasa_autos[i+1]
            return y

def calcular_integral(tiempo, tasa_autos, a, b):
    # Aproximación numérica de la integral utilizando el método del trapecio
    n = len(tiempo)
    h = (b - a) / (n - 1)
    integral = 0
    for i in range(1, n):
        xi = a + (i - 1) * h
        xi_1 = a + i * h
        integral += 0.5 * (interpolar(tiempo, tasa_autos, xi) + interpolar(tiempo, tasa_autos, xi_1)) * h
    return integral

def agregar_datos():
    x_value = float(simpledialog.askstring("Ingresar Datos", "Ingrese un valor para x:"))
    y_value = float(simpledialog.askstring("Ingresar Datos", "Ingrese un valor para y:"))
    tiempo_entries[-1].delete(0, tk.END)
    tiempo_entries[-1].insert(tk.END, x_value)
    tasa_autos_entries[-1].delete(0, tk.END)
    tasa_autos_entries[-1].insert(tk.END, y_value)

def calcular_autos():
    # Obtiene los datos ingresados en la interfaz
    tiempo = [float(tiempo_entry.get()) for tiempo_entry in tiempo_entries if tiempo_entry.get()]
    tasa_autos = [float(tasa_autos_entry.get()) for tasa_autos_entry in tasa_autos_entries if tasa_autos_entry.get()]
    a = float(a_entry.get())
    b = float(b_entry.get())

    # Calcula la integral utilizando el método del trapecio
    integral = calcular_integral(tiempo, tasa_autos, a, b)

    # Resultados
    autos_totales = integral
    tasa_por_minuto = integral / ((b - a) * 60)

    # Actualiza las etiquetas con los resultados
    autos_totales_label.config(text=f"Número total de autos: {autos_totales:.2f}")
    tasa_por_minuto_label.config(text=f"Tasa de autos por minuto: {tasa_por_minuto:.2f}")

    # Insertar fila en la tabla con los resultados
    tabla.insert("", "end", values=(interpolar(tiempo, tasa_autos, a), interpolar(tiempo, tasa_autos, (a+b)/2),
                                    interpolar(tiempo, tasa_autos, b), integral, "", ""))

    # Gráfico
    fig = plt.Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.plot(tiempo, tasa_autos, 'bo-')
    ax.set_xlabel('Tiempo')
    ax.set_ylabel('Tasa de autos')
    ax.set_title('Tasa de autos en función del tiempo')
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)

# Configuración de la interfaz gráfica
window = tk.Tk()
window.title("Cálculo de autos en una intersección")
window.geometry("500x600")

# Etiquetas y entradas para los datos de la tabla
tabla_label = tk.Label(window, text="Datos de la tabla:")
tabla_label.pack(pady=10)

tiempo_label = tk.Label(window, text="Tiempo:")
tiempo_label.pack()

tiempo_entries = []
for i in range(10):  # Puedes ajustar el rango según la cantidad máxima de tiempos que deseas permitir
    tiempo_entry = tk.Entry(window)
    tiempo_entry.pack()
    tiempo_entries.append(tiempo_entry)

tasa_autos_label = tk.Label(window, text="Tasa de autos:")
tasa_autos_label.pack()

tasa_autos_entries = []
for i in range(10):  # Puedes ajustar el rango según la cantidad máxima de tasas de autos que deseas permitir
    tasa_autos_entry = tk.Entry(window)
    tasa_autos_entry.pack()
    tasa_autos_entries.append(tasa_autos_entry)

# Botón para agregar datos
agregar_datos_button = tk.Button(window, text="Agregar Datos", command=agregar_datos)
agregar_datos_button.pack(pady=10)

# Etiquetas y entradas para el intervalo de integración
intervalo_label = tk.Label(window, text="Intervalo de integración:")
intervalo_label.pack(pady=10)

a_label = tk.Label(window, text="a:")
a_label.pack()

a_entry = tk.Entry(window)
a_entry.pack()

b_label = tk.Label(window, text="b:")
b_label.pack()

b_entry = tk.Entry(window)
b_entry.pack()

calcular_button = tk.Button(window, text="Calcular", command=calcular_autos)
calcular_button.pack(pady=10)

autos_totales_label = tk.Label(window, text="Número total de autos: ")
autos_totales_label.pack()

tasa_por_minuto_label = tk.Label(window, text="Tasa de autos por minuto: ")
tasa_por_minuto_label.pack()

# Tabla de resultados
from tkinter import ttk
tabla_columns = ("f(x0)", "f(x1)", "f(x2)", "I", "Etrunc", "Et")
tabla = ttk.Treeview(window, columns=tabla_columns, show="headings")
for column in tabla_columns:
    tabla.heading(column, text=column)
tabla.pack(pady=10)

# Configuración de la tabla scrollable
tabla_scrollbar = tk.Scrollbar(window, orient="vertical", command=tabla.yview)
tabla_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
tabla.configure(yscrollcommand=tabla_scrollbar.set)

window.mainloop()
