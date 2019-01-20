
# Classe Graphe

Voici le squelette de la classe Graphe que vous allez compléter au fur et à mesure de notre apprentissage.


```python
from graphviz import Graph
from dataclasses import dataclass
from typing import Dict, Set
 
 
@dataclass
class Graphe:
        """
        On définit un graphe à l'aide du dictionnaire des adjacents
        Par exemple :
        g = Graphe({{'1': {'2', '4', '3'}, '2': {'3'}, '3': {'4'}}})
        """
        dict_adj: Dict[str, Set[str]]
                
        def sommets(self) -> Set[str]:
                """
                Donne l'ensemble des sommets
                """
                s = set(self.dict_adj.keys())
                for v in self.dict_adj.values():
                                s |= v
                return s
        
        def adjacents(self, a):
                """
                Méthode pour avoir l'ensemble des adjacents d'un sommet
                """
                s = set([])
                if a in self.sommets():
                        if a in self.dict_adj:
                                s = set(self.dict_adj[a])
                        for v in self.dict_adj:
                                if a in self.dict_adj[v]:
                                        s |= {v}
                return s
        
        def __repr__(self):
                """ Affichage dans le terminal"""
                r = ''
                for v in sorted(list(self.sommets())):
                        r += ('\t' + v + ' -> { ')
                        for u in sorted(list(self.adjacents(v))):
                                r += (u + ' ')
                        r += '}\n'
                return r
                
        def dot(self, name: str = 'graphe') -> None:
                """
                Sortie graphique, ici au format PNG, à l'aide de Graphviz
                """
                d = Graph()
                d.node_attr.update(style='filled', color="#00ff005f")
                for v in self.dict_adj:
                        d.node(v)
                        for u in self.dict_adj[v]:
                                d.edge(v, u)
                d.render(name, view=True)#, format='png')
```


```python
g = Graphe({'1': {'2', '4', '3'}, '2': {'3'}, '3': {'4'}})
```


```python
g
```




    	1 -> { 2 3 4 }
    	2 -> { 1 3 }
    	3 -> { 1 2 4 }
    	4 -> { 1 3 }




```python
g.dot('graphe1')
```

### Exercice 1

Ajoutez une méthode `degre(self, a)` qui renvoie le degré d'un sommet `a` dans le graphe `self`. Vous pourrez regarder l'aide de `len` 


```python
?len
```


    [0;31mSignature:[0m [0mlen[0m[0;34m([0m[0mobj[0m[0;34m,[0m [0;34m/[0m[0;34m)[0m[0;34m[0m[0m
    [0;31mDocstring:[0m Return the number of items in a container.
    [0;31mType:[0m      builtin_function_or_method



### Exercice 2

Ajoutez une méthode `score(self)` qui renvoie le score d'un graphe `self` sous la forme d'un ensemble (`set`)


```python
?set
```


    [0;31mInit signature:[0m [0mset[0m[0;34m([0m[0mself[0m[0;34m,[0m [0;34m/[0m[0;34m,[0m [0;34m*[0m[0margs[0m[0;34m,[0m [0;34m**[0m[0mkwargs[0m[0;34m)[0m[0;34m[0m[0m
    [0;31mDocstring:[0m     
    set() -> new empty set object
    set(iterable) -> new set object
    
    Build an unordered collection of unique elements.
    [0;31mType:[0m           type



### Exercice 3

Ajoutez une méthode `est_isole(self, a)` qui teste si un sommet `a` est isolé dans le graphe `self`.

### Exercice 4

Créez une fonction `complet(n)` qui crée un graphe complet d'ordre `n`. Créez une fonction `roue(n)` qui crée une roue d'ordre `n`. Créez une fonction `cube(n)` qui crée un $n$-cube

### Exercice 5

Créez une fonction `rand_graph(n)` qui crée un graphe de `n` sommets aléatoirement. On pourra utiliser les fonctions `randint` et `sample` du module `random`.



```python
from random import sample, randint

?sample
```


    [0;31mSignature:[0m [0msample[0m[0;34m([0m[0mpopulation[0m[0;34m,[0m [0mk[0m[0;34m)[0m[0;34m[0m[0m
    [0;31mDocstring:[0m
    Chooses k unique random elements from a population sequence or set.
    
    Returns a new list containing elements from the population while
    leaving the original population unchanged.  The resulting list is
    in selection order so that all sub-slices will also be valid random
    samples.  This allows raffle winners (the sample) to be partitioned
    into grand prize and second place winners (the subslices).
    
    Members of the population need not be hashable or unique.  If the
    population contains repeats, then each occurrence is a possible
    selection in the sample.
    
    To choose a sample in a range of integers, use range as an argument.
    This is especially fast and space efficient for sampling from a
    large population:   sample(range(10000000), 60)
    [0;31mFile:[0m      ~/anaconda3/lib/python3.7/random.py
    [0;31mType:[0m      method




```python
?randint
```


    [0;31mSignature:[0m [0mrandint[0m[0;34m([0m[0ma[0m[0;34m,[0m [0mb[0m[0;34m)[0m[0;34m[0m[0m
    [0;31mDocstring:[0m
    Return random integer in range [a, b], including both end points.
            
    [0;31mFile:[0m      ~/anaconda3/lib/python3.7/random.py
    [0;31mType:[0m      method



Vous pourrez utiliser la construction par compréhension, par exemple:


```python
[str(k) for k in range(10)]
```




    ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']




```python
rand_graph(5)
```




    	0 -> { 1 2 3 4 }
    	1 -> { 0 1 3 4 }
    	2 -> { 0 4 }
    	3 -> { 0 1 3 4 }
    	4 -> { 0 1 2 3 }



### Exercice 6

Vérifiez sur des graphes aléatoires le théorème des poignées de main. Pour tester la parité, on pourra utiliser l'opérateur `%`

### Exercice 7

Créez une méthode `est_regulier` qui vérifie si un graphe est régulier. 
