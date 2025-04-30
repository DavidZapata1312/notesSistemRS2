def addNote():
    try:
        # Pedimos al usuario que ingrese las notas separadas por comas
        print("\n📝 Ingrese notas del 1 al 100, separadas por comas (ej: 75, 88, 59):")
        entrada = input("👉 ")
        # Convertimos la entrada a una lista de notas
        notes_raw = entrada.split(',')
        notes = []

        for note in notes_raw:
            valor = float(note.strip())  # Convertimos la nota a un número flotante
            if 1 <= valor <= 100:  # Verificamos si la nota está dentro del rango permitido
                notes.append(valor)

                # Imprimimos un mensaje de aprobación o reprobación según el valor de la nota
                if valor >= 60:
                    print(f"✅ ¡Bien! Tu nota de {valor} es suficiente para aprobar.")
                else:
                    print(f"❌ Uy... tu nota de {valor} no alcanza para aprobar.")
            else:
                print(f"⚠️ Nota fuera de rango ignorada: {valor}")  # Notificamos si la nota es inválida

    except ValueError:
        # Capturamos el error si no se ingresan valores válidos
        print("🚫 Error: una o más notas no son válidas. Asegúrate de ingresar solo números.")
        return []

    else:
        # Mostramos las notas válidas ingresadas
        print("\n📋 Notas válidas ingresadas:")
        print("   ➤", notes)
        return notes  # Retornamos la lista de notas válidas


def average(notas):
    # Verificamos si hay notas ingresadas
    if notas:
        # Calculamos el promedio
        promedio = sum(notas) / len(notas)
        print("\n📊 Calculando promedio...")
        print(f"   🎯 El promedio del grupo es: {promedio:.2f}")
    else:
        print("⚠️ No se ingresaron notas válidas para calcular el promedio.")  # Mensaje si no hay notas


def majorNotes(notas):
    # Pedimos al usuario un valor para comparar
    valComp = float(input("\n🔎 Ingrese el valor a comparar para contar notas mayores o iguales: "))
    if notas:
        contador = 0
        # Recorremos las notas para contar cuántas son mayores o iguales al valor ingresado
        for nota in notas:
            if nota >= valComp:
                contador += 1
        # Mostramos la cantidad de notas que cumplen con la condición
        print(f"\n📈 Hay {contador} nota(s) mayores o iguales a {valComp}.")
    else:
        print("⚠️ No se ingresaron notas válidas para realizar la comparación.")  # Mensaje si no hay notas


def equalNotes(notas):
    # Pedimos al usuario un valor para comparar
    valComp = float(input("\n🔍 Ingrese el valor a comparar para contar notas iguales: "))
    if notas:
        contador = sum(1 for nota in notas if nota == valComp)  # Contamos las notas que son iguales al valor
        # Mostramos la cantidad de notas que cumplen con la condición
        print(f"\n📌 Hay {contador} nota(s) exactamente igual(es) a {valComp}.")
    else:
        print("⚠️ No se ingresaron notas válidas para realizar la comparación.")  # Mensaje si no hay notas


# Uso del programa
print("\n================= 📚 Bienvenido al gestor de notas 📚 =================")
# Llamamos a la función para agregar notas y las almacenamos en una lista
notas_validas = addNote()
# Calculamos el promedio de las notas válidas
average(notas_validas)
# Contamos cuántas notas son mayores o iguales a un valor
majorNotes(notas_validas)
# Contamos cuántas notas son exactamente iguales a un valor
equalNotes(notas_validas)
# Finalizamos el programa
print("\n================= 🏁 Fin del programa. ¡Gracias! 🏁 =================\n")
