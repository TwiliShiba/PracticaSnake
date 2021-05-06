Practica #2. Herramientas Computacionales.

Equipo 2.

Andrés Adrián Yarte Villaseñor    A00829535

María Teresa Angulo Tello         A00825411

En esta práctica se implementaron algunas funcionalidades
adicionales al código de Snake de Free Python Games. El 
juego original puede encontrarse en el siguiente link:

http://www.grantjenks.com/docs/freegames/snake.html

La primera funcionalidad fue hacer que la serpiente lograra
dar una vuelta al canvas, al llegar al borde de arriba, abajo,
izquierda o derecha.
Esto se realizó con condiciones para verificar si la serpiente se encontraba
dentro del área delimitada o no. De no hacerlo, la cabeza sale del lado opuesto.

La segunda funcionalidad fue lograr que al correr el programa, los
colores de la serpiente y la comida se inicializaran de manera aleatoria
sin que el color de ambos se repitiera.
Para esto, se creó un array con todos los colores disponibles y la función
randrange para elegir de manera aleatoria los colores.

La tercera funcionalidad fue hacer que la comida "escapara" de la serpiente,
moviéndose una vez cada medio segundo, hacia arriba, abajo, izquierda o derecha,
de manera aleatoria.
Se utilizó la función randrange y condicionales para determinar a dónde iría
la comida.

Aprendimos cómo se puede hacer uso de los vectores dentro de turtle graphics de manera
más detallada y cómo cambiar el movimiento de algunos objetos con el input de nuestro
teclado, a través de la modificación del famoso "Snake Game".