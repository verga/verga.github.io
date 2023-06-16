Title: Applications: Probability
Slug: PS-A_proba
Date: 2018-10-07
Category: Lectures
Tags: teaching, statistical physics
Authors: Alberto Verga
Summary: Brief introduction to probability theory; solution of selected exercises.
status: hidden

$\newcommand{\I}{\mathrm{i}} 
\newcommand{\E}{\mathrm{e}} 
\newcommand{\D}{\mathop{}\!\mathrm{d}} 
\newcommand{\bra}[1]{\langle{#1}|}
\newcommand{\ket}[1]{|{#1}\rangle}
\newcommand{\braket}[1]{\langle{#1}\rangle}
\newcommand{\bbraket}[1]{\langle\!\langle{#1}\rangle\!\rangle}
\newcommand{\Tr}{\mathrm{Tr}}$

> [Lectures]({filename}PS-index.md) on statistical mechanics.


# Probability[^SH]

## Theory

A probability space is defined by a set $E$, the events or outcomes of an experiment, which are the subsets $E_n \subset E$ ($n=1,2,\ldots$), and a measure $P(E_n)$ satisfying the following *Kolmogorov* axioms:

* $P( \emptyset ) = 0$
* $P(E) = 1$
* if $n \ne m$ and $E_n \cap E_m = \emptyset$, $P(\cup_n E_n) = \sum_n P(E_n)$.

As a consequence on finds,
$$P(E_1 \cup E_2) = P(E_1) + P(E_2) - P(E_1 \cap E_2)\,.$$

The phenomenological measure of the event $E_n$ is given by its *frequency*: if $E_n$ is the outcome of some experiment, repeating the experiment $N$ times, the frequency is,
$$\nu_N(E_n) = \frac{\# E_n}{N}\,,$$
where $\# E_n$ is the number of occurrences of $E_n$ in the $N$ experiments. Therefore,
$$P(E_n) = \lim_{N \rightarrow \infty} \nu_N(E_n)\,.$$

An event can be associated with a *random variable* $X$, which takes the numerical values $x$, in the integers if discrete, with probability $p(x)$:
$$0\le p(x) \le 1\,,\quad \sum_{x \in X} p(x) =1\,.$$
The expected value of $X$ is given by the weighted sum,
$$\mathrm{E}[X] = \sum_{x \in X} x p(x)\,, \quad \braket{x} = \mathrm{E}[X]$$
And, more generally, the moments of degree $n$ are,
$$\braket{ x^n } = \sum_{x \in X} x^n p(x)\,.$$
The variance and the standard deviation are defined by the second moment:
$$\braket{\Delta x^2} = \braket{x^2} - \braket{x}^2$$
and,
$$\sigma = \mathrm{std} (x) = \sqrt{ \braket{\Delta x^2}}\,.$$
In the case of a continuous random variable $X = x \in \mathbb{R}$, the above formulas generalize straightforwardly. One defines, instead of the discrete distribution $p$, a continuous distribution function $F(x) = P(X<x)$ which gives the probability of the event $\{X<x\}$. Its derivative is the probability *density* function,
$$f(x)\ge0, \quad \int_{-\infty}^\infty \D x \, f(x) =1$$
with,
$$P(X<x) = F(x) = \int_{-\infty} ^x \D x \, f(x)\,,\quad \frac{\D F(x)}{\D x}=f(x)$$
Therefore,
$$\braket{x^n} = \int_{-\infty}^\infty \D x\, x^n \, f(x)\,.$$

The joint probability of a set of random variables $\boldsymbol X = (X_1,X_2,\ldots)$ is $P(\boldsymbol X)$. Two variables $X,Y$ are *independent* if their joint probability factorizes:
$$P(X,Y) = P(X) P(Y)\,,$$
or
$$f(x,y) = f(x) f(y)\,,$$
in the continuous case.

It is convenient to introduce the *characteristic function* $g$ of the density distribution $f$:
$$g_X(k) = \int_{-\infty}^\infty \D x \, \E^{-\I kx}f(x)\,.$$
The characteristic function of a sum of random variables is the product of the characteristic functions:
$$Y = \sum_n X_n \; \Rightarrow \; g_Y(k) = \prod_n g_{X_n}(k)\,.$$
The logarithm of the characteristic function is the *cumulant* generating function.

The characteristic function can also be defined by the expected value:
$$g_X(k) = \braket{\E^{-\I k x}} = \sum_n \frac{(-\I k)^n}{n!} \braket{x^n}\,,$$
which shows that the coefficients of its series expansion in $k$ are the *moments* $\braket{x^n}$. The moments may be computed through the derivatives:
$$\braket{x^n} =  \I^n \left( \frac{\partial }{\partial k} \right)^n \left. \braket{\E^{-\I k x}} \right|_{k=0}\,.$$ 

### Examples: counting configurations

<blockquote>
<table style="width:300px;">
<caption> Select \(n\) objects out of a total of \(N\) </caption>
<tr>
<th>Order</th>
<th>Repetition</th>
<th>   Number   </th>
</tr>
<tr>
<td>yes</td>
<td>yes</td>
<td>\(N^n\)  </td>
</tr>
<tr>
<td>yes</td>
<td>no</td>
<td>\(P^N_n=\frac{N!}{(N-n)!}\)</td>
</tr>
<tr>
<td>no</td>
<td>yes</td>
<td>\(\binom{N+n-1}{n}\)  </td>
</tr>
<tr>
<td>no</td>
<td>no</td>
<td>\(\binom{N}{n}=\frac{N!}{n!(N-n)!}\)</td>
</tr>
</table>
</blockquote>

As an example we take $N$ indistinguishable particles (objects) which can be in $S$ different states $s=1,\ldots,S$ (box), such that
$$N = \sum_{s=1}^S n_s\,, \quad n_s = 0, 1, \ldots$$
where $n_s$ is the number of particles in state $s$ (this number can be zero). The number $\Omega$ of sequences $(n_1,\ldots, n_S)$, representing microscopic states of $N$ particles, is equivalent to the number of arrangements of $N$ objects in $S$ boxes with repetition:
$$\Omega = \binom{S+N-1}{N}$$
The probability of an elementary event is then $P=1/\Omega$, the bose-einstein distribution in the microcanonical ensemble. The fermi-dirac case is obtained by restricting the number of particles to the set $n_s=0,1$, so we have no more than one particle in a given state. In this case $S>N$, $\Omega$ is the number of combinations of $N$ objects in $S$ boxes,
$$\Omega = \binom{S}{N}\,.$$

Other example is given by the Bernoulli process, in which we are interested in the number $n$ of successes in $N$ trials, if the probability of success is $p$. The probability of exactly $n$ occurrences of success among $N$ events is:
$$P_N(n) = \binom{N}{n} p^n \, (1-p)^{N-n}\,.$$
This formula can be applied to the random walk, choosing $p=1/2$ the probability to go to the left or to the right, $N=t$ the number of time steps, and $x=n - (N-n) = 2n -N$ the position of the walker after $n$ steps to the right and $N-n$ steps to the left:
$$p(x,t) = \binom{t}{\frac{x+t}{2}} \frac{1}{2^t}\,.$$
The long time limit gives a gaussian distribution. Indeed, using the stirling formula:
$$\ln N! \approx N \ln N - N\,,$$
one gets,
$$\ln p(x,t) \approx -t \ln 2 + t \ln t -\frac{t+x}{2} \ln \frac{t+x}{2} + \frac{t+x}{2} - \frac{t-x}{2} \ln \frac{t-x}{2} + \frac{t-x}{2}\,,$$
and substituting the expansion ($t \gg x$),
$$\ln \frac{t \pm x}{2} = \ln \frac{t}{2} \pm \frac{x}{t}\,,$$
$$\ln p(x,t) \approx t \ln \frac{t}{2} - \frac{t+x}{2} \left(\ln \frac{t}{2} + \frac{x}{t}\right) - \frac{t-x}{2} \left(\ln \frac{t}{2} - \frac{x}{t}\right) $$
which simplifies to,
$$\ln p(x,t) \approx - \frac{x^2}{t}\,.$$
After normalization one obtains the normal distribution $\mathcal{N}(0,1/\sqrt{2})$ of zero mean and variance $1/2$:
$$p(x,t) = \frac{\E^{-x^2/t}}{\sqrt{\pi t}}\,.$$
This result is compatible with the central limit theorem.

## The central limit theorem

The theorem of the *central limit* states that the sum of a large number of random variables is normally distributed:
$$Z_N = \frac{1}{\sqrt{N}\sigma} \left(\sum_n^N X_n-Nm\right) \;\rightarrow\;  \mathcal{N}(0,1)$$
where $X_n$ are independent random variables with $\braket{X} = m$ and $\mathrm{std}\,X = \sigma$.

It is simpler to work with the normalized variables $Y_n=(X_n-m)/\sigma$ of mean zero and unit variance. The characteristic function of $Z$ is,
$$g_Z(k) = g_Y(k/\sqrt{N})^N$$
where we used the identity $g_{X/a}(k) = g_X(k/a)$. In the large $N$ limit, the argument of $g$ is small and $g$ can be expanded in a taylor series:
$$g_Y(k/\sqrt{N}) = 1 - \I \braket{y} \frac{k}{\sqrt{N}} + [-\braket{y^2} + R(k/\sqrt{N})]  \frac{k^2}{2N}$$
where the error term vanishes faster than $k^2$. Applying this formula to $g_Y$, one obtains,
$$g_Z(k) = \left[ 1 - \big(1- R(k/\sqrt{N}) \big)  \frac{k^2}{2N}  \right]^N$$
Taking now the logarithm and using $\ln(1 \pm x) \approx \pm x$, we find,
$$\lim_{N\rightarrow\infty} \ln g_Z(k) = - \frac{k^2}{2} + \lim_{N\rightarrow\infty} R(k/\sqrt{N}) \frac{k^2}{2}= - \frac{k^2}{2}\,,$$
which leads to
$$g_Z(k) = \E^{- \frac{k^2}{2}}\,,$$
essentially the statement of the theorem. The gaussian distribution of $Z$ is obtained using the inverse transform,
$$f(z) = \frac{1}{2\pi}\int_{-\infty}^\infty \D k \, \E^{\I kz}g_Z(k) = \frac{\E^{-z^2/2}}{\sqrt{2\pi}}\,.$$

### Example: computing the characteristic function

The normal distribution is a probability law of the form $f(x) \sim \E^{-x^2/2}$, the gaussian bell. Under an affine transformation $x = (X-m)/\sigma$, a translation invariant distribution function (like the normal distribution), the distribution $F(X)$ changes as:
$$1 = \int_{-\infty}^\infty \D X \, F(X) =  \int_{-\infty}^\infty \D (\sigma x + m) \, F(X(x)) = \sigma \int_{-\infty}^\infty \D x \frac{1}{\sigma} f(x)\,,$$
or,
$$F(X) = \frac{1}{\sigma} f(x), \quad x = \frac{X-m}{\sigma}\,.$$
Therefore it is enough to consider,
$$f(x) = \frac{\E^{-x^2/2}}{\sqrt{2\pi}} \sim \mathcal{N}(0,1)\,,$$
and eventually, to obtain $F(X) \sim \mathcal{N}(m,\sigma)$, we make the variable change
$$x \rightarrow x(X) = \frac{X-m}{\sigma}, \quad f(x) \rightarrow F(X) = \frac{1}{\sigma}f(x(X)) = \frac{\E^{-(X-m)^2/2\sigma^2}}{\sqrt{2\pi \sigma^2}}\,.$$

The characteristic function is,
\begin{align*}g(k) &= \int_{-\infty}^\infty \frac{\D x}{\sqrt{2\pi}} \E^{-\I k x - x^2/2} \\ & = \int_{-\infty}^\infty \frac{\D x}{\sqrt{2\pi}} \exp\left[-\frac{1}{2}(x^2 - 2\I k x - k^2) -\frac{k^2}{2} \right] \\ & = \E^{-k^2/2}\, \int_{-\infty}^\infty \frac{\D x}{\sqrt{2\pi}} \E^{-(x-\I k )^2/2} \\ & = \E^{-k^2/2}\,.\end{align*}
Note that the cumulant generating function is at most, a second degree polynomial in $k$; this immediately implies that the only non vanishing cumulants are the mean and the variance. The characteristic function can easily expanded in series of $k$:
$$g(k) = \sum_{n=0}^\infty \frac{(-1)^n}{2^n} \frac{k^{2n}}{n!}\,,$$
which gives the even moments,
$$\braket{x^{2n}} = \frac{1}{2^n} \frac{(2n)!}{n!} \equiv (2n-1)!!$$
and, as anticipated, the odd moments are zero.

If the probability density $f(x)$ do not decrease fast enough when $x\rightarrow\infty$, the moments might not exist; this is the case of the cauchy distribution $f(x) \sim 1/(1+x^2)$. We start by finding the normalization constant:
$$\int_{-\infty}^\infty \frac{\D x}{1+x^2} = \pi$$
hence,
$$f(x) = \frac{1}{\pi} \frac{1}{1 + x^2}\,.$$
The first moment is zero by parity, but the second moment,
$$ \frac{1}{\pi}\int_{-\infty}^\infty \frac{\D x\,x^2}{1+x^2} = \text{ divergent}\,.$$
The characteristic function $g(k)$ is in fact a non analytic:
$$g(k) = \E^{-|k|}\,,$$
it depends on the absolute value of $k$, which has no derivative at $k=0$ (where we compute the moments). Using the residues theorem we can compute the fourier integral,
$$g(k) = \frac{1}{\pi}\int_{-\infty}^\infty \frac{\D x\, \E^{-\I kx}}{1+x^2}\,,$$
indeed,
$$\frac{1}{1+x^2} = \frac{1}{2\I} \left( \frac{1}{x-\I} - \frac{1}{x + \I}   \right)\,,$$
the first term, the $x=\I$ residue, gives $\E^k$ (with $k<0$), closing the contour on the upper complex $x$ plane, and the second one, $x=-\I$, gives $\E^{-k}$ (with $k>0$), and closing the contour on the lower complex plane.


## Probability theory of cumulants

The cumulant generating function is then given by,
$$c(k) = \ln g(k) = \sum_n \bbraket{x^n} \frac{(-\I k)^n}{n!}$$
where the second expression *defines* the cumulant $\bbraket{x^n}$. Comparing the two expressions, at each order one may compute the cumulant in terms of the moments.

As we saw before, if $X_1$ and $X_2$ are two independent random variables, then,
$$\braket{\E^{\I k( x_1 + x_2)}} = \braket{\E^{\I k x_1}} \braket{\E^{\I k x_2}}\,.$$
Therefore, the cumulant function $c_X(k) = \ln g_X(k)$, possesses the "extensivity" property,
$$\ln\braket{\E^{-\I k (x_1 + x_2)}} = \ln\braket{\E^{-\I k x_1}} + \ln\braket{\E^{-\I k x_2}} \,.$$
It is the generating function of the *cumulants*:
$$\bbraket{x^n} = \left( \frac{-1}{\I} \frac{\partial }{\partial k} \right)^n \left. c_X(k) \right|_{k=0}\,.$$
An explicit calculation leads to the following relations between the cumulants $\bbraket{x^n}$ and the moments $\braket{x^n}$ <strong style="color:DarkSlateBlue; background-color:LightGray;">EX</strong>,
\begin{align*}
\bbraket{x} & = \braket{x}\\
\bbraket{x^2} & = \braket{x^2} - \braket{x}^2\\
\bbraket{x^3} & = \braket{x^3} - 3 \braket{x^2} \braket{x} + 2 \braket{x}^3\\
\bbraket{x^4} & = \braket{x^4} - 3 \braket{x^2}^2 - 4 \braket{x^3} \braket{x} + 12 \braket{x^2}\braket{x}^2 - 6 \braket{x}^4
\end{align*}
The general form of the relations between cumulants and moments contains the [Bell polynomials](https://www.encyclopediaofmath.org/index.php/Bell_polynomial):
$$\braket{x^n} = \sum_{k=1}^n B_{n,k}(\bbraket{x},\ldots,\bbraket{x^{n-k+1}})$$
and the inverse formula,
$$\bbraket{x^n} = \sum_{k=1}^n (-1)^{k-1} (k-1)! B_{n,k}(\braket{x},\ldots,\braket{x^{n-k+1}})$$
The Bell polynomials encode the information about the partition of $n$ into $k$ blocks; for instance, $B_{n,k}(1,\ldots,1)$ is the number of ways to partition a set $\{1,\ldots,n\}$ into $k$ subsets. Their explicit form is,
$$B_{n,k}(x_1,\ldots x_{K}) = \sum_{s_1,\ldots,s_K} \delta\left(\sum_{l=1}^K s_l,k\right) \delta\left(\sum_{l=1}^K ls_l,n\right) n! \prod_{l=1}^K \frac{x_l^{s_l}}{s_l! l!^{s_l}}$$
($K=n-k+1$) where the two Kronecker deltas account for the constraints on the indices $s_l$. In this formula $l$ is the number of elements in each group (the size of the *cluster*), $s_l$ is the number of clusters of size $l$. We note that, 
$$\frac{n!}{\prod_l l!^{s_l}}$$
counts the number of combinations to pick the $l$-clusters from the set of $n$ elements; and the factors $s_l!$ are the number of permutations of the cluster $l$, giving the same partition (the same monomial) <strong style="color:DarkSlateBlue; background-color:LightGray;">EX</strong>.

As an example, the cumulant generating function of the gaussian distribution of mean $m$ and variance $\sigma^2$ is $\ln\braket{\E^{-\I k x}} = \I m k - \sigma^2 k^2/2$, giving $\bbraket{x^n} =0$ for $n>2$ <strong style="color:DarkSlateBlue; background-color:LightGray;">EX</strong>.

Generalization to $N$ variables is straightforward. The generating functions are:
$$\braket{x_1 \ldots x_N} = \left( \I^N \frac{\partial^N }{\partial k_1 \ldots \partial k_N} \right) \left. \braket{\E^{-\I \boldsymbol k \cdot \boldsymbol x}} \right|_{k=0}\,.$$
where $\boldsymbol x = (x_1,\ldots,x_N$ and $\boldsymbol k = (k_1,\ldots,k_N)$. Similarly for the cumulants,
$$\bbraket{x_1 \ldots x_N} = \left( \I^N \frac{\partial^N }{\partial k_1 \ldots \partial k_N} \right) \left. \ln \braket{\E^{-\I \boldsymbol k \cdot \boldsymbol x}} \right|_{k=0}\,.$$
For example, the third order cumulant is:
$$\bbraket{x_1 x_2 x_3} = \braket{x_1 x_2 x_3} - \braket{x_1 x_2} \braket{x_3} - \braket{x_1 x_3} \braket{x_2} - \braket{x_2 x_3} \braket{x_1} + 2\braket{x_1} \braket{x_2} \braket{x_3} \,,$$
which reduces to the previous formula if $x_1=x_2=x_3$. It can be also written as (using only the indices to simplify the notation),
$$\{(123)-(1)(2)(3)\} - \{ [(12) - (1)(2)](3) + [(13)- (1)(3)](2) + [(23) - (2)(3) ](1) \}\,,$$
making evident that if one of the moments factorizes the corresponding cumulant, vanishes. We can also invert the previous formulas to find the moments as a combination of cumulants <strong style="color:DarkSlateBlue; background-color:LightGray;">EX</strong>:
$$\braket{x_1x_2x_3} = \bbraket{x_1x_2x_3} + \bbraket{x_1x_2}\bbraket{x_3} + \bbraket{x_1x_3}\bbraket{x_2} + \bbraket{x_2x_3}\bbraket{x_1} + \bbraket{x_1}\bbraket{x_2}\bbraket{x_3}\,.$$
Knowledge of the cumulants of a random variable is enough to reconstruct the probability distribution. It is interesting to note that the above general formula of the multivariate moments can be written in a combinatorial form (see the discussion on the one random variable case) <strong style="color:DarkSlateBlue; background-color:LightGray;">EX</strong>[^SH]:
$$\braket{x_1\ldots x_n} = \sum_{\mathcal{P}} \prod_{s\in \mathcal{P}} \bbraket{x_s}$$
where, 

* $\mathcal{P}$ is one of the possible partitions of the set $\{1,\ldots,n\}$ in $|\mathcal{P}|$ blocks (we denote $|\mathcal{S}|$ the number of elements, cardinal, of the set $\mathcal{S}$),
* $s \in \mathcal{P}$ is an element of the list of blocks belonging to one partition $\mathcal{P}$,
* $x_{s}$ is a product of $|s|$ variables indexed by the block $s$.

The inverse formula reads,
$$\bbraket{x_1\ldots x_n} = \sum_{\mathcal{P}} (-1)^{|\mathcal{P|}-1}|\mathcal{P}-1|! \prod_{s\in \mathcal{P}} \braket{x_s}$$
An important consequence of this statement is that the cumulants are *irreducible*: the cumulant involving random *independent* variables is zero. In the language of graphs we introduce below, one refers to this property as that the cumulants correspond to *connected* graphs, graphs which cannot be decomposed into subgraphs by cutting an edge.

Therefore, the cumulants measure the non trivial, irreducible, correlations of a random variable, i.e. correlations that cannot be expressed in terms of lower order cumulants.


## Selected solutions to the exercises

### 1

The Rayleigh distribution is
$$f(x) = 2 x \E^{-x^2}$$
and the corresponding generating function is
$$g_X(k) = \E^{-k^2/2} - \frac{\I \sqrt{\pi}}{2} k \E^{-k^2/4} \mathrm{erfc}\left( \frac{\I k}{2} \right)$$
where
$$\mathrm{erfc}(x) = \frac{2}{\sqrt{\pi}} \int_x^\infty \D t \, \E^{-t^2}$$
is the complementary [error function](https://en.wikipedia.org/wiki/Error_function).

The moments can be calculated using the derivatives of $g_X$ or directly:
$$\braket{x^n} = 2 \int_0^\infty \D x \, x^{n+1} \E^{-x^2} = \Gamma\left(\frac{n}{2} + 1\right)$$
where
$$\Gamma(x) = \int_0^\infty \D t \, t^{x-1} \E^{-t}$$
is the Euler [gamma function](https://en.wikipedia.org/wiki/Gamma_function).

### 4

Information and entropy. Use the maximum entropy principle to find the distribution $p(v)$ of the velocity $v$ of one particle subject to the constraints: (V) $\braket{|v|} = c$, (E) $\braket{mv^2/2} = mc^2/2$. Show that the energy constraint (E) contains more information than the mean velocity constraint (V),
$$I_\text{E} - I_\text{V} > 0$$
compute this information difference in bits.

We use the lagrangian multipliers $(\alpha,\beta)$ to find the extremum of the entropy $S = S[p]$. The first case is,
$$S = -\int \D v \, p(v) \ln p(v) + \alpha \left( 1 - \int \D v\, p(v) \right) + \beta \left( c - \int \D v\, p(v)|v| \right)\,.$$
Variation of this functional gives,
$$\frac{\delta S}{\delta p} = 0 = -1 - \ln p(v) - \alpha - \beta |v|\,.$$
Variation on $\alpha$ gives the normalization condition, and over $\beta$, gives the constraint $\braket{|v|} = c$. These two conditions allow the calculation of the lagrangian multipliers. The final result is,
$$p(v) = \frac{\E^{-|v|/c}}{2c}\,.$$
A similar calculation gives a gaussian distribution in the case of the constraint $\braket{v^2} = c^2$:
$$p(v) = \frac{\E^{-v^2/2c^2}}{\sqrt{2\pi c^2}}.$$

Substituting these results into the expression of the entropy one can compute the information difference. For instance,
$$S = -\int \D v \, \frac{\E^{-|v|/c}}{2c} \ln \frac{\E^{-|v|/c}}{2c} = - \left. (x+1)\,\E^{-x}\right|_0^\infty - \ln(2 c)\, \left. \E^{-x}\right|_0^\infty=1 + \ln(2c) \,.$$
The final result is,
$$\Delta I = \frac{1 + \ln 2/\pi}{2 \ln 2}\,.$$

### 5

A simple model of a polymer consists in a chain of bonded atoms ($a$ is the link length) whose successive links can make an angle of $0$ or $\pi$, with probability $1/2$, for a total length $L$. 

* Find the number $\Omega$ of chains of length $L$ as a function of the number of atoms $N$. You may introduce the number of $0$ links $N_+$ and the number of $\pi$ links, such that $L=(N_+ - N_-)a$ and $N = N_+ + N_-$.
* Assume $L/a \ll N$ and show that $\Omega(N,L)$ approaches a gaussian distribution of variance $\sim N$ (as in a random walk). Deduce the entropy (using the Stirling approximation).
* Show that the force required to maintain the chain length at a fixed value $L$ follows the Hooke's law (for a well folded chain).
* If $L$ can take any value, not necessary small with respect to $Na$, use the Boltzmann weight $\sim \E^{-V/T}$ ($V$ is the potential of the external force), to demonstrate that the force is,
 
    $$f = \frac{T}{a} \mathrm{artanh}\left( \frac{L}{Na} \right)\,.$$

    (*Hint*. Consider one link.)

The calculation of the microcanonical entropy can be put in a form similar to the example given above about the Bernoulli process or random walk. Indeed, the entropy of a configuration with $N_+$ links with angle $0$, and $N_-$ links with angle $\pi$ has an entropy,
$$S = \ln \frac{N!}{N_+! N_-!}$$
This gives, in the relevant limit, an entropy quadratic in $L$, $S(T,L) \sim L^2$:
$$S \approx N \ln N - \frac{N+n}{2} \ln \frac{N+n}{2} -  \frac{N-n}{2} \ln \frac{N-n}{2}$$
where $n=L/a$; using $\ln(1\pm x) \approx \pm x$, we obtain,
$$S\approx \ln 2 - \frac{L^2}{2a^2N}.$$

To compute the force, we can use the thermodynamic relation for the free energy $F = F(T,L) = -T S(T,L) + E$,
$$dF = - S dT - f dL, \quad f= -f_\text{ext}\,.$$
Therefore,
$$-\frac{\partial S}{\partial L} = \frac{\partial^2 F}{\partial L \partial T} = \frac{\partial^2 F}{\partial T \partial L} = \frac{\partial f}{\partial T}$$
which leads to the formula
$$f_{\text{ext}} = T\frac{\partial S}{\partial L} \approx \frac{T}{N} L$$
similar to Hooke's law, but with a rigidity proportional to the temperature, manifestation of the entropic character of the force.

Another approach is to consider that each link is in thermal equilibrium with the applied force, independently to the other links; therefore, using the bolzmann weight,
$$p(\pm) \sim \exp \left( \pm \frac{fa}{T}  \right)$$
we obtain the expected value of the total length,
$$L = Na \frac{\E^{fa/T} - \E^{-fa/T}}{\E^{fa/T} + \E^{-fa/T}} = Na \tanh(fa/T)$$
This formula coincides with the previous one in the limit $T \gg fa$.

### Random matrices

### 6

We consider first, a random symmetric $N \times N$ matrix $M$, each element $i \le j$ distributed according to
$$p(x) = p(M_{ij}=x) = \begin{cases}\frac{1}{2a} & \text{for} \quad x\in (-a,a)\\
0 & \text{otherwise}\end{cases}\,.$$

* Calculate the characteristic function $p(k)$ of the distribution $p(M)$ and of the distribution of the trace $\mathrm{Tr}\,M$, $p_T(k)$.

* For large $N$ the cumulant of $N$ elements is $N$ times the cumulant of one element. Use the central limit theorem (gaussian distribution for large $N$) to compute $p(t)$, with $t = N^{-1/2} \mathrm{Tr}\, M$; show that,
$$p(t) = (3/2\pi a^2)^{1/2} \E^{-3t^2/2a^2}\,.$$

Consider now that $M$ is a $2\times2$ *gaussian* random matrix: each element is normally distributed with $\mathcal{N}(0,1)$ for the diagonal elements, and $\mathcal{N}(0,1/\sqrt{2})$ for the nondiagonal ones. (We denote $\mathcal{N}(0,\sigma)$ a normal distribution with zero mean and variance $\sigma^2$.)

* Compute the eigenvalues $\lambda_\pm$ of $M$ and show that the probability distribution of the "spacing" $s = (\lambda_+ - \lambda_-)/\Delta$, where $\Delta$ is such that the mean spacing is unity, is given by the [Wigner surmise]({filename}CH-rm.md):
$$p(s) = \frac{\pi s}{2} \E^{-\pi s^2/4}\,,$$
    where the mean value and normalization satisfy,
$$\int_0^\infty \D s\, p(s) s = \int_0^\infty \D s\, p(s) = 1\,.$$

* Verify numerically that the Wigner surmise correctly fits the level spacing histogram of *large* random symmetric matrices.


The characteristic function is the fourier transform of the probability distribution:
$$p_{ij}(k) = \int_{-a}^{a} \frac{\D x}{2a} \E^{-\I k x} = \frac{\sin ak}{ak}$$
The probability of each random element of $M$ is independent of the others, therefore the characteristic function of the sum of $N$ random variables $T = \Tr M = \sum_{i} p(M_{ii}$ is the product,
$$p_T(k) = \prod_{i=1}^N p_{ii}(k) = \left(  \frac{\sin ak}{ak} \right)^N\,.$$
(Note that $T$ is a sum of random variables, then it is itself a random variable.)

The first cumulant is determined by the mean value, which vanishes $\braket{M_{ij}} = 0$:
$$\braket{T}_c = N \braket{M_{ij}} = 0 \,.$$
The second order cumulant is simply (we use $\braket{M}=0$),
$$\braket{T^2}_c = N \braket{M_{ij}^2} = N \int_{-a}^{a} \frac{\D x}{2a} x^2 = N \frac{a^2}{3}\,.$$

Let us define the reduced variable $t = T/\sqrt{N}$; by the central limit theorem we have,
$$p(t) = \lim_{N \rightarrow \infty} P(T/\sqrt{N} = t) = \frac{\E^{-t^2/2 \braket{t^2}}}{\sqrt{2\pi \braket{t^2}}}\,.$$
Using the value of the moment $\braket{T^2}$, or $\braket{t^2} = a^2/3$, we obtain the solution
$$p(t) = \sqrt{\frac{3}{2\pi a^2}} \E^{-3t^2/2 a^2}\,.$$

We consider now the case of a gaussian matrix:
$$M = \begin{pmatrix} a & b \\ b & c \end{pmatrix} \,.$$
Its eigenvalues are,
$$\lambda_\pm = \frac{1}{2}\big[ \Tr M \pm \sqrt{d^2 + b^2} \big],\; d = (a-c)/2\\.$$
Therefore the reduced level separation is,
$$s = \frac{\lambda_+ - \lambda_-}{\Delta} = \frac{2}{\Delta} \sqrt{d^2 + b^2}\,,$$
where $\Delta$ is such that the probability distribution $p(s)$ of the level spacing satisfies,
$$\int \D s\, s p(s) = 1\,.$$
This condition together with the normalisation condition,
$$\int \D s\,  p(s) = 1\,.$$
means that we can determine $p(s)$ as a function of two unknown constants. The probability distribution of a matrix (the matrix is a random "variable"), depends only on the distribution of the random variables $d$ and $b$:
$$p_M(d,b) = A \exp(- d^2 - b^2)\,$$
where we used the fact that both $d$ and $b$ are gaussians of variance $1/2$. Therefore,
$$p(s) = \int \D d \D b \, p_M(d,b) \delta\big(s - \sqrt{d^2 + b^2} \big)\,.$$
The integral is easily computed in polar variables $r^2 = d^2 + b^2$,
$$p(s) = C s \E^{- B s^2}\,.$$
Putting this formula into the normalization and average conditions, we find $C$ and $B$; the final result is,
$$p(s) = \frac{\pi s}{2} \E^{-\pi s^2/4}\,,$$
a formula know as the Wigner surmise: it describes with a good precision the spacing distribution of the so-called GOE, the gaussian orthogonal ensemble of random matrices. Applications span from nuclear physics to quantum chaos.

### Notes

[^SH]: Shiryaev, A. N., Probability (1996).
