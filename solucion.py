import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

class IntegrationApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Métodos de Integración Numérica")
        self.geometry("800x600")

        self.tab_control = ttk.Notebook(self)
        self.tab_control.pack(fill=tk.BOTH, expand=True)

        self.data_tab = ttk.Frame(self.tab_control)
        self.trapezoidal_tab = ttk.Frame(self.tab_control)
        self.simpson13_tab = ttk.Frame(self.tab_control)
        self.simpson38_tab = ttk.Frame(self.tab_control)
        self.error_tab = ttk.Frame(self.tab_control)

        self.tab_control.add(self.data_tab, text="Datos")
        self.tab_control.add(self.trapezoidal_tab, text="Método del Trapecio")
        self.tab_control.add(self.simpson13_tab, text="Método de Simpson 1/3")
        self.tab_control.add(self.simpson38_tab, text="Método de Simpson 3/8")
        self.tab_control.add(self.error_tab, text="Comparación de Errores")

        self.x = []
        self.y = []

        # Datos ingresados
        self.data_label = tk.Label(self.data_tab, text="Ingrese los datos:")
        self.data_label.pack()

        self.x_label = tk.Label(self.data_tab, text="x:")
        self.x_label.pack()
        self.x_entry = tk.Entry(self.data_tab)
        self.x_entry.pack()

        self.y_label = tk.Label(self.data_tab, text="y:")
        self.y_label.pack()
        self.y_entry = tk.Entry(self.data_tab)
        self.y_entry.pack()

        self.add_button = tk.Button(self.data_tab, text="Agregar", command=self.agregar_dato)
        self.add_button.pack()

        self.data_tree = ttk.Treeview(self.data_tab, columns=("x", "y"), show="headings")
        self.data_tree.heading("x", text="x")
        self.data_tree.heading("y", text="y")
        self.data_tree.pack()

        # Método del Trapecio
        self.trapezoidal_result = 0.0
        self.trapezoidal_label = tk.Label(self.trapezoidal_tab, text="Resultado del Método del Trapecio: {:.2f}".format(self.trapezoidal_result))
        self.trapezoidal_label.pack()

        self.calculate_trapezoidal_button = tk.Button(self.trapezoidal_tab, text="Calcular", command=self.calcular_trapezoidal)
        self.calculate_trapezoidal_button.pack()

        self.trapezoidal_table_frame = ttk.Frame(self.trapezoidal_tab)
        self.trapezoidal_table_frame.pack()
        self.trapezoidal_table = ttk.Treeview(self.trapezoidal_table_frame, columns=("n", "h", "f(a)", "f(b)", "I", "Et"), show="headings")
        self.trapezoidal_table.heading("n", text="n")
        self.trapezoidal_table.heading("h", text="h")
        self.trapezoidal_table.heading("f(a)", text="f(a)")
        self.trapezoidal_table.heading("f(b)", text="f(b)")
        self.trapezoidal_table.heading("I", text="I")
        self.trapezoidal_table.heading("Et", text="Et")
        self.trapezoidal_table.pack()

        # Método de Simpson 1/3
        self.simpson13_result = 0.0
        self.simpson13_label = tk.Label(self.simpson13_tab, text="Resultado del Método de Simpson 1/3: {:.2f}".format(self.simpson13_result))
        self.simpson13_label.pack()

        self.calculate_simpson13_button = tk.Button(self.simpson13_tab, text="Calcular", command=self.calcular_simpson13)
        self.calculate_simpson13_button.pack()

        self.simpson13_table_frame = ttk.Frame(self.simpson13_tab)
        self.simpson13_table_frame.pack()
        self.simpson13_table = ttk.Treeview(self.simpson13_table_frame, columns=("n", "h", "f(a)", "f(b)", "I", "Et"), show="headings")
        self.simpson13_table.heading("n", text="n")
        self.simpson13_table.heading("h", text="h")
        self.simpson13_table.heading("f(a)", text="f(a)")
        self.simpson13_table.heading("f(b)", text="f(b)")
        self.simpson13_table.heading("I", text="I")
        self.simpson13_table.heading("Et", text="Et")
        self.simpson13_table.pack()

        # Método de Simpson 3/8
        self.simpson38_result = 0.0
        self.simpson38_label = tk.Label(self.simpson38_tab, text="Resultado del Método de Simpson 3/8: {:.2f}".format(self.simpson38_result))
        self.simpson38_label.pack()

        self.calculate_simpson38_button = tk.Button(self.simpson38_tab, text="Calcular", command=self.calcular_simpson38)
        self.calculate_simpson38_button.pack()

        self.simpson38_table_frame = ttk.Frame(self.simpson38_tab)
        self.simpson38_table_frame.pack()
        self.simpson38_table = ttk.Treeview(self.simpson38_table_frame, columns=("n", "h", "f(a)", "f(b)", "I", "Et"), show="headings")
        self.simpson38_table.heading("n", text="n")
        self.simpson38_table.heading("h", text="h")
        self.simpson38_table.heading("f(a)", text="f(a)")
        self.simpson38_table.heading("f(b)", text="f(b)")
        self.simpson38_table.heading("I", text="I")
        self.simpson38_table.heading("Et", text="Et")
        self.simpson38_table.pack()

        # Comparación de Errores
        self.error_fig = plt.Figure(figsize=(5, 4), dpi=100)
        self.error_ax = self.error_fig.add_subplot(111)
        self.error_ax.set_xlabel('Número de intervalos (n)')
        self.error_ax.set_ylabel('Error relativo (%)')
        self.error_ax.set_title('Comparación de Errores')
        self.error_canvas = FigureCanvasTkAgg(self.error_fig, master=self.error_tab)
        self.error_canvas.draw()
        self.error_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def agregar_dato(self):
        x_value = float(self.x_entry.get())
        y_value = float(self.y_entry.get())
        self.x.append(x_value)
        self.y.append(y_value)
        self.data_tree.insert("", "end", values=(x_value, y_value))
        self.x_entry.delete(0, tk.END)
        self.y_entry.delete(0, tk.END)

    def calcular_trapezoidal(self):
        if len(self.x) < 2:
            messagebox.showerror("Error", "Se necesitan al menos 2 puntos para aplicar el Método del Trapecio.")
            return

        self.trapezoidal_result = 0.0
        self.trapezoidal_table.delete(*self.trapezoidal_table.get_children())

        for i in range(1, len(self.x)):
            h = self.x[i] - self.x[i - 1]
            result = (h / 2) * (self.y[i - 1] + self.y[i])
            self.trapezoidal_result += result
            self.trapezoidal_table.insert("", "end", values=(i, h, self.y[i - 1], self.y[i], result, None))

        self.trapezoidal_label.configure(text="Resultado del Método del Trapecio: {:.2f}".format(self.trapezoidal_result))

    def calcular_simpson13(self):
        if len(self.x) < 3:
            messagebox.showerror("Error", "Se necesitan al menos 3 puntos para aplicar el Método de Simpson 1/3.")
            return

        if len(self.x) % 2 == 0:
            messagebox.showwarning("Advertencia", "La cantidad de puntos ingresados es par. Se omitirá el último punto.")
            self.x = self.x[:-1]
            self.y = self.y[:-1]
            self.data_tree.delete(*self.data_tree.get_children())
            for i in range(len(self.x)):
                self.data_tree.insert("", "end", values=(self.x[i], self.y[i]))

        self.simpson13_result = 0.0
        self.simpson13_table.delete(*self.simpson13_table.get_children())

        for i in range(1, len(self.x) - 1, 2):
            h = self.x[i] - self.x[i - 1]
            result = (h / 3) * (self.y[i - 1] + 4 * self.y[i] + self.y[i + 1])
            self.simpson13_result += result
            self.simpson13_table.insert("", "end", values=(i, h, self.y[i - 1], self.y[i + 1], result, None))

        self.simpson13_label.configure(text="Resultado del Método de Simpson 1/3: {:.2f}".format(self.simpson13_result))

    def calcular_simpson38(self):
        if len(self.x) < 4:
            messagebox.showerror("Error", "Se necesitan al menos 4 puntos para aplicar el Método de Simpson 3/8.")
            return

        if (len(self.x) - 1) % 3 != 0:
            messagebox.showwarning("Advertencia", "La cantidad de puntos ingresados no cumple con los requisitos para aplicar el Método de Simpson 3/8. Se omitirán los últimos puntos necesarios.")
            num_points = 3 * (len(self.x) // 3)
            self.x = self.x[:num_points + 1]
            self.y = self.y[:num_points + 1]
            self.data_tree.delete(*self.data_tree.get_children())
            for i in range(len(self.x)):
                self.data_tree.insert("", "end", values=(self.x[i], self.y[i]))

        self.simpson38_result = 0.0
        self.simpson38_table.delete(*self.simpson38_table.get_children())

        for i in range(1, len(self.x) - 2, 3):
            h = self.x[i] - self.x[i - 1]
            result = (3 * h / 8) * (self.y[i - 1] + 3 * self.y[i] + 3 * self.y[i + 1] + self.y[i + 2])
            self.simpson38_result += result
            self.simpson38_table.insert("", "end", values=(i, h, self.y[i - 1], self.y[i + 2], result, None))

        self.simpson38_label.configure(text="Resultado del Método de Simpson 3/8: {:.2f}".format(self.simpson38_result))

    def plot_error(self):
        n_values = []
        trapezoidal_errors = []
        simpson13_errors = []
        simpson38_errors = []

        for n in range(2, len(self.x)):
            n_values.append(n)

            # Cálculo del error del Método del Trapecio
            self.calcular_trapezoidal()
            trapezoidal_error = abs(self.trapezoidal_result - true_value) / true_value * 100
            trapezoidal_errors.append(trapezoidal_error)

            # Cálculo del error del Método de Simpson 1/3
            self.calcular_simpson13()
            simpson13_error = abs(self.simpson13_result - true_value) / true_value * 100
            simpson13_errors.append(simpson13_error)

            # Cálculo del error del Método de Simpson 3/8
            self.calcular_simpson38()
            simpson38_error = abs(self.simpson38_result - true_value) / true_value * 100
            simpson38_errors.append(simpson38_error)

        self.error_ax.clear()
        self.error_ax.plot(n_values, trapezoidal_errors, label="Método del Trapecio")
        self.error_ax.plot(n_values, simpson13_errors, label="Método de Simpson 1/3")
        self.error_ax.plot(n_values, simpson38_errors, label="Método de Simpson 3/8")
        self.error_ax.legend()
        self.error_canvas.draw()

if __name__ == "__main__":
    app = IntegrationApp()
    app.mainloop()
