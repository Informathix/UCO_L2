# coding: utf-8

from graphviz import Graph
from dataclasses import dataclass
from typing import Dict, Set, List
 
 
@dataclass
class Graphe:
        """
        On définit un graphe à l'aide du dictionnaire des adjacents
        Par exemple :
        g = Graphe({'1': {'2', '4', '3'}, '2': {'3'}, '3': {'4'}})
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
        
        def adjacents(self, a: str) -> Set[str]:
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
        
        def __repr__(self) -> str:
                """ Affichage dans le terminal"""
                r = ''
                for v in sorted(list(self.sommets())):
                        r += ('\t' + v + ' -> { ')
                        for u in sorted(list(self.adjacents(v))):
                                r += (u + ' ')
                        r += '}\n'
                return r
            
        def degre(self, s: str) -> int :
            """
            Renvoie le nombre de sommets adjacents au sommet s dans le graphe g
            """
            return len(g.adjacents(s))
        
        def score(self) -> List[int]:
            sc = []
            # to sort : trier
            for s in sorted(list(self.sommets())):
                sc.append(self.degre(s))
            return sc
            
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



## Exercice 3
#
# Ajoutez une méthode est_isole(self, a) qui teste si un sommet
# a est isolé dans le graphe self.


## Exercice 4
#
# Créez une fonction complet(n) qui crée un graphe complet d'ordre n.
# Créez une fonction roue(n) qui crée une roue d'ordre n.
# Créez une fonction cube(n) qui crée un 𝑛-cube


## Exercice 5
#
# Créez une fonction rand_graph(n) qui crée un graphe de n sommets aléatoirement.
# On pourra utiliser les fonctions randint et sample du module random.


# Exercice 6
#
# Vérifiez sur des graphes aléatoires le théorème des poignées de main.
# Pour tester la parité, on pourra utiliser l'opérateur %


# Exercice 7
#
# Créez une méthode est_regulier qui vérifie si un graphe est régulier. 

if __name__ == '__main__':
   g = Graphe({'1': {'2', '4', '3'}, '2': {'3'}, '3': {'4'}})
