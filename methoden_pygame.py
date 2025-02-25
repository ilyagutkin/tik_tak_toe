import pygame
import sys

# Pygame initialisieren
pygame.init()

# Fenstergröße und Titel
n = 5  # Größe des Gitters (n x n)
scroll_speed = 10  # Scrollgeschwindigkeit
scroll_y = 0  # Scrollposition
button_size = 100  # Größe der Buttons
screen_width = n * button_size
screen_height = n * button_size
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("n x n Button Grid")

# Farben definieren
weiß = (255, 255, 255)
blau = (0, 0, 255)
grau = (200, 200, 200)

# Methode zum Zeichnen eines Kreuzes
def draw_cross(x, y, size, color, surface):
    """Zeichnet ein Kreuz in der Mitte des gegebenen Feldes."""
    offset = size // 4  # Bestimmt die Größe der Linien
    pygame.draw.line(surface, color, (x + offset, y + offset), (x + size - offset, y + size - offset), 5)
    pygame.draw.line(surface, color, (x + size - offset, y + offset), (x + offset, y + size - offset), 5)

# Methode zum Zeichnen eines Kreises
def draw_circle(x, y, size, color=blau, surface=screen):
    """Zeichnet einen Kreis in der Mitte des gegebenen Feldes."""
    center = (x + size // 2, y + size // 2)  # Mittelpunkt des Buttons
    radius = size // 3  # Der Kreis hat etwa 2/3 der Feldgröße als Durchmesser
    pygame.draw.circle(surface, color, center, radius, 5)


# Funktion zum Zeichnen des Rasters und der Buttons
def draw_grid():
    for row in range(n):
        for col in range(n):
            x = col * button_size
            y = row * button_size
            pygame.draw.rect(screen, blau, (x, y, button_size, button_size), 3)
            pygame.draw.rect(screen, grau, (x + 5, y + 5, button_size - 10, button_size - 10))

# Funktion zum Überprüfen, ob auf einen Button geklickt wurde
def check_button_click(mouse_pos):
    x, y = mouse_pos
    col = x // button_size
    row = y // button_size
    if col < n and row < n:
        print(f"Button {row}, {col} wurde geklickt!")
        draw_circle(row,col,50)

# Hauptspiel-Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Linksklick
                check_button_click(event.pos)
            elif event.button == 4:  # Mausrad nach oben
                scroll_y = max(scroll_y + scroll_speed, 0)  # Begrenzung nach oben
            elif event.button == 5:  # Mausrad nach unten
                max_scroll = -(n * button_size - screen_height)
                scroll_y = min(scroll_y - scroll_speed, max_scroll)  # Begrenzung nach unten

        # Tastatur-Scrollen (Pfeiltasten ↑ ↓)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            scroll_y = max(scroll_y + scroll_speed, 0)
        if keys[pygame.K_DOWN]:
            max_scroll = -(n * button_size - screen_height)
            scroll_y = min(scroll_y - scroll_speed, max_scroll)
            
    # Bildschirm mit Weiß füllen
    screen.fill(weiß)

    # Gitter und Buttons zeichnen
    draw_grid()

    # Update des Fensters
    pygame.display.update()

    # FPS steuern
    pygame.time.Clock().tick(60)

