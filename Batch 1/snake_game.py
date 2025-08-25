
import tkinter as tk
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#AAD50E"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#222"
BORDER_COLOR = "#555"
GRID_COLOR = "#333"

class Snake:
    def __init__(self, canvas):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []
        for i in range(BODY_PARTS):
            self.coordinates.append([0, 0])
        for x, y in self.coordinates:
            square = self.create_rounded_rectangle(canvas, x, y, x + SPACE_SIZE, y + SPACE_SIZE, 10, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

    def create_rounded_rectangle(self, canvas, x1, y1, x2, y2, r=25, **kwargs):
        points = [x1+r, y1,
                  x2-r, y1,
                  x2, y1,
                  x2, y1+r,
                  x2, y2-r,
                  x2, y2,
                  x2-r, y2,
                  x1+r, y2,
                  x1, y2,
                  x1, y2-r,
                  x1, y1+r,
                  x1, y1]
        return canvas.create_polygon(points, smooth=True, **kwargs)

class Food:
    def __init__(self, canvas):
        x = random.randint(0, int(GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, int(GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x, y]
        self.draw_gradient_food(canvas, x, y)

    def draw_gradient_food(self, canvas, x, y):
        # Simulate gradient by drawing multiple ovals
        for i in range(10, 0, -1):
            color = f"#FF{hex(16*i)[2:].zfill(2)}{hex(16*i)[2:].zfill(2)}"
            canvas.create_oval(x+i, y+i, x+SPACE_SIZE-i, y+SPACE_SIZE-i, fill=color, outline="")
        canvas.create_oval(x+5, y+5, x+SPACE_SIZE-5, y+SPACE_SIZE-5, fill=FOOD_COLOR, tag="food", outline="")

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game - Enhanced UI")
        self.root.resizable(False, False)
        self.score = 0
        self.direction = 'down'
        self.setup_ui()
        self.reset_game()

    def setup_ui(self):
        self.label = tk.Label(self.root, text=f"Score: {self.score}", font=('Consolas', 32), bg="#444", fg="#FFF", pady=10)
        self.label.pack(fill=tk.X)
        self.canvas = tk.Canvas(self.root, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH, highlightthickness=0)
        self.canvas.pack(padx=10, pady=10)
        self.draw_border()
        self.draw_grid()
        self.restart_btn = tk.Button(self.root, text="Restart", font=('Consolas', 18), command=self.reset_game, bg="#AAD50E", fg="#222")
        self.restart_btn.pack(pady=5)
        self.root.bind('<Left>', lambda event: self.change_direction('left'))
        self.root.bind('<Right>', lambda event: self.change_direction('right'))
        self.root.bind('<Up>', lambda event: self.change_direction('up'))
        self.root.bind('<Down>', lambda event: self.change_direction('down'))

    def draw_border(self):
        self.canvas.create_rectangle(2, 2, GAME_WIDTH-2, GAME_HEIGHT-2, outline=BORDER_COLOR, width=6)

    def draw_grid(self):
        for i in range(0, GAME_WIDTH, SPACE_SIZE):
            self.canvas.create_line(i, 0, i, GAME_HEIGHT, fill=GRID_COLOR)
        for i in range(0, GAME_HEIGHT, SPACE_SIZE):
            self.canvas.create_line(0, i, GAME_WIDTH, i, fill=GRID_COLOR)

    def reset_game(self):
        self.canvas.delete("all")
        self.draw_border()
        self.draw_grid()
        self.score = 0
        self.direction = 'down'
        self.label.config(text=f"Score: {self.score}")
        self.snake = Snake(self.canvas)
        self.food = Food(self.canvas)
        self.game_running = True
        self.next_turn()

    def next_turn(self):
        if not self.game_running:
            return
        x, y = self.snake.coordinates[0]
        if self.direction == "up":
            y -= SPACE_SIZE
        elif self.direction == "down":
            y += SPACE_SIZE
        elif self.direction == "left":
            x -= SPACE_SIZE
        elif self.direction == "right":
            x += SPACE_SIZE
        self.snake.coordinates.insert(0, (x, y))
        square = self.snake.create_rounded_rectangle(self.canvas, x, y, x + SPACE_SIZE, y + SPACE_SIZE, 10, fill=SNAKE_COLOR, tag="snake")
        self.snake.squares.insert(0, square)
        if x == self.food.coordinates[0] and y == self.food.coordinates[1]:
            self.score += 1
            self.label.config(text=f"Score: {self.score}")
            self.canvas.delete("food")
            self.food = Food(self.canvas)
        else:
            del self.snake.coordinates[-1]
            self.canvas.delete(self.snake.squares[-1])
            del self.snake.squares[-1]
        if self.check_collisions():
            self.game_over()
        else:
            self.root.after(SPEED, self.next_turn)

    def change_direction(self, new_direction):
        if new_direction == 'left' and self.direction != 'right':
            self.direction = new_direction
        elif new_direction == 'right' and self.direction != 'left':
            self.direction = new_direction
        elif new_direction == 'up' and self.direction != 'down':
            self.direction = new_direction
        elif new_direction == 'down' and self.direction != 'up':
            self.direction = new_direction

    def check_collisions(self):
        x, y = self.snake.coordinates[0]
        if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
            return True
        for body_part in self.snake.coordinates[1:]:
            if x == body_part[0] and y == body_part[1]:
                return True
        return False

    def game_over(self):
        self.game_running = False
        self.canvas.create_rectangle(0, 0, GAME_WIDTH, GAME_HEIGHT, fill="#222", stipple="gray25", outline="")
        self.canvas.create_text(GAME_WIDTH/2, GAME_HEIGHT/2-40, font=('Consolas', 60, 'bold'), text="GAME OVER", fill="#FF3333", tag="gameover")
        self.canvas.create_text(GAME_WIDTH/2, GAME_HEIGHT/2+30, font=('Consolas', 32), text=f"Final Score: {self.score}", fill="#FFF", tag="gameover")

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()