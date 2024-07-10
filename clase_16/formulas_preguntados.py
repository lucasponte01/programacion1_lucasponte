import csv
import pygame
pygame.init()

def guardar_nombre_y_puntaje(puntaje, nombre):
    """
    Guarda el nombre y puntaje en un archivo CSV.
    """
    with open("clase_16/puntajes.csv", "a", newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerow([nombre, puntaje]) #Cuando writerow([nombre, puntaje]) se llama, se escribe una nueva línea en el archivo CSV con los valores de nombre y puntaje separados por comas.

def mostrar_puntajes(pantalla):
    """
    Lee los puntajes desde el archivo CSV y los ordena de mayor a menor.
    """
    font = pygame.font.SysFont("Arial Narrow", 50)
    lista_puntajes = []
    with open("clase_16/puntajes.csv", "r") as archivo:
        reader = csv.reader(archivo) #Se utiliza para leer un archivo CSV y convertir cada línea en una lista de valores.
        for i in reader:
            nombre, puntaje = i #nombre, puntaje = row asigna el primer elemento de row a la variable nombre y el segundo elemento a la variable puntaje.
            lista_puntajes.append((nombre, int(puntaje)))

    # Ordenar los puntajes de mayor a menor
    lista_puntajes.sort(key=lambda x: x[1], reverse=True)

    for i in range(3):
        if i < len(lista_puntajes):
            nombre, puntaje = lista_puntajes[i]
            texto = font.render(f"{i + 1}. {nombre}: {puntaje} puntos", True, (225, 225, 225))
            pantalla.blit(texto, (0,0 + i * 40))



def mostrar_preguntas(lista:list ,indice:int , pantalla):
    """
    utilizando el parametro indice marca las preguntas del parametro lista
    return: opciones1 , opciones2 , opciones3 , pregunta_actual
    """
    font = pygame.font.SysFont("Arial Narrow", 50)
    ubicacionrect_a = [0, 300]
    tamaño_rect_a = [335 , 35]
    color_rect_a =(18, 225, 232)
    boton_a = pygame.Rect(ubicacionrect_a, tamaño_rect_a)
    ubicacionrect_b = [0, 350]
    tamaño_rect_b = [335 , 35]
    color_rect_b =(18, 225, 232)
    boton_b = pygame.Rect(ubicacionrect_b, tamaño_rect_b)
    ubicacionrect_c = [0, 400]
    tamaño_rect_c = [335 , 35]
    color_rect_c =(18, 225, 232)
    boton_c = pygame.Rect(ubicacionrect_c, tamaño_rect_c)
    pregunta_actual = font.render(lista[indice]["pregunta"], True, (0, 0, 0))
    opciones1 = font.render(f"a:{lista[indice]["a"]}",True,(0,0,0))
    opciones2 = font.render(f"b:{lista[indice]["b"]}",True,(0,0,0))
    opciones3 = font.render(f"c:{lista[indice]["c"]}",True,(0,0,0))
    pygame.draw.rect(pantalla, color_rect_a , boton_a , border_radius=0)
    pygame.draw.rect(pantalla , color_rect_b , boton_b , border_radius=0)
    pygame.draw.rect(pantalla , color_rect_c , boton_c , border_radius=0)
    pantalla.blit(pregunta_actual, (-5, 10))
    pantalla.blit(opciones1, (0, 300))
    pantalla.blit(opciones2, (0, 350))
    pantalla.blit(opciones3, (0, 400))

