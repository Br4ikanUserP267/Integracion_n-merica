import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class TrapecioApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Método del Trapecio")
        self.geometry("400x400")

        self.x = []
        self.y = []
        self.trapecio = 0
        self.fa = 0
        self.fb = 0
        self.I = 0
        self.Etrunc = 0
        self.Et = 0

        self.fig = plt.Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.ax.set_xlabel('Tiempo (h)')
        self.ax.set_ylabel('Tasa de autos (autos por 4 min)')
        self.ax.set_title('Tasa de autos en función del tiempo')

        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.label = tk.Label(self, text="Resultado del método del trapecio: {:.2f}".format(self.trapecio))
        self.label.pack(side=tk.BOTTOM)

        self.add_button = tk.Button(self, text="Agregar Datos", command=self.agregar_datos)
        self.add_button.pack(side=tk.BOTTOM)

        self.show_button = tk.Button(self, text="Mostrar Resultados", command=self.mostrar_resultados)
        self.show_button.pack(side=tk.BOTTOM)

        self.tree = ttk.Treeview(self, columns=("x", "y"), show="headings")
        self.tree.heading("x", text="x")
        self.tree.heading("y", text="y")
        self.tree.pack(side=tk.BOTTOM)

        self.table_frame = ttk.Frame(self)
        self.table_frame.pack(side=tk.BOTTOM)
        self.table = ttk.Treeview(self.table_frame, columns=("fa", "fb", "I", "Etrunc", "Et"), show="headings")
        self.table.heading("fa", text="f(a)")
        self.table.heading("fb", text="f(b)")
        self.table.heading("I", text="I")
        self.table.heading("Etrunc", text="Etrunc")
        self.table.heading("Et", text="Et")
        self.table.pack()

    def agregar_datos(self):
        x_value = float(tk.simpledialog.askstring("Ingresar Datos", "Ingrese un valor para x:"))
        y_value = float(tk.simpledialog.askstring("Ingresar Datos", "Ingrese un valor para y:"))
        self.x.append(x_value)
        self.y.append(y_value)
        self.ax.plot(self.x, self.y, 'bo-')
        self.canvas.draw()
        self.actualizar_listado()

    def calcular_trapecio(self):
        self.trapecio = 0
        for i in range(1, len(self.x)):
            h = self.x[i] - self.x[i - 1]
            self.trapecio += 0.5 * h * (self.y[i] + self.y[i - 1])

    def calcular_resultados(self):
        self.fa = self.y[0]
        self.fb = self.y[-1]
        self.I = self.trapecio
        self.Etrunc = abs(self.I - (self.fb - self.fa))
        self.Et = abs(self.Etrunc / self.I) * 100



    def mostrar_resultados(self):
        self.calcular_trapecio()
        self.calcular_resultados()

        resultado = "Resultado del método del trapecio: {:.2f}".format(self.trapecio)
        messagebox.showinfo("Resultado", resultado)

        self.label.configure(text="Resultado del método del trapecio: {:.2f}".format(self.trapecio))

        self.actualizar_tabla()

    def actualizar_tabla(self):
        self.table.delete(*self.table.get_children())
        self.table.insert("", "end", values=(self.fa, self.fb, self.I, self.Etrunc, self.Et))

    def actualizar_listado(self):
        self.tree.delete(*self.tree.get_children())
        for i in range(len(self.x)):
            self.tree.insert("", "end", values=(self.x[i], self.y[i]))

    
if __name__ == "__main__":
    app = TrapecioApp()
    app.mainloop()
