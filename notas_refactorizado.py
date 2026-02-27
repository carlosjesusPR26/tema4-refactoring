# Refactorización del código para calcular la media de las notas de los alumnos y evaluar su rendimiento.
# Carlos Jesus Saorin Sanchez
#27-02-2026


def calcular_media(nombre, nota1, nota2, nota3): #Esta función calcula la media de las notas y evalúa el rendimiento del alumno.
    """
    Calcula la media de tres notas.
    Args:
        nota1 (float): Primera nota del alumno.
        nota2 (float): Segunda nota del alumno.
        nota3 (float): Tercera nota del alumno.
    Returns:
        float: La media de las tres notas (valor entre 0 y 10).
    """
    media = (nota1 + nota2 + nota3) / 3

    def mostrar_informacion(nombre, nota1, nota2, nota3, media):#Esta función muestra la información del alumno y su calificación.
        """
        Imprime la información del alumno y su calificación.
        Args:
            nombre (str): Nombre del alumno.
            nota1 (float): Primera nota del alumno.
            nota2 (float): Segunda nota del alumno.
            nota3 (float): Tercera nota del alumno.
        Returns:
            La media de las tres notas, las notas y el nombre del alumno.
        """
        print("Alumno: " + nombre)
        print("Nota 1: " + str(nota1))
        print("Nota 2: " + str(nota2))
        print("Nota 3: " + str(nota3))
        print("Media: " + str(media))

    mostrar_informacion(nombre, nota1, nota2, nota3, media) #Muestra la información del alumno y su calificación.
    if media >= 9:
        print("Sobresaliente")
    elif media >= 7 and media < 9:
        print("Notable")
    elif media >= 5 and media < 7:
        print("Aprobado")
    else:
        print("Suspenso")
    print("----------------------")
"""
   Evalua según la media de las tres notas.
    Args:
        nombre (str): Nombre del alumno.
        nota1 (float): Primera nota del alumno.
        nota2 (float): Segunda nota del alumno.
        nota3 (float): Tercera nota del alumno.
    Returns:
        Evaluación del alumno según su media.
    """
def main():
    calcular_media("Ana García", 8, 7, 9)
    calcular_media("Luis Pérez", 4, 5, 3)
    calcular_media("Marta Gómez", 6, 7, 5)

main()