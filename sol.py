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
        self.table_trapezoidal.pack(side=tk.LEFT)

        self.scrollbar_table_trapezoidal = ttk.Scrollbar(self.table_frame_trapezoidal, orient="vertical", command=self.table_trapezoidal.yview)
        self.scrollbar_table_trapezoidal.pack(side=tk.RIGHT, fill=tk.Y)
        self.table_trapezoidal.configure(yscrollcommand=self.scrollbar_table_trapezoidal.set)

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
        self.table_simpson13 = ttk.Treeview(self.table_frame_simpson13, columns=("fa", "fc", "fb", "I", "Etrunc"), show="headings")
        self.table_simpson13.heading("fa", text="f(a)")
        self.table_simpson13.heading("fc", text="f(c)")
        self.table_simpson13.heading("fb", text="f(b)")
        self.table_simpson13.heading("I", text="I")
        self.table_simpson13.heading("Etrunc", text="Etrunc")
        self.table_simpson13.pack(side=tk.LEFT)

        self.scrollbar_table_simpson13 = ttk.Scrollbar(self.table_frame_simpson13, orient="vertical", command=self.table_simpson13.yview)
        self.scrollbar_table_simpson13.pack(side=tk.RIGHT, fill=tk.Y)
        self.table_simpson13.configure(yscrollcommand=self.scrollbar_table_simpson13.set)

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
        self.table_simpson38 = ttk.Treeview(self.table_frame_simpson38, columns=("fa", "fb", "fc", "fd", "I", "Etrunc"), show="headings")
        self.table_simpson38.heading("fa", text="f(a)")
        self.table_simpson38.heading("fb", text="f(b)")
        self.table_simpson38.heading("fc", text="f(c)")
        self.table_simpson38.heading("fd", text="f(d)")
        self.table_simpson38.heading("I", text="I")
        self.table_simpson38.heading("Etrunc", text="Etrunc")
        self.table_simpson38.pack(side=tk.LEFT)

        self.scrollbar_table_simpson38 = ttk.Scrollbar(self.table_frame_simpson38, orient="vertical", command=self.table_simpson38.yview)
        self.scrollbar_table_simpson38.pack(side=tk.RIGHT, fill=tk.Y)
        self.table_simpson38.configure(yscrollcommand=self.scrollbar_table_simpson38.set)
        self.button_grafico_trapezoidal = tk.Button(self.table_frame_trapezoidal, text="Mostrar Gráfico", command=self.mostrar_grafico_trapezoidal)
        self.button_grafico_trapezoidal.pack(side=tk.BOTTOM)
    def agregar_datos_trapezoidal(self):
        x = simpledialog.askfloat("Datos", "Ingrese el valor de x:")
        y = simpledialog.askfloat("Datos", "Ingrese el valor de y:")
        if x is not None and y is not None:
            self.x_trapezoidal.append(x)
            self.y_trapezoidal.append(y)
            self.tree_trapezoidal.insert("", tk.END, values=(x, y))
        
    def mostrar_resultados_trapezoidal(self):
        if len(self.x_trapezoidal) > 1 and len(self.y_trapezoidal) > 1:
            self.trapezoidal = self.calcular_trapezoidal()
            self.I_trapezoidal, self.Etrunc_trapezoidal = self.calcular_area_error_trapezoidal()
            self.label_trapezoidal.configure(text="Resultado del método del Trapecio: {:.2f}".format(self.trapezoidal))
            self.mostrar_tabla_trapezoidal()
            self.mostrar_grafico_trapezoidal()
        else:
            messagebox.showwarning("Error", "Debe ingresar al menos 2 puntos para calcular el área.")
        
    def calcular_trapezoidal(self):
        n = len(self.x_trapezoidal)
        h = self.x_trapezoidal[1] - self.x_trapezoidal[0]
        suma = self.y_trapezoidal[0] + self.y_trapezoidal[-1]
        for i in range(1, n-1):
            suma += 2 * self.y_trapezoidal[i]
        return (h / 2) * suma
    
    def calcular_area_error_trapezoidal(self):
        n = len(self.x_trapezoidal)
        h = self.x_trapezoidal[1] - self.x_trapezoidal[0]
        suma = 0
        for i in range(1, n-1):
            suma += abs(self.y_trapezoidal[i])
        Etrunc = (h**2 / 12) * suma
        I = self.trapezoidal + Etrunc
        return I, Etrunc

    def mostrar_tabla_trapezoidal(self):
        self.table_trapezoidal.delete(*self.table_trapezoidal.get_children())
        n = len(self.x_trapezoidal)
        for i in range(n-1):
            fa = self.y_trapezoidal[i]
            fb = self.y_trapezoidal[i+1]
            I = (self.x_trapezoidal[i+1] - self.x_trapezoidal[i]) * (fa + fb) / 2
            Etrunc = (self.x_trapezoidal[i+1] - self.x_trapezoidal[i]) ** 3 * (fb - fa) ** 2 / 12
            self.table_trapezoidal.insert("", tk.END, values=(fa, fb, I, Etrunc))
        
    def mostrar_grafico_trapezoidal(self):
        self.ax.clear()
        self.ax.plot(self.x_trapezoidal, self.y_trapezoidal, "ro-")
        self.ax.fill_between(self.x_trapezoidal, self.y_trapezoidal, 0, alpha=0.2)
        self.canvas.draw()

    def agregar_datos_simpson13(self):
        x = simpledialog.askfloat("Datos", "Ingrese el valor de x:")
        y = simpledialog.askfloat("Datos", "Ingrese el valor de y:")
        if x is not None and y is not None:
            self.x_simpson13.append(x)
            self.y_simpson13.append(y)
            self.tree_simpson13.insert("", tk.END, values=(x, y))
        
    def mostrar_resultados_simpson13(self):
        if len(self.x_simpson13) > 2 and len(self.y_simpson13) > 2:
            self.simpson13 = self.calcular_simpson13()
            self.I_simpson13, self.Etrunc_simpson13 = self.calcular_area_error_simpson13()
            self.label_simpson13.configure(text="Resultado del método de Simpson 1/3: {:.2f}".format(self.simpson13))
            self.mostrar_tabla_simpson13()
            self.mostrar_grafico_simpson13()
        else:
            messagebox.showwarning("Error", "Debe ingresar al menos 3 puntos para calcular el área.")
        
    def calcular_simpson13(self):
        n = len(self.x_simpson13)
        h = self.x_simpson13[1] - self.x_simpson13[0]
        suma = self.y_simpson13[0] + self.y_simpson13[-1]
        for i in range(1, n-1):
            if i % 2 == 0:
                suma += 2 * self.y_simpson13[i]
            else:
                suma += 4 * self.y_simpson13[i]
        return (h / 3) * suma
    
    def calcular_area_error_simpson13(self):
        n = len(self.x_simpson13)
        h = self.x_simpson13[1] - self.x_simpson13[0]
        suma = 0
        for i in range(1, n-1):
            if i % 2 == 0:
                suma += 2 * abs(self.y_simpson13[i])
            else:
                suma += 4 * abs(self.y_simpson13[i])
        Etrunc = (h**4 / 180) * suma
        I = self.simpson13 + Etrunc
        return I, Etrunc

    def mostrar_tabla_simpson13(self):
        self.table_simpson13.delete(*self.table_simpson13.get_children())
        n = len(self.x_simpson13)
        for i in range(n-2):
            fa = self.y_simpson13[i]
            fb = self.y_simpson13[i+1]
            fc = self.y_simpson13[i+2]
            I = (self.x_simpson13[i+2] - self.x_simpson13[i]) * (fa + 4*fc + fb) / 6
            Etrunc = (self.x_simpson13[i+2] - self.x_simpson13[i]) ** 5 * (fb - 2*fc + fa) ** 4 / 2880
            self.table_simpson13.insert("", tk.END, values=(fa, fc, fb, I, Etrunc))
        
    def mostrar_grafico_simpson13(self):
        self.ax.clear()
        self.ax.plot(self.x_simpson13, self.y_simpson13, "ro-")
        x = np.linspace(self.x_simpson13[0], self.x_simpson13[-1], 100)
        y = np.interp(x, self.x_simpson13, self.y_simpson13)
        self.ax.fill_between(x, y, 0, alpha=0.2)
        self.canvas.draw()

    def agregar_datos_simpson38(self):
        x = simpledialog.askfloat("Datos", "Ingrese el valor de x:")
        y = simpledialog.askfloat("Datos", "Ingrese el valor de y:")
        if x is not None and y is not None:
            self.x_simpson38.append(x)
            self.y_simpson38.append(y)
            self.tree_simpson38.insert("", tk.END, values=(x, y))
        
    def mostrar_resultados_simpson38(self):
        if len(self.x_simpson38) > 3 and len(self.y_simpson38) > 3:
            self.simpson38 = self.calcular_simpson38()
            self.I_simpson38, self.Etrunc_simpson38 = self.calcular_area_error_simpson38()
            self.label_simpson38.configure(text="Resultado del método de Simpson 3/8: {:.2f}".format(self.simpson38))
            self.mostrar_tabla_simpson38()
            self.mostrar_grafico_simpson38()
        else:
            messagebox.showwarning("Error", "Debe ingresar al menos 4 puntos para calcular el área.")
        
    def calcular_simpson38(self):
        n = len(self.x_simpson38)
        h = self.x_simpson38[1] - self.x_simpson38[0]
        suma = self.y_simpson38[0] + self.y_simpson38[-1]
        for i in range(1, n-1):
            if i % 3 == 0:
                suma += 2 * self.y_simpson38[i]
            else:
                suma += 3 * self.y_simpson38[i]
        return (3 * h / 8) * suma
    
    def calcular_area_error_simpson38(self):
        n = len(self.x_simpson38)
        h = self.x_simpson38[1] - self.x_simpson38[0]
        suma = 0
        for i in range(1, n-1):
            if i % 3 == 0:
                suma += 2 * abs(self.y_simpson38[i])
            else:
                suma += 3 * abs(self.y_simpson38[i])
        Etrunc = (3 * h**5 / 80) * suma
        I = self.simpson38 + Etrunc
        return I, Etrunc

    def mostrar_tabla_simpson38(self):
        self.table_simpson38.delete(*self.table_simpson38.get_children())
        n = len(self.x_simpson38)
        for i in range(n-3):
            fa = self.y_simpson38[i]
            fb = self.y_simpson38[i+1]
            fc = self.y_simpson38[i+2]
            fd = self.y_simpson38[i+3]
            I = (self.x_simpson38[i+3] - self.x_simpson38[i]) * (fa + 3*fb + 3*fc + fd) / 8
            Etrunc = (self.x_simpson38[i+3] - self.x_simpson38[i]) ** 5 * (fd - 3*fc + 3*fb - fa) ** 4 / 6480
            self.table_simpson38.insert("", tk.END, values=(fa, fb, fc, fd, I, Etrunc))
        
    def mostrar_grafico_simpson38(self):
        self.ax.clear()
        self.ax.plot(self.x_simpson38, self.y_simpson38, "ro-")
        x = np.linspace(self.x_simpson38[0], self.x_simpson38[-1], 100)
        y = np.interp(x, self.x_simpson38, self.y_simpson38)
        self.ax.fill_between(x, y, 0, alpha=0.2)
        self.canvas.draw()
    
    
    def mostrar_grafico_errores(self):
        x = ['Trapecio', 'Simpson 1/3', 'Simpson 3/8']
        y = [self.Etrunc_trapezoidal, self.Etrunc_simpson13, self.Etrunc_simpson38]
        
        fig, ax = plt.subplots()
        ax.plot(x, y, marker='o', linestyle='-', color='blue')
        ax.set_xlabel('Método')
        ax.set_ylabel('Error de Truncamiento')
        ax.set_title('Errores de Truncamiento')
        
        self.ax.clear()
        self.canvas.get_tk_widget().pack_forget()
        self.canvas = FigureCanvasTkAgg(fig, master=self)
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        self.ax = ax
        self.ax.grid()
        self.canvas.draw()

        self.canvas.get_tk_widget().lift() 
if __name__ == "__main__":
    app = SimpsonApp()
    app.mainloop()


