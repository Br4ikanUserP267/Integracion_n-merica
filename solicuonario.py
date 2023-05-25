import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class SimpsonApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Métodos de Integración")
        self.geometry("800x600")
        
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        self.trapezoidal_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.trapezoidal_frame, text="Trapecio")

        self.simpson13_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.simpson13_frame, text="Simpson 1/3")

        self.simpson38_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.simpson38_frame, text="Simpson 3/8")

        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        self.ax.grid()

        self.x_trapezoidal = []
        self.y_trapezoidal = []
        self.trapezoidal = 0
        self.I_trapezoidal = 0
        self.Etrunc_trapezoidal = 0

        self.x_simpson13 = []
        self.y_simpson13 = []
        self.simpson13 = 0
        self.I_simpson13 = 0
        self.Etrunc_simpson13 = 0

        self.x_simpson38 = []
        self.y_simpson38 = []
        self.simpson38 = 0
        self.I_simpson38 = 0
        self.Etrunc_simpson38 = 0

        self.label_trapezoidal = tk.Label(self.trapezoidal_frame, text="Resultado del método del Trapecio: {:.2f}".format(self.trapezoidal))
        self.label_trapezoidal.pack(side=tk.TOP)

        self.add_button_trapezoidal = tk.Button(self.trapezoidal_frame, text="Agregar Datos", command=self.agregar_datos_trapezoidal)
        self.add_button_trapezoidal.pack(side=tk.BOTTOM)

        self.show_button_trapezoidal = tk.Button(self.trapezoidal_frame, text="Mostrar Resultados", command=self.mostrar_resultados_trapezoidal)
        self.show_button_trapezoidal.pack(side=tk.BOTTOM)

        self.tree_trapezoidal = ttk.Treeview(self.trapezoidal_frame, columns=("x", "y"), show="headings")
        self.tree_trapezoidal.heading("x", text="x")
        self.tree_trapezoidal.heading("y", text="y")
        self.tree_trapezoidal.pack(side=tk.BOTTOM)

        self.table_frame_trapezoidal = ttk.Frame(self.trapezoidal_frame)
        self.table_frame_trapezoidal.pack(side=tk.BOTTOM)
        self.table_trapezoidal = ttk.Treeview(self.table_frame_trapezoidal, columns=("fa", "fb", "I", "Etrunc"), show="headings")
        self.table_trapezoidal.heading("fa", text="f(a)")
        self.table_trapezoidal.heading("fb", text="f(b)")
        self.table_trapezoidal.heading("I", text="I")
        self.table_trapezoidal.heading("Etrunc", text="Etrunc")
        self.table_trapezoidal.pack()

        self.label_simpson13 = tk.Label(self.simpson13_frame, text="Resultado del método de Simpson 1/3: {:.2f}".format(self.simpson13))
        self.label_simpson13.pack(side=tk.TOP)

        self.add_button_simpson13 = tk.Button(self.simpson13_frame, text="Agregar Datos", command=self.agregar_datos_simpson13)
        self.add_button_simpson13.pack(side=tk.BOTTOM)

        self.show_button_simpson13 = tk.Button(self.simpson13_frame, text="Mostrar Resultados", command=self.mostrar_resultados_simpson13)
        self.show_button_simpson13.pack(side=tk.BOTTOM)

        self.tree_simpson13 = ttk.Treeview(self.simpson13_frame, columns=("x", "y"), show="headings")
        self.tree_simpson13.heading("x", text="x")
        self.tree_simpson13.heading("y", text="y")
        self.tree_simpson13.pack(side=tk.BOTTOM)

        self.table_frame_simpson13 = ttk.Frame(self.simpson13_frame)
        self.table_frame_simpson13.pack(side=tk.BOTTOM)
        self.table_simpson13 = ttk.Treeview(self.table_frame_simpson13, columns=("fa", "fb", "I", "Etrunc"), show="headings")
        self.table_simpson13.heading("fa", text="f(a)")
        self.table_simpson13.heading("fb", text="f(b)")
        self.table_simpson13.heading("I", text="I")
        self.table_simpson13.heading("Etrunc", text="Etrunc")
        self.table_simpson13.pack()

        self.label_simpson38 = tk.Label(self.simpson38_frame, text="Resultado del método de Simpson 3/8: {:.2f}".format(self.simpson38))
        self.label_simpson38.pack(side=tk.TOP)

        self.add_button_simpson38 = tk.Button(self.simpson38_frame, text="Agregar Datos", command=self.agregar_datos_simpson38)
        self.add_button_simpson38.pack(side=tk.BOTTOM)

        self.show_button_simpson38 = tk.Button(self.simpson38_frame, text="Mostrar Resultados", command=self.mostrar_resultados_simpson38)
        self.show_button_simpson38.pack(side=tk.BOTTOM)

        self.tree_simpson38 = ttk.Treeview(self.simpson38_frame, columns=("x", "y"), show="headings")
        self.tree_simpson38.heading("x", text="x")
        self.tree_simpson38.heading("y", text="y")
        self.tree_simpson38.pack(side=tk.BOTTOM)

        self.table_frame_simpson38 = ttk.Frame(self.simpson38_frame)
        self.table_frame_simpson38.pack(side=tk.BOTTOM)
        self.table_simpson38 = ttk.Treeview(self.table_frame_simpson38, columns=("fa", "fb", "I", "Etrunc"), show="headings")
        self.table_simpson38.heading("fa", text="f(a)")
        self.table_simpson38.heading("fb", text="f(b)")
        self.table_simpson38.heading("I", text="I")
        self.table_simpson38.heading("Etrunc", text="Etrunc")
        self.table_simpson38.pack()

        #hacer error 
        self.error_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.error_frame, text="Errores")

        self.error_button = tk.Button(self.error_frame, text="Mostrar Errores", command=self.plot_errors)
        self.error_button.pack()

        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.error_frame)
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        self.ax.grid()

    def agregar_datos_trapezoidal(self):
        x = simpledialog.askfloat("Agregar Datos", "Ingrese el valor de x:")
        if x is not None:
            y = simpledialog.askfloat("Agregar Datos", "Ingrese el valor de y:")
            if y is not None:
                self.x_trapezoidal.append(x)
                self.y_trapezoidal.append(y)
                self.tree_trapezoidal.insert("", tk.END, values=(x, y))

    def mostrar_resultados_trapezoidal(self):
        self.ax.clear()
        self.ax.plot(self.x_trapezoidal, self.y_trapezoidal, marker="o", linestyle="-", label="Datos")
        self.ax.set_xlabel("x")
        self.ax.set_ylabel("y")
        self.ax.grid()

        self.trapezoidal = self.calcular_trapezoidal()
        self.label_trapezoidal.config(text="Resultado del método del Trapecio: {:.2f}".format(self.trapezoidal))

        self.I_trapezoidal = self.calcular_I_trapezoidal()
        self.Etrunc_trapezoidal = self.calcular_Etrunc_trapezoidal()

        self.table_trapezoidal.delete(*self.table_trapezoidal.get_children())
        self.table_trapezoidal.insert("", tk.END, values=("---", "---", self.I_trapezoidal, self.Etrunc_trapezoidal))

        self.canvas.draw()

    def calcular_trapezoidal(self):
        n = len(self.x_trapezoidal)
        h = self.x_trapezoidal[1] - self.x_trapezoidal[0]
        s = self.y_trapezoidal[0] + self.y_trapezoidal[n-1]
        for i in range(1, n-1):
            s += 2 * self.y_trapezoidal[i]
        return (h / 2) * s

    def calcular_I_trapezoidal(self):
        n = len(self.x_trapezoidal)
        h = self.x_trapezoidal[1] - self.x_trapezoidal[0]
        return (h / 2) * (self.y_trapezoidal[0] + self.y_trapezoidal[n-1])

    def calcular_Etrunc_trapezoidal(self):
        n = len(self.x_trapezoidal)
        h = self.x_trapezoidal[1] - self.x_trapezoidal[0]
        return -(h**2) / 12 * (self.x_trapezoidal[n-1] - self.x_trapezoidal[0]) * max(self.y_trapezoidal)

    def agregar_datos_simpson13(self):
        x = simpledialog.askfloat("Agregar Datos", "Ingrese el valor de x:")
        if x is not None:
            y = simpledialog.askfloat("Agregar Datos", "Ingrese el valor de y:")
            if y is not None:
                self.x_simpson13.append(x)
                self.y_simpson13.append(y)
                self.tree_simpson13.insert("", tk.END, values=(x, y))

    def mostrar_resultados_simpson13(self):
        self.ax.clear()
        self.ax.plot(self.x_simpson13, self.y_simpson13, marker="o", linestyle="-", label="Datos")
        self.ax.set_xlabel("x")
        self.ax.set_ylabel("y")
        self.ax.grid()

        self.simpson13 = self.calcular_simpson13()
        self.label_simpson13.config(text="Resultado del método de Simpson 1/3: {:.2f}".format(self.simpson13))

        self.I_simpson13 = self.calcular_I_simpson13()
        self.Etrunc_simpson13 = self.calcular_Etrunc_simpson13()

        self.table_simpson13.delete(*self.table_simpson13.get_children())
        self.table_simpson13.insert("", tk.END, values=("---", "---", self.I_simpson13, self.Etrunc_simpson13))

        self.canvas.draw()

    def calcular_simpson13(self):
        n = len(self.x_simpson13)
        h = self.x_simpson13[1] - self.x_simpson13[0]
        s = self.y_simpson13[0] + self.y_simpson13[n-1]
        for i in range(1, n-1):
            if i % 2 == 0:
                s += 2 * self.y_simpson13[i]
            else:
                s += 4 * self.y_simpson13[i]
        return (h / 3) * s

    def calcular_I_simpson13(self):
        n = len(self.x_simpson13)
        h = self.x_simpson13[1] - self.x_simpson13[0]
        return (h / 3) * (self.y_simpson13[0] + self.y_simpson13[n-1])

    def calcular_Etrunc_simpson13(self):
        n = len(self.x_simpson13)
        h = self.x_simpson13[1] - self.x_simpson13[0]
        return -(h**4) / 180 * (self.x_simpson13[n-1] - self.x_simpson13[0]) * max(self.y_simpson13)

    def agregar_datos_simpson38(self):
        x = simpledialog.askfloat("Agregar Datos", "Ingrese el valor de x:")
        if x is not None:
            y = simpledialog.askfloat("Agregar Datos", "Ingrese el valor de y:")
            if y is not None:
                self.x_simpson38.append(x)
                self.y_simpson38.append(y)
                self.tree_simpson38.insert("", tk.END, values=(x, y))

    def mostrar_resultados_simpson38(self):
        self.ax.clear()
        self.ax.plot(self.x_simpson38, self.y_simpson38, marker="o", linestyle="-", label="Datos")
        self.ax.set_xlabel("x")
        self.ax.set_ylabel("y")
        self.ax.grid()

        self.simpson38 = self.calcular_simpson38()
        self.label_simpson38.config(text="Resultado del método de Simpson 3/8: {:.2f}".format(self.simpson38))

        self.I_simpson38 = self.calcular_I_simpson38()
        self.Etrunc_simpson38 = self.calcular_Etrunc_simpson38()

        self.table_simpson38.delete(*self.table_simpson38.get_children())
        self.table_simpson38.insert("", tk.END, values=("---", "---", self.I_simpson38, self.Etrunc_simpson38))

        self.canvas.draw()

    def calcular_simpson38(self):
        n = len(self.x_simpson38)
        h = self.x_simpson38[1] - self.x_simpson38[0]
        s = self.y_simpson38[0] + self.y_simpson38[n-1]
        for i in range(1, n-1):
            if i % 3 == 0:
                s += 2 * self.y_simpson38[i]
            else:
                s += 3 * self.y_simpson38[i]
        return (3 * h / 8) * s

    def calcular_I_simpson38(self):
        n = len(self.x_simpson38)
        h = self.x_simpson38[1] - self.x_simpson38[0]
        return (3 * h / 8) * (self.y_simpson38[0] + self.y_simpson38[n-1])

    def calcular_Etrunc_simpson38(self):
        n = len(self.x_simpson38)
        h = self.x_simpson38[1] - self.x_simpson38[0]
        return -(3 * h**5) / 80 * (self.x_simpson38[n-1] - self.x_simpson38[0]) * max(self.y_simpson38)
    
    
    def get_error_values(self):
        trapezoidal_error = self.calcular_Etrunc_trapezoidal()
        simpson13_error = self.calcular_Etrunc_simpson13()
        simpson38_error = self.calcular_Etrunc_simpson38()
        return trapezoidal_error, simpson13_error, simpson38_error

    def plot_errors(self):
        trapezoidal_error, simpson13_error, simpson38_error = self.get_error_values()

        methods = ["Trapezoidal", "Simpson 1/3", "Simpson 3/8"]
        errors = [trapezoidal_error, simpson13_error, simpson38_error]

        # Colores para las líneas
        colors = ['red', 'green', 'blue']

        # Generar la gráfica de líneas
        plt.plot(methods, errors, marker='o', linestyle='-', color=colors)

        # Configurar etiquetas y título
        plt.ylabel('Error de truncamiento')
        plt.title('Comparación de errores de truncamiento')

        # Mostrar la gráfica
        plt.show()

if __name__ == "__main__":
    app = SimpsonApp()
    app.mainloop()
