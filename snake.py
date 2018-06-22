from tkinter import *
from random import randint


class Snake:
    head_x = 200
    head_y = 200
    food_x = randint(0, 79) * 5
    food_y = randint(0, 79) * 5
    head_dir = 'RIGHT'
    body = []
    body_pos = []
    score = 0
    ate_food = False
    game_over = False

    def __init__(self, w):
        # Create initial snake
        self.body.append(w.create_rectangle(
            self.head_x - 15, self.head_y, self.head_x - 10, self.head_y + 5, fill='black'))
        self.body_pos.append((self.head_x - 15, self.head_y))
        self.body.append(w.create_rectangle(
            self.head_x - 10, self.head_y, self.head_x - 5, self.head_y + 5, fill='black'))
        self.body_pos.append((self.head_x - 10, self.head_y))
        self.body.append(w.create_rectangle(self.head_x - 5, self.head_y, self.head_x, self.head_y + 5, fill='black'))
        self.body_pos.append((self.head_x - 5, self.head_y))
        self.body.append(w.create_rectangle(self.head_x, self.head_y, self.head_x+5, self.head_y + 5, fill='black'))
        self.body_pos.append((self.head_x, self.head_y))

        # Create initial food
        self.food = w.create_rectangle(self.food_x, self.food_y, self.food_x+5, self.food_y+5, fill='red')
        w.pack()
        print(self.body)

    def check_game_over(self, w):
        if self.head_x > 395 or self.head_x < 0 or self.head_y < 0 or self.head_y > 395 or\
                (self.head_x, self.head_y) in self.body_pos[:len(self.body_pos) - 1]:
            self.game_over = True
            # w.create_rectangle(100, 100, 300, 300, fill='white')
            button = Button(master, text='Quit', command=master.destroy)
            button.pack()

    def get_new_head(self):
        if self.head_dir == 'RIGHT':
            self.head_x += 5
        elif self.head_dir == 'LEFT':
            self.head_x -= 5
        elif self.head_dir == 'UP':
            self.head_y -= 5
        elif self.head_dir == 'DOWN':
            self.head_y += 5

    def check_food(self, w):
        if self.head_x == self.food_x and self.head_y == self.food_y:
            self.ate_food = True
            w.delete(self.food)
            self.score += 1
            self.food_x = randint(0, 79) * 5
            self.food_y = randint(0, 79) * 5
            self.food = w.create_rectangle(self.food_x, self.food_y, self.food_x + 5, self.food_y + 5, fill='red')
            w.pack()

    def draw(self, w):
        self.check_food(w)
        self.get_new_head()
        if self.ate_food:
            pass
        else:
            w.delete(self.body.pop(0))
            self.body_pos.pop(0)
        self.ate_food = False
        self.body.append(w.create_rectangle(self.head_x, self.head_y, self.head_x + 5, self.head_y + 5, fill='black'))
        self.body_pos.append((self.head_x, self.head_y))
        w.pack()
        self.check_game_over(w)

    def key_down(self, e):
        if e.keysym == 'Down' and self.head_dir != 'UP':
            self.head_dir = 'DOWN'
        if e.keysym == 'Up' and self.head_dir != 'DOWN':
            self.head_dir = 'UP'
        if e.keysym == 'Left' and self.head_dir != 'RIGHT':
            self.head_dir = 'LEFT'
        if e.keysym == 'Right' and self.head_dir != 'LEFT':
            self.head_dir = 'RIGHT'


master = Tk()
window = Canvas(master, width=400, height=400)
window.create_rectangle(0, 0, 400, 400, fill='green', outline='green')
text = Text(master, height=1, width=15)
text.insert(INSERT, "Score: ")
text.pack()
snake = Snake(window)
master.bind("<KeyPress>", snake.key_down)
while True:
    try:
        master.update_idletasks()
        master.update()
    except:
        print('Game Over')
        break
    if snake.game_over:
        pass
    else:
        text.delete('1.0', END)
        text.insert(END, 'Score: ' + str(snake.score))
        Tk.after(master, 100, snake.draw(window))
