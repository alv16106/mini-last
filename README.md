# Algoritmos genéticos
Rodrigo Alvarado - 16106

Javier Ramos - 16230

## Problema elegido
### <b> Algoritmos genéticos, criaturas aprendiendo a comer</b>
En la aplicación investigada, se le esta enseñando a criaturas generadas de manera randomizada, como alcanzar un pedazo de comida. Para esto no solo deben moverse, sino tambien girar y tocar la comida con una de sus extremidades.
### Alelos
Las criaturas estan compuestas de nodos y articulaciones, los alelos son:
* Numero de articulaciones
* Largo de las conexiones
* Fuerza de las conexiones
* Cantidad de neuronas en el cerebro
* Forma de las neuronas
* Peso de cada axion
### Genoma
El genoma esta definido como un objeto dentro del programa de Processing, que se ve asi:
```
ArrayList<Node> n;
ArrayList<Muscle> m;
float d;
int id;
boolean alive;
float creatureTimer;
float mutability;
Brain brain;
int[] name;
```
### Fenotipo
El fenotipo son el numero de nodos, numero de conexiones y su fuerza, que se aprecia en el color y grosor de las conexiones.
### Fitness
Se da un punto por cada comida que la criatura logra alcanzar y se da una fraccion de punto dependiendo de que tan cerca esta la 
criatura de la siguiente comida que spawneo, todo esto en un intervalo de 15 segundos.
### Criterios de selección
Se inicia con grupos de 100 criaturas. Se seleccionan las 50 criaturas que obtienen el mayor puntaje y se eliminan las 50 que tienen el menor0
### Criterio de cruce
Las criaturas se mezclan de manera aleatoria entre las que lograron pasar el filtro.
### Criterios de mutación
Cada criatura cuenta con un float que determina que tan mutable es, esa mutabilidad permite que los hijos tengan variacion genetica, mientras más alto este número, mas cambios pueden suceder en la proxima iteración

 

### Sources:
https://www.youtube.com/watch?v=ghwXmA1s1I4
https://github.com/carykh/evolutionSteer