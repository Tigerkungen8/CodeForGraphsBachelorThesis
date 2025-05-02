import tkinter as tk
import random

# Define constants
CANVAS_WIDTH = 600
CANVAS_HEIGHT = 600
BALL_RADIUS = 20
BALL_COLORS = ["red", "green", "blue", "orange", "purple"]
BALL_SPEED = 2
NEW_BALL_INTERVAL = 1000  # in milliseconds
GAME_DURATION = 60  # 60 seconds

class CatchTheBallGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Catch the Ball")

        # Create Canvas widget
        self.canvas = tk.Canvas(self.root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
        self.canvas.pack()

        # Initialize score and game end flag
        self.score = 0
        self.game_over = False

        # Create a list to store ball objects
        self.balls = []

        # Create a Timer to generate new balls at regular intervals
        self.root.after(NEW_BALL_INTERVAL, self.create_ball)

        # Create a label to display the score and timer
        self.info_label = tk.Label(self.root, text="Score: 0 | Time: 60 seconds", font=("Helvetica", 14))
        self.info_label.pack()

        # Bind mouse click event to the Canvas
        self.canvas.bind("<Button-1>", self.catch_ball)

        # Initialize the timer
        self.timer = GAME_DURATION
        self.update_timer()

    def create_ball(self):
        if not self.game_over:
            x = random.randint(BALL_RADIUS, CANVAS_WIDTH - BALL_RADIUS)
            y = -BALL_RADIUS
            color = random.choice(BALL_COLORS)
            ball = self.canvas.create_oval(x - BALL_RADIUS, y - BALL_RADIUS, x + BALL_RADIUS, y + BALL_RADIUS, fill=color)
            self.balls.append(ball)
            self.move_ball(ball)
            self.root.after(NEW_BALL_INTERVAL, self.create_ball)

    def move_ball(self, ball):
        if not self.game_over and ball in self.balls:
            self.canvas.move(ball, 0, BALL_SPEED)
            x1, y1, x2, y2 = self.canvas.coords(ball)
            if y2 > CANVAS_HEIGHT:
                self.remove_ball(ball)
                self.decrement_score()

            # Continue moving the ball
            self.root.after(10, self.move_ball, ball)

    def remove_ball(self, ball):
        if ball in self.balls:
            self.balls.remove(ball)
            self.canvas.delete(ball)

    def catch_ball(self, event):
        if not self.game_over:
            x, y = event.x, event.y
            for ball in self.balls:
                x1, y1, x2, y2 = self.canvas.coords(ball)
                if x1 < x < x2 and y1 < y < y2:
                    self.remove_ball(ball)
                    self.increment_score()

    def increment_score(self):
        if not self.game_over:
            self.score += 1
            self.info_label.config(text=f"Score: {self.score} | Time: {self.timer} seconds")

    def decrement_score(self):
        if not self.game_over and self.score > 0:
            self.score -= 1
            self.info_label.config(text=f"Score: {self.score} | Time: {self.timer} seconds")

    def update_timer(self):
        if not self.game_over:
            self.timer -= 1
            self.info_label.config(text=f"Score: {self.score} | Time: {self.timer} seconds")
            if self.timer == 0:
                self.end_game()
            else:
                self.root.after(1000, self.update_timer)

    def end_game(self):
        self.game_over = True
        self.info_label.config(text=f"Game Over | Final Score: {self.score}")

if __name__ == "__main__":
    root = tk.Tk()
    game = CatchTheBallGame(root)
    root.mainloop()
