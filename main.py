import pygame
import random
import sys

# 1. Inicializar Pygame CE
pygame.init()

# 2. Configurar la pantalla
ANCHO = 600
ALTO = 400
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mi Primer Juego con Pygame CE")

# 3. Colores (RGB)
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
BLANCO = (255, 255, 255)

# 4. Configurar el Jugador (cuadrado verde)
tamano_jugador = 30
jugador_x = ANCHO // 2
jugador_y = ALTO // 2
velocidad = 5

# 5. Configurar la Comida (cuadrado rojo)
tamano_comida = 20
comida_x = random.randint(0, ANCHO - tamano_comida)
comida_y = random.randint(0, ALTO - tamano_comida)

# 6. Puntuación y reloj
puntuacion = 0
pygame.font.init()
fuente = pygame.font.SysFont("arial", 24)
reloj = pygame.time.Clock()

# 7. Bucle principal del juego
jugando = True
while jugando:
    # a) Control de eventos (Cerrar la ventana)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False

    # b) Capturar teclas presionadas para mover al jugador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and jugador_x > 0:
        jugador_x -= velocidad
    if teclas[pygame.K_RIGHT] and jugador_x < ANCHO - tamano_jugador:
        jugador_x += velocidad
    if teclas[pygame.K_UP] and jugador_y > 0:
        jugador_y -= velocidad
    if teclas[pygame.K_DOWN] and jugador_y < ALTO - tamano_jugador:
        jugador_y += velocidad

    # c) Crear rectángulos para detectar colisiones
    rect_jugador = pygame.Rect(jugador_x, jugador_y, tamano_jugador, tamano_jugador)
    rect_comida = pygame.Rect(comida_x, comida_y, tamano_comida, tamano_comida)

    # d) Colisión: si el jugador toca la comida
    if rect_jugador.colliderect(rect_comida):
        puntuacion += 1
        comida_x = random.randint(0, ANCHO - tamano_comida)
        comida_y = random.randint(0, ALTO - tamano_comida)

    # e) Dibujar elementos en la pantalla
    pantalla.fill(NEGRO)  # Limpiar fondo

    pygame.draw.rect(pantalla, VERDE, rect_jugador)  # Jugador
    pygame.draw.rect(pantalla, ROJO, rect_comida)    # Comida

    # Mostrar puntuación
    texto = fuente.render(f"Puntos: {puntuacion}", True, BLANCO)
    pantalla.blit(texto, (10, 10))

    # f) Actualizar la pantalla
    pygame.display.flip()

    # g) Controlar los FPS (60 fotogramas por segundo)
    reloj.tick(60)

# Finalizar Pygame
pygame.quit()
sys.exit()