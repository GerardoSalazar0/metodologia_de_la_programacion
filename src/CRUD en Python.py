# CRUD in Python
# Materia: Metodología de la Programación 
# Profesor: Charly Mercury 
# Estudiante: Gerardo Salazar de la Fuente (2530032) 1-1 IM  


# Resumen Ejecutivo:
"""
# Un CRUD es un sistema que permite realizar cuatro operaciones básicas
# sobre datos: Create (crear), Read (leer), Update (actualizar) y Delete (eliminar).
# En este programa elegí usar un diccionario donde cada item se almacena
# mediante una clave única (item_id) porque permite acceso rápido y directo
# a los elementos sin tener que recorrer toda una lista.
# El uso de funciones facilita la organización del programa, separando la lógica
# de cada operación y haciendo el código más claro y fácil de mantener.
# El programa incluye un menú principal que permite al usuario crear, leer,
# actualizar, eliminar y listar elementos, validando entradas antes de procesarlas.
"""


# PROBLEMA: CRUD CON FUNCIONES 
# Descripción:
"""
Este programa implementa un CRUD simple (Crear, Leer, Actualizar, Eliminar), sistema para 
elementos almacenados en la memoria. Cada artículo tiene una identificación, nombre, precio, 
y cantidad. Las operaciones CRUD se dividen en funciones y 
el programa utiliza un menú de texto para la interacción del usuario.
"""

# Inputs:
#   - Menu option (string/int)
#   - For CREATE/UPDATE: item_id, name, price, quantity
#   - For READ/DELETE: item_id

# Outputs:
# - Messages such as:
#   "Item created", "Item updated", "Item deleted",
#   "Item not found", "Error: invalid input", "Items list:"

# Validations:
# - item_id not empty
# - price and quantity must be valid numbers >= 0
# - menu option must be valid
# - cannot create an item with an existing id


# Código: 

items_data = {}  # main data structure


def create_item(data, item_id, name, price, quantity):
    if item_id in data:
        return False
    data[item_id] = {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    return True


def read_item(data, item_id):
    return data.get(item_id)


def update_item(data, item_id, new_name, new_price, new_quantity):
    if item_id not in data:
        return False
    data[item_id]["name"] = new_name
    data[item_id]["price"] = new_price
    data[item_id]["quantity"] = new_quantity
    return True


def delete_item(data, item_id):
    if item_id not in data:
        return False
    del data[item_id]
    return True


def list_items(data):
    print("Items list:")
    if not data:
        print("No items available")
    for item_id, item in data.items():
        print(f"ID: {item_id}, Name: {item['name']}, Price: {item['price']}, Quantity: {item['quantity']}")


def validate_number(value, allow_float=True):
    try:
        if allow_float:
            num = float(value)
        else:
            num = int(value)
        if num < 0:
            return None
        return num
    except:
        return None


EXIT_OPTION = "0"

while True:
    print("\n------ ITEM CRUD MANAGER ------")
    print("1) Create item")
    print("2) Read item by id")
    print("3) Update item by id")
    print("4) Delete item by id")
    print("5) List all items")
    print("0) Exit")

    option = input("Select an option: ").strip()

    if option == EXIT_OPTION:
        print("Exiting program...")
        break

    # CREATE
    elif option == "1":
        item_id = input("Enter item id: ").strip()
        if item_id == "":
            print("Error: invalid input")
            continue

        name = input("Enter name: ").strip()
        price_raw = input("Enter price: ").strip()
        quantity_raw = input("Enter quantity: ").strip()

        price = validate_number(price_raw, allow_float=True)
        quantity = validate_number(quantity_raw, allow_float=False)

        if price is None or quantity is None:
            print("Error: invalid input")
            continue

        ok = create_item(items_data, item_id, name, price, quantity)
        print("Item created" if ok else "Error: item already exists")

    # READ
    elif option == "2":
        item_id = input("Enter item id: ").strip()
        if item_id == "":
            print("Error: invalid input")
            continue

        item = read_item(items_data, item_id)
        if item is None:
            print("Item not found")
        else:
            print(f"ID: {item_id}, Name: {item['name']}, Price: {item['price']}, Quantity: {item['quantity']}")

    # UPDATE
    elif option == "3":
        item_id = input("Enter item id: ").strip()
        if item_id == "":
            print("Error: invalid input")
            continue

        new_name = input("Enter new name: ").strip()
        new_price_raw = input("Enter new price: ").strip()
        new_quantity_raw = input("Enter new quantity: ").strip()

        new_price = validate_number(new_price_raw, allow_float=True)
        new_quantity = validate_number(new_quantity_raw, allow_float=False)

        if new_price is None or new_quantity is None:
            print("Error: invalid input")
            continue

        updated = update_item(items_data, item_id, new_name, new_price, new_quantity)
        print("Item updated" if updated else "Item not found")

    # DELETE
    elif option == "4":
        item_id = input("Enter item id: ").strip()
        if item_id == "":
            print("Error: invalid input")
            continue
        deleted = delete_item(items_data, item_id)
        print("Item deleted" if deleted else "Item not found")

    # LIST
    elif option == "5":
        list_items(items_data)

    else:
        print("Error: invalid input")



# Test cases:
# 1) Normal: 
"""
1) Create item
2) Read item by id
3) Update item by id
4) Delete item by id
5) List all items
0) Exit
Select an option: 1
Enter item id: 3225ABC
Enter name: Bread
Enter price: 33
Enter quantity: 2
Item created

------ ITEM CRUD MANAGER ------
1) Create item
2) Read item by id
3) Update item by id
4) Delete item by id
5) List all items
0) Exit
Select an option: 5
Items list:
ID: 3225ABC, Name: Bread, Price: 33.0, Quantity: 2 """

# 2) Border:
"""
1) Create item
2) Read item by id
3) Update item by id
4) Delete item by id
5) List all items
0) Exit
Select an option: 1
Enter item id: 3225ABC
Enter name: Bread
Enter price: 33
Enter quantity: 2
Item created

------ ITEM CRUD MANAGER ------
1) Create item
2) Read item by id
3) Update item by id
4) Delete item by id
5) List all items
0) Exit
Select an option: 5
Items list:
ID: 3225ABC, Name: Bread, Price: 33.0, Quantity: 2"""

# 3) Error: invalid menu, empty id, non-numeric price
"""------ ITEM CRUD MANAGER ------
1) Create item
2) Read item by id
3) Update item by id
4) Delete item by id
5) List all items
0) Exit
Select an option: 1
Enter item id: sdlg777
Enter name: 21
Enter price:
Enter quantity:
Error: invalid input
"""


# ======================================================================
# CONCLUSIONES 
# ======================================================================
"""
El uso de funciones permitió organizar la lógica del CRUD de manera modular, 
clara y fácil de mantener. Trabajar con un diccionario como estructura principal 
simplificó el acceso a los elementos mediante sus llaves, haciendo más eficiente la lectura 
y actualización de datos. La validación de entradas representó un reto importante, 
pero se resolvió verificando tipos, rangos y existencia de IDs antes de ejecutar cada operación. 
Además, separar la lógica del menú y las funciones evitó duplicar código y redujo errores. 
Este CRUD puede ampliarse fácilmente para sistemas reales agregando persistencia en archivos, 
bases de datos o conectándolo a una interfaz gráfica o API web, convirtiéndose en la base de 
un sistema de inventarios mucho más robusto.
"""



# ======================================================================
# REFERENCIAS 
# ======================================================================

# https://keepcoding.io/blog/crud-en-python/ 
# https://entrenamiento-frameworks-web-python.readthedocs.io/es/latest/leccion6/crud_app.html 
# https://cosasdedevs.com/posts/como-crear-un-crud-en-python-parte-1-estructura-y-clase/ 
# https://www.w3schools.com/python/ref_string_isnumeric.asp 
# https://es.stackoverflow.com/questions/353529/c%C3%B3mo-regresar-al-inicio-de-un-programa-con-python 
# https://www.gyata.ai/es/python/python-main-function 
# https://www.daniweb.com/programming/software-development/threads/451737/validating-personal-id-number



# ======================================================================
# REPOSITORIO DE GITHUB
# ======================================================================

# 
