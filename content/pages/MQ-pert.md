Title: Théorie des perturbations
Slug: MQ-pert
Date: 2020-03-16
Category: Lectures
Tags: teaching, quantum mechanics, undergraduates
Authors: Alberto Verga
Summary: Cours élémentaire de mécanique quantique; méthodes de perturbation stationnaire et dépendante du temps
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

# Méthodes d'approximation

## Perturbation stationnaire

Les systèmes physiques sont généralement caractérisés par un ensemble de paramètres dimensionnels; ces paramètres ne sont pas tous indépendants, puisque les propriétés physiques sont indépendantes du système d'unités, mais peuvent s'exprimer en fonction d'un certain nombre de paramètres non dimensionnels. Par exemple, l'oscillateur harmonique avec les unités de masse, la masse de la particule $[m]$, le temps, l'inverse de la fréquence $[1/\omega]$, et la longueur, exprimée à l'aide de la constante de planck $[\ell=(\hbar/m\omega)^{1/2}]$, ne comporte aucun paramètre dimensionnel:
\begin{equation}
H_0 = \frac{p^2}{2} + \frac{x^2}{2} \tag{oscillateur}
\end{equation}
avec $x$ la position et $p$ l'impulsion adimensionnelles; de même, le hamiltonien de l'atome d'hydrogène avec le choix du rayon de Bohr $[\mathrm{a_0}]$ et du rydberg $[\mathrm{Ry}]$ comme unités de longueur et d'énergie,
$$\mathrm{a_0} = \frac{4\pi \epsilon_0 \hbar^2}{m e^2}, \quad \mathrm{Ry} = \frac{\hbar^2}{2m a_0^2}$$
ainsi que de la masse réduite comme unité de masse (unités atomiques), se réduit à la forme adimensionnelle, 
\begin{equation}
  H_0 = \frac{\bm p^2}{2} - \frac{2}{r} \tag{coulomb}
\end{equation}
avec $r$ le rayon en coordonnées sphériques (avec origine le centre de masse), distance entre le noyau et l'électron, et $\bm p$ leur impulsion relative.

Souvent parmi ces paramètres sans dimensions on en trouve un petit, disons
$$\lambda \ll 1\,.$$
Par exemple, l'atome d'hydrogène peut être soumis à un champ extérieur de faible énergie par rapport au rydberg: un champ électrique $\mathcal{E}$ (dirigé selon la direction $z$) qui interagit avec le dipôle atomique, et dont l'énergie est donnée par $V = -ez\mathcal{E}$. Dans ce cas, le paramètre sans dimensions approprié est le rapport de l'énergie du dipôle (à l'échelle du rayon de Bohr) et du rydberg:
$$\lambda = \frac{e \mathrm{a_0} \mathcal{E}}{\mathrm{Ry}} \ll 1$$
ce qui est généralement vrai pour des champs électriques typiques utilisés en laboratoire dans les expériences de spectroscopie atomique. Par conséquent, le hamiltonien du système physique comportant un petit paramètre peut se séparer en deux parties, la partie $H_0$ du système sans perturbation, et $\lambda V$, le terme de perturbation:
\begin{equation}
  H = H_0 + \lambda V,\quad \lambda \ll 1\,.
\end{equation}
Le terme de *perturbation* aura donc un faible effet sur les niveaux d'énergie $\varepsilon_n$ et les fonctions propres $\ket{n}$, du système non perturbé:
\begin{equation}
  H_0 \ket{n} = \varepsilon_n \ket{n}
\end{equation}
où l'on suppose un spectre discret, ici $n$ est le nombre quantique associé à l'énergie (e.g. les niveaux de l'oscillateur ou de l'atome d'hydrogène, selon la signification de $H_0$).

L'idée de la méthode de perturbation est de construire les états propres et les énergies de $H$ par des approximations successives en puissances du petit paramètre $\lambda$, à partir de la base d'états $\ket{n}$ et des énergies $\varepsilon_n$ du système non perturbé. Nous allons donc chercher les vecteurs propres $\ket{N}$ et valeurs propres $E_n$ de $H$
\begin{equation}
  \label{e:pHvp}
  H \ket{N} = E_n \ket{N}\,,
\end{equation}
sous la forme des séries,
\begin{align}
  E_n &= \varepsilon_n + \lambda E_{n}^{(1)} + \lambda^2 E_{n}^{(2)} + \cdots 
  \nonumber \\
  \ket{N} &= \ket{n} + \lambda \ket{N^{(1)}} + \lambda^2 \ket{N^{(2)}} + \cdots 
  \label{e:pS}
\end{align}
où les indices entre parenthèses correspondent à l'ordre de l'approximation. Nous commençons par le cas non dégénéré, dans lequel chaque valeur propre $\varepsilon_n$ correspond à un unique vecteur propre $\ket{n}$. La base de $H_0$ est orthonormée; nous pouvons aussi supposer
\begin{equation*}
\braket{n|N^{(i)}} = 0,\quad i=1,2,\ldots
\end{equation*}
Après substitution de \eqref{e:pS} dans \eqref{e:pHvp}, on obtient à l'ordre $\lambda$:
\begin{equation}
  \label{e:po1}
  (H_0 - \varepsilon_n) \ket{N^{(1)}} = (E_n^{(1)} -V) \ket{n}\,.
\end{equation}
En multipliant cette équation d'abord par $\bra{n}$, nous obtenons la première correction de l'énergie:
\begin{equation}
  \label{e:pE1}
  E^{(1)}_n = \braket{n|V|n}\,;
\end{equation}
en la multipliant ensuite par $\bra{m}$ (avec $m \ne n$), nous obtenons,
$$
  (\varepsilon_m - \varepsilon_n) \braket{m|N^{(1)}} =
  - \braket{m|V|n}
$$
qu'on peut compléter par l'unité $\sum_m \ket{m} \bra{m} = 1$ pour déduire la correction de l'état propre à l'ordre 1:
\begin{equation}
  \label{e:pV1}
  \ket{N^{(1)}} = \sum_{m \ne n} \frac{\braket{m|V|n}}{\varepsilon_n - \varepsilon_m}\ket{m}\,.
\end{equation}
À l'ordre suivant, en $\lambda^2$, l'équation \eqref{e:pHvp} donne,
\begin{equation}
  \label{e:po2}
  (H_0 - \varepsilon_n) \ket{N^{(2)}} = 
  E^{(2)}_n \ket{n} + (E^{(1)}_n - V) \ket{N^{(1)}}\,.
\end{equation}
En suivant la même méthode nous obtenons, après multiplication à gauche par $\bra{n}$, l'expression $E^{(2)} = \braket{n|V|N^{(1)}}$; ou, en substituant dans celle-ci l'équation \eqref{e:pV1}, et en observant que $\braket{n|N^{(1)}}=0$, nous aboutissons à 
\begin{equation}
  \label{e:pE2}
  E^{(2)}_n = \sum_{m \ne n} 
  \frac{|\braket{m|V|n}|^2}{\varepsilon_n - \varepsilon_m}\,.
\end{equation}
Les équations \eqref{e:pE1} et \eqref{e:pE2} sont le principaux résultats de la théorie des perturbations indépendantes du temps. Elles peuvent se résumer dans la formule:
\begin{equation}
  \label{e:pE12}
  E_n = \varepsilon_n + \lambda \braket{n|V|n} +
  \lambda^2 \sum_{m \ne n} 
  \frac{|\braket{m|V|n}|^2}{\varepsilon_n - \varepsilon_m}\,.
\end{equation}
L'utilisation pratique de la méthode de perturbation est simple: on résout d'abord le problème à valeurs propres du hamiltonien non perturbé pour avoir la forme explicite des niveaux d'énergie et des vecteurs propres $\varepsilon_n$ et $\ket{n}$; pour ensuite calculer la correction en $\lambda$ par la formule \eqref{e:pE1}; si celle-ci s'avère être nulle (cela dépend de la forme de $V$), on passe à l'ordre suivant et on calcule $E_n^{(2)}$ à l'aide de \eqref{e:pE2}. L'effet physique d'une petite perturbation sur un niveau non dégénéré est de déplacer le niveau d'énergie d'une grandeur de l'ordre de $\lambda$ ou de $\lambda^2$, sans affecter qualitativement les propriétés du système non perturbé.

Si l'état d'énergie $\varepsilon_n = \varepsilon$ est dégénéré $D$ fois, la perturbation $V$ introduit un effet physique intéressant, la *levée de dégénérescence*, qui change qualitativement les propriétés du système original $H_0$. Pour trouver les niveaux d'énergie perturbés il suffit de considérer le sous-espace de dimension $D$, dans lequel la forme du hamiltonien dans la base $\ket{n}$, est
$$
  H_{D} = \begin{pmatrix}
    \varepsilon + \lambda v_{11} & \lambda v_{12} 
                                 & \cdots & \lambda v_{1{D}} \\
    \lambda v_{21} & \varepsilon +\lambda v_{22} & \cdots &  \\
    \vdots & & \ddots & \\
    \lambda v_{{D}1} & & & \varepsilon + \lambda v_{DD}
  \end{pmatrix}  = \varepsilon 1_{D}+ \lambda V_{D}
$$
avec $1_{D}$ la matrice unité et $V_{D}$ la perturbation dans le sous-espace $D$, et de résoudre le problème de valeurs et vecteurs propres. Les états d'énergie au premier ordre de la théorie de perturbation d'un état dégénéré, sont donc les racines $E$ du polynôme caractéristique:
\begin{equation}
  \label{e:pED}
  \det \left( \lambda V_{D} - E^{(1)} 1_{D} \right) = 0\,,\quad
  E^{(1)} = E_{n1}, \ldots, E_{nD}\,.
\end{equation}
En effet, $H_D$ est diagonal avec unique valeur propre $\varepsilon$ pour $\lambda = 0$; au premier ordre, \eqref{e:pED} permet de calculer la correction à l'ordre $\lambda$ du niveau dégénéré, dans chacune des directions données par les vecteurs propres de \eqref{e:pED}.




## Problèmes

### 1
Montrez que si $\ket{\psi_\lambda}$ est un état qui diffère d'une grandeur d'ordre $\lambda$ de l'état fondamental $\ket{\psi_0}$, l'énergie $E(\lambda)=\langle \psi_\lambda|H|\psi_\lambda\rangle$ diffère de $E_0$, l'énergie de l'état fondamental, d'une grandeur d'ordre $\lambda^2$.

### 2
Estimez l'énergie de l'état fondamental d'un oscillateur quartique:
$$
H=\frac{p^2}{2m}+\lambda x^4\,.
$$
par la méthode variationnelle. Utilisez comme ansatz une fonction d'onde gaussienne; comparez le résultat avec celui du cours:
$$E = \frac{9}{2\times286^{1/3}}\lambda^{1/3}$$

### 3
Une particule est soumise à l'action d'un potentiel central,
$$
V(r)=-\frac{4\hbar^2}{3ma^2}\E^{-r/a}
$$
Avec $\psi(r;\alpha)\sim\exp(-\alpha r/a)$ comme fonction test, calculez la valeur de $\alpha$ qui minimise l'erreur sur l'énergie de l'état fondamental.
  
### 4
Calculez les niveaux d'énergie du hamiltonien
$$
H=\left(
\begin{array}{ccc}
1  & 0  & 0  \\
0  & 3  & 0  \\
0  & 0  & -1  
\end{array}
\right)+
\left(
\begin{array}{ccc}
0  & b  & 0  \\
b  & 0  & 0  \\
0  & 0  & b  
\end{array}
\right)\,.
$$
Comparez le résultat avec celui de la théorie des perturbations ($b\ll1$ petit).

### 5
Une particule dans une boîte [$V_0(x)=0,\;0\le x\le a$ et $V_0(x)=\infty$ ailleurs] est perturbée par un potentiel $V(x)=-\lambda\sin(\pi x/a)$. Calculez approximativement l'énergie de l'état fondamental.

### 6
Une particule dans une boîte [$V(x)=0,\;-L/2\le x\le L/2$ et $V(x) = \infty$ ailleurs] est perturbée par un potentiel $V(x)=v,\;-a/2\le x\le a/2$, avec $v>0$ et $a<L$. Calculez les niveaux d'énergie en perturbation.

### 7
Un oscillateur harmonique $H_0$ de masse $m$ et fréquence $\omega$ est perturbé par un potentiel $V$ quartique en $x$.
$$
  H=H_0+V=\frac{p^2}{2m}+\frac{m \omega^2}{2}x^2+g x^4\,.
$$
où $g$ est la constante de couplage.

* Trouvez le paramètre adimensionnel $\lambda$ de couplage, dans les unités naturelles de $H_0$; travaillez par la suite dans ce système d'unités (dans lequel $H_0$ ne contient aucun paramètre). 
* Calculez par perturbation les niveaux d'énergie du hamiltonien. Utilisez les opérateurs $a$ et $a^\dagger$ pour calculer les éléments de matrice $\braket{m|V|n}$ de la perturbation $V\sim x^4$.
* Discutez la limite de validité, selon le niveau d'énergie, de la série de perturbation.

### 8
Une particule de masse $m$ se trouve dans un puits de potentiel bidimensionnel infini
$$
V(x,y) = \begin{cases} 0 & \text{if}\quad 0 \le x,y \le a \\
\infty & \text{ailleurs} \end{cases}
$$
Calculez les énergies du niveau fondamental et du premier niveau excité en présence d'une perturbation $V(x,y) = v x^2$ ($0\le x\le a$). Tenez compte d'éventuelles dégénérescences. Faites le graphe des niveaux d'énergie sans et avec perturbation et discutez l'effet de celle-ci.

### 9
Un atome d'hydrogène se trouve dans un champ magnétique extérieur constant $\bm B$ de faible intensité; le potentiel de la perturbation est 
  $$
    V= \frac{e}{m}\bm L \cdot \bm B  
  $$
  où $\bm L$ est le moment angulaire orbital de l'électron. Nous négligeons par simplicité, l'effet dû au spin (effet Zeeman).  Calculez le déplacement des énergies $\varepsilon_n$ des états $\ket{nlm}$. Discutez la levée de dégénérescence de ces niveaux. Remarquez que vous pouvez choisir un axe de quantification dans la direction du champ extérieur.

### 10
(Désintégration beta) Un atome de tritium $^3$H, charge nucléaire $Z=1$, se transforme en un atome He$^+$, $Z=2$. Calculez la probabilité de trouver l'électron, après le changement soudain de charge, dans son état fondamental.

### 11
(Changement d'orbital) Calculez la probabilité de transition de l'état 1s à l'état 2p d'un atome H soumis à un champ électrique dirigé selon $z$:
$$
\mathcal{E}=\mathcal{E}_0\E^{-t/\tau},\quad t>0\,.
$$
Calculez au premier ordre de la perturbation, la probabilité de transition vers les trois états p $m=-,1,0,1$), à des temps longs $t \gg \tau$.

### 12
(Excitation d'énergie) Une molécule se trouve dans un état de vibration $n=2$, avec une énergie $E_n=E_2=3\hbar \omega_0/2$, correspondant à l'hamiltonien d'un oscillateur harmonique de fréquence $\omega_0$. À $t=0$ on l'excite avec un champ électrique:
$$
\bm{\mathcal{E}}(t)=\mathcal{E}_0\cos(\omega_0t)\,,
$$
dans la direction de l'axe de la molécule ($x$). Écrivez le nouveau hamiltonien à $t>0$ sous la forme $H=H_0(p,x)+f(t)V(x)$ ($V$ est donc dû au moment dipolaire $qx$).

Calculez les éléments de matrice $V_{2n}$ et déduisez les probabilités de transition $P_{2n}$ en considérant l'approximation de perturbation harmonique à temps courts ($t\ll\omega_0^{-1}$). 

### 13
Considérez un système à deux niveaux $E_1<E_2$ perturbé par un potentiel:
$$
V_{11}=V_{22}=0,\quad V_{12}=V^*_{21}=V_0\E^{\I\omega t}.
$$
Initialement le système se trouve dans l'état 1, les amplitudes de probabilité sont $c_1(0)=1$ et $c_2(0)=0$. Résolvez exactement le problème (trouvez $\ket{\psi(t)}=c_1(t)\ket{1}+c_2(t)\ket{2}$) et comparez la probabilité de transition $P_{12}$ avec le résultat de la théorie des perturbations ($V_0$ petit) dans le cas $\omega\approx\omega_{12}$ et dans le cas $\omega\ll\omega_{12}$.

### 14
Un oscillateur quantique qui se trouve initialement dans son état fondamental, est perturbé par une *force*,
$$F(t) = F_0 \E^{-t/\tau}, \quad (t>0)$$
Calculez au premier ordre de la théorie de perturbations dépendante du temps la probabilité d'excitation de l'oscillateur vers des états de plus haute énergie.

