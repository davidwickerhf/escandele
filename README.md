# Esercizio Candele

Sia data una stanza quadrata di dimensione N. Dentro la stanza ci sono una o più candele con intensità
luminosa L. La luce delle candele perde di intensità (L-1) ogni posizione. Se un punto della stanza riceve
luce da più di una candela, prenderà il valore maggiore disponibile tra le due candele. Ogni punto ha di
base luce 0.
Quanti punti bui (con luce 0) della stanza ci sono?

N = 5  | L = 3
- X X X X X
- X C X X X
- X X X X X
- X X X X X
- X X X X X

Output:
- 2 2 2 1 0
- 2 3 2 1 0
- 2 2 2 1 0
- 1 1 1 1 0
- 0 0 0 0 0

**Tempo di risoluzione: Circa 1 ora e 10 minuti**

## Utilizzo
#### PARTENDO DA UNA MATRICE
```python
from escandele import Room

room_matrix = [['x', 'x', 'x', 'x', 'x'], ['X', 'C', 'X', 'X', 'X'], ['x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'x']]
light_strengh = 3

# Inizializza Oggetto Stanza
room = Room(room=room_matrix, l=light_strengh)
```

#### PARTENDO DALLA DIMENSIONE & I PUNTI LUCE
```python
from escandele import Room

# Inizializza Oggetto Stanza
room = Room.from_coords(n=5, lights=[(0, 0), (4,4)], l=3)
```

#### OGGETTO STANZA
- ```room.empty_spots``` -> Lista di oggetti Spot con luce pari a 0