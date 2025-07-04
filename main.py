class Libro:
    def __init__(self, titulo: str, autor: str, año: int, id: int):
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.id = id

    def __str__(self):
        return f"ID: {self.id} | Título: {self.titulo} | Autor: {self.autor} | Año: {self.año}"


class Biblioteca:
    def __init__(self):
        self.libros = {}  

    def añadir_libro(self, libro: Libro):
        if libro.id in self.libros:
            print(f"❌ Error: Ya existe un libro con el ID {libro.id}.")
        else:
            self.libros[libro.id] = libro
            print(f"✅ Libro '{libro.titulo}' añadido correctamente.")

    def eliminar_libro(self, id: int):
        if id in self.libros:
            libro_eliminado = self.libros.pop(id)
            print(f"🗑️ Libro '{libro_eliminado.titulo}' eliminado correctamente.")
        else:
            print(f"❌ Error: No se encontró un libro con el ID {id}.")

    def buscar_libro(self, criterio: str):
        criterio = criterio.lower()
        encontrados = [
            libro for libro in self.libros.values()
            if criterio in libro.titulo.lower() or criterio in libro.autor.lower()
        ]
        if encontrados:
            print("\n📚 Libros encontrados:")
            for libro in encontrados:
                print(libro)
        else:
            print(f"🔍 No se encontraron libros que coincidan con '{criterio}'.")

    def listar_libros(self):
        if not self.libros:
            print("📭 La biblioteca está vacía.")
        else:
            print("\n📘 Listado de libros:")
            for libro in sorted(self.libros.values(), key=lambda l: l.titulo.lower()):
                print(libro)


def mostrar_menu():
    print("\n--- Sistema de Gestión de Biblioteca ---")
    print("1. Añadir libro")
    print("2. Eliminar libro")
    print("3. Buscar libro")
    print("4. Listar todos los libros")
    print("5. Salir")


def main():
    biblioteca = Biblioteca()

    while True:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opción (1-5): "))
        except ValueError:
            print("⚠️ Ingrese un número válido.")
            continue

        if opcion == 1:
            titulo = input("Título del libro: ").strip()
            autor = input("Autor del libro: ").strip()
            try:
                año = int(input("Año de publicación: "))
                id = int(input("ID del libro: "))
                if año <= 0:
                    print("⚠️ El año debe ser mayor a cero.")
                    continue
                if not titulo or not autor:
                    print("⚠️ Título y autor no pueden estar vacíos.")
                    continue
                nuevo_libro = Libro(titulo, autor, año, id)
                biblioteca.añadir_libro(nuevo_libro)
            except ValueError:
                print("⚠️ El año y el ID deben ser números enteros.")

        elif opcion == 2:
            try:
                id = int(input("ID del libro a eliminar: "))
                biblioteca.eliminar_libro(id)
            except ValueError:
                print("⚠️ El ID debe ser un número entero.")

        elif opcion == 3:
            criterio = input("Ingrese título o autor a buscar: ")
            biblioteca.buscar_libro(criterio)

        elif opcion == 4:
            biblioteca.listar_libros()

        elif opcion == 5:
            print("👋 Saliendo del sistema...")
            break

        else:
            print("⚠️ Opción no válida. Elegí del 1 al 5.")


if __name__ == "__main__":
    main()