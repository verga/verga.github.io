Title: Théorie de la Diffusion
Slug: MQ-diffusion
Date: 2020-03-10
Category: Lectures
Tags: teaching, quantum mechanics, undergraduates
Authors: Alberto Verga
Summary: Cours élémentaire de mécanique quantique; diffusion par un potentiel central
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

# Théorie de la diffusion élastique par un potentiel central

La collision entre deux particules est un processus d'interaction tel que les états initial et final peuvent être considérés comme étant proches de ceux des particules libres; ceci implique l'existence d'une longueur et d'un temps caractéristiques de collision. En effet, les particules, initialement séparées par une distance $r$ très grande par rapport à la portée de l'interaction $V(r)$, disons $\ell$, s'éloignent à des grandes distances après la collision. On a donc bien avant et bien après la collision $r \gg \ell$. Le temps de collision $\tau$, est par conséquent court par rapport à la durée du processus $t \gg \tau$, de telle façon à ce qu'on peut considérer les états initial et final comme étant stationnaires. On peut en outre supposer que la collision ne change pas l'énergie $E$ des particules, auquel cas on dit que la diffusion est *élastique*. Un diffusion inélastique implique par exemple un changement de niveau d'énergie, ou même un transformation dans une autre particule, de la particule incidente après échange avec l'autre particule.

On a donc, un processus de superposition des deux états stationnaires $\psi_i$, l'état "initial" des particules incidentes l'une sur l'autre, et un état "final" $\psi_f$, de l'onde sortante, qui doit tenir compte du centre de diffusion (voir le schéma dans la figure).

Il convient de décrire la collision entre les deux particules de masse $m_1$ et $m_2$, dans le repère inertiel (centre des masse), de telle façon que les grandeurs physiques ne dépendent que de la distance $r$ entre les particules. Dans ce repère la collision est celle d'une particule effective de masse réduite
$$m = \frac{m_1 m_2}{m_1 + m_2}$$
incident avec une énergie $E$ sur un centre de diffusion $V(r)$ fixe. Ainsi, l'état initial est simplement celui d'une onde plane,
$$\psi_i = \E^{\I k z}, \quad k = \sqrt{\frac{2mE}{\hbar^2}}$$
La fonction d'onde $\psi_i$, d'amplitude 1, représente un flux (densité de courant de probabilité) égale à la vitesse de la particule $v = \hbar k/m$.

Après la collision, la particule est diffusée par l'interaction $V(r)$, essentiellement comme un onde radiale:
$$\psi_f \sim \psi_i + f(k,\Omega) \frac{\E^{\I k r}}{r}$$
où $f(k,\Omega)$ est l'*amplitude de diffusion*, qui dépend de l'angle solide $\Omega$ défini par la direction de la particule diffusée $\bm r/r$ par rapport à la direction incidente $\hat{\bm z}$ (voir figure). Dans le cas qui nous intéresse où $V=V(r)$, l'amplitude de diffusion ne dépend que de l'angle sphérique $\theta$, avec $\D \Omega = 2\pi \sin \theta \D \theta$, et de l'énergie $E$.

> <img src="{static}/images/MQ-sigma.svg" alt="scattering cross section" style="height: 230px;"/>
> 
> Onde plane incidente vers un centre de diffusion $V(r)$, dont la portée est de l'ordre de $\ell$, et onde sphérique sortante d'amplitude de diffusion $f$ dans l'angle solide $\Omega$.

La forme de la fonction d'onde sortante découle de la forme des solutions asymptotiques de l'équation de schrödinger (pour de valeurs $r \rightarrow \infty$). En effet, on peut écrire,
$$ \frac{\hbar^2}{2m} \nabla ^2 \psi_k(\bm r) + E_k \psi_k(\bm r) = V(r) \psi_k (\bm r)$$
et utiliser la solution de l'équation de Green,
$$\left( \frac{\hbar^2}{2m} \nabla ^2 + E_k \right) G_k(\bm r) = \delta(\bm r)$$
avec $G$ la fonction de Green, pour transformer l'équation pour $\psi_k$ en équation intégrale:
$$\psi_k(\bm r) = \E^{\I k z} + \int \D \bm r'\, G_k(\bm r - \bm r') V(\bm r') \psi_k(\bm r')$$

La fonction de Green pour l'onde sortante (c'est-à-dire $\sim \E^{\I k r}$), est donnée par l'intégrale
$$G_k(\bm r) = \int \frac{\D \bm p}{(2\pi)^3} \frac{\E^{\I \bm p \cdot \bm r}}{E_k - \hbar^2p^2/2m} $$
calculée sur un contour qui se referme par le demi-plan complexe *supérieur*. (Celle correspondante à un contour sur le demi-plan inférieur est associée à une onde entrante de l'infini $\sim \E^{-\I k r}$.) On obtient, du résidu en $p = k$, $$G_k(\bm r) = -\frac{m}{2\pi \hbar^2} \frac{\E^{\I k r}}{r}$$ ce qui permet d'écrire l'équation de schrödinger comme, $$\psi_k(\bm r) =  \E^{\I k z} - \frac{m}{2\pi \hbar^2} \int \D \bm r'\, \frac{\E^{\I k |\bm r-\bm r'|}}{|\bm r - \bm r'|} V(\bm r') \psi_k(\bm r')$$ 

> <img src="{static}/images/MQ-Gcontour.svg" alt="outgoing Green function countour" style="height: 230px;"/>
> 
> Contour dans le plan complexe $p$ pour le calcul de la fonction de Green sortante.

> Calcul de $G$:
>
$$G_k(\bm r) = -\frac{m}{2 \pi^2 \hbar^2} \int_0^\infty \frac{\D p \, p}{p^2 - k^2} \int_0^\pi \D\theta \, \sin\theta \E^{\I p r \cos\theta}$$
> 
> l'intégrale sur $\theta$ donne
> 
$$\int_0^\pi \D\theta \, \sin\theta \E^{\I p r \cos\theta} = \frac{\E^{\I p r} - \E^{-\I p r}}{\I p r}$$
>  d'où,
$$G_k(\bm r) = -\frac{m}{2 \pi^2 \hbar^2 \I r} \int_0^\infty \D p \, p \frac{\E^{\I p r} - \E^{-\I p r}}{p^2 - k^2}$$
> 
> la seconde intégrale peut s'ajouter à la première après le changement $p \rightarrow -p$:
>
$$G_k(\bm r) =  -\frac{m}{2 \pi^2 \hbar^2 \I r} \int_{-\infty}^\infty \D p \, p \frac{\E^{\I p r}}{p^2 - k^2}$$
> 
> On sépare le deux pôles:
>
$$ \frac{p}{p^2 - k^2} = \frac{p}{2k} \left[ \frac{1}{p-k} - \frac{1}{p+k} \right]$$
>
> dont seulement le premier contribue à $G$:
>
$$G_k(\bm r) = -\frac{m}{2  \pi^2 \hbar^2 \I r} \left( 2\I \pi \frac{k}{2k}  \E^{\I k r} \right)$$
> ce qui donne le résultat.

À des distances $r \gg \ell$ on a $V(r) \rightarrow 0$, et $k |\bm r = \bm r'| \approx kr - \bm k' \cdot \bm r'$ ($\bm k' = k \hat{\bm r}$ est le vecteur d'onde d'après la collision); par conséquent,
$$\int \ldots \frac{\E^{\I |\bm r-\bm r'|}}{|\bm r - \bm r'|} \ldots \approx \frac{\E^{\I k r}}{r} \int \ldots \E^{-\I \bm k' \cdot \bm r'} \ldots$$
dont on déduit l'expression asymptotique de $\psi_k(\bm r)$ avec
\begin{equation}
    f(k,\Omega) = -\frac{m}{2 \pi^2 \hbar^2} 
    \int \D \bm r' \E^{-\I \bm k' \cdot \bm r'} V(\bm r') \psi_k(\bm r')
    \label{f}
\end{equation}

## Section efficace de diffusion

La densité courant de probabilité $j$ est reliée à la fonction d'onde par la relation
$$ \bm j = \frac{\hbar}{m} \mathrm{Im} \left[ \psi^\star \nabla \psi \right]$$
Pour l'onde incidente on a
$$\bm j_i = n_k \bm v_k = \frac{\hbar k}{m} \hat{\bm z}$$
avec $v_k = (\hbar/m) k$ la vitesse et $n_k = |\psi_k|^2 = 1$ (selon la normalization choisie) la densité de probabilité. Selon la formule asymptotique, le flux de probabilité transmis après la collision est 
$$j_f \approx \frac{\hbar k}{m} |f(k,\Omega)|^2 \frac{\hat{\bm r}}{r^2}$$
où nous avons utilisé l'approximation $\nabla(1/r) \sim 1/r^2$ et $\nabla f \sim f/r$.
Si une source fournit un flux $F_k = n_k v_k$ de particules par unité de temps, le nombre de particules détectées sur une surface $\D \bm S$, dans l'angle solide $\D \Omega$, serait,
$$\D N = \bm j_f \cdot \D \bm S = \frac{\hbar k}{m} |f(k, \Omega)|^2 \D \Omega = F \frac{\D\sigma}{\D \Omega} \D \Omega$$
avec $\D S = r^2 d\Omega$ et
\begin{equation}
    \frac{\D\sigma}{\D \Omega} = |f(k,\Omega)|^2
    \label{sigma} 
\end{equation}
la *section efficace différentielle,* ou par unité d'angle solide, $\sigma = \sigma(k, \Omega)$. C'est justement cette grandeur $\sigma$ ayant les dimensions d'une aire par unité d'angle solide, qui est la grandeur mesurable dans les expériences de collision.

## Approximation de Born

Si on remplace dans cette dernière formule ($\ref{sigma}$) la fonction d'onde par l'onde incidente, on obtient l'*approximation de Born*:
\begin{equation}
    f(k,\Omega) = -\frac{m}{2 \pi^2 \hbar^2}
    \int \D \bm r' \E^{\I (\bm k - \bm k') \cdot \bm r'} V(\bm r') =
    -\frac{m}{2 \pi^2 \hbar^2} V_{\bm k - \bm k'}
    \label{born}
\end{equation}
($\bm k = k \hat{\bm z}$ est le vecteur d'onde d'avant la collision) dans laquelle l'amplitude de diffusion est donnée par la transformée de fourier de l'interaction.

En tenant compte du caractère élastique de la collision on a $k=k'$, donc,
$$q^2 = (\bm k - \bm k')^2 = 2k^2 - 2k^2 \cos\theta = (2k\sin\theta/2)^2$$
Pour un potentiel du type de Yukawa, qui modélise les interaction de nucléons,
$$V(r) = g \frac{\hbar c}{r} \E^{-r/\ell}$$
avec $g$ une constante adimensionnelle et $\ell$ la portée, la transformée de fourier est
$$V_q = 4\pi\ell^2  \frac{\hbar c g}{(\ell q)^2 + 1}$$
ce qui donne pour la section efficace,
$$\frac{\D\sigma}{\D\Omega} = \frac{(\hbar c g)^2}{\left( 4 E_k \sin^2\theta/2 + \epsilon^2 \right)^2},\quad \epsilon = \frac{\hbar^2}{2m\ell^2} $$
exprimée comme une fonction de l'énergie $E_k=\hbar^2 k^2/2m$ et de l'angle de difussion $\theta$. Notez que quand $\ell \rightarrow \infty$ on retrouve le résultat classique pour la diffusion dans un potentiel coulombien, la formule de Rutherford (en dépit du fait que les hypothèses de validité de l'approximation de Born, sont dans le cas coulombien, fausses!).

## Amplitude de diffusion et déphasage

Pour tirer parti de la conservation du moment angulaire du fait de l'isotropie de l'interaction, il convient d'écrire la fonction d'onde dans la base des harmoniques sphériques. Ceci nous permettra d'exhiber les propriétés de la diffusion pour les différentes valeurs du nombre quantique orbital $l$. L'onde incidente (avec $\bm k$ parallèle à l'axe $z$, axe de symétrie de la diffusion) se decompose en polynômes de legendre $P_l = Y_{l0}$:
$$\E^{\I \bm k \cdot \bm r} = \sum_{l=0}^\infty \I^l (2l+1) P_l(\cos\theta) \mathrm{j}_l(r)$$
où $\mathrm{j}_l(kr)$ est la fonction de [Bessel sphérique](https://en.wikipedia.org/wiki/Bessel_function), elle est la partie réelle de la fonction sphérique de hankel,
$$\mathrm{j}_l(kr) = \frac{1}{2} \left[ \mathrm{h}_l(kr) + \mathrm{h}^\star_l(kr) \right]$$
Tandis que la fonction d'onde sortante s'écrit comme,
$$\psi_k(\bm r) = \sum_{l=0}^\infty \I^l (2l+1) P_l(\cos\theta) R_l(r)$$
avec $R_l(r)$ la fonction d'onde radiale; elle obéit à l'équation de schrödinger,
$$\left[ \frac{\D^2}{\D r} + k^2 - \frac{l(l+1)}{r^2} \right] r R_l(r) = \frac{2m}{\hbar^2} V(r) r R_r(r)$$
Pour des grandes distances, dans la région où le terme du potentiel devient négligeable, la solution générale est de la forme,
$$R_l(r) = B_l \left[ \mathrm{h}_l^\star(kr) + S_l(E_k) \mathrm{h}_l(kr) \right]$$
avec $B$ et $S$ deux constantes qu'on détermine à l'aide des conditions aux limites. Rappelons le comportement asymptotique des fonctions de hankel:
$$\mathrm{h}_l(z) \sim \frac{\E^{\I z - \I\pi l/2 - \I\pi/2}}{z}$$
donc $\mathrm{h}^\star$ doit être associée à l'onde entrante (d'amplitude 1) et $\mathrm{h}$ à l'onde sortante; comme le potentiel ne modifie pas l'onde entrante on doit avoir (par comparaison avec l'expression de $\E^{\I k z}$, $B_l=1/2$. En outre, on doit aussi avoir $|S_l|=1$ (dans la collision élastique le nombre de particules entrant et sortant est le même pour toute valeur de $E$). On défini le déphasage $\delta_l$ entre l'onde entrante et sortante par la relation:
$$S_l(E_k) = \E^{\I 2 \delta_l(k)}$$
On cherche le lien entre l'amplitude de diffusion $f(k,\Omega0$ et le déphasage $\delta_l(k)$. Dans ce but on étudie le comportement asymptotique de la solution radiale à l'équation de schrödinger.

Avec ces définitions, on écrit la fonction d'onde diffusée comme,
$$\psi_k(\bm r) = \E^{\I \bm k \cdot \bm r} + \sum_{l=0}^\infty \I^l (2l+1) P_l(\cos\theta) \left( \E^{\I 2\delta_l} - 1 \right) \mathrm{h}_l(kr)$$
(la fonction de hankel conjuguée $\mathrm{h}^\star$, a été absorbée dans le premier terme, celui de l'onde plane) et en comparant avec la formule,
$$\psi_k(\bm r) = \E^{\I \bm k \cdot \bm r} +  \frac{f(k,\Omega)}{r} \E^{\I k r}$$
on arrive à l'identification ($\mathrm{h}_l(kr) \sim \E^{\I kr}/\I^{l+1} kr$),
\begin{equation}
    f(k,\theta) = \frac{1}{k}
    \sum_{l=0}^\infty (2l+1) P_l(\cos\theta)
    \E^{\I \delta_l} \sin\delta_l
    \label{fk}
\end{equation}
La section efficace est donnée par l'intégrale sur $\D\Omega$ de $|f|^2$, ce qui est facile de calculer tenant compte de la relation d'orthogonalité des polynômes,
$$\frac{1}{2}\int_{-1}^{1} \D x \, P_l(x) P_{l'}(x) = \frac{\delta_{ll'}}{2l +1}$$
On obtient,
$$\sigma_l = \frac{4\pi}{k^2}(2l+1)\sin^2\delta_l$$ 
ou, pour la section efficace totale,
$$\sigma(E) = \frac{4\pi}{k^2} \sum_{l=0}^\infty (2l+1) \sin^2\delta_l(E)\,,$$
qui est une fonction de l'énergie de la particule $E=E_k=\hbar^2 k^2/2m$.

### Bibliographie

* Griffiths, David J., and Darrell F. Schroeter (1995). Introduction to quantum mechanics. Cambridge University Press, 2018.
* Cohen-Tannoudji, Claude, Bernard Diu, and Franck Laloë (1973). Mécanique Quantique: Nouvelle édition. EDP sciences, 2018.

### Problèmes

1. Montrez que la section efficace de la diffusion par une sphère rigide de rayon $a$,
    $$V(r) = \begin{cases} 0\,, & r \le a\\ \infty\,, & r > a \end{cases}$$
    est
    $$\sigma = \frac{4\pi}{k^2} \sum_{l=0}^\infty (2l+1) \left| \frac{\mathrm{j}_l(ka)}{\mathrm{h}_l(ka)}  \right|^2$$
    Étudiez la limite $ka \ll 1$; quelle est la valeur de $l$ qui contribue davantage à la diffusion?
2. Diffusion en une dimension. Considérez le problème du mouvement d'une particule de masse $m$ et énergie $E>0$ dans la demi droite négative ($x<0$):
    $$V(r) = \begin{cases} 0\,, & x < -a\\ -V_0\,, & -a \le x \le 0\\ \infty\,, & x > 0 \end{cases}$$
    Trouvez la fonction d'onde et montrez explicitement que l'amplitude de l'onde réfléchie est de valeur absolu égale à 1 (l'amplitude de l'onde incidente est 1). Montrez que pour $E \ll V_0$ le déphasage entre l'onde entrante et l'onde sortante est $\delta = - ka$.
3. Utilisez l'approximation de Born pour calculer la section efficace en fonction de l'énergie $E$, pour le potentiel 
    $$V(r) = V_0 \E^{-(r/a)^2}$$
    Réponse:
    $$\sigma = \frac{\pi^2}{2} \frac{V_0^2}{\epsilon^2 k^2}\left(1 - \E^{-2a^2k^2} \right)$$
    avec $\epsilon = \hbar^2/m a^2$ l'unité d'énergie, et $k^2=2mE/\hbar^2$.
4. Démontrez le théorème optique:
    $$\sigma = \frac{4\pi}{k} \mathrm{Im}\, f(0)$$


## Applications

### Le puits sphérique

On se propose d'étudier la diffusion d'une particule de masse $m$ et d'énergie $E$ par un potentiel central constant $-V_0$ et de portée $\ell$:
$$V(r) = -V_0 \Theta(\ell - r)$$
avec $\Theta$ la marche de heaviside (il est nul pour $r > \ell$). La solution $\psi(\bm r)$, de l'équation stationnaire de schrödinger est séparable dans les coordonnées sphériques $(r,\theta, \phi)$:
$$\psi(\bm r) = R_l(r) Y_{lm}(\theta, \phi)$$
avec $R_l$ la partie radiale et $Y$ les harmonique sphériques (fonctions propres de l'opérateur du moment cinétique $\bm L$); $l$ est le nombre quantique orbital, et $m$ le nombre quantique magnétique (valeur propre de $L_z$),
$$L^2 Y_{lm} = \hbar^2 l(l+1) Y_{lm}, \quad L_z Y_{lm} = \hbar m Y_{lm}$$

> <img src="{static}/images/MQ-puits-r.svg" alt="spherical well" style="height: 230px;"/>

Il convient de définir $m=\ell=\hbar=1$ comme les unités naturelles du problème; $\hbar^2/m \ell^2$ est donc l'unité d'énergie. Le nombre d'onde est, pour $r>\ell$, $k=(2mE/\hbar^2)^{1/2} \rightarrow k = \sqrt{2E}$; dans la région centrale $r < \ell$, le nombre d'onde est $q=\sqrt{2}\sqrt{E+V_0}$. Avec ces notations, l'équation radiale s'écrit,
$$\left( \frac{\D^2}{\D r^2} + \frac{2}{r} \frac{\D}{\D r} - \frac{l(l+1)}{r^2} + k^2 \right) R_l(r) = 0, \; r > \ell$$
et pour $r<\ell$ on remplace $k$ par $q$. La solution de cette équation différentielle est donnée par une combinaison linéaire des fonctions de bessel sphériques:
$$\mathrm{j}_l(\rho) = (-\rho)^l \left( \frac{1}{\rho} \frac{\D}{\D \rho} \right)^l \frac{\sin \rho}{\rho}$$
et
$$\mathrm{n}_l(\rho) = -(-\rho)^l \left( \frac{1}{\rho} \frac{\D}{\D \rho} \right)^l \frac{\cos \rho}{\rho}$$
ou des fonctions de hankel:
$$\mathrm{h}_l(\rho) = \mathrm{j}_l(\rho) + \I \mathrm{n}_l(\rho), \quad \mathrm{h}^\star_l(\rho) = \mathrm{j}_l(\rho) - \I \mathrm{n}_l(\rho)$$
En fonction des bessels, l'onde radiale est
$$R_L(r) = C \mathrm{j}_l(qr), \; r \le \ell$$
et
$$R_L(r) = A \mathrm{j}_l(kr) + B \mathrm{n}_l(kr), \; r > \ell$$
avec $A,B,C$ des constantes qu'on doit déterminer par la condition de normalization (ici le flux de particules) et la continuité de $R_l(r)$ et de sa dérivée en $r=\ell$. Le terme en $C$ correspond à la solution "intérieure", elle est fortement dépendante des détails du potentiel, ici visible par sa dépendance sur $V_0$ à travers $q$; le terme en $A,B$ est le terme de diffusion, il correspond à la superposition des ondes incidente et transmise dans la région "extérieure" (au delà de la portée du potentiel).

La solution pour $r > \ell$ peut donc s'écrire
$$R_L(r) = \frac{1}{2} \mathrm{h}^\star_l(kr) + \frac{\E^{\I 2 \delta_l(k)}}{2} \mathrm{h}_l(kr), \; r > \ell$$
avec $1/2 = A + \I B$ et $\E^{\I 2 \delta_l} = A - \I B$ (où nous avons posé comme auparavant, que le flux incident est 1), ce qui nous permet de faire le lien avec le déphasage dû à la diffusion. À la discontinuité du potentiel la dérivée logarithmique de la fonction d'onde,
$$\alpha_l = \left. \frac{\D R_l(r)}{\D r} \right|_{r = \ell} = q \left. \frac{\D \ln \mathrm{j}_l(q r)}{\D r} \right|_{r = \ell}$$
doit être continue:
$$\alpha_l = \left. \frac{\D}{\D r} \ln\Big(\mathrm{h}^\star_l +  \E^{\I 2 \delta_l(k)} \mathrm{h}_l \Big) \right|_{r = \ell}$$ 
D'où on peut dégager $\delta_l$:
$$\cot \delta_l = \left. \frac{\mathrm{n}'_l - \alpha_l \mathrm{n}_l}{\mathrm{j}'_l - \alpha_l \mathrm{j}_l} \right|_{r=\ell}$$
Avec la valeur de $\alpha_l$ donnée par la solution intérieur, cette formule nous donne le déphasage en fonction de l'énergie $E$ et des paramètres du potentiel $\ell$ et $-V_0$. 

### Propriétés du déphasage à basse énergie

La section efficace $\sigma_l \sim \sin^2 \delta_l$ aura un maximum autour de $\delta_l \sim \pi/2$, ce qui correspond à un zéro de la cotangente. Voyons le comportement de $\delta_l$ à basse énergie
$$\ell k \rightarrow 0$$
On peut utiliser le comportement des bessels près de l'origine:
$$\mathrm{j}_l(\rho) \rightarrow \frac{\rho^l}{(2l+1)!!}$$
et
$$\mathrm{n}_l(\rho) \rightarrow -\frac{(2l+1)!!}{\rho^{l-1}}$$
avec la notation $(2l+1)!!=1\times 3 \times 5 \times \ldots \times (2l+1)$. On obtient,
$$\cot \delta_l \approx \frac{[(2l+1)!!]^2}{(2l+1) (\ell k)^{2l+1}} \frac{l+1 + \ell \alpha_l}{l - \ell \alpha_l}$$
Les valeurs de l'énergie pour lesquelles la cotangente s'annule
$$l + 1 + \ell \alpha_l = 0, \quad \delta_l = \pi n + \frac{\pi}{2}$$
sont des *résonances*, et correspondent à un fort couplage des particules au moment de la collision. Pour ces valeurs de l'énergie on a,
$$\sigma_l = \frac{4\pi (2l+1)}{k^2}$$

On observe en outre, que pour $\ell k \ll 1$ seul l'orbital s ($l=0$) contribue significativement à la section efficace:
$$\delta_l \sim k^{-(2l+1)}$$
On a donc,
$$ \sigma_0(k) = \frac{4\pi \sin^2 \delta_0(k)}{k^2}$$
Remarquons que cette formule est en fait asymptotiquement valable pour tout potentiel à portée finie et à basse énergie.

> <img src="{static}/images/MQ-phase.svg" alt="dephasing" style="height: 230px;"/>
>
> Le déphasage est positif $\delta_l > 0$ pour un potentiel attractif $V<0$ et négatif $\delta_l <0$ pour un potentiel répulsif $V>0$. Ici on représente la fonction radiale pour $l=0$, $R_l \sim \mathrm{j}_l(kr)$.

Pour $l=0$ le déphasage s'écrit,
$$k \cot \delta_0 = - \frac{1 + \ell \alpha_0(0)}{\ell^2 \alpha_0(0)} \equiv - \frac{1}{a}$$
où $a$ est la *longueur de diffusion*, elle peut être positive (pour un potentiel répulsif) ou négative (pour un potentiel attractif, sans état liée). La section efficace devient en termes de $a$,
$$\sigma_0 = \frac{4\pi a^2}{1 + (ak)^2}$$
ce qui correspond, dans la limite $k \rightarrow 0$, au cas d'une sphère rigide de rayon $a$. Remarquez que pour $k = \I/a$, dans la présente approximation, on aurait une divergence de la section efficace. C'est justement le cas d'un état liée $E_B < 0$:
$$E_B = - \frac{\hbar^2}{2ma^2}$$

En effet, en récrivant,
$$\E^{2\I \delta_l} - 1 = \frac{2a k}{\I - a k}$$
on voit qu'une longueur $a=1/k$ correspond à un *pôle* de l'amplitude de diffusion $f(k,\theta)$. Dans le cas d'un état liée $k = \I \kappa$, ou $\kappa = 1/a$ correspond à la taille de cet état liée (on doit donc avoir $a > 0$, pour s'assurer de la décroissance de $R_0(r)$, $r \rightarrow \infty$):
$$\sigma_B(E) = \frac{2\pi\hbar^2}{m} \frac{1}{E - E_B}$$
On obtient donc la contribution de l'état $-E_B$ à la section efficace $l=0$. Le choix physique du pôle avec le bon signe ($\kappa = 1/a >0$), conduit à un résultat fini. Un résultat toutefois assez remarquable: la diffusion d'une onde *s* par un potential ayant un état liée $E_B$ est entièrement déterminée par l'énergie de cet état.


### Formule de Breit-Wigner

Un effet intéressant apparaît dans le cas d'un puits profond $E\ll V_0$ dû à la présence des état liés. En effet, le potentiel effectif dans l'équation radiale est,
$$V_\text{eff} = \frac{l(l+1)}{r^2} - V_0 \Theta(\ell - r)$$
ce qui implique que pour $l>0$ des états virtuels (quasi liés) peuvent apparaître à des énergies $E_R>0$ positives. 

Dans la région des paramètres,
$$\ell k \ll l \ll \ell q, \quad E_0 \ll V_0$$
en utilisant la forme asymptotique $\rho \gg 1$,
$$\mathrm{j}_l(\rho) \approx \frac{1}{\rho} \sin(\rho - l\pi/2)$$
et
$$\mathrm{n}_l(\rho) \approx - \frac{1}{\rho} \cos(\rho - l\pi/2)$$
on a
$$\alpha_l \approx -1/\ell + q \cot(\ell q - \pi l/2)$$
La condition de résonance devient,
$$l + 1 + \ell \alpha_l \approx l + \ell q  \cot(\ell q - \pi l/2) = 0$$
ou, d'une façon équivalente, 
$$\cot(\ell q - \pi l/2) \approx -\frac{l}{\ell q} \ll 1$$
ou encore approximativement $\ell q - l\pi/2$ est proche $\pi/2$, ce qui correspond à la condition d'existence d'un état liée (comme on peut se rendre compte en écrivant la condition de continuité pour $E < 0$).

> <img src="{static}/images/MQ-veff.svg" alt="scattering cross section" style="height: 230px;"/>
>
> Le terme de moment cinétique modifie le potentiel central attractif permettant l'apparition d'un état virtuel à l'énergie $E_R$ (de résonance) protégé par une barrière. La section efficace possède un pic à $E=E_R$, d'allure de lorentzienne.

Autour de la résonance $E \approx E_R$, on a,
$$l + 1 + \ell \alpha_l(E) \approx \ell (E-E_R) \alpha'_l(E_R)$$
et 
$$l - \ell \alpha_l(E) \approx 2l+1$$
En remplaçant dans la formule pour $\cot \delta_l$ on obtient,
$$\cot \delta_l = -\frac{E-E_R}{\Gamma_R}$$
avec
$$\Gamma_R = - \frac{2 \ell^{2l}}{[(2l+1)!!]^2} \frac{k^{2l+1}}{\alpha'_l(E_R)}$$
ou, en dégageant le déphasage,
$$\delta_l(E) \approx \frac{\pi}{2} + \arctan \left( 2\frac{E - E_R}{\Gamma_R} \right)$$
Ce qui conduit à la *formule de Breit-Wigner* de la section efficace à basse énergie près d'un état virtuel:
$$\sigma_l(E) = \frac{4\pi}{k^2} \frac{\Gamma_R^2}{4(E-E_R)^2 + \Gamma_R^2}$$
(voir les figures).

> <img src="{static}/images/MQ-deltal.svg" alt="deltal" style="height: 230px;"/>
> <img src="{static}/images/MQ-sigmaR.svg" alt="sigmaR" style="height: 230px;"/>
>
> Comportement du déphasage $\delta_l$ et de la section efficace différentielle près de la résonance en $E = E_R$.
