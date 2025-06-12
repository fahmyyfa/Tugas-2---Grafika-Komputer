import pygame
import sys

# Inisialisasi
pygame.init()

# Ukuran layar
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aplikasi Gambar")

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
colors = {
    'black': (0, 0, 0),
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255)
}

# Mode gambar
modes = ['dot', 'free', 'line', 'rect', 'circle', 'ellipse']
current_mode = 'dot'
current_color = BLACK
start_pos = None

# Font
font = pygame.font.SysFont(None, 30)

# Tombol mode
def draw_mode_buttons():
    for i, mode in enumerate(modes):
        label = font.render(mode.capitalize(), True, BLACK)
        screen.blit(label, (10, 10 + i * 30))

# Tombol warna
def draw_color_buttons():
    for i, (name, color) in enumerate(colors.items()):
        pygame.draw.rect(screen, color, (WIDTH - 70, 10 + i * 50, 40, 40))

# Cek klik pada tombol mode
def get_mode_click(pos):
    for i, mode in enumerate(modes):
        rect = pygame.Rect(10, 10 + i * 30, 100, 30)
        if rect.collidepoint(pos):
            return mode
    return None

# Cek klik pada tombol warna
def get_color_click(pos):
    for i, (name, color) in enumerate(colors.items()):
        rect = pygame.Rect(WIDTH - 70, 10 + i * 50, 40, 40)
        if rect.collidepoint(pos):
            return color
    return None

# Gambar bentuk
def draw_shape(surface, end_pos):
    global start_pos
    if current_mode == 'line' and start_pos:
        pygame.draw.line(surface, current_color, start_pos, end_pos, 2)
    elif current_mode == 'rect' and start_pos:
        x, y = start_pos
        w, h = end_pos[0] - x, end_pos[1] - y
        pygame.draw.rect(surface, current_color, pygame.Rect(x, y, w, h), 2)
    elif current_mode == 'circle' and start_pos:
        x, y = start_pos
        radius = int(((end_pos[0] - x) ** 2 + (end_pos[1] - y) ** 2) ** 0.5)
        pygame.draw.circle(surface, current_color, (x, y), radius, 2)
    elif current_mode == 'ellipse' and start_pos:
        x1, y1 = start_pos
        x2, y2 = end_pos
        rect = pygame.Rect(min(x1,x2), min(y1,y2), abs(x2-x1), abs(y2-y1))
        pygame.draw.ellipse(surface, current_color, rect, 2)
    elif current_mode == 'dot':
        pygame.draw.circle(surface, current_color, end_pos, 2)
    elif current_mode == 'free':
        pygame.draw.circle(surface, current_color, end_pos, 2)

# UI
def draw_ui():
    draw_mode_buttons()
    draw_color_buttons()

# Main
def main():
    global current_mode, current_color, start_pos

    canvas = pygame.Surface((WIDTH, HEIGHT))
    canvas.fill(WHITE)

    running = True
    drawing = False

    while running:
        screen.blit(canvas, (0, 0))
        draw_ui()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                color_clicked = get_color_click(event.pos)
                if color_clicked:
                    current_color = color_clicked
                    continue

                mode_clicked = get_mode_click(event.pos)
                if mode_clicked:
                    current_mode = mode_clicked
                    continue

                if current_mode in ['line', 'rect', 'circle', 'ellipse']:
                    start_pos = event.pos
                elif current_mode in ['dot', 'free']:
                    draw_shape(canvas, event.pos)
                    drawing = True

            elif event.type == pygame.MOUSEBUTTONUP:
                if current_mode in ['line', 'rect', 'circle', 'ellipse'] and start_pos:
                    draw_shape(canvas, event.pos)
                    start_pos = None
                elif current_mode == 'free':
                    drawing = False

            elif event.type == pygame.MOUSEMOTION:
                if drawing and current_mode == 'free':
                    draw_shape(canvas, event.pos)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
