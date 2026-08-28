expenses = []


def add_expense():
    category = input("Categoria de gasto: ")
    description = input("Descripción del gasto: ")
    amount = float(input("Costo del gasto: "))
    new_expense = {"category": category, "description": description, "amount": amount}
    expenses.append(new_expense)

def view_expenses():
    for item in expenses:
        print(f"Categoria: {item['category']} - Descripción: {item['description']} - Monto: {item['amount']}")


def view_total():
    total = 0
    for item in expenses: 
        total = total + item['amount']
    print(f"Total gastado: {total}")


def view_by_category():
    category = input("Ingrese la categoría: ")
    for item in expenses:
        if category == item['category']:
            print(f"Los elementos de la categoría son: Descripción: {item['description']} - Monto: {item['amount']}")


def save_to_file():
    with open("expenses.txt", "w", encoding="utf-8") as file:
        for item in expenses:
            file.write(f"Categoria: {item['category']} - Descripción: {item['description']} - Monto: {item['amount']}\n")


if __name__ == "__main__":
    while True:
        print("1. Agregar gasto")
        print("2. Ver todos los gastos")
        print("3. Ver total gastado")
        print("4. Ver gastos por categoría")
        print("5. Guardar y salir")
        
        option = input("Elige una opción: ")
        if option == "1":
            add_expense()
        elif option == "2":
            view_expenses()
        elif option == "3":
            view_total()
        elif option == "4":
            view_by_category()
        elif option == "5":
            save_to_file()
            break
        else: 
            print("Ingrese una opción valida del 1 al 5")
       
        
    