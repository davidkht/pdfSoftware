# main.py
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import os
import pdf_tools

class PDFApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de PDFs")
        self.root.geometry("500x400")
        self.create_widgets()

    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        unir_btn = ttk.Button(main_frame, text="Unir PDFs", command=self.unir_pdfs)
        unir_btn.pack(pady=10, fill=tk.X)
        
        dividir_btn = ttk.Button(main_frame, text="Dividir PDF", command=self.dividir_pdf)
        dividir_btn.pack(pady=10, fill=tk.X)
        
        eliminar_btn = ttk.Button(main_frame, text="Eliminar Páginas", command=self.eliminar_paginas)
        eliminar_btn.pack(pady=10, fill=tk.X)
        
        extraer_btn = ttk.Button(main_frame, text="Extraer Páginas", command=self.extraer_paginas)
        extraer_btn.pack(pady=10, fill=tk.X)

    def unir_pdfs(self):
        directorio = filedialog.askdirectory(title="Seleccionar directorio con PDFs a unir")
        if directorio:
            salida = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")], title="Guardar PDF unido como")
            if salida:
                pdf_tools.unir_pdfs(directorio, salida)
                messagebox.showinfo("Éxito", f"PDFs unidos correctamente en {salida}")

    def dividir_pdf(self):
        archivo_pdf = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")], title="Seleccionar PDF a dividir")
        if archivo_pdf:
            intervalos_frame = ttk.Frame(self.root, padding="10")
            intervalos_frame.pack(fill=tk.BOTH, expand=True)

            ttk.Label(intervalos_frame, text="Intervalos (ej. 1-3,4-6)").pack(pady=5)
            intervalos_entry = ttk.Entry(intervalos_frame)
            intervalos_entry.pack(pady=5, fill=tk.X)
            
            def confirmar():
                intervalos_str = intervalos_entry.get()
                try:
                    intervalos = [(int(x.split('-')[0]), int(x.split('-')[1])) for x in intervalos_str.split(',')]
                    directorio_salida = filedialog.askdirectory(title="Seleccionar directorio para guardar PDFs divididos")
                    if directorio_salida:
                        pdf_tools.dividir_pdf(archivo_pdf, [(inicio - 1, fin - 1) for inicio, fin in intervalos], directorio_salida)
                        messagebox.showinfo("Éxito", f"PDF dividido y guardado en {directorio_salida}")
                    intervalos_frame.destroy()
                except ValueError:
                    messagebox.showerror("Error", "Por favor ingresa intervalos válidos.")
                    intervalos_frame.destroy()

            confirmar_btn = ttk.Button(intervalos_frame, text="Confirmar", command=confirmar)
            confirmar_btn.pack(pady=10)

    def eliminar_paginas(self):
        archivo_pdf = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")], title="Seleccionar PDF para eliminar páginas")
        if archivo_pdf:
            eliminar_frame = ttk.Frame(self.root, padding="10")
            eliminar_frame.pack(fill=tk.BOTH, expand=True)

            ttk.Label(eliminar_frame, text="Páginas a eliminar (ej. 1,3,5)").pack(pady=5)
            paginas_entry = ttk.Entry(eliminar_frame)
            paginas_entry.pack(pady=5, fill=tk.X)
            
            def confirmar():
                paginas_str = paginas_entry.get()
                try:
                    paginas_a_eliminar = [int(x) for x in paginas_str.split(',')]
                    salida = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")], title="Guardar PDF sin páginas eliminadas como")
                    if salida:
                        pdf_tools.eliminar_paginas(archivo_pdf, [pagina - 1 for pagina in paginas_a_eliminar], salida)
                        messagebox.showinfo("Éxito", f"Páginas eliminadas y archivo guardado en {salida}")
                    eliminar_frame.destroy()
                except ValueError:
                    messagebox.showerror("Error", "Por favor ingresa números de página válidos.")
                    eliminar_frame.destroy()

            confirmar_btn = ttk.Button(eliminar_frame, text="Confirmar", command=confirmar)
            confirmar_btn.pack(pady=10)

    def extraer_paginas(self):
        archivo_pdf = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")], title="Seleccionar PDF para extraer páginas")
        if archivo_pdf:
            extraer_frame = ttk.Frame(self.root, padding="10")
            extraer_frame.pack(fill=tk.BOTH, expand=True)

            ttk.Label(extraer_frame, text="Páginas a extraer (ej. 1,3,5)").pack(pady=5)
            paginas_entry = ttk.Entry(extraer_frame)
            paginas_entry.pack(pady=5, fill=tk.X)
            
            def confirmar():
                paginas_str = paginas_entry.get()
                try:
                    paginas_a_extraer = [int(x) for x in paginas_str.split(',')]
                    salida = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")], title="Guardar PDF con páginas extraídas como")
                    if salida:
                        pdf_tools.extraer_paginas(archivo_pdf, [pagina - 1 for pagina in paginas_a_extraer], salida)
                        messagebox.showinfo("Éxito", f"Páginas extraídas y guardadas en {salida}")
                    extraer_frame.destroy()
                except ValueError:
                    messagebox.showerror("Error", "Por favor ingresa números de página válidos.")
                    extraer_frame.destroy()

            confirmar_btn = ttk.Button(extraer_frame, text="Confirmar", command=confirmar)
            confirmar_btn.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFApp(root)
    root.mainloop()