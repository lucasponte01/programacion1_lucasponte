"""
Desafío:
A. Analizar detenidamente el set de datos (puede agregarle más preguntas si así
lo desea).
B. #Crear una pantalla de inicio, con 3 (tres) botones, “Jugar”, “Ver Puntajes”,
“Salir”, la misma deberá tener alguna imagen cubriendo completamente el
fondo y tener un sonido de fondo. Al apretar el botón jugar se iniciará el juego.
Opcional: Agregar un botón para activar/desactivar el sonido de fondo.

C. #Crear 2 botones uno con la etiqueta “Pregunta”, otro con la etiqueta “Reiniciar”

D. #Imprimir el Puntaje: 000 donde se va a ir acumulando el puntaje de las
respuestas correctas. Cada respuesta correcta suma 10 puntos.

E.#Al hacer clic en el botón “Pregunta” debe mostrar las preguntas comenzando
por la primera y las tres opciones, cada clic en este botón pasa a la siguiente
pregunta.

F. #Al hacer clic en una de las tres palabras que representa una de las tres
opciones, si es correcta, debe sumar el puntaje, reproducir un sonido de
respuesta correcta y dejar de mostrar las otras opciones.

G. Solo tiene 2 intentos para acertar la respuesta correcta y sumar puntos, si
agotó ambos intentos, deja de mostrar las opciones y no suma puntos. Al
elegir una respuesta incorrecta se reproducirá un sonido indicando el error y
se ocultará esa opción, obligando al usuario a elegir una de las dos restantes.

H. #Al hacer clic en el botón “Reiniciar” debe mostrar las preguntas comenzando
por la primera y las tres opciones, cada clic pasa a la siguiente pregunta.
También debe reiniciar el puntaje.

I. Una vez terminado el juego se deberá pedirle el nombre al usuario, guardar
ese nombre con su puntaje en un archivo, y volver a la pantalla de inicio.

J. #Al ingresar a la pantalla “Ver Puntajes”, se deberá mostrar los 3 (tres) mejores
puntajes ordenados de mayor a menor, junto con sus nombres de usuario
correspondientes. Debe haber un botón para volver al menú principal.
"""


from datos import lista
import pygame
from pygame.locals import *
from formulas_preguntados import *
pygame.init() 

#pantalla inicio
config_pantalla = [1000,700]
screen = pygame.display.set_mode(config_pantalla)
pygame.display.set_caption("Preguntados")
#imagenes
imagen_menu = pygame.image.load("clase_16/preguntados-netflix-trivia-quest.webp") 
imagen_menu = pygame.transform.scale(imagen_menu, (1000 , 700))
imagen_juego = pygame.image.load("clase_16/Preguntados.jpg")
imagen_juego = pygame.transform.scale(imagen_juego, (1000 , 700))
imagen_puntaje = pygame.image.load("clase_16/3c129bd0-abef-11ee-beb5-e1400df560f2.jpg.webp") 
imagen_puntaje = pygame.transform.scale(imagen_puntaje, (1000 , 700))
#sonidos
pygame.mixer.init()
pygame.mixer.music.set_volume(0.1)
sonido_menu = pygame.mixer.Sound("clase_16/los-angeles-20922.mp3")
sonido_click_correcto = pygame.mixer.Sound("clase_16\correct-156911.mp3")
sonido_click_incorrecto = pygame.mixer.Sound("clase_16\wronganswer-37702.mp3")
sonido_menu.set_volume(0.05)
sonido_menu.play()
sonido_menu.stop()
sonido_click_correcto.set_volume(0.05)
sonido_click_correcto.play(1)
sonido_click_correcto.stop()
sonido_click_incorrecto.set_volume(0.05)
sonido_click_incorrecto.play(1)
sonido_click_incorrecto.stop()

#botones
ubicacionrect = [400, 100]
tamaño_rect = [200 , 50]
color =  (251, 255, 0) 
boton1 = pygame.Rect(ubicacionrect, tamaño_rect)
#==========#
ubicacionrect1 = [375 , 180]
tamaño_rect1 = [250 , 50]
color_rect1 = (251, 255, 0)
boton2 = pygame.Rect(ubicacionrect1 , tamaño_rect1)
#==========#
ubicacionrect2 = [400 , 260]
tamaño_rect2 = [200 , 50]
color_rect2 = (251, 255, 0)
boton3 = pygame.Rect(ubicacionrect2 , tamaño_rect2)
#===========================segunda pantalla===================================#
#botones
ubicacionrect_pregunta = [0, 50]
tamaño_rect_pregunta = [200 , 50]
color_rect_pregunta =(18, 225, 232)
boton_pregunta = pygame.Rect(ubicacionrect_pregunta, tamaño_rect_pregunta)
#============#
ubicacionrect_reiniciar = [800, 50]
tamaño_rect_reiniciar = [200 , 50]
color_rect_reiniciar =(18, 225, 232)
boton_reiniciar = pygame.Rect(ubicacionrect_reiniciar, tamaño_rect_reiniciar)
#=============#
ubicacionrect_volver = [0, 650]
tamaño_rect_volver = [125 , 50]
color_rect_volver =(0, 0, 232)
boton_volver = pygame.Rect(ubicacionrect_volver, tamaño_rect_volver)
#===========#
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
#textos
font = pygame.font.SysFont("Arial Narrow", 50)
txt_jugar = font.render("jugar", True, (255, 0, 0))
#========#
txt_puntaje = font.render("Ver Puntajes" , True , (255, 0, 0))
#=========#
txt_salir = font.render("salir" , True , (255, 0, 0))
#==========#
txt_pregunta = font.render("pregunta" , True , (0, 0, 0))
#=========#
txt_reiniciar = font.render("reiniciar" , True , (0, 0, 0))
#=========#
score = "0"
txt_score = font.render(f"Score:{score}" , True , (255, 0, 0))
#==================#
indice = -1
txt_respuesta_correcta = font.render(f"la respuesta {lista[indice]["correcta"]} es correcta" , True , (0,0,0))
txt_respuesta_incorrecta = font.render(f"la respuesta 'a' es incorrecta" , True , (0,0,0))
txt_respuesta_incorrectab = font.render(f"la respuesta 'b' es incorrecta" , True , (0,0,0))
txt_respuesta_incorrectac = font.render(f"la respuesta 'c' es incorrecta" , True , (0,0,0))
#==========#
intentos = 2
txt_intentos = font.render(f"{intentos} intentos restantes" , True , (0,0,0))
#=========#
txt_ingreso = font.render(f"ingrese su nombre:" , True , (0,0,0))
mi_texto = ""
#=============#
txt_volver = font.render(f"volver" , True , (225,225,225))
###########################################################################
#banderas
reinicio = False
esta_jugando = False
juega = False
pregunta = False
opcion_a = False
opcion_a_incorrecta = False
opcion_b = False
opcion_b_incorrecta = False
opcion_c = False
opcion_c_incorrecta = False
puntajes = False
running = True
while running:
   # Se verifica si el usuario cerro la ventana
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False
      if event.type == pygame.MOUSEBUTTONDOWN:
         print(event.pos)
         if boton1.collidepoint(event.pos):
            esta_jugando = True   
            juega = True     
            reinicio = False
         if boton_pregunta.collidepoint(event.pos) :
            indice = indice + 1
            intentos = 2
            opcion_a = False
            opcion_a_incorrecta = False
            opcion_b = False
            opcion_b_incorrecta = False
            opcion_c = False
            opcion_c_incorrecta = False
            pregunta = True
            mostrar_preguntas(lista , indice , screen)
         if boton_a.collidepoint(event.pos) and  "a" == lista[indice]["correcta"]:
            opcion_a = True
            opcion_b = False
            opcion_c = False
            opcion_b_incorrecta = False
            opcion_c_incorrecta = False
            sonido_click_correcto.play(0)
            score = int(score) + 10
            score = str(score)
            txt_score = font.render(f"Score:{score}" , True , (255, 0, 0))
            txt_respuesta_correcta = font.render(f"la respuesta {lista[indice]["correcta"]} es correcta" , True , (0,0,0))
         else:
            if boton_a.collidepoint(event.pos) and "a" != lista[indice]["correcta"]:
               opcion_a = False
               opcion_b = False
               opcion_c = False
               opcion_a_incorrecta = True
               opcion_b_incorrecta = False
               opcion_c_incorrecta = False
               sonido_click_incorrecto.play(0)
               intentos = intentos - 1
               txt_intentos=font.render(f"{intentos} intentos restantes" , True , (0,0,0))
               txt_respuesta_incorrecta = font.render(f"la respuesta 'a' es incorrecta" , True , (0,0,0))
            if intentos == 0:
               intentos = 2
               indice +=1
               mostrar_preguntas(lista , indice , screen) 
               opcion_a_incorrecta = False
         if boton_b.collidepoint(event.pos) and "b" == lista[indice]["correcta"]:
            opcion_a = False
            opcion_b = True
            opcion_c = False
            opcion_a_incorrecta = False
            opcion_c_incorrecta = False
            sonido_click_correcto.play(0)        
            score = int(score) + 10
            score = str(score)
            txt_score = font.render(f"Score:{score}" , True , (255, 0, 0))
            txt_respuesta_correctaa = font.render(f"la respuesta {lista[indice]["correcta"]} es correcta" , True , (0,0,0))
         else:
            if boton_b.collidepoint(event.pos) and "b" != lista[indice]["correcta"]:
               opcion_a = False
               opcion_b = False
               opcion_c = False
               opcion_b_incorrecta = True
               opcion_a_incorrecta = False
               opcion_c_incorrecta = False
               sonido_click_incorrecto.play(0)
               intentos = intentos - 1
               txt_intentos=font.render(f"{intentos} intentos restantes" , True , (0,0,0))
               txt_respuesta_incorrectab = font.render(f"la respuesta 'b' es incorrecta" , True , (0,0,0))
            if intentos == 0:
               intentos = 2
               indice +=1
               opcion_b_incorrecta = False
               mostrar_preguntas(lista , indice , screen)   
         if boton_c.collidepoint(event.pos) and "c" == lista[indice]["correcta"]:
            opcion_a = False
            opcion_c = True
            opcion_b = False
            opcion_b_incorrecta = False
            opcion_a_incorrecta = False
            sonido_click_correcto.play(0)
            score = int(score) + 10
            score = str(score)
            txt_score = font.render(f"Score:{score}" , True , (255, 0, 0))
            txt_respuesta_correcta = font.render(f"la respuesta {lista[indice]["correcta"]} es correcta" , True , (0,0,0))
         else:
            if boton_c.collidepoint(event.pos) and "c" != lista[indice]["correcta"]:
               opcion_a = False
               opcion_b = False
               opcion_c = False
               opcion_c_incorrecta = True
               opcion_b_incorrecta = False
               opcion_a_incorrecta = False
               sonido_click_incorrecto.play(0)
               intentos = intentos - 1
               txt_intentos=font.render(f"{intentos} intentos restantes" , True , (0,0,0))
               txt_respuesta_incorrectac = font.render(f"la respuesta 'c' es incorrecta" , True , (0,0,0))
            if intentos == 0:
               intentos = 2
               indice +=1
               opcion_c_incorrecta = False
               mostrar_preguntas(lista , indice , screen) 
         if boton_reiniciar.collidepoint(event.pos):
            indice = 0
            score = 0
            score = str(score)
            txt_score = font.render(f"Score:{score}" , True , (255, 0, 0))
            mostrar_preguntas(lista , indice , screen)
            esta_jugando = True
            opcion_a = False
            opcion_a_incorrecta = False
            opcion_b = False
            opcion_b_incorrecta = False
            opcion_c = False
            opcion_c_incorrecta = False
         elif indice >= 16:
            reinicio = True           
         if boton2.collidepoint(event.pos):
            puntajes = True
            esta_jugando = False
            juega = True
            opcion_a = False
            opcion_a_incorrecta = False
            opcion_b = False
            opcion_b_incorrecta = False
            opcion_c = False
            opcion_c_incorrecta = False
            pregunta = False
            mostrar_puntajes( screen) 
         if boton_volver.collidepoint(event.pos):
            indice = -1
            juega = False
         if boton3.collidepoint(event.pos) and juega == False:
            running = False
      if event.type == pygame.KEYDOWN:
            mi_texto += event.unicode
            text_surface = font.render(mi_texto, True, (0, 0, 0))
            if event.key == pygame.K_RETURN:
               guardar_nombre_y_puntaje (score, mi_texto)
               esta_jugando = False
               juega = False
               reinicio = False
               indice = 0
               score = 0
               score = str(score)
               txt_score = font.render(f"Score:{score}" , True , (255, 0, 0))
               puntajes = False
               mi_texto = ""
               text_surface = font.render(mi_texto, True, (0, 0, 0))
#===============================lo que se muestra en pantalla===============================#
   if esta_jugando == True:
      sonido_menu.stop()
      screen.blit(imagen_juego , (0, 0))
      pygame.draw.rect(screen , color_rect_pregunta ,boton_pregunta, border_radius= 10)
      pygame.draw.rect(screen , color_rect_reiniciar ,boton_reiniciar, border_radius= 10)
      screen.blit(txt_score , (0 , 670))
      screen.blit(txt_pregunta , (25 , 55))
      screen.blit(txt_reiniciar , (830 , 55))
      if pregunta == True:
         mostrar_preguntas(lista , indice , screen)
         if opcion_a == True: 
            screen.blit(txt_respuesta_correcta , (0 , 600))
            pygame.draw.rect(screen , color_rect_b , boton_b , border_radius=0)
            pygame.draw.rect(screen , color_rect_c , boton_c , border_radius=0)
         else:
            if opcion_a_incorrecta == True:
               screen.blit(txt_respuesta_incorrecta , (0 , 600))
               pygame.draw.rect(screen , color_rect_a , boton_a , border_radius=0)
               screen.blit(txt_intentos , (650, 620))
         if opcion_b == True: 
            screen.blit(txt_respuesta_correcta , (0 , 600))
            pygame.draw.rect(screen , color_rect_a , boton_a , border_radius=0)
            pygame.draw.rect(screen , color_rect_c , boton_c , border_radius=0)
         else:
            if opcion_b_incorrecta == True:
               screen.blit(txt_respuesta_incorrectab , (0 , 600))
               pygame.draw.rect(screen , color_rect_b , boton_b , border_radius=0)
               screen.blit(txt_intentos , (650, 620))
         if opcion_c == True:
            screen.blit(txt_respuesta_correcta , (0 , 600))
            pygame.draw.rect(screen , color_rect_a , boton_a , border_radius=0)
            pygame.draw.rect(screen , color_rect_b , boton_b , border_radius=0)
         else:
            if opcion_c_incorrecta == True:
               screen.blit(txt_respuesta_incorrectac , (0 , 600))
               pygame.draw.rect(screen , color_rect_c , boton_c , border_radius=0)
               screen.blit(txt_intentos , (650, 620))
         if reinicio == True: 
            screen.blit(txt_ingreso , (170,650 ))
            text_nombre = font.render(mi_texto, True, (0, 0, 0))
            screen.blit(text_nombre, (570 , 650))
   elif juega == False:
         screen.blit(imagen_menu , (0, 0))
         sonido_menu.play()
         pygame.draw.rect(screen , color ,boton1, border_radius= 10)
         screen.blit(txt_jugar, (455, 110))
         pygame.draw.rect(screen , color_rect1 , boton2 , border_radius= 10)
         screen.blit(txt_puntaje, (393,190))
         pygame.draw.rect(screen , color_rect2 , boton3 , border_radius= 10)
         screen.blit(txt_salir, (460 , 270))
   else:
      if puntajes == True:
         sonido_menu.stop()
         screen.blit(imagen_puntaje , (0, 0))
         mostrar_puntajes(screen) 
         pygame.draw.rect(screen , color_rect_volver ,boton_volver, border_radius= 10)
         screen.blit(txt_volver , (10,659)) 
   pygame.display.flip()