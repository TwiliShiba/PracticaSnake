from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

colors = ['blue', 'black', 'purple', 'pink', 'brown']
"Guarda los colores para la serpiente y la comida"
rand = randrange(0, 5)
snake_color = colors[rand]
colors.pop(rand)
rand = randrange(0, 4)
fruit_color = colors[rand]
"Nota: Todo esto asegura que los dos colores no sean iguales"

def change(x, y):
    "Change snake direction."
    "Cambia la dirección de la serpiente"
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    "La función retorna un valor True o False dependiendo de si la"
    "cabeza de la serpiente se encuentra dentro del área delimitada"
    return -200 < head.x < 190 and -200 < head.y < 190

def edges(head):
    "Lleva a la serpiente al lado opuesto del área delimitada"
    if head.x == -200:
        head.x = 190
    elif head.x == 190:
        head.x = -200
    elif head.y == 190:
        head.y = -200
    elif head.y == -200:
        head.y = 190

def move_food():
    "Mueve la comida un espacio en hacia arriba, abajo, izquierda o derecha"
    "de manera aleatorio"
    rand_move = randrange(0, 4)
    "Condición que determina hacia donde se moverá la serpiente, evitando"
    "que la comida vaya más allá del área delimitada"
    if rand_move == 0:
        if food.x == 190:
            food.x -= 10
        else:
            food.x += 10
    elif rand_move == 1:
        if food.x == -180:
            food.x += 10
        else:
            food.x -= 10
    elif rand_move == 2:
        if food.y == 190:
            food.y -= 10
        else:
            food.y += 10
    elif rand_move == 3:
        if food.y == -180:
            food.y += 10
        else:
            food.y -= 10
    
    ontimer(move_food, 500)

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    "Condición que revisa si la cabeza de la serpiente está sobre su cuerpo"
    "En caso de que sea verdadero, es un game over"
    if head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    "Si la serpiente no se encuentra dentro del área, se manda a llamar la función edges"
    if not inside(head):
        edges(head)

    snake.append(head)

    "Si la cabeza de la serpiente está en las mismas coordenadas de la serpiente, se imprime"
    "la longitud de la serpiente en la terminal y se reposiciona la comida al azar"
    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        "Quita el primer elemento del array serpiente si no se cumple la condición"
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, snake_color)

    square(food.x, food.y, 9, fruit_color)
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
bgcolor('#C5EEFA')
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
move_food()
done()