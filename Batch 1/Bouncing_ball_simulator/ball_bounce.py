
"""
Bouncing Ball Simulator
A fun physics simulation of bouncing balls with gravity
Use ESC to quit, SPACE to add more balls, R to reset
"""

import pygame
import time
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions and settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (30, 30, 60)  # Deep blue night sky
FPS = 60

# Initialize display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('🏀 Bouncing Ball Simulator - Press SPACE to add balls, R to reset, ESC to quit')
clock = pygame.time.Clock()

class BouncingBall:
    """A colorful ball that bounces around the screen with realistic physics"""
    
    # Physics constants
    GRAVITY = 0.5  # How fast balls fall
    BOUNCE_DAMPING = 0.85  # Energy loss on bounce (makes it more realistic)
    
    def __init__(self):
        """Create a new ball with random properties"""
        # Random starting position (avoid edges)
        self.x = random.randint(50, SCREEN_WIDTH - 50)
        self.y = random.randint(50, SCREEN_HEIGHT // 2)
        
        # Random velocity for interesting movement
        self.velocity_x = random.randint(-8, 8)
        self.velocity_y = random.randint(-5, 5)
        
        # Random size and color for variety
        self.radius = random.randint(10, 25)
        self.color = (
            random.randint(100, 255),  # Red
            random.randint(100, 255),  # Green
            random.randint(100, 255)   # Blue
        )
    
    def update_position(self):
        """Update ball position based on physics"""
        # Apply gravity (balls fall down naturally)
        self.velocity_y += self.GRAVITY
        
        # Update position based on velocity
        self.x += self.velocity_x
        self.y += self.velocity_y
        
        # Bounce off walls with energy loss
        if self.x <= self.radius or self.x >= SCREEN_WIDTH - self.radius:
            self.velocity_x *= -self.BOUNCE_DAMPING
            # Keep ball inside screen
            self.x = max(self.radius, min(SCREEN_WIDTH - self.radius, self.x))
        
        # Bounce off floor and ceiling
        if self.y <= self.radius:
            self.velocity_y *= -self.BOUNCE_DAMPING
            self.y = self.radius
        elif self.y >= SCREEN_HEIGHT - self.radius:
            self.velocity_y *= -self.BOUNCE_DAMPING
            self.y = SCREEN_HEIGHT - self.radius
    
    def draw(self, surface):
        """Draw the ball on the screen with a nice visual effect"""
        # Draw main ball
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)
        
        # Add a highlight for 3D effect
        highlight_color = tuple(min(255, c + 60) for c in self.color)
        pygame.draw.circle(surface, highlight_color, 
                         (int(self.x - self.radius//3), int(self.y - self.radius//3)), 
                         self.radius//3)
def create__balls(count=5):
    """Create a list of bouncing balls to start the simulation"""
    return [BouncingBall() for _ in range(count)]

def draw_instructions(surface):
    """Draw helpful instructions on screen"""
    font = pygame.font.Font(None, 24)
    instructions = [
        "SPACE: Add more balls",
        "R: Reset simulation", 
        "ESC: Quit"
    ]
    
    for i, instruction in enumerate(instructions):
        text = font.render(instruction, True, (255, 255, 255))
        surface.blit(text, (10, 10 + i * 25))

def main():
    """Main game loop with user interaction"""
    # Create initial balls
    ball_list = create_initial_balls(10)
    
    # Game loop
    running = True
    
    print("🏀 Bouncing Ball Simulator Started!")
    print("Controls: SPACE = Add balls, R = Reset, ESC = Quit")
    
    while running:
        # Handle user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SPACE:
                    # Add a new ball
                    ball_list.append(BouncingBall())
                    print(f"Added ball! Total balls: {len(ball_list)}")
                elif event.key == pygame.K_r:
                    # Reset simulation
                    ball_list = create_initial_balls(5)
                    print("Simulation reset!")
        
        # Clear screen with gradient-like background
        screen.fill(BACKGROUND_COLOR)
        
        # Update and draw all balls
        for ball in ball_list:
            ball.update_position()
            ball.draw(screen)
        
        # Draw instructions
        draw_instructions(screen)
        
        # Draw ball counter
        font = pygame.font.Font(None, 36)
        ball_count_text = font.render(f"Balls: {len(ball_list)}", True, (255, 255, 255))
        screen.blit(ball_count_text, (SCREEN_WIDTH - 150, 10))
        
        # Update display
        pygame.display.flip()
        clock.tick(FPS)  # Maintain smooth 60 FPS
    
    print("Thanks for playing! 🎮")
    pygame.quit()
    sys.exit()

# Run the simulation
if __name__ == "__main__":
    main()