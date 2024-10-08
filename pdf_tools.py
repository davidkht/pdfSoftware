# pdf_tools.py
import os
import PyPDF2

# Módulo para unir PDF
def unir_pdfs(directorio, salida):
    pdf_writer = PyPDF2.PdfWriter()
    
    for archivo in os.listdir(directorio):
        if archivo.endswith('.pdf'):
            ruta_pdf = os.path.join(directorio, archivo)
            pdf_reader = PyPDF2.PdfReader(ruta_pdf)
            
            for pagina in range(len(pdf_reader.pages)):
                pdf_writer.add_page(pdf_reader.pages[pagina])
    
    with open(salida, 'wb') as archivo_salida:
        pdf_writer.write(archivo_salida)
    print(f"PDFs unidos correctamente en {salida}")

# Módulo para dividir PDF
def dividir_pdf(archivo_pdf, intervalos, directorio_salida):
    pdf_reader = PyPDF2.PdfReader(archivo_pdf)
    total_paginas = len(pdf_reader.pages)
    
    for inicio, fin in intervalos:
        if inicio < 0 or fin >= total_paginas:
            raise ValueError("Intervalo fuera de rango. Por favor ingresa intervalos válidos.")
    
    for i, (inicio, fin) in enumerate(intervalos):
        pdf_writer = PyPDF2.PdfWriter()
        for pagina in range(inicio, fin + 1):
            pdf_writer.add_page(pdf_reader.pages[pagina])
        
        salida = os.path.join(directorio_salida, f'parte_{i + 1}.pdf')
        with open(salida, 'wb') as archivo_salida:
            pdf_writer.write(archivo_salida)
        print(f"Parte {i + 1} guardada como {salida}")

# Módulo para eliminar páginas específicas
def eliminar_paginas(archivo_pdf, paginas_a_eliminar, salida):
    pdf_reader = PyPDF2.PdfReader(archivo_pdf)
    total_paginas = len(pdf_reader.pages)
    
    if any(pagina < 0 or pagina >= total_paginas for pagina in paginas_a_eliminar):
        raise ValueError("Una o más páginas a eliminar están fuera de rango. Por favor ingresa números de página válidos.")
    
    pdf_writer = PyPDF2.PdfWriter()
    for pagina in range(total_paginas):
        if pagina not in paginas_a_eliminar:
            pdf_writer.add_page(pdf_reader.pages[pagina])
    
    with open(salida, 'wb') as archivo_salida:
        pdf_writer.write(archivo_salida)
    print(f"Páginas eliminadas. Nuevo archivo guardado en {salida}")

# Módulo para extraer páginas específicas
def extraer_paginas(archivo_pdf, paginas_a_extraer, salida):
    pdf_reader = PyPDF2.PdfReader(archivo_pdf)
    total_paginas = len(pdf_reader.pages)
    
    if any(pagina < 0 or pagina >= total_paginas for pagina in paginas_a_extraer):
        raise ValueError("Una o más páginas a extraer están fuera de rango. Por favor ingresa números de página válidos.")
    
    pdf_writer = PyPDF2.PdfWriter()
    for pagina in paginas_a_extraer:
        pdf_writer.add_page(pdf_reader.pages[pagina])
    
    with open(salida, 'wb') as archivo_salida:
        pdf_writer.write(archivo_salida)
    print(f"Páginas extraídas y guardadas en {salida}")