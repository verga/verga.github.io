Title: Problèmes et exercices
Slug: MQ-problemes 
Date: 2020-04-01
Category: Lectures
Tags: teaching, quantum mechanics, undergraduates
Authors: Alberto Verga
Summary: Corrigé des problèmes de mécanique quantique pour la licence de physique
status: hidden

$\newcommand{\I}{\mathrm{i}}
\newcommand{\E}{\mathrm{e}}
\newcommand{\D}{\mathop{}\!\mathrm{d}}
\newcommand{\Tr}{\mathrm{Tr}}
\newcommand{\bra}[1]{\langle{#1}|}
\newcommand{\ket}[1]{|{#1}\rangle}
\newcommand{\braket}[1]{\langle{#1}\rangle}
\newcommand{\bbraket}[1]{\langle\!\langle{#1}\rangle\!\rangle}
\newcommand{\bm}{\boldsymbol}$

## Niveaux de Landau

Trouvez les niveaux d'énergie d'une particule de masse $m$ et charge $-e$ confinée dans le plan $(x,y)$ et soumise à l'action d'un champ magnétique constant $\bm B$ dirigé selon $z$.

Montrez que le potentiel vecteur peut s'écrire $\bm A = (-By,0,0)$
Écrivez le hamiltonien 
$$H = \frac{1}{2m}\big(\bm p + e \bm A \big)^2$$
explicitement, en fonction des coordonnées de l'impulsion et de la postion
Montrez que la solution de l'équation de Schrödinger se ramène à celle d'un oscillateur dans la direction $y$ dont la position d'équilibre est:
$$y_0 = \frac{p_x}{eB}$$
Calculez la fréquence d'un tel oscillateur.
Trouvez les niveaux d'énergie (Landau)
Si l'aire du système est $S=L_xL_y$, montrez que la dégénérescence du niveau fondamental est
$$\nu_0 = \frac{L_y}{2\pi \hbar / e B L_x}  = \frac{BS}{\Phi_0} = \frac{\Phi}{\Phi_0}$$
avec $\Phi_0 = h/e$ le quantum de flux magnétique et $\Phi$ le flux magnétique.

### Solution

Avec le choix de jauge du potentiel vecteur $\bm A = (-By,0,0)$ le système est invariant par translation selon la coordonné $x$; le hamiltonien
$$H = \frac{1}{2m} \left[ (p_x-eBy)^2 + p_y^2 \right]$$
est indépendant de l'opérateur $x$. Le système défini par $H$ contient les paramètres dimensionnels $m,B$ et $\hbar$; il convient donc de définir des unités appropriées:

* masse $m$
* temps $\omega_c^{-1}$, avec $\omega_c = eB/m$ la fréquence de cyclotron (rappelons que le mouvement classique d'une charge dans un champ magnétique constant est une trajectoire circulaire)
* longueur $\ell = \sqrt{\hbar/m\omega_c}$

Dans la suite on travaille avec ces unités ($m=e=\hbar=1$), avec $B$ la fréquence et $\sqrt{1/B}$ la longueur. Le hamiltonien devient, en complétant le carré:
$$H = \frac{p_y^2}{2} + \frac{B^2}{2}(y - Bp_x)^2 = \frac{p_y^2}{2} + \frac{B^2Y^2}{2} $$
avec $Y=y - p_x/B$, qui est analogue au hamiltonien d'un oscillateur unidimensionel de fréquence $B$. Les niveaux d'énergie sont par conséquent:
$$E_n = B \left( n + \frac{1}{2} \right) = \hbar \omega_c \left(n + \frac{1}{2} \right), \; n = 0, 1, 2, \ldots$$
où $n$ est le niveau de Landau.

Si on considère le système comme étant un rectangle d'aire $L_xL_y$ avec des conditions de bord périodiques dans la direction invariante par translation $x$, l'impulsion $p_x = 2\pi i/L_x,\, i = 0,1,2, \ldots$ est quantifié. Ce qui implique que la position de l'oscillateur $y_0=p_x/B = 2\pi i/L_x B$ doit satisfaire $y_0 < L_y$. Le nombre possible d'états $i$ est donc,
$$i < \frac{L_xL_yB}{2\pi} = \nu, \; \nu = \frac{\Phi}{\Phi_0}$$
où $\Phi = BL_xL_y$ est le flux à travers la surface et $\Phi_0 = 2\pi\hbar/e$ le flux magnétique élémentaire (par spin).
avec $\nu$ la dégénérescence du niveau d'énergie.

On s'est limité à analyser le problème en choisissant une jauge particulier de $\bm A$, or les propriétés du système doivent être indépendantes d'un tel choix. Notons toutefois  que ce choix peut être dicté par, par exemple, la géométrie et les symétries du problème: le choix fait de jauge est particulièrement intéressant si un courant est présent dans la direction $x$, qui est la situation pertinente pour l'effet hall quantique. Prenons donc le hamiltonien de l'électron dans un champ $B=B_z=\mathrm{const}$,
$$H = \frac{1}{2} \big( P_x^2 + P_y^2 \big), \quad P_x = p_x + A_x,\; P_y = p_y + A_y$$
où nous avons introduit les opérateurs $\bm P$ proportionnels à la vitesse (dans la description classique lagrangienne). Il est intéressant de calculer le commutateur,
$$[P_x, P_y] = -\I B$$
En effet, dans la représentation des coordonnées on a $[p_x, f(x)] = -\I\partial_x f$, ce qui donne,
$$[p_x + A_x, p_y + A_y] = [p_x,A_y] + [A_x, p_y] = -\I(\partial_x A_y - \partial_y A_x)$$
qui eat la composante $z$ de $\nabla \wedge \bm A$. Par conséquent on peut introduire les opérateurs d'annihilation et de création, équivalents à ceux de l'oscillateur harmonique:
$$a = \frac{1}{\sqrt{2B}} (P_x - \I P_y), \;  a^\dagger = \frac{1}{\sqrt{2B}} (P_x + \I P_y)$$
définition qui permet de récrire $H$ sous la forme,
$$H = B \left( a^\dagger a + \frac{1}{2} \right)$$
puisque leur commutateur suit la règle
$$[a,a^\dagger] = 1$$
On en déduit que le spectre est bien $E_n = B(n+1/2)$ indépendant du choix de jauge.

Notez cependant qu'on est parti d'un problème en deux dimensions et que pour le moment on n'a qu'une description semblable à un oscillateur unidimensionnel: il nous manque quelque chose! Effectivement, on peut définir deux autres opérateurs indépendants, liées non pas à la "vitesse", mais à la position par rapport au "centre de masse":
\begin{equation}
  \label{XY}
  X= x + \frac{P_y}{B}, \; Y = y - \frac{P_x}{B}
\end{equation}
Ces formules correspondent au formules du mouvement classique, c'est-à-dire à la trajectoire circulaire de rayon $r$ et fréquence $\omega_c$, autour du centre de masse $(X,Y)$
$$x(t) = X + r \cos \omega_c t,\; y = Y - r \sin \omega_c t$$
formules qu'avec la condition $\dot{X} = \dot{Y} = 0$, donnent précisément la définition $\eqref{XY}$ des opérateurs quantiques.

Ces deux opérateurs suivent la règle de commutation,
$$[X,Y] = \I/B$$
et permettent donc d'introduire une *nouvelle* paire d'opérateurs,
$$b = \sqrt{\frac{B}{2}} (X + \I Y), \; b^\dagger = \sqrt{\frac{B}{2}} (X - \I Y)$$
satisfaisant la règle de commutation,
$$[b,b^\dagger]=1$$
L'opérateur 
$$R^2 = X^2 + Y^2 = \frac{2}{B} \left( b^\dagger b + \frac{1}{2} \right)$$
nous donne les valeurs possibles du centre de masse:
$$r_0^2 = \frac{2}{B} \left( i + \frac{1}{2} \right)$$
avec $i = 0, 1, \ldots$. Cet opérateur commute avec le hamiltonien $[H,R^2]=0$, on a donc deux entiers $(n,i)$ qui caractérisent ensemble les états de l'électron.

Si on considère un système d'aire $S = \pi a^2$ (cercle de rayon $a$) les valeurs possibles de $i$ seront,
$$r_0 < a \; \Rightarrow \; i < \frac{B}{2} a^2 = \frac{B S}{2\pi} = \frac{\Phi}{\Phi_0} = \nu$$
résultat qui coïncide avec le calcul précédent de la dégénérescence.

## Deux spins

Trouvez les niveaux d'énergie et les vecteurs propres d'un système constitué de deux spin $1/2$, dont le hamiltonien est

$$H = - \frac{J}{\hbar^2} \bm{S}_1 \cdot \bm{S}_2$$

### Solution

L'interaction d'échange entre deux spins proches $\bm S_1$ et $\bm S_2$, peut être décrite par le hamiltonien de Heisenberg:
$$H = -\frac{J}{\hbar^2} \bm S_1 \cdot \bm S_2$$
où $J$ est la constante de couplage mesuré en unités d'énergie. L'opérateur de spin est proportionnel aux matrices de pauli:
$$\bm S_i = \frac{\hbar}{2} (X_i,Y_i,Z_i),\; i=1,2$$
qu'une fois substitué dans $H$, donne:
$$H = -\frac{J}{4} (X\otimes X + Y\otimes Y + Z\otimes Z)\,.$$

Pour représenter le hamiltonien par une matrice, on définit une base de l'espace de hilbert à quatre dimensions de deux spins à partir des vecteurs canoniques du spin $1/2$:
$$\ket{0}=\begin{pmatrix}1\\0\end{pmatrix}\,,\quad \ket{0}=\begin{pmatrix}0\\1\end{pmatrix},$$
On obtient:
$$\ket{00} = \ket{0}\otimes\ket{0},\,
  \ket{01} = \ket{0}\otimes\ket{1},\,
  \ket{10} = \ket{1}\otimes\ket{0},\,
  \ket{11} = \ket{1}\otimes\ket{1}.$$
Dans cette base, le hamiltonien s'écrit explicitement:
$$H = -\frac{J}{4}\begin{pmatrix}1 & 0 & 0 & 0\\0 & -1 & 2 & 0\\0 & 2 & -1 & 0\\0 & 0 & 0 & 1\end{pmatrix}$$

L'utilisation de la bibliothèque ``sympy`` nous permet de résoudre le problème à valeurs propres $H \ket{n} = E_n \ket{n}$, avec $n = 0, 1, 2, 3$, le quatre niveaux d'énergie possibles. La diagonalization directe de $H$ determine les valeurs propres:
$$E = \{(-J/4,3),(3J/4,1)\}$$
où la première valeur $E=E_t=-J/4$ correspond à l'état triplet (puisqu'il est trois fois dégénéré), et la deuxième valeur $E=E_s=3J/4$, correspond à l'état singlet. Si l'interaction spin-spin est de type ferromagnétique ($J>0$), l'état triplet est celui de plus basse énergie, dans le cas contraire, si l'interaction est anti-ferromagnétique ($J<0$), le singlet correspond à l'état fondamental.

Les vecteurs propres respectifs sont: pour $E_t = -J/4$ (triplet),
$$\begin{pmatrix}1\\0\\0\\0\end{pmatrix} = \ket{00}, \,
  \begin{pmatrix}0\\0\\0\\1\end{pmatrix} = \ket{11}, \,
  \frac{1}{\sqrt{2}}\begin{pmatrix}0\\1\\1\\0\end{pmatrix} = \frac{\ket{01} + \ket{10}}{\sqrt{2}}$$
et pour le niveau $E_t = 3J/4$ (singlet),
$$\frac{1}{\sqrt{2}}\begin{pmatrix}0\\1\\-1\\0\end{pmatrix} = \frac{\ket{01} - \ket{10}}{\sqrt{2}}$$

En fait, la structure de la matrice $H$ est telle qu'une résolution directe est facile; en effet, $H$ peut s'écrire comme la somme directe de trois matrices:
$$H = -\frac{J}{4}\left[ (1) \oplus \begin{pmatrix}-1&2 \\ 2&-1\end{pmatrix} \oplus (1) \right]$$
ce qui nous donne immédiatement deux valuers propres $-J/4$ avec les vecteurs propres $\ket{00}$ et $\ket{11}$. Le polynoôme caractéristique de la matrice deux par deux restante est,
$$(J/4 - E)^2 - J^2/4 =0$$
dont les racines sont $E= -J/4, 3J/4$. Les vecteurs propres s'obtiennent sans effort.

#### Code

```python
import sympy
from sympy import I, Rational, Matrix
from sympy.physics.quantum import TensorProduct
#
sympy.init_printing()
X = Matrix([[0,1],[1,0]])
Y = Matrix([[0,-I],[I,0]])
Z = Matrix([[1,0],[0,-1]])
h = -Rational(1,4) * (TensorProduct(X,X) + TensorProduct(Y,Y) + TensorProduct(Z,Z))
h
```

$$\frac{1}{4}\left[\begin{matrix}-1 & 0 & 0 & 0\\0 & 1 & -2 & 0\\0 & -2 & 1 & 0\\0 & 0 & 0 & -1\end{matrix}\right]$$

```python
vn = h.eigenvects()
vn
```

$$\left[ \left( - \frac{1}{4}, \  3, \  \left[ \left[\begin{matrix}1\\0\\0\\0\end{matrix}\right], \  \left[\begin{matrix}0\\1\\1\\0\end{matrix}\right], \  \left[\begin{matrix}0\\0\\0\\1\end{matrix}\right]\right]\right), \  \left( \frac{3}{4}, \  1, \  \left[ \left[\begin{matrix}0\\-1\\1\\0\end{matrix}\right]\right]\right)\right]
$$

#### Note

Le hamiltonien peut aussi s'écrire à l'aide de l'opérateur 
$$\bm S = \bm S_1 + \bm S_2$$
de spin total. On remarque que,
$$2 \bm S_1 \cdot \bm S_2 = \bm S^2 - \bm S_1^2 - \bm S_2^2\,.$$
Or, les deux derniers termes sont diagonaux:
$$\bm S_i^2 = \frac{3\hbar^2}{4} I$$
avec $I$ l'opérateur identité. On a donc trivialement:
$$[H, \bm S^2] = 0, \; [H, S_z] = 0$$
avec $S_z = S_{z1} + S_{z2}$, la composante $z$ du spin total. Ceci signifie qu'on peut définir une base $\ket{sm}$ avec
$$\bm S^2 \ket{sm} = \hbar^2 s(s+1) \ket{sm}, \; S_z \ket{sm} = \hbar m \ket{sm}$$
qui est aussi base de $H$ (les opérateurs sont compatibles). Applicant $\bm S^2$ et $S_z$ aux vecteurs de la base canonique, il est facile de retrouver les résultats de la première partie de l'exercice:
$$\ket{s=0, m=0} = \frac{1}{\sqrt{2}}\left( \ket{10} - \ket{01} \right)$$
est le singlet; le triplet correspond aux trois vecteurs avec $s=1$ et les projections $-1,0,1$ de $S_z$:
$$\ket{s=1,m=-1} = \ket{11},\; \ket{s=1,m=0} = \frac{1}{\sqrt{2}}\left( \ket{10} + \ket{01} \right)\, \; \ket{s=1,m=1} = \ket{00}.$$


## Effet relativiste sur l'atome d'hydrogène

On considère l'atome H dans l'approximation du noyau fixe (on néglige la différence entre la masse réduite et la masse de l'électron). Montrez que pour des vitesses petites devant celle de la lumière $c$, l'énergie cinétique peut être approximée, en tenant compte de la première correction relativiste:
$$K \approx \frac{p^2}{2m} - \frac{p^4}{8m^3c^2}$$
où $p^4 = \bm p^2 \bm p^2$. On suppose le hamiltonien non perturbé celui de l'atome d'hydrogène non relativiste:
$$H_0 = \frac{p^2}{2m} - \frac{e^2}{4\pi \varepsilon_0 r}$$
calculez en utilisant la théorie de perturbations la correction relativiste du spectre d'énergie:
$$E^{(1)}_n = - \frac{1}{2} mc^2 \alpha^4 \left[ -\frac{3}{4n^4} + \frac{1}{n^3(l+1/2)} \right]$$
Pour cela utilisez la relation:
$$\left( \frac{p^2}{2m} \right)^2 = \left( H_0 + \frac{e^2}{4\pi\varepsilon_0 r} \right) \left( H_0 + \frac{e^2}{4\pi\varepsilon_0 r} \right)$$
et calculez 
$$\left\langle \frac{1}{r^k} \right\rangle, \; k=1,2$$
dans la base $\ket{nlm}$ de $H_0$.

### Solution

On spécifie d'abord les unités. On choisit l'unité de masse celle de l'électron $m$ (on considère le proton fixe, autrement on remplace $m$ par la masse réduite); l'unité de longueur est le rayon de Bohr $a_0$:
$$\frac{e^2}{4\pi \varepsilon_0 a_0} = \frac{\hbar^2}{m a_0^2}, \quad a_0 = \frac{4\pi\varepsilon_0}{e^2} \frac{\hbar^2}{m}$$
et l'unité d'énergie est le Hartree $\mathrm{Ha}=2\mathrm{Ry}$:
$$\mathrm{Ha} = \frac{\hbar^2}{ma_0^2}$$
ce qui est équivalent à $m=e^2/4\pi \varepsilon_0=\hbar=1$. La constante de structure fine $\alpha$ est définie par le rapport entre l'énergie de couloumb et l'énergie au repos $mc^2$ de l'électron:
$$\alpha^2 = \frac{\hbar^2}{ma_0^2} \frac{1}{mc^2} = \left( \frac{\hbar}{mca_0} \right)^2$$
ou,
$$\alpha = \frac{\hbar}{mc} \frac{e^2}{4\pi \varepsilon_0} \frac{m}{\hbar^2}= \frac{e^2}{4\pi\varepsilon_0 \hbar c}$$
ce qui est équivalent au rapport de la longueur d'onde de Compton de l'électron $\lambda_e = \hbar/mc$ et du rayon de Bohr:
$$\alpha = \frac{e^2}{4\pi\varepsilon_0 \hbar c} = 7.2973\,5256\,93\times 10^{-3}$$
Dans les [unités atomiques](https://en.wikipedia.org/wiki/Hartree_atomic_units) $a_0=m=\hbar=e=4\pi\varepsilon_0=1$ la vitesse de la lumière vaut
$$c = 1/\alpha = 137.035\,999\,084\,.$$

L'énergie cinétique relativiste est,
$$K = \sqrt{c^2 {\bm p}^2 + m^2 c^4} - mc^2 = mc^2 \left(\sqrt{1 + (\bm p/mc)^2} - 1\right)$$
ou, dans les unités atomiques, qu'on utilise désormais,
$$K = \frac{1}{\alpha^2}\left(\sqrt{1 + (\alpha p)^2} - 1\right)$$
On vérifie que pour le régime non relativiste $p \ll mc = 1/\alpha$, le second terme dans la racine satisfait $\alpha p \ll 1$, on peut donc envisager un développement en puissance de $\alpha$. Le développement limité de la racine,
$$\sqrt{1 + (\alpha \bm p)^2} = 1 + \alpha^2 \frac{\bm p^2}{2} - \frac{\alpha^4 \bm p^4}{8} + \cdots$$
donne,
$$K = \frac{\bm p^2}{2} - \alpha^2\frac{\bm p^4}{8} + \cdots$$
Le deuxième terme apparaît comme une perturbation de l'énergie cinétique classique, dont le paramètre est $\alpha^2$. Dans cette approximation le hamiltonien s'écrit:
$$H = H_0  - \alpha^2\frac{p^4}{8}$$
avec
$$H_0 = \frac{\bm p^2}{2} - \frac{1}{r}$$
le hamiltonien de l'atome H non perturbé. Les états d'énergie non perturbés $\ket{nlm}$ satisfont l'équation de Schrödinger,
$$H_0 \ket{nlm} = \epsilon_{n} \ket{nlm}, \quad \epsilon_n = -\frac{1}{2n^2}\, [\mathrm{Ha}]$$
avec $n = 1, 2,\ldots$ le niveau d'énergie (nombre quantique principal) et $(l,m)$ les nombres quantiques du moment angulaire: $l=0,1,\ldots < n$, $-l \le m \le l$. En négligeant le spin, les états d'énergie $\epsilon_n$ son
$$\sum_{l=0}^{n-1}(2l+1) = 2 \frac{n(n-1)}{2} + n = n^2$$
fois dégénérés (comme vous pouvez le démontrer par recurrence). On peut encore noter que le terme de perturbation commute avec le moment angulaire,
$$[\bm L, \bm p^4]=0$$
ce qui signifie que l'opérateur $\bm p^4$ est diagonal dans la base non perturbée $\ket{nlm}$. Au premier ordre on a donc,
$$E^{(1)}_{nl} = -\frac{\alpha^2}{8} \braket{nlm|\bm p^4|nlm}\,.$$
Le calcul direct des intégrales est difficile; le calcul se simplifie si on exprime $p^2$ en termes de $H$:
$$\alpha^2\frac{\bm p^4}{8} = \frac{\alpha^2}{2} \left(\frac{p^2}{2}\right)^2 = \frac{\alpha}{2} \left(H_0 + \frac{1}{r}\right)^2$$
(on note $p^2=\bm p^2 = \bm p \cdot \bm p$). Ou, après expansion du produit,
$$E^{(1)}_{nl} = - \frac{\alpha^2}{2}\left( \epsilon_n^2 + 2\epsilon_n \braket{nlm| \frac{1}{r} |nlm} + \braket{nlm| \frac{1}{r^2} |nlm} \right)$$
Le calcul des niveaux d'énergie perturbés se réduit donc au calcul de valeurs espérées de $1/r$ et $1/r^2$; on remarque que ces deux opérateurs sont proportionnels aux termes de coulomb et du moment angulaire de $H_0$, respectivement. 

Le premier terme se calcule directement, il donne une correction de la forme:
$$\Delta E = -\frac{\alpha^2}{2}\epsilon_n^2 = -\frac{\alpha^2}{8n^4}\,.$$
Avant the passer au calcul de $\braket{1/r}$, rappelons le théorème du viriel (valable en classique et quantique--pour les valeurs moyennes). Si l'énergie potentielle est une puissance de la position $V \sim r^k$, on a
$$0 = \braket{\frac{\D \bm r \cdot \bm p}{\D t}} = \braket{\dot{\bm r} \cdot \bm p} +  \braket{\bm r \cdot \dot{\bm p}} = \braket{\frac{\partial H}{\partial \bm p} \cdot p} - \braket{\bm r \cdot \frac{\partial H}{\partial \bm r}}$$
ce qui revient à
$$0 = \braket{p^2} - \braket{\bm r \cdot \frac{\partial V}{\partial \bm r}}$$
ou en posant $K = p^2/2$ et $V \sim r^k$,
$$2\braket{K} = k \braket{V}$$
le théorème du viriel (voir la discussion de ce théorème dans le Landau-Lifshitz de Mécanique).

On peut maintenant appliquer ce résultat au cas coulombien $k = -1$,
$$\braket{H_0} = - \braket{K} = \frac{1}{2} \braket{V}$$
d'où on déduit:
$$\braket{\frac{1}{r}} = \frac{1}{n^2}$$
puisque $\braket{H} = -1/2n^2$. On a donc,
$$\Delta E = -\braket{\frac{\alpha^2\epsilon_n}{r}} = \frac{\alpha^2}{2n^4}$$

Concernant le terme $\braket{1/r^2}$, en comparant avec le terme en $l(l+1)/2r^2$, on constate que le paramètre $l$, en présence de la perturbation, change de valeur:
$$l(l+1) \rightarrow l(l+1) - \alpha^2 = l'(l'+1)$$
où $l'$ est le nouveau nombre quantique orbital. Si on se rappelle que le nombre quantique principal peut s'écrire comme $n = n_r + l + 1$, avec $n_r$ le nombre quantique radial, le spectre d'énergie devient,
$$E = \frac{1}{2(n_r+l'+1)^2}$$
Le terme proportionnel à $\alpha^2$ (l'ordre de la perturbation) est donc calculé par un développement limité:
$$\Delta E = \alpha^2 \left. \frac{\D E}{\D \alpha^2} \right|_{\alpha^2=0} = \alpha^2 \left. \frac{\D E}{\D l'} \right|_{l'=l} \left. \frac{\D l'}{\D \alpha^2} \right|_{l'=l}$$
L'application de la formule donne,
$$\Delta E = \braket{\frac{-\alpha^2}{2r^2}} = -\frac{\alpha^2}{n^3(2l+1)}$$

> **Théorème de [Hellmann-Feynman](https://en.wikipedia.org/wiki/Hellmann%E2%80%93Feynman_theorem)**
> Soit un hamiltonien qui dépend d'un paramètre $a$, $H_a$; les valeurs propres et les vecteurs propres seront également fonction du paramètre:
>
$$H_a \ket{a} = E_a \ket{a},\quad \braket{a|a} = 1$$
>
> Calculons la dérivée par rapport au paramètre $a$ de la valeur espérée $\braket{a|H_a|a}= E_a$:
>
$$\frac{\D \bra{a}}{\D a} H_a \ket{a} + \bra{a} H_a \frac{\D \ket{a}}{\D a} + \braket{a|\dot{H}_a|a} = \dot{E}_a$$
>
> en utilisant l'équation de Schrödinger des vecteurs propres, le côté gauche de la formule précédente devient,
> 
$$ E_a \frac{\D \bra{a}}{\D a} \ket{a} + E_a \bra{a} \frac{\D \ket{a}}{\D a} + \braket{a|\dot{H}_a|a} = \dot{E}_a$$
> 
> or, en vu de
>
$$0= \frac{\D}{\D a} \braket{a|a} = \frac{\D \bra{a}}{\D a} \ket{a} + \bra{a} \frac{\D \ket{a}}{\D a}$$
>
> les deux premières termes se cancellent, nous amenant au résultat:
>
$$\braket{a|\dot{H}_a|a} = \dot{E}_a$$
> 
> qui est connu comme le théorème de Hellmann-Feynman. (Le point est la dérivée par rapport au paramètre.)

On peut retrouver le résultat sur la moyenne de $1/r^2$ à partir du théorème en l'appliquant à $H_0$, en particulier au terme du moment angulaire en choisissant $l$ comme paramètre à varier (les autres termes sont indépendants de $l$):
\begin{align*}
\frac{\D}{\D l} E_{nl} &= -\frac{\D}{\D l} \frac{1}{2(n_r + l + 1)^2}\\
&= \frac{1}{n^3} \\
&= \bra{nlm} \frac{\D}{\D l} H_0 \ket{nlm}\\
&= \bra{nlm} \frac{\D}{\D l} \frac{l(l+1)}{2r^2}\ket{nlm} \\ 
&=  \bra{nlm} \frac{2l+1}{2r^2}\ket{nlm}
\end{align*}
où on a encore utilisé $n = n(l) = n_r + l + 1$, ce qui conduit au résultat:
$$\braket{nlm| \frac{1}{r^2} |nlm} = \frac{1}{n^3(l + 1/2)}$$ 

En collectant les différents résultats, on obtient la correction des niveaux d'énergie au premier ordre de la théorie des perturbations:
$$E^{(1)}_{nl} = \frac{3\alpha^2}{8n^4} -  \frac{\alpha^2}{n^3(2l+1)} \, [\mathrm{Ha}]$$
Le résultat dans les unités d'origine contient le factor $\hbar^2/ma_0^2 = mc^2\alpha^2 = \mathrm{Ha}$, qui restitue l'unité d'énergie.

On constate que la correction relativiste de l'énergie cinétique modifie la position de niveaux ainsi qu'elle enlève une partie de la dégénérescence, puisque maintenant l'énergie dépend aussi du nombre orbital $l$; cependant, dû à la symétrie de la perturbation, la dégénérescence magnétique (en $m$) persiste.

Un calcul numérique nous montre que la correction de l'état fondamental est de l'ordre de $-3.328\,\mathrm{Ha}$. Les corrections sont négatives: les niveaux non perturbés se décalent ver le bas.

```python
from scipy.constants import *
def energy0(n,l):
    return - 1/(2*n**2)
def energy1(n,l):
    return (3/8)*alpha**2/n**4 - alpha**2/(n**3*(2*l+1))
#
e0 = [energy0(n,l) for n in range(1,4) for l in range(n)]
e1 = [energy1(n,l) for n in range(1,4) for l in range(n)]
level = [[n,l] for n in range(1,4) for l in range(n)];
```

<table class="table table-striped" style="width: 400px">
<thead class="thead-dark">
<tr>
<th>\((n,l)\) </th>
<th>\(\epsilon_n\) </th>
<th>\(E_{nl}^{(1)}\) </th>
</tr>
</thead>
<tbody>
<tr>
<td>\((1,0)\)</td>
<td>\(-0.5\)</td>
<td>\(-3.328\,10^{-5}\)</td>
</tr>
<tr>
<td>\((2,0)\)</td>
<td>\(-0.125\)</td>
<td>\(-5.408\,10^{-6}\)</td>
</tr>
<tr>
<td>\((2,1)\)</td>
<td>\(-0.125\)</td>
<td>\(-9.707\,10^{-7}\)</td>
</tr>
</tbody>
</table>


Dans le tableau, pour chaque niveau $(n,l)$ on montre l'énergie non perturbé $\epsilon_n$ et la correction relativiste $E^{(1)}$ en $\mathrm{Ha} = 27.2\,\mathrm{eV}$.

## Oscillateur soumis à une force dépendante du temps

Un oscillateur quantique qui se trouve initialement dans son état fondamental, est perturbé par une force,

$$F(t) = F_0 \E^{-t/\tau}, \quad (t>0)$$

Calculez au premier ordre de la théorie de perturbations dépendante du temps la probabilité d'excitation de l'oscillateur vers des états de plus haute énergie.

### Solution

Notons d'abord que la perturbation du hamiltonien de l'oscillateur harmonique de masse $m$ et fréquence $\omega$,
$$H_0 = \frac{p^2}{2m} + \frac{m\omega^2 x^2}{2}$$
est
$$F(x,t) = - \frac{\D}{\D x}V(x,t), \quad V(x,t) = -F_0 x \E^{-t/\tau}, \; t>0$$
linéaire dans l'opérateur position $x$. Le hamiltonien total est donc
$$H = H_0 + V = \frac{p^2}{2} + \frac{x^2}{2} - \lambda x \E^{t/\tau}, \; \lambda= \frac{F_0}{\sqrt{\hbar m \omega^3}}$$
dans les unités $m=\omega=\hbar=1$. La valeur de $\lambda$ est facilement calculée en utilisant les unités:
$$\mathrm{L} = \sqrt{\frac{\hbar}{m\omega}},\; \mathrm{T} = 1/\omega,\; \mathrm{M} = m, \mathrm{E} = \hbar \omega$$
et en notant les dimensions de la force  $F_0 = \mathrm{MLT^{-2}}$
$$\lambda = \frac{F_0}{[F_0]}= F_0 \frac{1}{m \omega^2}\sqrt{\frac{m\omega}{\hbar}}\,.$$

Avant de traiter la perturbation rappelons les propriétés de $H_0$. En terme des opérateurs de création $a$ et annihilation $a^\dagger$,
$$a = \frac{x + \I p}{\sqrt{2}},\quad a^\dagger = \frac{x - \I p}{\sqrt{2}}$$
le hamiltonien se réduit à,
$$H_0 = a^\dagger a + \frac{1}{2}.$$
Les valeurs et vecteurs propres de l'oscillateur sont solution de
$$H_0 \ket{n} = \epsilon_n \ket{n},$$
ce qui donne,
$$\epsilon_n = n + \frac{1}{2}$$
avec $n = 0, 1, \ldots$, les niveaux d'énergie. On a encore les relations,
$$a \ket{n} = \sqrt{n} \ket{n-1},\quad a^\dagger \ket{n} = \sqrt{n+1} \ket{n+1}\,,$$
qui nous renseignent sur la façon dont les opérateurs $a$ et $a^\dagger$ agissent sur l'état de l'oscillateur $\ket{n}$.

En présence de la perturbation temporelle les états d'énergie ne sont plus stationnaires et des transitions entre les niveaux d'énergie peuvent se produire. La conséquence est que l'état devient en général une superposition de la forme:
$$\ket{\psi(t)} = \sum_n \psi_n(t) \E^{-\I \epsilon_n t} \ket{n}$$
lequel satisfait l'équation de Schrödinger:
\begin{align*}
\I \frac{\partial }{\partial t}\ket{\psi(t)} &= \sum_n \epsilon_n \psi_n(t) \E^{-\I \epsilon_n t} \ket{n} + \I \sum_n \dot{\psi}_n(t) \E^{-\I \epsilon_n t} \ket{n} \\ &= H_0 \ket{\psi(t)} + \sum_n \psi_n(t) \E^{-\I \epsilon_n t} V(x,t) \ket{n}
\end{align*}
ou, après simplification du terme $H_0$:
$$\I \sum_n \dot{\psi}_n(t) \E^{-\I \epsilon_n t} \ket{n} = \sum_n \psi_n(t) \E^{-\I \epsilon_n t} V(x,t) \ket{n}$$
On multiplie cette équation par le bra $\bra{m}$, et on utilise l'orthonormalisation $\braket{m|n} = \delta_{mn}$, pour obtenir,
$$\I \dot{\psi}_m(t) \E^{-\I \epsilon_m t}= \sum_n \psi_n(t) \E^{-\I \epsilon_n t} \braket{m|V(x,t)|n}\,.$$ 
En intégrant sur le temps, on transforme l'équation différentielle en intégrale:
$$\psi_m(t) = \psi_m(t_i) + \frac{1}{\I}\sum_n \int_{t_i}^t \D t' \E^{\I(\epsilon_m-\epsilon_n)t'} \braket{m|V(x,t')|n}\psi_n(t')$$
($t_i$ est le temps de référence) qu'on résout par itération; au premier ordre dans la perturbation on a,
$$\psi_m(t) = \psi_m(t_i) + \frac{1}{\I} \sum_n \int_{t_i}^t \D t' \E^{\I(\epsilon_m-\epsilon_n)t'} \braket{m|V(x,t')|n}\psi_n(t_i)\,.$$
On suppose qu'avant la perturbation le système se trouvait dans un état d'énergie bien défini $\ket{i}$:
$$\ket{\psi(t_i)} = \ket{i}, \quad \psi_m(t_i) = \delta_{im}$$
ce qui permet de simplifier l'équation de l'amplitude de la perturbation $\psi_m(t)$:
$$\psi_m(t) = \delta_{im} + \frac{1}{\I}\int_{t_i}^t \D t' \E^{\I(\epsilon_m-\epsilon_i)t'} \braket{m|V(x,t')|i}\,.$$
En général l'état final $\ket{\psi(t)} = \ket{f}$ est différent de $\ket{i}$:
$$\psi_f(t) = \frac{1}{\I}\int_{t_i}^t \D t' \E^{\I(\epsilon_f-\epsilon_i)t'} \braket{f|V(x,t')|i}\,.$$
La probabilité de transition $P_{fi}$ entre l'état initial $\ket{i}$ et l'état final $\ket{f}$, est simplement donnée par le carré de l'amplitude:
$$P_{fi}(t) = |\psi_f(t)|^2 = \left| \int_{t_i}^t \D t' \E^{\I(\epsilon_f-\epsilon_i)t'} \braket{f|V(x,t')|i} \right|^2\,,$$
qui se calcule une fois déterminés les éléments de matrice de la perturbation dans la base du hamiltonien non perturbé: $\braket{f|V|i}$.

Dans notre cas on doit calculer $\braket{n|x|0}$, puisque l'état initial est l'état fondamental et l'état final un certain niveau excité qu'on va déterminer,
$$\braket{n|x|0} = \frac{1}{\sqrt{2}} \braket{n| a + a^\dagger | 0} = \frac{1}{\sqrt{2}} \braket{n|1}=\frac{\delta_{n1}}{\sqrt{2}}$$
(bien évidement $a\ket{0} = 0$ et $a^\dagger \ket{0} = \ket{1}$). On trouve que la seule amplitude non nulle est celle de la transition entre l'état fondamental et le premier état excité. La probabilité de transition est par conséquent:
\begin{align*}
P_{10}(t) &= \frac{\lambda^2}{2} \left| \int_0^t \D t' \E^{\I t'} \E^{-t'/\tau} \right|^2 \\
&= \frac{\lambda^2}{2} \left| \frac{\E^{\I t - t/\tau} - 1}{\I - 1/\tau}  \right|^2 \\
&= \frac{\lambda^2}{2} \frac{\E^{-2t/\tau} - 2 \E^{-t/\tau} \cos(t) + 1}{1 + 1/\tau^2}
\end{align*}
qu'on obtient en séparant partie réelle et imaginaire $\E{\I x} = \cos x + \I \sin x$ et utilisant $|a + \I b|^2 = |a|^2 + |b|^2$ ainsi que $|z_1/z_2| = |z_1|/z_2|$. Dans la limite $t \gg \tau$, on trouve,
$$P_{10}(t) = \frac{\lambda^2}{2} \frac{\tau^2}{1 + \tau^2}$$
qui est indépendante du temps. On remarque que pour $\tau \rightarrow \infty$ le maximum de la probabilité tends vers,
$$\lim_{\tau \rightarrow \infty} \lim_{t \rightarrow \infty} P_{10}(t) = \frac{\lambda^2}{2}$$

> <img src="{static}/images/MQ-p10t.svg" alt="probabilité de transition" style="height: 230px;"/>
>
> La probabilité d'excitation de l'état fondamental d'un oscillateur harmonique, en unités de $\lambda^2 = F_0^2/m\omega^3\hbar$, et pour différentes valeurs de $\tau$; $\tau$ est le paramètre de relaxation de la force $F=F_0\E^{-t/\tau}$. On montre la valeur asymptotique $t \rightarrow \infty$: bien après l'application de la force $t \gg \tau$ on a unejj probabilité $(\lambda \tau)^2/2(1+\tau^2)$ de trouver l'oscillateur, initialement à l'état fondamental, dans le premier état excité $n = 1$. Le temps est mesuré en unités de la pulsation de l'oscillateur.

Si au contraire, on fixe la valeur du temps et on fait tendre $\tau \rightarrow \infty$ on obtient une probabilité qui varie périodiquement, avec la période de l'oscillateur:
$$\lim_{\tau \rightarrow \infty} P_{10}(t) = \lambda^2(1-\cos t)$$
(rappelez vous que la méthode suppose $\lambda \ll 1$), ce qui correspond à l'application d'une force constante à partir de $t = 0$.


## Diffusion par une sphère rigide

Montrez que la section efficace de la diffusion par une sphère rigide de rayon $a$,
$$V(r) = \begin{cases} \infty\,, & r \le a\\ 0\,, & r \ge a \end{cases}$$
est
$$\sigma = \frac{4\pi}{k^2} \sum_{l=0}^\infty (2l+1) \left| \frac{\mathrm{j}_l(ka)}{\mathrm{h}_l(ka)}  \right|^2$$
Étudiez la limite $ka \ll 1$; quelle est la valeur de $l$ qui contribue davantage à la diffusion?

### Solution

> <img src="{static}/images/MQ-diff_Sph.svg" alt="rigid sphere scattering" style="height: 250px;"/>
> 
> La sphère rigide est représentée par un potentiel infini à l'intérieur et nul à l'extérieur.


On commence avec quelques rappels sur l'équation de Schrödinger en coordonnées sphériques $(r,\theta,\phi)$. Pour la particule libre de masse $m=1$ le hamiltonien est $H = p^2/2$, et les états stationnaires sont les solutions de l'équation à valeurs et vecteurs propres $H\ket{\psi} = E \ket{\psi}$. En représentation position on a:
\begin{equation} \label{p2} p^2 = p_r^2 + \frac{L^2}{r^2}, \quad p_r^2 = -\frac{1}{r^2} \frac{\partial }{\partial r} r^2 \frac{\partial }{\partial r}\end{equation}
et $\bm L$ le moment cinétique, dont les vecteurs propres sont les harmoniques sphériques:
$$Y_{lm}(\theta,\phi) = \braket{\theta\phi|lm}$$
où ($\hbar=1$),
\begin{equation} \label{L2} L^2 \ket{lm} = l(l+1) \ket{lm}, \quad L_z \ket{lm} = m \ket{lm} \end{equation}
sont les nombres quantiques orbital ($l=0,1, \ldots$) et magnétique ($m$, $-l \le m \le m$). En coordonnées on a:
$$L^2 = \frac{1}{\sin \theta} \frac{\partial }{\partial \theta } \sin \theta \frac{\partial }{\partial \theta } + \frac{1}{\sin^2 \theta } \frac{\partial^2 }{\partial \phi^2}$$
et
$$L_z = -\I \frac{\partial }{\partial \phi}$$
Comme le hamiltonien commute avec $L^2$ et $L_z$, les vecteurs propres $\ket{lm}$ sont aussi vecteurs propres de $H$. La fonction d'onde peut donc s'écrire comme:
$$\psi(r,\theta,\phi) = R_{l}(r) Y_{lm}(\theta,\phi) = \braket{r\theta\phi|\psi}$$
avec $R$ la fonction d'onde radial ($R$ dépend des paramètres $l$ et de $E$). Elle satisfait, en substituant $\psi$ dans $H \psi = E \psi$, l'équation différentielle:
$$\frac{p_r^2}{2} R_{l}(r) + \frac{l(l+1)}{2} R_{l}(r) = E R_{l}(r)$$
où on a utilisé $\eqref{p2}$ et $\eqref{L2}$. La solution de cette équation dépend de deux constantes (c'est une équation de deuxième degré), et peut s'écrire comme une superposition de fonctions de bessel sphériques:
$$R_{l} = A_l \mathrm{j}_l(kr) + B_l \mathrm{n}_l(kr)$$
En effet, l'équation radiale,
$$R'' + \frac{2}{r}R' - \frac{l(l+1)}{r^2} + k^2 R = 0, \quad k = \sqrt{2E}$$
($R' = \D R / \D r$) se réduit pour $l=0$, à
$$(rR)'' + k^2 rR = 0$$
où on s'est servi de
$$(rR)'' = R' + (rR')' = 2R' + rR''$$
Or cette équation est élémentaire:
$$R_0 = A_0 \mathrm{j}_0(kr) + B_0 \mathrm{n}_0(kr)$$
avec,
$$\mathrm{j}_0(r) = \frac{\sin r}{r}, \quad  \mathrm{n}_0(kr) = - \frac{\cos r}{r}$$
Notez que la solution en $\mathrm{n}_0(kr)$ est singulière à l'origine, tandis que les deux décroissent à l'infini comme $\sim 1/r$.

La solution pour $l=1,2,\ldots$, s'obtient par recurrence. En effet, posant $R_l(r) = r^l w_l(r)$, on peut démontrer:
$$w_{l+1} = \frac{1}{r} \frac{\D}{\D r} w_l$$
ou,
$$w_{l} = \left( \frac{1}{r} \frac{\D}{\D r} \right)^l w_0\,.$$
Ce qui donne (en ajoutant le facteur $r^l$):
$$\mathrm{j}_{l} = (-r)^l \left( \frac{1}{r} \frac{\D}{\D r} \right)^l \frac{\sin r}{r}\,, \quad \mathrm{j}_{l} = -(-r)^l \left( \frac{1}{r} \frac{\D}{\D r} \right)^l \frac{\cos r}{r}$$
(le facteur $(-1)^l$ est introduit par convention).

Pour $r\rightarrow 0$ on a le comportement,
$$\mathrm{j}_l(r) = \frac{r^l}{1\times3\times \ldots \times (2l+1)} = \frac{r^l}{(2l+1)!!}$$
et
$$\mathrm{n}_l(r) = -\frac{1\times3\times \ldots \times (2l-1)}{r^{L+1}} = \frac{(2l-1)!!}{r^{l+1}}$$
et pour $r\rightarrow\infty$,
$$\mathrm{j}_l(r) = \frac{1}{r} \sin\left( r - \frac{\pi l}{2} \right),\quad \mathrm{n}_l(r) = -\frac{1}{r} \cos\left( r - \frac{\pi l}{2} \right)$$
La combinaison complexe:
$$\mathrm{h}_l(r) = \mathrm{j}_l(r) + \I \mathrm{n}_l(r)$$
la fonction de hankel, se comporte asymptotiquement comme,
\begin{equation} \label{hinfty} \mathrm{h}_l(r) = \frac{\E^{\I r - \I \pi l/2}}{\I r}\end{equation}

On a maintenant l'expression générale de la fonction d'onde pour une particule libre en coordonnées sphériques: 
\begin{equation} \label{psir} \psi(r,\theta,\phi) = \sum_l [A_l \mathrm{j}_l(kr) + B_l \mathrm{n}_l(kr)] P_l(\cos \theta) \end{equation}
où les polynômes de legendre $P_l$ sont reliés aux harmonique sphériques par la formule:
$$Y_{l0} = \sqrt{\frac{2l + 1}{4\pi}} P_l(\cos \theta)$$
(dans notre problème toute dépendance de $\phi$ doit disparaître par symétrie, on pose donc $m=0$).

Comme le potentiel de la sphère rigide s'annule pour $r>a$, il nous suffit de nous assurer de la continuité de la fonction d'onde en $r=a$, avec la solution à l'intérieur de la sphere, qui doit être nulle: $\psi(r,\theta,\phi) = 0$ ($r < a$). En outre, loin de l'origine (centre de diffusion), la fonction d'onde de l'onde diffusée, doit correspondre à une onde sphérique sortante, telle que la fonction d'onde à grande distance de l'origine ($r \gg a$) soit de la forme:
\begin{equation} \label{asymp} \psi \sim \E^{\I k z} + f(\theta) \frac{\E^{\I kr}}{r}\end{equation}
avec $f(\theta)$ l'amplitude de diffusion (elle dépend aussi de l'orbital $l$ et de l'énergie $E$). L'onde sphérique sortante se superpose à l'onde plane d'énergie $E$ incidente $\E^{\I k z}$, avec $k = \sqrt{2E}$.

La difficulté qui se présente pour satisfaire ces conditions asymptotiques (onde incidente et diffusée) et de bord (continuité de la fonction d'onde, dans le cas présent), c'est que le potentiel est bien à symétrie sphérique mais l'onde incidente ne l'est pas, elle brise cette symétrie puisqu'elle définie une direction privilégiée (on en a choisi $z$ pour la direction de l'onde incidente). Pour pouvoir raccorder la solution sphérique du potentiel à l'onde incidente, on l'exprime à l'aide d'un développement en polynômes de legendre (en analogie avec la fonction d'onde $\eqref{psir}$):
\begin{equation} \label{oi} \E^{\I k z} = \sum_l \I^l (2l+1) \mathrm{j}_l(kr) P_l(\cos \theta)\end{equation}
On voudrait que pour $r \gg a$ la solution générale $\eqref{psir}$ se comporte comme $\E^{\I kr}/r$, ce qui correspond à la fonction de hankel $\eqref{hinfty}$, on choisit $B_l = \I A_l$:
$$\psi(r,\theta) = \E^{\I k z} + \sum_l A_l \mathrm{h}_l(kr) P_l(\cos \theta)$$
qu'on peut récrire en utilisant $\eqref{oi}$:
\begin{equation} \label{os} \psi(r,\theta) = \sum_l \I^l (2l+1)\left[ \mathrm{j}_l(kr) + \I C_l \mathrm{h}_l(kr) \right] P_l(\cos \theta)\end{equation}
où on a redéfini les constantes $A_l$ au profit de $C_l$. Notez que $\psi$ est une superposition d'une exponentielle (onde plane) et des bessel spériques, elle est donc solution de l'équation de Schrödinger avec potentiel nul (région extérieure à la sphère rigide). Elle satisfait par construction la condition asymptotique $\eqref{asymp}$. On fixe $A_l$ en observant que pour $r = a$ on a $\psi = 0$:
$$C_l = - \frac{\mathrm{j}_(ka)}{\mathrm{h}_l(ka)}$$

Si maintenant on compare $\eqref{asymp}$ et $\eqref{os}$ on déduit:
$$f_l(k,\theta) = \sum_l \frac{2l+1}{k} C_l P_l(\cos\theta)$$
qu'on sait est reliée à la section efficace par la formule:
$$\frac{\D \sigma_l}{\D \theta} = 2\pi |f_l(k,\theta)|^2$$ 
ou
$$\sigma(k) = \frac{4\pi}{k^2}\sum_l (2l+1) |C_l|^2$$
où on a utilisé la relation d'orthogonalité des polynômes:
$$\int_{-1}^{1} \D x \, P_l(x) P_{l'}(x) = \frac{2}{2l+1} \delta_{ll'}$$
on arrive au résultat recherché:
$$\sigma(k) =  \frac{4\pi}{k^2}\sum_l (2l+1) \left| \frac{\mathrm{j}_(ka)}{\mathrm{h}_l(ka)} \right|^2$$

Le premier terme de la somme, $l = 0$ est,
$$\sigma_0(k) = \frac{4\pi}{k^2} (ka)^2 \frac{\sin^2(ka)}{(ka)^2} \approx 4\pi a^2$$
où la dernière approximation correspond au résultat en supposant basse énergie $1/k \ll a$ (la longueur d'onde de la particule est plus grande que la taille de la sphère). 

Dans cette limite de basse énergie, on peut utiliser le développement limité des fonctions de bessel sphériques:
$$\frac{\mathrm{j}_l^2}{\mathrm{j}_l^2 + \mathrm{n}_l^2} \approx \frac{\mathrm{j}_l^2}{\mathrm{n}_l^2} \approx \frac{(ka)^{2(2l+1)}}{(2l+1)^2 [(2l-1)!!]^4}$$
ce qui décroit rapidement avec $l$ ($ka < 1$). On en déduit que le terme en $l=0$ domine la diffusion à basse énergie. Cette observation est valable pour tout potentiel central de porté de l'ordre de $a$. On peut aussi remarquer que le résultat classique de la diffusion par une sphère dure est $\sigma_c= \pi r^2$ (l'aire projetée de la sphère sur la direction de la particule incidente), 4 fois plus petit que le cas quantique.


> <img src="{static}/images/MQ-diffS0.svg" alt="cross section small k" style="height: 230px;"/>
> <img src="{static}/images/MQ-diffS1.svg" alt="cross section large k" style="height: 230px;"/>
>
> Section efficace en fonction de l'énergie. À basse énergie elle approche $4\pi a^2$, tandis qu'à haute énergie elle tend asymptotiquement vers $2\pi a^2$.

#### Codes:

Voici le code de la figure du potentiel (diffusion), écrit en [``asymptote``](https://ctan.org/pkg/asymptote?lang=en):

```asy
import solids;
import graph3;
settings.render=0;
settings.prc=false;

size(250,IgnoreAspect);

// define axes
real b = 2.7;
xaxis3( "$x$", -b, b, gray(0.8) );
yaxis3( "$y$", -b, b, gray(0.8) );
zaxis3( "$z$", -b, b, gray(0.8) );
dot( (0,0,1), gray(0.5) );
dot( (0,0,-1), gray(0.5) );
dot( (0,1,0), gray(0.5) );
dot( (0,-1,0), gray(0.5) );
dot( (1,0,0), gray(0.5) );
dot( (-1,0,0), gray(0.5) );

// draw the sphere
revolution V = sphere(O,1);
draw( V, 1, longitudinalpen = nullpen );
draw( V.silhouette() );

// put labels
real theta = pi/2*1.1;
real phi = 0.2;
real R = 1.02;
triple A = (R*sin(theta)*cos(phi), R*sin(theta)*sin(phi), R*cos(theta));
label( "$r = a$", A, gray(0.5) );
label( "$V = \infty$", (0,0.5,0.6) );
label( "$V = 0$", (-0.7,1.2,1.6) );
```

Code python pour les figures de la section efficace:

```python
%pylab inline
import scipy
from scipy.special import *
#
def scat(k,N):
    # computes the cross section
    l = arange(N)
    j2 = spherical_jn(l,k)**2
    n2 = spherical_yn(l,k)**2
    h2 = j2 + n2
    return (4*pi/k**2)*sum((2*l+1)*j2/h2)
def sect(k, N):
    # test convergence as a function of N = max(l)
    return array([scat(k, n) for n in range(1, N)])
#
def sigma(k, o = 35):
    # cross section as a function of k
    return array([scat(kn,o) for kn in k])
#
# k << 1
k = linspace(0.01,1,40)
plot(k,sigma(k)/(4*pi), 'k-')
plot([0],[1],'ok')
xlabel(r"$ka$")
ylabel(r"$\sigma_l/4\pi a^2$");
#
# k >> 1
k = linspace(0.2,50,100)
plot(k,sigma(k, 60)/(4*pi), 'k-')
plot([k[0], k[-1]], [0.5, .5],'k:')
plot([0],[1],'ok')
#
xlabel(r"$ka$")
ylabel(r"$\sigma_l/4\pi a^2$");
ylim(-0.1,1.1)
yticks([0,0.5,1]);
```

## Intrication et inégalité de Bell

### Matrice densité et intrication

La matrice densité d'un système composite est définie par (voir le cours)
$$\rho=\sum_i p_i \ket{\psi_i}\bra{\psi_i}, \; \sum_i p_i = 1$$
Un système est pur si $\rho = \ket{psi}\bra{\psi}$. Soit un système pur formé de deux qubits A et B, son espace de hilbert est le produit tensoriel $\mathcal{H} = \mathcal{H}_1 \otimes \mathcal{H}_1$, des espaces de chaque qubit.  L'état $\psi \in \mathcal{H}$ n'est pas intriqué s'il peut s'écrire comme un produit:
$$\ket{\psi} = \ket{A} \otimes \ket{B}$$
autrement $\ket{\psi}$ est intriqué.

Pour tester la pureté d'un état on utilise le fait que pour un état pur $\Tr \, \rho^2 = 1$ et pour un état mixte (celui d'un système composite où chaque composante à une probabilité $p_i$ de se trouver dans l'état $\psi_i$) la trace du carré de la matrice densité est strictement inférieure à 1:
$$\Tr \, \rho^2 < 1$$
(état mixte).

Un qubit peut se trouver dans un superposition de deux états $\ket{0}$ (spin up) et $\ket{1}$ (spin down), éléments de la base canonique et vecteurs propres de la matrice de pauli $\sigma_z = Z$.

* Calculez la matrice densité d'un système d'un seul qubit dans l'état 
    $$\ket{+} = \frac{1}{\sqrt{2}} (\ket{0} + \ket{1})$$
    qui est un vecteur propre de $\sigma_x = X$.
* Calculez la matrice densité d'un système de deux qubits se trouvant dans l'état
    $$\ket{\psi} = \ket{+} \otimes \ket{+} = \ket{++}$$ 
    (on omet le symbole $\otimes$ pour simplifier la notation, notez que le premier $+$ correspond au sous-système A, et le second au B)
* Appliquez l'opérateur représenté par la matrice diagonale ($4\times4$):
    $$\mathrm{CZ} = \mathrm{diag}(1,1,1,-1)$$
    à l'état $\ket{++}$. Montrez que l'état résultant $\ket{\psi} = \mathrm{CZ} \ket{++}$ est intriqué.
* Calculez la matrice densité $\rho = \ket{\psi}\bra{\psi}$

L'état général d'un système de deux qubits est,
$$\ket{\psi} = \sum_{i,j} \psi_{ij} \ket{a_i} \otimes \ket{b_j} = \Psi \ket{A} \otimes \ket{B},\; i,j=0,1$$
où la matrice $\Psi$ représente l'état $\ket{\psi}$ (oui, on peut représenter un vecteur par une matrice!) . Avec cette notation la matrice densité correspondante est,
$$\rho = ket{A} \otimes \ket{B} \Psi \Psi^\dagger \bra{B} \otimes \bra{A}$$
(les $\Psi$ commutent avec les kets). La matrice densité réduite de A est la trace partielle sur B de $\rho$:
$$\rho_A = \Tr_B \rho = \ket{A} \Psi \Psi^\dagger \bra{A} = \sum_{ii'} (\Psi \Psi^\dagger)_{ii'} \ket{a_i}\bra{a_{i'}}$$

* Calculez la trace partielle de $\rho$ est montrez que la matrice densité réduite du premier qubit est
    $$\rho_A = \frac{1}{2} I$$
    avec $I = \mathrm{diag}(1,1)$ la matrice identité
* Discutez (point important!) la différence physique entre l'état $\ket{+}$ et l'état $\rho_A$ (le deux se réfèrent à un qubit).

On est maintenant en position d'étudier le théorème de Bell, qui nous montre qu'un état intriqué contient des corrélations non classiques (une sorte de preuve que la nature est quantique!).

### Inégalité de Bell

Alice (A) et Bob (B) ont chacun une particule (un qubit dans le cas quantique); Alice fait deux mesures sur les propriétés $Q$ et $R$ de sa particule (par exemple deux orientations du moment cinétique, ou spin dans le cas quantique) et Bob mesure $S$ et $T$; on suppose que ces propriétés ne prennent que les valeurs $+1$ ou $-1$. On s'intéresse à la grandeur 
$$O=QS + RS + RT - QT$$
La distribution de probabilité $p(q,r,s,t)$ que $Q=q$, $R=r$, $S=s$ et $T=t$ est arbitraire.

* Montrez que la valeur espérée $\mathrm{E}(O)  = \braket{O} \le 2$ (résultat classique)

Supposons maintenant que les propriétés de la particule correspondent à des opérateurs quantiques et que l'état de deux particules (deux qubits, ou deux spins) est l'état de Bell:
$$\ket{\Phi} = \frac{1}{\sqrt{2}} (\ket{01} - \ket{10})$$
Alice mesure les propriétés $Q$ et $R$ définies par les opérateurs:
$$Q = Z_A, \quad R = X_A$$
et Bob mesure $S$ et $T$:
$$S = -\frac{1}{\sqrt{2}} ( Z_B + X_B), \quad T = \frac{1}{\sqrt{2}} ( Z_B - X_B)$$

* Montrez que 
    $$\braket{O} = 2 \sqrt{2}$$
* Discutez ce résultat!

Notez que l'état quantique distribué à Alice et Bob est un état intriqué; changez-le par un quelconque état produit et voyez le résultat:

* est-il en contradiction avec le résultat classique?


