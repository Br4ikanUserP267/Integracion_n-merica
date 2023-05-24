import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class NumericalIntegrationApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Integración Numérica")
        self.geometry("800x600")

        self.x = []
        self.y = []
        self.rectangulo = 0
        self.trapecio = 0
        self.simpson = 0

        self.fig = plt.Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.ax.set_xlabel('Tiempo (h)')
        self.ax.set_ylabel('Tasa de autos (autos por 4 min)')
        self.ax.set_title('Tasa de autos en función del tiempo')

        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.add_button = tk.Button(self, text="Agregar Datos", command=self.agregar_datos)
        self.add_button.pack(side=tk.TOP)

        self.tabControl = ttk.Notebook(self)
        self.tabControl.pack(expand=1, fill="both")

        self.rectangulo_tab = ttk.Frame(self.tabControl)
        self.tabControl.add(self.rectangulo_tab, text="Regla del Rectángulo")

        self.trapecio_tab = ttk.Frame(self.tabControl)
        self.tabControl.add(self.trapecio_tab, text="Regla del Trapecio")

        self.simpson_tab = ttk.Frame(self.tabControl)
        self.tabControl.add(self.simpson_tab, text="Regla de Simpson 3/8")

        self.error_tab = ttk.Frame(self.tabControl)
        self.tabControl.add(self.error_tab, text="Comparativa de Errores")

        self.rectangulo_label = tk.Label(self.rectangulo_tab, text="Resultado de la Regla del Rectángulo: {:.2f}".format(self.rectangulo))
        self.rectangulo_label.pack(side=tk.BOTTOM)

        self.trapecio_label = tk.Label(self.trapecio_tab, text="Resultado de la Regla del Trapecio: {:.2f}".format(self.trapecio))
        self.trapecio_label.pack(side=tk.BOTTOM)

        self.simpson_label = tk.Label(self.simpson_tab, text="Resultado de la Regla de Simpson 3/8: {:.2f}".format(self.simpson))
        self.simpson_label.pack(side=tk.BOTTOM)

        self.error_text = tk.Text(self.error_tab, height=10)
        self.error_text.pack(side=tk.BOTTOM)

        self.tree = ttk.Treeview(self, columns=("x", "y"), show="headings")
        self.tree.heading("x", text="x")
        self.tree.heading("y", text="y")
        self.tree.pack(side=tk.BOTTOM)

    def agregar_datos(self):
        x_value = float(tk.simpledialog.askstring("Ingresar Datos", "Ingrese un valor para x:"))
        y_value = float(tk.simpledialog.askstring("Ingresar Datos", "Ingrese un valor para y:"))
        self.x.append(x_value)
        self.y.append(y_value)
        self.ax.plot(self.x, self.y, 'bo-')
        self.canvas.draw()
        self.actualizar_listado()

    def calcular_rectangulo(self):
        self.rectangulo = 0
        for i in range(1, len(self.x)):
            h = self.x[i] - self.x[i - 1]
            self.rectangulo += h * self.y[i - 1]

    def calcular_trapecio(self):
        self.trapecio = 0
        for i in range(1, len(self.x)):
            h = self.x[i] - self.x[i - 1]
            self.trapecio += 0.5 * h * (self.y[i] + self.y[i - 1])

    def calcular_simpson(self):
        self.simpson = 0
        for i in range(1, len(self.x) - 1, 2):
            h = self.x[i] - self.x[i - 1]
            self.simpson += (h / 3) * (self.y[i - 1] + 4 * self.y[i] + self.y[i + 1])

    def mostrar_resultados(self):
        self.calcular_rectangulo()
        self.calcular_trapecio()
        self.calcular_simpson()

        rectangulo_resultado = "Resultado de la Regla del Rectángulo: {:.2f}".format(self.rectangulo)
        self.rectangulo_label.configure(text=rectangulo_resultado)

        trapecio_resultado = "Resultado de la Regla del Trapecio: {:.2f}".format(self.trapecio)
        self.trapecio_label.configure(text=trapecio_resultado)

        simpson_resultado = "Resultado de la Regla de Simpson 3/8: {:.2f}".format(self.simpson)
        self.simpson_label.configure(text=simpson_resultado)

        self.actualizar_errores()

    def actualizar_errores(self):
        self.error_text.delete("1.0", tk.END)
        error_rectangulo = abs(self.rectangulo - (self.y[-1] - self.y[0]))
        error_trapecio = abs(self.trapecio - (self.y[-1] - self.y[0]))
        error_simpson = abs(self.simpson - (self.y[-1] - self.y[0]))
        self.error_text.insert(tk.END, "Comparativa de Errores:\n\n")
        self.error_text.insert(tk.END, "Regla del Rectángulo: {:.2f}\n".format(error_rectangulo))
        self.error_text.insert(tk.END, "Regla del Trapecio: {:.2f}\n".format(error_trapecio))
        self.error_text.insert(tk.END, "Regla de Simpson 3/8: {:.2f}\n".format(error_simpson))

    def actualizar_listado(self):
        self.tree.delete(*self.tree.get_children())
        for i in range(len(self.x)):
            self.tree.insert("", "end", values=(self.x[i], self.y[i]))


if __name__ == "__main__":
    app = NumericalIntegrationApp()
    app.mainloop()
