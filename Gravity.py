import pygame
import math
import sys

# --- Setup ---
pygame.init()
WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gravity Sandbox")
clock = pygame.time.Clock()

# --- Colors ---
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (180, 180, 180)
RED = (200, 50, 50)
BLUE = (100, 149, 237)

# --- Constants ---
TIME_STEP = 0.05

# --- Planet class ---
class Planet:
    def __init__(self, x, y, mass, radius, color, vel=(0,0)):
        self.x = float(x)
        self.y = float(y)
        self.mass = mass
        self.radius = radius
        self.color = color
        self.vx, self.vy = vel
        self.trail = []

    def draw(self, win):
        # Draw trail
        for i, pos in enumerate(self.trail):
            pygame.draw.circle(win, self.color, (int(pos[0]), int(pos[1])), max(1, self.radius//5))
        pygame.draw.circle(win, self.color, (int(self.x), int(self.y)), self.radius)

    def update(self, planets, G):
        ax, ay = 0.0, 0.0
        for p in planets:
            if p == self:
                continue
            dx = p.x - self.x
            dy = p.y - self.y
            dist2 = dx*dx + dy*dy
            if dist2 == 0:
                continue
            dist = math.sqrt(dist2)

            # Gravity only (no collision)
            force = G * p.mass / dist2
            ax += force * (dx / dist)
            ay += force * (dy / dist)

        # Update velocity & position
        self.vx += ax * TIME_STEP
        self.vy += ay * TIME_STEP
        self.x += self.vx * TIME_STEP
        self.y += self.vy * TIME_STEP

        # Add to trail
        self.trail.append((self.x, self.y))
        if len(self.trail) > 30:
            self.trail.pop(0)

        # Update color based on mass & velocity
        speed = math.sqrt(self.vx**2 + self.vy**2)
        intensity = min(255, int(self.mass/2 + speed*5))
        self.color = (intensity, 50, 255-intensity)

# --- Slider class ---
class Slider:
    def __init__(self, x, y, w, min_val, max_val, start_val, label):
        self.x = x
        self.y = y
        self.w = w
        self.min_val = min_val
        self.max_val = max_val
        self.value = start_val
        self.knob_x = x + (start_val - min_val) / (max_val - min_val) * w
        self.dragging = False
        self.label = label

    def draw(self, win):
        pygame.draw.line(win, GREY, (self.x, self.y), (self.x+self.w, self.y), 4)
        pygame.draw.circle(win, WHITE, (int(self.knob_x), self.y), 10)
        font = pygame.font.SysFont(None, 24)
        text = font.render(f"{self.label}: {int(self.value)}", True, WHITE)
        win.blit(text, (self.x + self.w + 20, self.y-12))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if abs(event.pos[0] - self.knob_x) < 15 and abs(event.pos[1] - self.y) < 15:
                self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION and self.dragging:
            self.knob_x = max(self.x, min(event.pos[0], self.x+self.w))
            self.value = self.min_val + (self.knob_x - self.x) / self.w * (self.max_val - self.min_val)

# --- Simulation ---
planets = []
dragging = False
temp_start = None
temp_planet = None

# --- Sliders ---
size_slider = Slider(50, HEIGHT-120, 200, 5, 50, 15, "Size")       # left-bottom
mass_slider = Slider(50, HEIGHT-80, 200, 5, 2000, 225, "Mass")     # below size
gravity_slider = Slider(350, HEIGHT-80, 200, 1, 300, 100, "Gravity") # moved farther right



def main():
    global dragging, temp_start, temp_planet
    running = True
    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Handle sliders
            size_slider.handle_event(event)
            mass_slider.handle_event(event)
            gravity_slider.handle_event(event)

            # Place new planet
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[1] < HEIGHT-100:
                    temp_start = event.pos
                    x, y = temp_start
                    radius = int(size_slider.value)
                    mass = mass_slider.value
                    temp_planet = Planet(x, y, mass=mass, radius=radius, color=BLUE)
                    planets.append(temp_planet)
                    dragging = True

            elif event.type == pygame.MOUSEBUTTONUP and dragging:
                end_pos = pygame.mouse.get_pos()
                dx = end_pos[0] - temp_start[0]
                dy = end_pos[1] - temp_start[1]
                temp_planet.vx = dx * 0.1
                temp_planet.vy = dy * 0.1
                dragging = False
                temp_planet = None

            # Reset
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    planets.clear()

        # Drag line preview
        if dragging and temp_planet:
            start_x, start_y = temp_start
            cur_x, cur_y = pygame.mouse.get_pos()
            pygame.draw.line(screen, RED, (start_x, start_y), (cur_x, cur_y), 2)

        # Update and draw planets
        for p in planets[:]:
            p.update(planets, gravity_slider.value)
            p.draw(screen)

        # Draw sliders
        size_slider.draw(screen)
        mass_slider.draw(screen)
        gravity_slider.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
