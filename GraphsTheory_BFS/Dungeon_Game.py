# Rif: https://www.youtube.com/watch?v=LbC0ejgACkE
# Rif: https://www.youtube.com/watch?v=9PC2r6MAw1Q
# Si affronta Dungeon Game Problem:
"""
A   B   C
D   E   F
G   H   I

La principesa si trova in "I", io parto da "A".
In ogni casella ho un valore positivo o negativo che mi rappresenta la salute.
Devo trovare la principessa senza che la mia salute si azzeri.

Valori:
-2       -3      +3
-5       -10     +1
+10      +30     -5

La principessa si trova a "-5".
Io parto da "-2".

- Partendo dall'inizio, devo entrare con un MINIMO di salute +3 altrimenti vado subito
>= 0 dopo che combatto con il demone -2.
- Successivamente mi possono muovere solo verso sotto o verso destra.
- Ovviamente la dimensione iniziale non dipende solo dalla prima room, ma anche dalle successive,
che determinano la quantità di salute.
- Devo arrivare con il minimo valore di salute alla fine (shortest path)

Partiamo dalla fine:
- Ho -5, voglio il minimo sopravvissuto.
- Quindi dopo il combattimento mi deve rimanere 1.
- X - 5 = 1 => X = +6

Ora posso entrare in questa ultima stanza o da sopra (+1) o da sinistra (+30)
Per entrambi posso usare lo stesso ragionamento, poiche devo uscire con +6.
Se entro da sopra:
- X + 1 = 6 => X = +5

Se entro da sinistra:
- X + 30 = 6 => X = -24 (ERROR, non posso entrare in una stanza con salute negativa)
Prendo pertanto X = 1, che è il minimo valore accettabile per entrare in questa stanza (2,1), anche se
questo mi genererà un surplus finale.

Ora siamo sul nodo (1,1) e posso spostarmi verso sotto o verso sinistra:
- verso sinistra: X - 10 = 5 => X = 15
- verso giu: X - 10 = 1 => X = 11

Ovviamente prendo il valore più basso, 11.
Inserisco 11 nella cella (1,1)

Ora vado nella cella (2, 0):
- Ho X + 10 = 1 => X = -9 NON è POSSIBILE, quindi assegno il minimo valore in (2,0) = 1.

Continuo il procedimento sulla (1,0):
- Verso giu = X - 5 = 1 => X = 6
- Verso destra: X - 5 = 11 => X = 16

Prendo quello minore e ottengo 6

Avrà una nuova matrice:

7   5   2
6   11  5
1   1   6

"""

import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List

class Solution:

    # Iterative 1
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])

        dp = [[float("inf")] * (n+1) for _ in range(m+1)]
        dp[m][n-1] = 1
        dp[m-1][n] = 1

        for i in reversed(range(m)):
            for j in reversed((range(n))):
                needed = min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j]

                if needed < 1:  # Case if we have extra life
                    needed = 1

                dp[i][j] = needed

        return dp[0][0]


# Utilizzo la classe tester per lanciarlo.
class tester(unittest.TestCase):
    def test1(self):
        dungeon = [[-2, -3, 3],
                   [-5, -10, 1],
                   [10, 30, -5]]

        Output = 7
        self.assertEqual(Output, Solution().calculateMinimumHP(dungeon))
