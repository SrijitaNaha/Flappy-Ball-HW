import pgzrun
from random import randint, uniform

# Constants
TITLE = 'Flappy Ball'
WIDTH, HEIGHT = 800, 600
GRAVITY = 2000.0  # pixels per second per second
MIN_BALL_RADIUS = 20
MAX_BALL_RADIUS = 60

# Colors
def random_color():
    return (randint(0, 255), randint(0, 255), randint(0, 255))

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = uniform(-200, 200)
        self.vy = 0
        self.radius = randint(MIN_BALL_RADIUS, MAX_BALL_RADIUS)
        self.color = random_color()
        self.bounciness = uniform(0.5, 0.9)

    def draw(self):
        screen.draw.filled_circle((self.x, self.y), self.radius, self.color)

    def update(self, dt):
        # Apply constant acceleration formulae
        uy = self.vy
        self.vy += GRAVITY * dt
        self.y += (uy + self.vy) * 0.5 * dt

        # detect and handle bounce
        if self.y > HEIGHT - self.radius:  # we've bounced!
            self.y = HEIGHT - self.radius  # fix the position
            self.vy = -self.vy * self.bounciness  # inelastic collision

        # X component doesn't have acceleration
        self.x += self.vx * dt
        if self.x > WIDTH - self.radius or self.x < self.radius:
            self.vx = -self.vx

def draw():
    screen.clear()
    for ball in balls:
        ball.draw()

def update(dt):
    for ball in balls:
        ball.update(dt)

def on_key_down(key):
    """Pressing a key will kick the balls upwards."""
    if key == keys.SPACE:
        for ball in balls:
            ball.vy = -500

balls = [Ball(randint(50, WIDTH - 50), randint(50, HEIGHT - 50)) for _ in range(10)]

pgzrun.go()