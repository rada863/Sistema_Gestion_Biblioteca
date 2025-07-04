import markdown
# a alguno le puede servir esto son libres de usarlo 

# Leer el archivo Markdown
with open("README.md", "r", encoding="utf-8") as archivo_md:
    contenido_md = archivo_md.read()

# Convertir a HTML
contenido_html = markdown.markdown(contenido_md)

# Guardar como archivo HTML
with open("README.html", "w", encoding="utf-8") as archivo_html:
    archivo_html.write(contenido_html)

print("✅ Conversión completada. Archivo 'README.html' generado.")