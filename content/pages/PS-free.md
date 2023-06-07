Title: Free particles in the grand canonical ensemble
Slug: PS-free
Date: 2018-04-15
Category: Lectures
Tags: teaching, statistical physics
Authors: Alberto Verga
Summary: Quantum free systems, identical particles, fermions and bosons statistics
status: hidden

$\newcommand{\I}{\mathrm{i}} 
\newcommand{\E}{\mathrm{e}} 
\newcommand{\D}{\mathop{}\!\mathrm{d}} 
\newcommand{\Di}[1]{\mathop{}\!\mathrm{d}#1\,} 
\newcommand{\Dd}[1]{\frac{\mathop{}\!\mathrm{d}}{\mathop{}\!\mathrm{d}#1}}
\newcommand{\bra}[1]{\langle{#1}|}
\newcommand{\ket}[1]{|{#1}\rangle}
\newcommand{\braket}[1]{\langle{#1}\rangle}$

> [Lectures]({filename}PS-index.md) on statistical mechanics.

# Non interacting bosons and fermions

In classical physics the thermodynamics of non interacting particles is essentially that of the ideal gas, described by the equation of state, $PV = NT$, relating the intensive variables $P$ pressure and $T$ temperature to the extensive ones, $N$ the number of particles and $V$ the volume. Interesting new phenomena appear in the quantum realm, even in the non interacting case, as a result of one of the most fundamental laws of nature: the identity of elementary particles, and by extension, of elementary excitations in condensed matter.

## Identity of particles

The identity of particles is a fundamental fact of quantum physics: the spectrum of solar hydrogen is identical to the one recorded in the laboratory; the exchange of particles of an ideal gas, even if they are distinguishable in classical mechanics, do not increase the entropy (Gibbs paradox). The identity of photons can be experimentally tested, as for instance in the interference of two photons in a beam splitter, the [Hong-Ou-Mandel](https://en.wikipedia.org/wiki/Hong–Ou–Mandel_effect) effect.

In order to understand the meaning and devise the physical consequences of the particles identity, let us consider a simple system consisting of two particles. Its hilbert space is 
$$\mathcal{H} = \mathcal{H}_1 \otimes \mathcal{H}_1\,.$$
where $\mathcal{H}_1$ is the one particle hilbert space. A two particle state is then of the form,
$$\ket{s_1} \otimes \ket{s_2} = \ket{1,2}\,,$$
where we introduced the basis kets $\ket{s}$ for the single particle states with $s\equiv 1,2,\ldots$, the labels associated to the set of quantum numbers (*i.e.* momentum, spin,...): particle 1 (slot one in the ket) is in state $s_1=1$ and particle 2 (slot two in the ket) is in state $s_2 = 2$. Now, exchanging $2$ and $1$, $\ket{2,1}$, that is putting particle 1 in state $2$ and particle 2 in state $1$, $12\rightarrow21$, the physical properties of the system must be preserved. This exchange leads to the two possibilities:
$$\ket{1,2} = \ket{2,1},\; \text{or} \; \ket{1,2} = - \ket{2,1}\,,$$
since both are compatible with the fact that another exchange returns the system to its initial state, $12\rightarrow 21 \rightarrow 12$. The first case corresponds to *symmetric* states and the second one to antisymmetric states, their are related to the spin of the particles (in fact, it is a quantum *relativistic* phenomenon): integer spin particles, called *bosons*, have symmetric states under permutation of particles; half integer particles, *fermions*, have antisymmetric states. Photons are bosons of spin $1$, electrons are fermions of spin $1/2$.

Instead of the hilbert space of $N$ particles $\mathcal{H}_N$, it is possible to describe a system of an arbitrary number of particles using a representation in terms of *occupation numbers*, the so called [fock space](https://en.wikipedia.org/wiki/Second_quantization) $\mathcal{F}$, which is a direct sum of symmetrized hilbert spaces:
$$\mathcal{F} = \bigoplus_{N=0}^\infty \mathrm{S}_\pm\mathcal{H}_N\,,$$
where $\mathrm{S}_+$ is the symmetrization operator for bosons and $\mathrm{S}_-$ is the fermion's antisymmetrization operator, and $N=0$ corresponds to the vacuum state $\ket{0}$. The occupation numbers $n_s$ are simply the number of particles in a given state $s$ ($s=1,2,\ldots$, where each $s$ represents, in general, a set of quantum numbers; the number of states $N_s$ can obviously be infinity).

A state in the fock space is defined by the corresponding set of occupation numbers $\ket{n_1,n_2,\ldots}$. It can be build from the vacuum state applying successively creation and annihilation operators of particles at a given state (an abstract generalization of the harmonic oscillator operators $a$ and $a^\dagger$, respectively). For instance, the state $\ket{1,2}$ of two bosons can be constructed as:
$$\ket{1,2} = a^\dagger_1 a^\dagger_2 \ket{0}=  a^\dagger_2 a^\dagger_1 \ket{0}= \ket{2,1}$$
from which we obtain the *commutation* relations,
$$[a_s,a_r] = 0 = [a^\dagger_s, a^\dagger_r]$$
(using that $a$ is the adjoint of $a^\dagger$). A similar calculation for fermions leads to *anti*-commutation relations
$$\{c_s,c_r\} = 0 = \{c^\dagger_s, c^\dagger_r\}$$
using $c$ and $c^\dagger$ for the fermionic operators. An immediate consequence of the anticommutation of fermions is that two fermions cannot be in the same state $\ket{1,1}$ (because it it symmetric!): this is the content of the Pauli *exclusion principle*. The occupation numbers $n_s$ are the eigenvalues of the operators $a^\dagger_s a_s$ for bosons and $c^\dagger_s c_s$ for fermions. The boson operator is similar to the harmonic oscillator, its spectrum are integers; the spectrum of fermion operator contains, in contrast, only the two values $0,1$. Indeed, the algebra of boson and fermion operators is completed by the commutation relations
$$[a_s, a_s^\dagger] = 1, \quad {c_s, c_s^\dagger} = 1.$$
As a consequence the occupation number operators
$$a_s^\dagger a_s = \hat{n}_s, \quad c_s^\dagger c_s = \hat{n}_s$$
have the spectrum $n_s=0,1,2,\ldots$ for bosons and $n_s=0,1$ for fermions.

Therefore, a $N$-particles boson state can be written,
$$\ket{n_1,n_2,\ldots,n_{N_s}}\,,\quad \sum_{s=1}^{N_s} n_s = N\,,$$
where particles in a similar state are grouped: the $N$-state is thus given by the number $n_s$ of particles in each different state $s$. For a fermion state we must track the order of the occupation numbers $n=0,1$,
$$\ket{n_1,n_2,\ldots,n_{N_s}}\,,\quad n_s = 0,1\,,$$
because the permutation of two occupation numbers change the state sign. For instance, a general boson state is,
$$(a_1^\dagger)^{n_1} (a_2^\dagger)^{n_2} \ldots \ket{0} = \ket{n_1, n_2, \ldots}$$
and for fermions we have,
$$(c_1^\dagger)^{n_1} (c_2^\dagger)^{n_2} \ldots \ket{0} = \ket{n_1, n_2, \ldots}$$
both states having automatically the correct symmetry, symmetric for bosons and antisymmetric for fermions; $\ket{0}$ is the vacuum state, the state without particles.

> The boson occupation numbers can be any integer number $n_s=0,1,2,\ldots$, and the fermion occupation numbers can only take on two values $n_s=0,1$.

The fact that the number of particles is arbitrary, makes the fock space the natural framework for the grand canonical ensemble. The hamiltonian of free bosons has the general *diagonal* form,
$$H_B = \sum_s \epsilon_s a^\dagger_s a_s\,,$$
where the $\epsilon_s$ are the energy levels and $a^\dagger_s a_s$ is a number operator with, as we said above, eigenvalues the occupation numbers $n_s \in \mathbb{N}$. A similar expression holds for the free fermions,
$$H_F = \sum_s \epsilon_s c^\dagger_s c_s\,,$$
where the number operator of state $s$, $c^\dagger_s c_s$ has a spectrum of occupation numbers $n_s=0,1$ with two values. The respective grand partition functions are
$$Z_B(T,\mu) = \mathrm{Tr}\, \E^{-(H_B - \mu N_B)/T}\,,\quad N_B = \sum_s a^\dagger_s a_s\,,$$
and
$$Z_F(T,\mu) = \mathrm{Tr}\, \E^{-(H_F - \mu N_F)/T}\,,\quad N_F = \sum_s c^\dagger_s c_s\,.$$
Using the explicit form of $H_B$ and $N_B$, and the properties of the fock states to exchange the trace and the product (the basis states are product states of the occupation numbers), we can put the grand partition function in the form,
$$Z_B= \mathrm{Tr}\,\exp\left(-\sum_s \frac{\epsilon_s - \mu}{T}a^\dagger_s a_s\right) = \mathrm{Tr}\,\bigotimes_s \exp\left(-\frac{\epsilon_s - \mu}{T} a^\dagger_s a_s\right) = \prod_s \sum_{n_s=0}^\infty \E^{-(\epsilon_s - \mu)n_s/T}$$
which can be easily summed up,
$$Z_B(T,\mu) = \prod_s \frac{1}{1-\E^{-(\epsilon_s - \mu)/T} }\,.$$
A similar calculation for the fermions, the only difference is in the values of $n_s$, leads to,
$$Z_F(T,\mu) = \prod_s \sum_{n_s=0,1} \E^{-(\epsilon_s - \mu)n_s/T} = \prod_s \left(1 + \E^{-(\epsilon_s - \mu)/T} \right)\,.$$

We remark that, in the boson case, the condition for convergence is ensured if the chemical potential is negative $\mu < 0$ ($\epsilon > 0$ for free particles), or more generally when the energy is bounded from below, $\mu < \min \epsilon_s$.

> The grand potential of non interacting bosons and fermions is
>
$$\Phi(T, \mu, V) = \pm T \sum_s \ln \left( 1 \mp z \E^{-\epsilon_s/T} \right)\,,\quad z = \E^{\mu/T}$$
>
> where $\epsilon_s$ is the energy spectrum, $z$ the fugacity, and the top sign is for bosons and the bottom one is for fermions. In the classical limit $\E^{-(\epsilon_s-\mu)/T} \ll 1$, the grand potential reduces to
>
$$\Phi = -T \sum_s \E^{-(\epsilon_s - \mu)/T}$$
>
> which corresponds to the Boltzmann distribution.

The expected values of the energy $\braket{H}$  and the particle number $\braket{\hat{N}}=N$ are given by the bosons and fermions occupation numbers $\braket{a^\dagger_s a_s}$ and $\braket{c^\dagger_s c_s}$, respectively:
$$\braket{n_s} = \frac{1}{\E^{(\epsilon_s - \mu)/T} \mp 1}\,, \quad \sum_s \braket{n_s} = \braket{\hat{N}}=N\,,$$
and,
$$\braket{H} = \sum_s \epsilon_s \braket{n_s} \,,$$
where $\braket{n_s}$ are the bose (upper sign) and fermi (lower sign) one particle distribution functions <strong style="color:DarkSlateBlue; background-color:LightGray;">EX</strong>. (Notation: we sometimes may write $\braket{n_s} = n_s$.)

### Free particles: ideal boson and fermion gases

The state $s = (s, \boldsymbol p)$ of free particles is characterized by their spin $s$ and momentum $\boldsymbol p$. The energy spectrum,
$$\epsilon_p = \frac{p^2}{2m} \,,$$
possesses a $g_s= 2s + 1$ spin degeneracy ($m$ is the mass). Moreover, in a cubic box of volume $V$, the momentum is
$$\boldsymbol p = \frac{2\pi \hbar}{V^{1/3}} \boldsymbol n\,,\quad \boldsymbol n \in \mathbb{Z}^3\,,$$
which, in the limit $V \rightarrow \infty$ tends to a continuum, allowing the replacement of the sum over states by an integral:
$$ \sum_{(s,\boldsymbol p)} \ldots \rightarrow g_s \frac{V}{(2\pi \hbar)^3} \int_{\mathbb{R}^3} \D \boldsymbol p \, \dots$$
We note that in this limit, the grand potential $\Phi \sim V$ is manifestly extensive. Therefore, the problem of the statistical properties of an ideal quantum gas reduces to the calculation of the integral:
$$\Phi(T,z,V) = \pm \frac{g_sVT}{(2\pi)^3} \int_{\mathbb{R}^3} \D \boldsymbol p \, \ln \left( 1 \mp z \E^{-\epsilon_{\boldsymbol p}/T} \right) = \pm \frac{g_sVT}{2\pi^2} \int_0^\infty p^2 \D p \, \ln \left( 1 \mp z \E^{-p^2/2T} \right)$$
where we introduced units such that $m=\hbar=1$. After a change of variables $p^2/2T \rightarrow x$ and one integration by parts, we obtain,
\begin{equation}
  \Phi(T,z,V) = \mp \frac{g_s V T}{\lambda^3} \mathrm{Li}_{5/2}(\pm z)
  \label{Phi}
\end{equation}
where $\lambda = (2\pi/T)^{1/2}$ is the de Broglie thermal length, and $\mathrm{Li}_\nu(z)$ is the [polylogarithm](https://en.wikipedia.org/wiki/Polylogarithm) function <strong style="color:DarkSlateBlue; background-color:LightGray;">EX</strong>:
$$\mathrm{Li}_{\nu}(z) = \frac{1}{\Gamma(\nu)} \int_0^\infty \D x \frac{x^{\nu-1}}{z^{-1}\E^x - 1}\,, \quad \mathrm{Li}_\nu(z) = \sum_{n=1}^\infty \frac{z^n}{n^\nu}\,,$$
here $\Gamma(\nu)$ is the Euler gamma function,
$$\Gamma(\nu) = \int_0^\infty \D x \, x^{\nu-1}\E^{-x}\,,$$
see the notes below. Usually, $\pm\mathrm{Li}_{\nu+1}(\pm z)$ are called [bose and fermi integrals](https://dlmf.nist.gov/25.12), respectively. (See the note below.)[^NO] 

Thermodynamic quantities are then obtained form the grand potential:
$$E = -T^2 \frac{\partial}{\partial T} \frac{\Phi(T,z)}{T}\,, \quad
N = -z \frac{\partial}{\partial z} \frac{\Phi(T,z)}{T}\,, $$
for the energy and the number of particles, where, when deriving with respect to $T$ one considers $V=\text{const.}$ and $z=\text{const.}$, and when deriving with respect to $z$, $T=\text{const}$; and
$$S = \frac{E - \mu N - \Phi}{T} = -\left. \frac{\partial\Phi}{\partial T}\right|_z + \left. \frac{\mu z}{T^2} \frac{\partial \Phi}{\partial z}\right|_T = -\left. \frac{\partial \Phi(T,\mu)}{\partial T}\right|_{V,\mu}$$
for the entropy. An immediate consequence of these formulas is that the ideal gas relation,
$$E = \frac{3}{2} PV$$
is satisfied for the free quantum gases <strong style="color:DarkSlateBlue; background-color:LightGray;">EX</strong>.

We can immediately compute the density,
$$\frac{N}{V} = -\frac{z}{VT} \frac{\partial \Phi}{\partial z} = \frac{g_s}{\lambda^3} \mathrm{Li}_{3/2}(z) \approx \frac{g_s}{\lambda^3} \left( z \pm \frac{z^2}{2^{3/2}} \right)$$
we used in the last equation the approximation for $z\ll 1$ (the few first terms of the series defining the $\mathrm{Li}_\nu$ function), near the classical limit of high temperature ($T \gg \mu$); iteratively inverting this last approximation we obtain the fugacity as a power series of the density $N/V=n$,
$$z \approx \frac{\lambda^3 n}{g_s} \left( 1 \mp \frac{1}{2^{3/2}} \frac{\lambda^3n}{g_s} \right)$$
from which we derive an approximated expression for the pressure $P = -\Phi/V$,
$$P \approx nT \left(1 \mp \frac{1}{2^{5/3}} \frac{\lambda^3 n}{g_s} \right)$$
We observe that the effect of the exchange of identical particles is to decrease the pressure of the boson gas with respect to the classical one, and to increase the pressure of the fermion gas. These effectives attraction and repulsion, are not related to particle interactions (of course, the particles are free), they are the result of an *entropic effect*, the identity of particles increases the disorder, or in other terms, it decreases the quantity of information with respect to a system of distinguishable particles. Indeed, the entropy of a system of bosons or fermions is (<strong style="color:DarkSlateBlue; background-color:LightGray;">EX</strong>):
$$ S/G = -\sum_s \left[ n_s \ln n_s \mp (1 \pm n_s) \ln (1 \pm n_s)\right]\,,$$
($G$ is the total number of states such that $N=G\sum_s n_s$) using the bose and fermi distributions: the first term corresponds to the classical entropy, to which a second term is added, *increasing* the value of $S$. The classical limit, valid for bosons and fermions, is recovered when $n_s \ll 1$, when the temperature is large with respect to any microscopic energy.

### Black body and bose degenerate gas

In the limit of low temperature or high density, when the energy per particle is larger than the thermal one, new quantum effects appear in non interacting systems. One of such effects, the black body radiation, is even at the origin of quantum mechanics.

The photon, first described by Einstein (1905) in his work on the photoelectric effect, is a *massless* boson of spin $1$, it has hence only two internal degrees of freedom or polarizations (which are perpendicular to its momentum), it is the quanta of the electromagnetic field. The photon energy $\hbar \omega$ is proportional to the photon momentum $\boldsymbol p = \hbar \boldsymbol k$, where $\omega$ and $\boldsymbol k$ are the frequency (multiplied by $2\pi$) and the wavevector, respectively:
$$\omega = c |\boldsymbol k|$$
with $c = 299\, 792\, 458 \, \mathrm{m\,s^{-1}}$ the speed of light (exact value in SI units). The interaction of the electromagnetic field with matter realizes, in particular, through the emission and absorption of photons by the matter atoms; the balance of these processes, controled exclusively by the temperature, determines the thermodynamical equilibrium: this specific state of matter-radiation equilibrium, is called a "black body". As a consequence of the exchange of photons with matter, the number of photons in a cavity maintained at a fixed temperature is not conserved, and the equilibrium condition leads to the constraint of zero chemical potential $\mu = 0$. Under such constraint the canonical and grand canonical ensembles are identical.

Non interacting massive bosons also show an interesting quantum phenomenon when the energy per particle is much larger than the thermal energy: the ground state energy level $\epsilon_0$, tends to populate at a macroscopic scale. This contrast with the behavior at high temperature where the levels occupation follows the Boltzmann law $n_s \sim \E^{-\epsilon_s/T}$, and equipartition of the energy over all degrees of freedom dominates. This phenomenon, the [Bose-Einstein condensation]({static}/pdfs/PS-BEC.pdf), was observed in the laboratory for the first time at the end of the twenty century, 70 years after their theoretical prediction.

#### Black body radiation

The partition function (it is convenient to introduce units such that $k_{\mathrm{B}}=\hbar=c=1$) is,
$$\ln Z = 2 \sum_{\boldsymbol k \ne 0} \ln (1 - \E^{\omega_{\boldsymbol k}/T} ) = \frac{2V}{(2\pi)^3} \int_0^\infty 4\pi k^2 \D k\, \ln(1 - \E^{-\omega_{\boldsymbol k}/T} )$$
(the factor $2$ accounts for the two polarizations) which, after a change of variable from the wavenumber to the frequency $k = \omega/c = \omega$ together with the substitution $x =\hbar \omega/k_BT = \omega/T$, and an integration by parts, gives <strong style="color:DarkSlateBlue; background-color:LightGray;">EX</strong>,
$$\ln Z = \frac{VT^3}{3\pi^2} \int_0^\infty \D x \frac{x^3}{\E^{x}-1}= \frac{2V}{\pi^2}T^3 \mathrm{Li}_4(1) = \frac{\pi^2V}{45}T^3\,.$$
The free energy is therefore,
$$F = - \frac{\pi^2V}{45}T^4 = -\frac{\pi^2V}{45(\hbar c)^3}T^4\,,$$
from which one obtains the entropy and energy:
$$\frac{S}{V} = \frac{16\sigma}{3c} T^3 \,, \quad \frac{E}{V} = \frac{4\sigma}{c} T^4 \, \quad \sigma = \frac{\pi^2 c k_{\mathrm{B}}^4}{60(\hbar c)^3}\,,$$
where the expression for the energy is the *Stefan law* and $\sigma$ the Stefan constant.

To compute the energy distribution of the radiation, we need to count the number of electromagnetic modes in a cavity of volume $V$; this is naturally given by the wavenumber, $k/2\pi \sim n \in \mathbb{N}$:
$$\text{modes } \sim V \times 2 \times \frac{\D \boldsymbol k}{(2\pi)^3} \;\rightarrow\; V \times \,2 \times 4\pi k^2 \frac{\D k}{(2\pi)^3}\,,$$
where the factor $2$ comes from the two possible polarizations, and the last expression make use of the isotropy of the radiation field by counting the number of modes in a spherical shell of width $\D k$. Note that the number of modes corresponds to the expression we used to replace the summation over the discrete wavenumbers to the integral: $V \D \boldsymbol p/(2\pi \hbar)^3$.

Using the results of the grand canonical ensemble, we find the the average occupation number of photons of energy $\omega$ is,
$$n_\omega = \frac{1}{\E^{\omega/T} - 1},$$
which gives the energy distribution (replacing $k=\omega/c$ in the formula for the number of modes):
$$E(\omega) \D \omega = \frac{VT}{\pi^2} \frac{\omega^3 \D \omega}{\E^{\omega/T} - 1}\,,$$
the *Planck radiation law* (1900). Note that, after integration, one obtains the Stefan law <strong style="color:DarkSlateBlue; background-color:LightGray;">EX</strong>,
$$E = \frac{V}{\pi^2} \int_0^\infty \D \omega\, \frac{\omega^3}{\E^{\omega/T} - 1} = \frac{6V}{\pi^2} T^4 \mathrm{Li}_4(1) = \frac{\pi^2 V}{15} T^4\,,$$
or in Si units:
$$E = \frac{\pi^2 V k_\mathrm{B}^4}{15 (\hbar c)^3} T^4\,,$$
in accordance with the previous result. (See the note below, on the choice of units.)[^UN]

#### Bose-Einstein condensation

The density $n = N/V$ of a free boson gas obeys the formula we derived previously using ($\ref{Phi}$),
$$n = \left(\frac{T}{2\pi}\right)^{3/2} \mathrm{Li}_{3/2}(\E^{\mu/T}) = \left(\frac{T}{2\pi}\right)^{3/2} \sum_{k=1}^\infty \frac{\E^{k\mu/T}}{k^{3/2}}$$
(for spinless particles, $g_s = 1$) that fails to converge for chemical potentials above $\mu = 0$. At the threshold the temperature as a function of the density is given by:
$$T_c = \frac{2\pi}{\zeta(3/2)^{2/3}} n^{2/3} = 3.3125 n^{2/3}\,,$$
lowering further the temperature, at fixed density, would make the chemical potential positive ($\zeta_{3/2}= \zeta(3/2)$ is the Riemann zeta function). The problem is that for $T<T_c$, the approximation consisting in the replacement of the sum over the energy levels by an integral is no longer justified, because a fraction of the particles condenses into the ground state ($\epsilon_{\boldsymbol p} = 0$), the first term of the sum. Indeed, the number of particle residing in the ground state is,
$$N_0= \braket{a^\dagger_0 a_0} = \frac{1}{\E^{\mu/T}-1} = \frac{z}{1-z} \,,$$
which increases to infinity, or becomes negative, at $\mu=0$. Therefore, to avoid the divergences we split the sum into a ground energy term and the rest, the excited states that can be approximated by an integral, to obtain the fraction of particles in the condensate <strong style="color:DarkSlateBlue; background-color:LightGray;">EX</strong>:
$$\frac{N_0}{N} = 1 - \left(\frac{T}{T_c}\right)^{3/2} \,, \quad T \le T_c\,.$$
The Bose-Einstein condensation is just the appearance of a macroscopic fraction of bosons occupying the zero energy ground state. One interesting prediction is that there is a sharp value of the temperature ($=T_c$) at which the transition between the normal state and the condensate happens; in addition, this critical temperature depends on the particle density.

In experiments, boson atoms are trapped in an external potential created by lasers. In a first approximation this potential is harmonic, and thus the energy levels turn to be of the form,
$$\epsilon_{\boldsymbol n} = \hbar \omega\, (n_x + n_y + n_z + 3/2)\,,\quad \boldsymbol n \in \mathbb{N}^3\,,$$
in three dimensions, where the characteristic frequency $\omega$ depends on the curvature of the potential minimum. This expression differs notably with the free particle energy, which is quadratic in the momentum. However, the qualitative picture depicted above, remains true; even if important quantitative differences appear. Let us calculate the thermodynamics of a system of $N$ bosons in a harmonic trap, with energies given by $\epsilon_{\boldsymbol n}$.

The relation between the chemical potential $\mu$ and the number of bosons $N$ is obtained from the summation of the occupation numbers $n_\epsilon$,
$$N = \sum_{\boldsymbol n} \frac{1}{\E^{-\mu/T}\E^{\omega(n_x + n_y + n_z + 3/2)/T} - 1}$$
(as usual we have $k_{\mathrm{B}} = \hbar = 1$). The critical value of the chemical potential is, instead of zero,
$$\mu_c = 3\omega/2\,,$$
for chemical potentials larger than this one, the number of particle would be negative. The number of particles in the ground state $N_0$, $\epsilon_{\boldsymbol n}=\epsilon_0$, is then determined by,
$$ N - N_0 = \sum_{\boldsymbol n \ne 0} \frac{1}{\E^{\omega(n_x + n_y + n_z)/T} - 1}\,,$$
which is the number of particles in the excited states. This sum, being convergent, can safely be approximated by an integral in the limit of large $N\rightarrow\infty$:
$$N-N_0 = \int_0^\infty \frac{\D \boldsymbol n}{\E^{\omega(n_x + n_y + n_z)/T} - 1}\,.$$
The integral can be done transforming the integrand into a power series <strong style="color:DarkSlateBlue; background-color:LightGray;">EX</strong>; however, it is more useful to calculate the density of states $\nu(\epsilon)$ in order to change the $\boldsymbol n$ variable by the energy $\epsilon_{\boldsymbol n}$. In the continuous limit, which is our present approximation, the number of energy levels smaller than $n = \epsilon/\omega$ is the volume $\Omega(n)$ defined by:
$$\Omega(n) = \{n_x \ge 0,\; n_y \ge 0,\; n_z \ge 0,\;\text{with }\, n_x + n_y + n_z \le n\}\,,$$
that is the volume of a pyramid of base a triangle of area,
$$\frac{1}{2}\sqrt{2} \frac{\sqrt{2}}{2} n^2$$
and height $n$, giving a volume $V(n) = \text{area}\times \text{height}/3$,
$$\Omega(n)=\frac{n^3}{6}\,,$$
the sixth of the cube of edge $n$; using that 
$$d\Omega(n) = \frac{n^2}{2} \D n = \frac{\epsilon^2}{2\omega^2} \frac{\D \epsilon}{\omega} = \nu(\epsilon) \D \epsilon\,,$$
we find the density of states of a three dimensional harmonic oscillator,
$$\nu(\epsilon) = \frac{\epsilon^2}{2\omega^3}$$
up to subdominant terms $\mathcal{O(\epsilon/\omega)}$ (our approximation is consistent with the limit $\epsilon/\omega \gg 1$). Therefore, the integral over $\boldsymbol n$ becomes,
$$N-N_0 = \int_0^\infty \D \epsilon\, \nu(\epsilon)n_\epsilon = \int_0^\infty \frac{\D \epsilon}{2\omega^3} \frac{\epsilon^2}{\E^{\epsilon/T} - 1} = \frac{\zeta(3)}{\omega^3} T^3\,.$$
The critical temperature corresponds to the threshold below which the ground state is populated with a macroscopic number of particles. It is then the temperature at which $N_0=0$, or,
$$T_c = \frac{ \hbar \omega}{k_\mathrm{B}} \left( \frac{N}{\zeta(3)}  \right)^{1/3} \,,$$
similar to the free case with, instead of the power $2/3$, we obtain a $1/3$ exponent. The main qualitative difference is that now the critical temperature depens on the number of trapped particles and not, as before, on the particle *density*.

> <img src="{static}/images/PS-bcondensate.svg" height="200">
>
> Franction of condensed particles as a function of the temperature; the dashed line corresponds to the free bosons and the continuous one to the trapped ones.


An analogous computation gives the energy for $T \le T_c$ ($\mu = 3\omega/2$):
$$E = \int_0^\infty \D \epsilon\, \nu(\epsilon)n_\epsilon \epsilon = \int_0^\infty \frac{\D \epsilon}{2\omega^3} \frac{\epsilon^3}{\E^{\epsilon/T} - 1} = \frac{3\zeta(4)}{\omega^3} T^4$$
which obviously determined by exclusively by the excited states $\epsilon > 0$. Using these two last equations, we can write the energy of the condensate as,
$$\frac{E}{NT_c} = \frac{3\zeta(4)}{\zeta(3)} \left( \frac{T}{T_c}\right)^4\,.$$
Note that for free bosons the exponent of the temperature is $5/2$, rather than $4$ for the bosons in a trap. It is also worth mentioning that the harmonic trap makes the bosons behave much like a relativistic degenerate gas, for which the energy is linear in the momentum: $\epsilon_{\boldsymbol p} \sim |\boldsymbol p|$ (compare with the black body expression of the thermodynamic energy, also proportional to the power four of the temperature $E \sim T^4$).

### Degenerate fermions $z \rightarrow \infty$

The occupation number of a fermi gas at energy $\epsilon$ 
$$n_\epsilon = \frac{1}{\E^{(\epsilon - \mu)/T} + 1}$$
and at low temperature $T \ll \mu$, tends to zero if $\epsilon > \mu$ and to one if $\epsilon < 0$:
$$ n_\epsilon = \theta(\epsilon_F - \epsilon),\quad \epsilon_F = \left.\mu\right|_{T=0}$$
at $T=0$, where we defined the fermi energy $\epsilon_F$ as the chemical potential separating the low energy region of occupied levels, to the high energy region of unoccupied levels. The existence of this energy is a result of the exclusion principle: adding fermions to a system a zero temperature, must be done by occupying progressively higher energy unoccupied states. This is in contrast to the bosons, for which increasing the population of the fundamental level do not contribute to the energy.

Using the free particle $\epsilon = p^2/2m$ density of states (take $m=1$) <strong style="color:DarkSlateBlue; background-color:LightGray;">EX</strong>,
$$\nu(\epsilon) = \frac{V\sqrt{2}}{\pi^2} \epsilon^{1/2} \left[ \frac{m}{\hbar^2} \right]^{3/2} \,,$$
(standard units in brackets) we can calculate the number of particles below the fermi level $\epsilon_F$
$$N = \int_0^\infty \D \epsilon\, \nu(\epsilon) n_\epsilon = \frac{V\sqrt{2}}{\pi^2} \int_0^\infty \D \epsilon \, \epsilon^{1/2} \theta(\epsilon_F - \epsilon) = \frac{2}{3} V \frac{\sqrt{2}}{\pi^2} \epsilon_F^{3/2} \,,\quad (T=0)$$
at zero temperature. This formula relates the gas density to the fermi energy:
$$\epsilon_F = \frac{(3\pi^2)^{2/3}}{2} n^{2/3} \; [\hbar^2/m] = T_F \, [k_\mathrm{B}]\,,$$
where we indicate in square brackets the dimensional factor, and defined the fermi temperature $T_F$ (in kelvin). It is also useful to write the density of state in the form,
$$\nu(\epsilon) = \frac{3N}{2} \frac{\epsilon^{1/2}}{\epsilon_F^{3/2}}\,,$$
where we replaced the volume by the number of particles:
$$V = \frac{3\pi^2}{2^{3/2}} \frac{N}{\epsilon_F^{3/2}} \, [\hbar^2/m]^{3/2}\,.$$

In a similar way we calculate the energy,
$$E = \int_0^\infty \D \epsilon\, \nu(\epsilon) n_\epsilon \epsilon = \frac{V\sqrt{2}}{\pi^2} \int_0^{\epsilon_F} \D \epsilon \, \epsilon^{3/2} = \frac{2}{5} V \frac{\sqrt{2}}{\pi^2} \epsilon_F^{5/2}\,, \quad (T=0)$$
or, using the expression of $N$,
$$\frac{E}{N} = \frac{3}{5} \epsilon_F \,.$$

These expressions are valid at $T=0$, the behavior of the degenerated fermi gas at low temperature can be obtained using the asymptotic expansion of the polylogarithm function. In fact, keeping two terms of this expansion,[^NO]
$$-\mathrm{Li}_s(-z) = \frac{(\ln z)^s}{\Gamma(s+1)} + \frac{\pi^2}{6} \frac{(\ln z)^{s-2}}{\Gamma(s-1)}  \,,$$
is enough to estimate the corrections to the zero temperature calculations. The exact formula for the energy is,
$$E = \frac{3}{2}PV = -\frac{3}{2}\Phi = \frac{3}{2} \frac{N}{\epsilon_F^{3/2}} T^{5/2} \int_0^\infty \D x \frac{x^{3/2}}{z^{-1}\E^x + 1}\,,$$
where we substituted the volume $V$ by its expression in terms of the fermi energy,
$$V = \frac{3}{2} \frac{\pi^2}{\sqrt{2}} \frac{N}{\epsilon_F^{3/2}}\,,$$
and the integral is $-\Gamma(5/2) \mathrm{Li}_{5/2}(-z)$. Therefore,
$$E = \frac{3}{2} \frac{N}{\epsilon_F^{3/2}} \left( \frac{2}{5} \mu^{5/2} + \frac{\pi^2}{4} T^2 \mu^{1/2} \right)\,.$$
The grand potential in the gran canonical natural variables is then,
$$\Phi(T,\mu,V) = -\frac{2\sqrt{2}}{3\pi^2} V \left( \frac{2}{5} \mu^{5/2} + \frac{\pi^2}{4} T^2 \mu^{1/2} \right)\,.$$
Now, the equation of $N$ at finite temperature gives an implicit formula for the chemical potential:
$$N= \frac{3}{2} \frac{N}{\epsilon_F^{3/2}} T^{3/2} \int_0^\infty \D x \frac{x^{1/2}}{z^{-1}\E^x + 1} = -\frac{3}{2} \frac{N}{\epsilon_F^{3/2}} T^{3/2} \Gamma(3/2) \mathrm{Li}_{3/2}(-z)\,,$$
or, substituting the asymptotic expansion,
$$1 = \frac{\mu^{3/2}}{\epsilon_F^{3/2}} \left[ 1 + \frac{\pi^2}{8} \left( \frac{T}{\mu}\right)^2\right]\,,$$
which is readily inverted to obtain,
$$\mu = \epsilon_F \left[ 1 - \frac{\pi^2}{12} \left( \frac{T}{\epsilon_F}\right)^2\right]\,,$$
in agreement with the definition $\mu = \epsilon_F$ at $T=0$, plus a quadratic correction in the temperature. Note that to obtain this relation $N=N(\mu$) we also could use more straightforwardly $N=-\partial \Phi/\partial \mu$.

Putting the value of $\mu$ in the formula for $E$, we finally get an explicit expression of the energy in the range $T \ll \epsilon_F$,
$$E = \frac{3}{5} N \epsilon_F \left[ 1 + \frac{5\pi^2}{12} \left( \frac{T}{\epsilon_F}\right)^2\right]\,.$$
$$\frac{C_V}{N} = \frac{\pi^2}{2} \frac{T}{\epsilon_F}\,,$$
linear in $T$, and similarly for the entropy,
$$S = -\frac{\partial \Phi}{\partial T} = N \frac{\pi^2}{2} \frac{T}{\epsilon_F}\,,$$
This is an important result, showing that the specific heat and the entropy at low temperatures of a fermi gas, tend to zero in accordance with the Nernst principle.

## Notes

[^NO]: **Polylogarithmic** function

    The polylogarithmic function is defined be the series,
    $$\mathrm{Li}_\nu(z) = \sum_{n=1}^\infty \frac{z^n}{n^\nu}\,,$$
    which can be viewed as a generalization of the Riemann zeta function,
    $$\zeta(\nu) = \mathrm{Li}_\nu(1) = \sum_{n=1}^\infty \frac{1}{n^\nu}\,.$$
    Analytic continuation gives the integral formula,

    $$\mathrm{Li}_{\nu}(z) = \frac{1}{\Gamma(\nu)} \int_0^\infty \D x \frac{x^{\nu-1}}{z^{-1}\E^x - 1}\,.$$

    The asymptotic expansion for large $z$ of the polylogarithm is,

    $$\mathrm{Li}_s(-z) = -2 \sum_{k=0}^\infty \eta(2k) \frac{(\ln z)^{s-2k}}{\Gamma(s-2k+1)}\,$$

    where the Dirichlet function $\eta$ is related to the Riemann zeta:

    $$\eta(s) = (1-2^{1-s}) \zeta(s)\,,\quad \eta(1) = \ln 2$$

    and 

    $$\zeta(2k) = -\frac{1}{2} (2\pi)^{2k} \frac{(-1)^{k} B_{2k}}{(2k)!}, \quad \zeta(2) = \frac{\pi^2}{6},\; \zeta(4) = \frac{\pi^4}{90}$$

    where $B_n$ are the Bernoulli numbers. This asymptotic expansion can be obtained using the Sommerfeld method <strong style="color:DarkSlateBlue; background-color:LightGray;">EX</strong>.

    The two first terms of the asymptotic expansion,
    
    $$-\mathrm{Li}_s(-z) = \frac{(\ln z)^s}{\Gamma(s+1)} + \frac{\pi^2}{6} \frac{(\ln z)^{s-2}}{\Gamma(s-1)}  \,,$$

    The derivative of the polylogarithmic function of order $\nu$ depends on the function of order $\nu-1$:

    $$z \frac{\partial}{\partial z} \mathrm{Li}_\nu(z)  = \mathrm{Li}_{\nu-1}(z)\,.$$

    Explicit values of the Gamma function,

    $$n! = \Gamma(n+1)\,, \quad \Gamma(n+ 1/2) = \frac{(2n)!}{4^nn!}\sqrt{\pi}$$

[^UN]: Note on the choice of **units**

    With the convention $k_\mathrm{B} = \hbar = c = 1$, one may apply the conversion factors:

    $$1\,[\mathrm{m}] = \frac{1}{c}\,[\mathrm{s}], \quad 1 [\mathrm{m^{-1}}] = \frac{\hbar}{c}\,[\mathrm{kg}] = \hbar c\,[\mathrm{J}] = \frac{\hbar c}{k_{\mathrm{B}}} \, [\mathrm{K}]$$

    using the SI numerical values of the physical constants. For instance, to recover the Stefan constant from its value, one introduces the dimensional units $\mathrm{J/s\, m^2\, K^4}$ using the above factors:

    $$\frac{k_\mathrm{B}^4}{c^2\hbar^3} =  3.44716123286048\,10^{-7} \frac{\mathrm{J}}{\mathrm{s\, m^2\, K^4}}$$

    from which one obtains

    $$\sigma = \frac{\pi^2}{60} \frac{k_\mathrm{B}^4}{c^2\hbar^3} = 5.67035294585\,10^{-8} \, \mathrm{J/s\, m^2\, K^4}$$

    Consider the nondimensional expresion $V T^3$ and note that $\hbar c$ is an energy times length, then:

    $$VT^3 \rightarrow V \left( \frac{ k_B T}{\hbar c} \right)^3\,.$$
    
    This trick allows recovering of the SI units easily.
