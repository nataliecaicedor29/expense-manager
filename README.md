# Expense Manager

Programa en Python para gestionar gastos personales desde la terminal. Permite agregar gastos por categoría, ver el listado completo, consultar el total gastado, filtrar por categoría, y guardar todo en un archivo de texto.

## Tecnologías

- Python (sin librerías externas)

## Estructura

El programa está organizado en 5 funciones con responsabilidades separadas, más un menú interactivo:

- `add_expense()` — pide categoría, descripción y monto, y agrega el gasto a la lista
- `view_expenses()` — muestra todos los gastos registrados
- `view_total()` — suma y muestra el total gastado
- `view_by_category()` — filtra y muestra los gastos de una categoría específica
- `save_to_file()` — guarda todos los gastos en `expenses.txt`

## Instalación y uso

1. Clona el repositorio y entra a la carpeta del proyecto
2. Ejecuta el programa: python main.py
3. Usa el menú interactivo para agregar gastos, consultarlos, o guardarlos en archivo.