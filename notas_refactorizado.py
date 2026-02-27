
def calcular_media(nombre, nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3

    def mostrar_informacion(nombre, nota1, nota2, nota3, media):
        print("Alumno: " + nombre)
        print("Nota 1: " + str(nota1))
        print("Nota 2: " + str(nota2))
        print("Nota 3: " + str(nota3))
        print("Media: " + str(media))
    
    mostrar_informacion(nombre, nota1, nota2, nota3, media)
    if media >= 9:
        print("Sobresaliente")
    elif media >= 7 and media < 9:
        print("Notable")
    elif media >= 5 and media < 7:
        print("Aprobado")
    else:
        print("Suspenso")
    print("----------------------")
def main():
    calcular_media("Ana García", 8, 7, 9)
    calcular_media("Luis Pérez", 4, 5, 3)
    calcular_media("Marta Gómez", 6, 7, 5)

main()