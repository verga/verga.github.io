Title: Outils numériques: python scientifique
Slug: ON-python
Date: 2020-12-31
Category: Lectures
Tags: teaching, numerical methods
Authors: Alberto Verga
Summary: Introduction au language python et aux la bibliothèque numpy et matplotlib
status: hidden

$\newcommand{\I}{\mathrm{i}} 
\newcommand{\E}{\mathrm{e}} 
\newcommand{\D}{\mathop{}\!\mathrm{d}}$

# Python

Python est un langage de programmation interactif, dont les multiples applications vont du développement web et réseaux, au calcul scientifique en passant par la manipulation des données et l'intelligence artificielle. Il se distingue des langages compilés comme le fortran ou le C, dont les types des objets sont statiques, par ses objets dynamiques. On dit donc que python est un langage interprété, dans le sens où chaque instruction peut être exécuté immédiatement.

Python se caractérise par une syntaxe simple et intuitive (d'où sa popularité), notamment par le fait que les espaces et par conséquent l'indentation des lignes, sont significatifs: la porté d'un bloc de code est associée à un changement d'indentation. Il s'agit en outre d'un langage souple qui permet la programmation à différents niveaux d'abstraction, du code procédural au code orienté objet. Python possède un ensemble de bibliothèques dédiées aux applications les plus diverses, depuis le script système et le serveur web, jusqu'aux packages de calcul vectoriel (numpy), scientifique (scipy), des données (pandas), ou graphique (matplotlib,pillow). Des scientifiques proposent de boîtes à outils pour l'astronomie (astropy), la mécanique quantique (qutip), la matière condensée (kwant, tenpy,quimb), ou les réseaux et l'intelligence artificielle (pytorch, tensorflow). Cette liste est loin d'être exhaustive ou même représentative des milliers de packages python (il doit en avoir 200000 dans le site PyPi).

## Éléments du langage

Le mots réservés sont:

    False      await      else       import     pass
    None       break      except     in         raise
    True       class      finally    is         return
    and        continue   for        lambda     try
    as         def        from       nonlocal   while
    assert     del        global     not        with
    async      elif       if         or         yield
    
Python est donc une langue avec 35 mots! 

Un programme python consiste en une séquence de lignes avec les instructions du code ou des commentaires. Les opérations de base sont:

    +       -       *       **      /       //      % 

et les opérations logiques:
    
    <       >       <=      >=      ==      !=
    
- `**` est la puissance `3**3 = 27`
- `//` est la division entière: `1//2 -> 0`
- `%` est modulo `7 % 4 -> 3`

Ajoutons l'opérateur d'affectation `=` qui affecte l'expression de droite à la variable de gauche. Les combinaisons `+=, -=, *=, /=` sont des raccourcis (grosso modo) qui combinent la variable de gauche avec l'expression de droite par l'opération correspondante: 

    :::python
    a = 1 # affecte l'entier 1 à la variable de nom a
    a +=1 # donne a = 2
    
Les types usuels de varaibles sont

- `bool` les logiques `True, False, None` Par exemple `not True is False` donne `True` (vérifiez)
- `int` les entiers (ils sont exacts), `1, 10, -3, 0, 3141592653589793238462643383279502884`
- `float` les réels `1.0, -89.4, 2e-3`
- `complex` les complexes `1+1j, 6.8 - 0.1j`

Avec les entiers on peut faire des rationnels utilisant [`Fraction`](https://docs.python.org/3/library/fractions.html):

    :::python
    import fractions
    fractions.Fraction(2,3) + fractions.Fraction(3,2)
    
En plus des types de base on a aussi de types composés, ou objets "itérables", c'est-à-dire dont les éléments sont indexés et peuvent donc être sélectionnés à l'aide de "slices"

- `string` (guillemets) ou chaînes de caractères immutable (non modifiable) de la forme "Bienvenue!" ou "jusqu'à" (python accepte l'encodage utf8)

- `tuple` (parenthèses) liste immutable de la forme `(a, b, c)`

        :::python
        a = (1, 2, 35, 2)
        a[2] # donne 35
    
    le tuple est indexé à partir de 0, ses éléments sont séléctionné par un "slice": `a[1:3]` donne le tuple `(2,35)` 

- `list` (crochets) tableau modifiable (dynamique: on peut ajouter ou retrancher d'éléments), de la forme `[1, b, 'c']` (les éléments n'ont pas besoin d'être du même type)

        :::python
        a = [1, "jusqu'à"]
        a[1] # donne "jusqu'à"
      
- `set` (accolades) immutable ensemble d'éléments sans répétition et ordonnés `{1,8,3} -> {1,3,8}`. Par exemple:

        :::python
        a = (8, 3, 1, 3)
        set(a) # donne {1, 3, 8}
   
    on peut faire `list(set(a))` pour transformer le n-uplet `a` en un tableau modifiable (de type list)
    
- `dict` dictionnaire; la syntaxe est 

        :::python
        a = {"a": 1, "b": 2}
        a["a"] # donne 1
        a.values() # donne dict_values([1,2])
      
    le dictionnaire associe des clés (étiquettes) (les clés forment un `set`, elle sont donc uniques, elle peuvent être des mots, mais aussi de nombres), aux données ou valeurs; la liste de valeurs s'obtient avec la méthode `values()`:
    
        :::python
        a = {"a":1,"b":[2,3],"a":2,3:4} # donne {'a': 2, 'b': [2,3], 3: 4}, 
                                        # notez la substitution de "a"

    la méthode `dico.items()` ennumère les clés est les valeurs du dictionaire nommé dico (vérifiez):
    
        :::python
        dico = {"A": (0,0), "B": (0,4), "C": (3,0)} # triangle rectangle
        for clef, valeur in dico.items():
        print(clef+" : ", valeur)
        plt.plot([0,0,4,0],[0,3,0,0], 'k-');

## Tableaux Numpy

### Création

<table class="table table-striped" style="width: 500px">
<thead class="thead-dark">
<tr>
<th>routine</th>
<th>description</th>
</tr>
<tbody>
<tr>
<td> array </td>   <td> <code>array([[1,0],[0,1j]], dtype = complex)</code> matrice complexe dimension 2 </td>
</tr>
<tr>
<td>  zeros </td> <td> <code>zeros((2,3)</code> matrice de zéros avec 2 lignes et 3 colonnes </td>
</tr>
<tr>
<td>  ones   </td> <td>  idem zeros, mais tous les éléments sont 1 </td>
</tr>
<tr>
<td>  arange  </td> <td> <code>arange(5)</code> donne [0, 1, 2, 3, 4] </td>
</tr>
<tr>
<td>  linspace </td> <td> <code>linspace(-pi, pi, 129)</code> 129 valeurs entre \(-\pi\) et \(\pi\) </td>
</tr>
<tr>
<td>  meshgrid </td> <td> grille bidimensionnelle, pour faire des fonction \(f(x,y)\) </td>
</tr>
<tr>
<td>  diag </td> <td> <code>diagonal(arange(4), -1)</code> matrice 5x5 avec 0,1,2,3 sous la diagonale </td>
</tr>
</tbody>
</table>

Le module `random` contient plusieurs routines de génération de nombres aléatoires. Pour utiliser le module il faut importer le "générateur aléatoire":

```python
from numpy.random import default_rng
rng = default_rng()
r = rng.random(25) # 25 nombres aléatoires dans [0,1)
```

<table class="table table-striped" style="width: 500px">
<thead class="thead-dark">
<tr>
<th>routine</th>
<th>description</th>
</tr>
<tbody>
<tr>
<td>   integers </td>  <td>   entiers <code>randint(0,2,12)</code> séquence de 12 zéros et uns </td>  
</tr>
<tr>
<td>   choice  </td>  <td> choisit aléatoirement les éléments d'une liste </td>  
</tr>
<tr>
<td>   random   </td>  <td>  réels <code>random(3,4)</code> tableau 3x4 de nombres aléatoires dans \([0,1)\) </td>  
</tr>
<tr>
<td>   standard_normal  </td>  <td>  distribution normale </td>  
</tr>
</tbody>
</table>


### Propriétés

| routine | description |
| ------- |:----------- |
| shape   | donne les dimensions d'un tableau |
| max, min | sélectionne l'élément maximal et minimal |
| argmax, argmin | donne l'indice du max et du min |
| sum     | fait la somme des éléments `sum(a**2)` |
| mean    | comme `sum`, moyenne |
| where   | `where(a > 0)` *tuple* contenant un tableau avec les éléments de `a` positifs |

### Modifications

| routine | description |
| ------- |:----------- |
| reshape | `reshape(arange(12), (4,3))` tableau 4x3 |
| ravel   | donne un vecteur à partir d'un tableau quelconque |
| roll    | `roll(arange(5), 1)` déplace vers la gauche de 1 cran (-1, vers la droite), cyclique |
| transpose | géméralisation de la transposition de matrices |
| vstack  | `vstack(a,b)` a: 2x3 b: 4x3 donne un array (2+4)x3 |
| hstack  | idem vstack dans la direction horizontale |

### Opérations 

| routine | description |
| ------- |:----------- |
| + - / * ** // | fonctionnent sur les éléments |
| dot     | `dot(a,b)` contraction du dernier indice de `a` avec l'avant-dernier de b |
| matmul  | produit de matrices |
| kron    | produit de kronecker, a et b avec le même *nombre* de dimensions |
| tensordot | produit tensoriel |
| einsum | conventions d'einstein (très utile!), opérations complexes sur des tenseurs |


## Ressources

* Documentation [python officielle](https://docs.python.org/3/)
* Référence officielle [numpy.org](https://numpy.org/doc/stable/reference/index.html)
* Livre en ligne sur [numpy](https://www.labri.fr/perso/nrougier/from-python-to-numpy/)

En complément, on peut trouver utile les livres disponibles sur le web:

* [Dive into python](https://diveintopython3.problemsolving.io/)
* [Patterns, Recipes and Idioms](https://python-3-patterns-idioms-test.readthedocs.io/en/latest/index.html)
* [Programing for Computations](https://link-springer-com.lama.univ-amu.fr/book/10.1007/978-3-030-16877-3) contient la plupart de sujets traités en travaux pratiques; disponible en accès libre aux formats pdf et epub

