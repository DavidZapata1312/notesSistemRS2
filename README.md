# Gestor de Notas

Programa en Python para gestionar y analizar notas de estudiantes. Permite ingresar notas, calcular el promedio y realizar comparaciones con valores proporcionados por el usuario.

## Funcionalidades

- **Ingreso de Notas**: El usuario ingresa notas separadas por comas (rango 1-100).
- **Cálculo del Promedio**: El programa calcula el promedio de las notas válidas.
- **Contar Notas Mayores o Iguales**: Permite contar cuántas notas son mayores o iguales a un valor.
- **Contar Notas Iguales**: Permite contar cuántas notas son exactamente iguales a un valor.

## Ejemplo de Ejecución

```text
================= 📚 Bienvenido al gestor de notas 📚 =================

📝 Ingrese notas del 1 al 100, separadas por comas (ej: 75, 88, 59):
👉 75, 88, 59, 45

✅ ¡Bien! Tu nota de 75.0 es suficiente para aprobar.
✅ ¡Bien! Tu nota de 88.0 es suficiente para aprobar.
❌ Uy... tu nota de 59.0 no alcanza para aprobar.
❌ Uy... tu nota de 45.0 no alcanza para aprobar.

📋 Notas válidas ingresadas:
   ➤ [75.0, 88.0, 59.0, 45.0]

📊 Calculando promedio...
   🎯 El promedio del grupo es: 66.75

🔎 Ingrese el valor a comparar para contar notas mayores o iguales: 60

📈 Hay 3 nota(s) mayores o iguales a 60.0.

🔍 Ingrese el valor a comparar para contar notas iguales: 59

📌 Hay 1 nota(s) exactamente igual(es) a 59.0.

================= 🏁 Fin del programa. ¡Gracias! 🏁 =================
