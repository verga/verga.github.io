Title: Problems and exercises: quantum gases
Slug: PS-A_qgas
Date: 2019-08-17
Category: Lectures
Tags: teaching, statistical physics
Authors: Alberto Verga
Summary: Problems on non-interacting Bose and Fermi gases
status: hidden

$\newcommand{\I}{\mathrm{i}} 
\newcommand{\E}{\mathrm{e}} 
\newcommand{\D}{\mathop{}\!\mathrm{d}} 
\newcommand{\bra}[1]{\langle{#1}|}
\newcommand{\ket}[1]{|{#1}\rangle}
\newcommand{\braket}[1]{\langle{#1}\rangle}
\newcommand{\bbraket}[1]{\langle\!\langle{#1}\rangle\!\rangle}$

> [Lectures]({filename}PS-index.md) on statistical mechanics.

### 1 

Investigate how the usual laws of Stefan black body radiation $\sim T^4$, and Debye specific heat of a solid $\sim T^3$, are modified if one assumes that the spatial dimension is $D$.

We start with the computation of the solid angle in $D$-dimensions. From dimensional analysis we can write that the area of a $D$-sphere is $A_D = \Omega_D R^{D-1}$, where the numerical constant $\Omega_D$ is the solid angle. The corresponding volume would be $ V_D = A_D (R/D)$. Note that the integral,
$$I_D = \left( \int_{-\infty}^\infty \D x \, \E^{-x^2} \right)^D = \pi^{D/2}\,,$$
is a multidimensional gaussian,
$$I_D = \int_{-\infty}^{\infty} \D x_1 \ldots \D x_D \, \exp\left( \sum_{n=1}^{D} x^2_n \right)\,.$$
Writing the volume element as,
$$\D x_1 \ldots \D x_D = \Omega_D R^{D-1} \D R, \quad R^2 = \sum_{n=1}^D x_n^2\,,$$
we obtain,
$$I_D = \Omega_D \int_{0}^\infty \D R \, R^{D-1} \E^{-R^2}\,,$$
and, changing the variable to $x=R^2$, $\D x/2\sqrt{x} = \D R$, we can transform the integral into the euler gamma function:
$$I_D = \frac{\Omega_D}{2} \int \D x \, x^{D/2-1} \E^{-x} = \frac{\Omega_D}{2} \Gamma\left( \frac{D}{2} \right)\,,$$
which finally gives,
$$\Omega_D = \frac{2\pi^{D/2}}{\Gamma(D/2)}\,.$$

Now we calculate the density of states. For a photon $\epsilon = c p$:
\begin{align*}g(\epsilon)\D \epsilon &= g L^D \Omega_D p^{D-1} \frac{\D p}{(2\pi\hbar)^D} \\ &= \frac{ 2^{1-D} g V_D }{ \pi^{D/2} (\hbar c)^D \Gamma(D/2) } \epsilon^{D-1} \D \epsilon \\ &= g_D \epsilon^{D-1} \D \epsilon\,,\end{align*}
where $g = D-1$ are the number of the photon polarization states (for the phonons we replace it by $g = D$ degrees of freedom), $L$ is the hypercube side length, $V_D = L^D$, and we used the fact that the photon field is isotrope, uniformly distributed over the $\Omega_D$ directions, and its number is proportional to the volume of a sphere of radius $\sim L \epsilon/\hbar c$, up to an energy equal to $\epsilon$. The phonon density of states is similar with the velocity of light $c$ replaced by the sound speed $c_s$. Note that the first line of the previous formula is general, the second line may change if the dispersion relation changes (the relation between energy and momentum).

We can now compute the partition function,
$$Z(T,V_D) = \sum_{\{n_s\}} \E^{-\epsilon_s n_s/T}\,,$$
where $n_s$ is the boson occupation number of state $\epsilon_s$. Therefore,
$$Z(T, V_D) = \prod_s \sum_{n_s = 0}^\infty \E^{-\epsilon_s n_s/T} = \prod_s \big(1 - \E^{-\epsilon_s/T}\big)^{-1}\,,$$
and,
$$\ln Z(T, V_D) = - \sum_s \ln \big(1 - \E^{-\epsilon_s/T}\big)\,,$$
or, approximating the sum by an integral over the energies, we obtain,
$$\ln Z(T, V_D) = - \int_0^\infty \D \epsilon \, g(\epsilon) \ln \big(1 - \E^{-\epsilon/T}\big)\,.$$
This formula is valid for $\mu = 0$ and non-interacting bosons; then it can be applied to photons as well as phonons or other quasiparticles having bose statistics.

Using the above results on the density of states we get,
$$\ln Z(T, V_D) = -g_D V_D \int_0^\infty \D x \, x^{D-1} \ln \big(1 - \E^{-x} \big) T^D \equiv g_D V_D C_D T^D\,,$$
where we defined the numerical constant $C_D$ to find the dependency on the temperature explicitly:
$$C_D = \frac{1}{D} \int_0^\infty \D x \, \frac{x^D}{\E^{x} - 1} = \frac{\Gamma(D+1)}{D} \mathrm{Li}_{D+1}(1)$$
using the polylogarithm function $\mathrm{Li_s(z)}$, which for $z=1$ and $s>0$ is given by the riemann zeta, $\mathrm{Li}_s(1) = \zeta(s)$. In particular for $s=4=D+1)$, we have $C_3 = \pi^4/45$ and one recovers the three dimensional result.

From the partition function we derive the thermodynamic quantities:

* Pressure, $P = (T/V_D) \ln Z = g_D C_D T^{D+1}$
* Energy density, $e = -(1/V_D) \partial \ln Z/ \partial (1/T) = D g_D C_D T^{D+1}$
* Entropy density, $s = (1/V_D) \partial PV_D/ \partial T|_{V_D} = (D+1) g_D C_D T^D$
* Specific heat (at constant volume), $C_V = \partial u/\partial T|_{V_D} = D(D+1)g_D C_D T^D$

Note that the ratio $P/e = 1/D$. Therefore, for general $D$ we find,
$$C_V \sim T^D$$
for photons; for phonons this is also the low temperature behavior, at high temperature we have to take into account the Debye high frequency correction:
$$\int_0^{\hbar \omega_M} \D \epsilon g(\epsilon) = \frac{g_D (\hbar \omega_M)^D}{D} = D N, \quad g_D = \frac{ 2^{1-D} D V_D }{ \pi^{D/2} (\hbar c_s)^D \Gamma(D/2) }\,,$$
which means that the number of phonons cannot exceed the total number of oscillation modes in the solid; this defines the Debye cutoff frequency $\omega_D$ (assuming for simplicity a mean isotropic sound velocity $c_s$). In $D=3$,
$$\omega_M = \left(\frac{6\pi^2N}{V}\right)^{1/3} c_s\,.$$
Therefore, the appropriated density of states in the Debye interpolation approximation, is,
$$g(\epsilon) = \Theta(\hbar \omega_M - \epsilon) g_D \epsilon^{D-1}\,.$$
that can be applied to compute the thermodynamic quantities over the whole temperature range. In fact, even if the low temperature approximation is accurate, the actual behavior of solids at finite or high temperature is only roughly captured by the Debye interpolation formula. The Debye formulas depend on $C_D$ with the cutoff at $\omega_M$:
$$C_D(\omega_M/T) = \frac{1}{D} \int_0^{\hbar \omega_M/T} \D x \, \frac{x^D}{\E^{x} - 1}\,.$$ 

The internal energy is,
\begin{align*}E(T) &= \int_0^{\hbar \omega_M} g(\epsilon) \D \epsilon \, \frac{\epsilon}{\E^{\epsilon/T} - 1} \\ &= \frac{ND^2}{(\hbar \omega_M)^D} \int_0^{\hbar \omega_M} \D \epsilon \frac{\epsilon^D}{\E^{\epsilon/T} - 1} \\ &= \frac{ND^3}{(\hbar \omega_M)^D} T^{D+1} C_D(\omega_M/T)\end{align*}
and the specific heat, its temperature derivative:
$$C_V = \frac{ND^3}{(\hbar \omega_M)^D} \left[ (D+1) C_D + T \frac{\D C_D}{\D T} \right] T^D\,.$$

In the high temperature regime $T \gg \hbar \omega_M$,
$$C_D(\omega_M) \approx \frac{1}{D^2} \left(\frac{\hbar \omega_M}{T}\right)^D - \frac{1}{2D(D+1)} \left(\frac{\hbar \omega_M}{T}\right)^{D+1} + \frac{1}{12D(D+2)} \left(\frac{\hbar \omega_M}{T}\right)^{D+2} + \cdots$$
which gives, after replacement, the specific heat,
$$C_V \approx ND \left[ 1 - \frac{D}{12(D+2)} \left(\frac{\hbar \omega_M}{T}\right)^2 + \cdots \right]\,.$$
We observe that the leading term is the classical expression for the heat capacity (independent of the temperature) and the correction is negative ($\sim 1/T$).

### 2

Graphite is a stack of weakly coupled flat crystal layers of carbon atoms; experiments show that, instead of the usual Debye scaling with the temperature, the specific heat of graphite is proportional to $T^2$. Explain this behavior. You may assume that oscillations are two dimensional and the sound velocity is anisotropic (one mode through the layers, and two modes, on the layer plane).

We assume that $k_z$ oscillations are negligible with respect to the plane $(k_x,k_y)$ oscillations, thus giving $k \approx \sqrt{k_x^2 + k_y^2}$: due to the layered structure of graphite and the weak coupling between layers, only two dimensional phonons are important in this approximation. The density of states, for a linear dispersion, can then be written as,
$$ g(\omega) = \frac{L^2 2\pi\omega}{(2\pi)^2} \left( \frac{1}{c_z^2} + \frac{2}{c^2} \right) \,,$$
where we used that in the interval $k$ to $k+ \D k$ the number of modes is $(L/2\pi)^2 2\pi k \D k$, for a square of side $L$.

We use the Debye interpolation formula, and introduce the cutoff frequency $\omega_M$ (see previous exercise). The thermodynamic energy is given by,
$$E = \hbar \int_0^{\omega_M} \D \omega \frac{g(\omega) \omega}{\E^{\hbar \omega/T} - 1}\,,$$
or
$$C_V = \frac{\D E}{\D T} = \int_0^{\omega_M} \D \omega \, \frac{g(\omega)}{\big( \E^{\hbar \omega/T} - 1 \big)^2} \left( \frac{\hbar \omega}{T} \right)^2\,,$$
which, after a straightforward change of variable, can be written as,
$$C_V = \frac{L^2}{2\pi \hbar^2} \left( \frac{1}{c_z^2} + \frac{2}{c^2} \right) I\left( \frac{\hbar \omega}{T} \right) T^2\,,$$
where,
$$I(z) = \int_0^z \D x \, \frac{x^3 \E^x}{(\E^x - 1)^2}\,.$$
At low temperatures $\hbar \omega \gg T$, the limit of the integral can be extended to infinity, $I(\infty) = 6 \zeta(3)$, giving the behavior $C_V \sim T^2$:
$$C_V \approx \frac{3L^2}{\pi \hbar^2} \left( \frac{1}{c_z^2} + \frac{2}{c^2} \right) \zeta(3) T^2\,,$$
which tends to zero for $T \rightarrow 0$ is it should, the characteristic exponent is $\sim T^2$, differs from the usual phonon behavior in a solid ($\sim T^3$).

At high temperature $T \gg \hbar \omega$, the dimensionless variable $x=\hbar \omega/T$ is small; we can the use the expansion $\E^x = 1+ x$ of the exponential inside the integral:
$$I(z) \approx \int_0^z \D x\, \frac{x^3}{x^2}= \frac{z^2}{2} = \frac{1}{2}\left( \frac{\hbar \omega_M}{T} \right)^2 \,,$$
which leads to the classical result:
$$C_V = \frac{1}{4\pi} \left( \frac{1}{c_z^2} + \frac{1}{c^2} \right) (L\omega_M)^2\,,$$
note in addition that $(L\omega_M)^2 = N (a\omega_M)^2$, if $a$ is the crystal step and $N$ the total number of atoms in each layer (the physical quantities are defined per length unit in the $z$ direction).


### 3

Identical particles. A system consists in two identical non interacting particles in contact with a bath at $T$. Calculate the partition function of the two particle system $Z_2$ in terms of the one particle $Z_1$, in the case of bosons and fermions (spinless). Assuming that $Z_1 = V/\lambda^3$, compute the thermodynamics of the two particles system: energy, pressure and heat capacity at constant volume ($\lambda^2 = 2\pi\hbar^2/mT$).

The state of a free particle is determined by its momentum $p=\hbar k$, the eigenvalue of the $P$ operator. For two bosons the quantum state is symmetric,
$$\ket{p_1,p_2}_B = \begin{cases} \frac{1}{\sqrt{2}} \big( \ket{p_1}\ket{p_2} + \ket{p_2}\ket{p_1} \big) & \text{for}\; p_1 \ne p_2 \\ \ket{p}\ket{p} & \text{for}\; p_1 = p_2 = p \end{cases}\,,$$
and for fermions the state is antisymmetric,
$$\ket{p_1,p_2}_F = \begin{cases} \frac{1}{\sqrt{2}} \big( \ket{p_1}\ket{p_2} - \ket{p_2}\ket{p_1} \big) & \text{for}\; p_1 \ne p_2 \\ \text{no state} & \text{for}\; p_1 = p_2 = p \end{cases}\,.$$
The two particles partition function is defined by,
$$Z_2(V,T) = \mathrm{Tr}\, \E^{-H/T}, \quad H = \frac{P_1^2}{2m} + \frac{P_2^2}{2m}\,.$$
For bosons we consider the symmetric state to compute the trace:
$$Z_2^B = \sum_{p_1 > p_2} \frac{1}{2} \big( \bra{p_1}\bra{p_2} + \bra{p_2}\bra{p_1} \big) \E^{-H/T} \big( \ket{p_1}\ket{p_2} + \ket{p_2}\ket{p_1} \big) + \sum_p \bra{p}\bra{p} \E^{-H/T} \ket{p} \ket{p} \,.$$
Using $p_1>p_2$ in the first sum we avoid counting twice the same configuration. In momentum representation $H$ is diagonal and one can replace the operator by its eigenvalues, when applied to a momentum ket:
$$Z_2^B = \sum_{p_1 > p_2} \exp\left( -\frac{p_1^2 + p_2^2}{2mT} \right) + \sum_p \exp\left( -\frac{p^2}{mT} \right)$$
or, equivalently,
$$Z_2^B = \frac{1}{2} \sum_{p_1 , p_2} \exp\left( -\frac{p_1^2 + p_2^2}{2mT} \right) + \frac{1}{2} \sum_p \exp\left( -\frac{p^2}{mT} \right)$$
which can be related to the one particle partition function:
$$Z_2^B = \frac{1}{2} Z_1^2(V,T) + \frac{1}{2} Z_1(V,T/2)$$
where in the second term we absorbed the factor two in the exponential as a rescaling of the temperature.

A similar computation, using the antisymmetric state, gives the fermion partition function:
$$Z_2^F = \frac{1}{2} Z_1^2(V,T) - \frac{1}{2} Z_1(V,T/2)$$
which differs to the boson one, in the sign of the second term. This second term contains the quantum correlations of identical particles; the first term corresponds to the classical result.

Indeed, if we take the classical result (perfect gas),
$$Z_1 = \frac{V}{\lambda^3},\quad \lambda = \sqrt{2\pi\hbar^2/mT}$$
for the one particle partition function, we see that quantum effects are negligible if $\lambda \ll V^{1/3}$, the thermal wavelength is small with respect to the system's size. In such a case the second term can be dropped, giving a result which is independent of the quantum statistics; however, it naturally includes the factor $2! = 2$ which takes into account the identity of particles.

In this approximation, we can expand the logarithm of the partition function,
$$Z_2(T) = \frac{1}{2} Z_1^2(T) \left[ 1 + \frac{Z_1(T/2)}{Z_1^2(T)} \right]$$ 
as
$$\ln Z_2(T) \approx 2 \ln Z_1(T) \pm \frac{Z_1(T/2)}{Z_1^2(T)} - \ln 2$$
(the upper sign is for bosons, and the lower one is for fermions) to obtain the quantum correction to the classical result (the second term in the previous expansion),
$$\Delta \ln Z_2(T) = \pm \frac{\lambda(T)^3}{V} \frac{\lambda(T)^3}{\lambda(T/2)^3}$$
or,
$$\Delta \ln Z_2(T) = \pm \left( \frac{\pi \hbar^2}{m} \right)^{3/2} \frac{1}{V T^{3/2}}\,.$$
The internal energy correction is,
$$\Delta E_\pm = - \frac{\D \Delta\ln Z_2}{\D (1/T)} = \mp \left( \frac{\pi \hbar^2}{m} \right)^{3/2} \frac{3}{2V T^{1/2}}\,,$$
and the heat capacity,
$$C_V(T)_\pm = \pm \frac{3}{4V} \left( \frac{\pi \hbar^2}{m T} \right)^{3/2}\,,$$
showing that the correction vanishes at high temperatures.


### 4

Bose gas in $D$ dimensions. Generalize the computation of a free Bose gas $\epsilon = p^2/2m$, to $D$ dimensions. Calculate the grand potential $\Phi_D(T,\mu,V)$ by approximating the sum over energies by an integral. Establish the range of validity of this approximation and, if necessary, separate the fundamental state from the integral in the computation of the number of particles. Deduce the thermodynamic properties, $N$, $P$, $E$ and $C_V$. Sketch $C_V(T)$ for all temperatures.

The grand partition function is,
$$Z = Z(z,V,T) = \prod_p \sum_{n_p = 0}^\infty \E^{-n_p \epsilon_p/T} z^{n_p}\,,$$
where the product is over the momentum, $n_p$ is the number of particles with momentum $p$, $\epsilon_p = p^2/2m$ the particle's energy, and $z=\E^{\mu/T}$ is the fugacity. Summing the series, we get,
$$Z = \prod_p \big(1 - z \E^{-\epsilon_p/T} \big)^{-1}\,.$$
To obtain the mean number of particles $\braket{N}$, we use,
$$\braket{N} = \frac{\partial \ln Z}{\partial \ln z} = \sum_p  \big(z^{-1} \E^{\epsilon_p/T} - 1\big)^{-1}\,.$$
In order to compute this sum, we must count the momentum states. In a box of side $L$ in $D$ dimensions, each component of the momentum takes the quantized values $p=\hbar(2\pi/L)k$ with $k$ an integer; when $L$ is large, the spacing between nearby modes tighten, and we can replace the sum by an integral over the energies $\epsilon=\epsilon_p$:
$$\sum_p \rightarrow \int_0^\infty \D \epsilon \, g(\epsilon)\,$$
where the density of states $g(\epsilon)$, is deduced from the number of states $N(\epsilon)$ of energy below $\epsilon$, filling a sphere of radius $R(\epsilon) = k = (L/2\pi\hbar) (2m\epsilon)^{1/2}$:
$$N(\epsilon) = \frac{\Omega_D}{D} R^D(\epsilon), \quad \Omega_D = \frac{2\pi^{D/2}}{\Gamma(D/2)}\,,$$
(see problem 1 in this series) which gives,
$$g(\epsilon) = \frac{\D N(\epsilon)}{\D \epsilon} = \frac{V_D}{2(2\pi\hbar)^D} \Omega_D (2m)^{D/2}\epsilon^{D/2-1} = V_D g_D \epsilon^{D/2-1}$$
where $V_D = l^D$ is the system's volume, and $g_D = (\Omega_D/2) (m/2\pi^2\hbar^2)^{D/2}$. However, the replacement of the sum by the integral supposes that only an infinitesimal fraction of particles occupies each state, assuring convergence; this requirement cannot be satisfied if the fugacity of the ground state ($\epsilon_p=0$) tends to unity, signaling that a macroscopic fraction of the available $N$ particles condense. In order to take into account the population of the ground state we separate this term form the sum to write:
$$ \frac{\braket{N}}{V_D} = n = g_D \int_0^\infty \D \epsilon \, \frac{\epsilon^{D/2-1}}{z^{-1} \E^{\epsilon/T} - 1} + \frac{1}{V_D} \frac{z}{1-z}\,.$$
This formula that, unless $z \rightarrow 1$, the second term is negligible in the thermodynamic limit ($N, V \rightarrow \infty$ with fixed density $n = N/V$). Otherwise, and if the integral is convergent, for $z \rightarrow 1$ the gas form a condensate with density,
$$n_0 = \frac{1}{V_D} \frac{z}{1-z}\,,$$
or,
$$z \approx 1 - \frac{1}{n_0V}\,.$$
Convergence of the integral for $z \approx 1$ is ensured only if $D>2$; otherwise the numerator $\epsilon^{D/2-1}$ diverges at $\epsilon \rightarrow 0$, and the separation between ground and excited states do not longer holds. Therefore, the condensation effect cannot take place in $D = 1$ or $D = 2$ systems.

The excited states are described by the first integral term:
$$n(T) = g_D \Gamma(D/2) \mathrm{Li}_{D/2}(z) T^{D/2}\,,$$
where
$$\mathrm{Li}_s(z) = \frac{1}{\Gamma(s)} \int_0^\infty \D x \frac{x^{s-1}}{z^{-1} \E^x -1}\,,$$
is the polylogarithm function. At $T=0$ we expect that $n_0 = N/V$, at high temperature the fraction of particles in the ground state tends to zero; therefore, we define the condensation temperature $T=T_c$ at $z=1$ and $n_0 =0$,
$$ \frac{N}{V} = g_D\Gamma(D/2) \zeta_{D/2} T_c^{D/2}\,.$$
where $\mathrm{Li}_{D/2}(1) = \zeta_{D/2}$,
$$T_c = \left( \frac{n}{g_D \Gamma(D/2) \zeta_{D/2}} \right)^{2/D}\,,$$
for fixed density $n$. Below $T_c$, $n_0$ is finite but $z =1$ remains near one ($V \rightarrow \infty$),
$$ \frac{N}{V} = n = n_0 + n\left( \frac{T}{T_c} \right)^{D/2}\,,$$
or,
$$ \frac{n_0}{n} = 1 - \left( \frac{T}{T_c} \right)^{D/2}\,.$$

We compute now, using the same method, the thermodynamic potential $\Phi$:
$$\ln Z = -\sum_p \ln \big(1 - z \E^{-\epsilon_p/T} \big) \approx - \ln(1 -z) - \int_0^\infty \D \epsilon \, \ln\big( 1 - z \E^{-\epsilon/T} \big)\,.$$
Integrating by parts we find,
$$\Phi = -T\ln Z = T \ln(1 - z) - \int_0^\infty \D \epsilon \, \frac{N(\epsilon)}{z^{-1} \E^{\epsilon/T} - 1}\,,$$
where the number of states can be written, using the previous notations,
$$N(\epsilon) = \frac{2}{D} V_D g_D \epsilon^{D/2}\,.$$
From the relation $\Phi = -PV$, we obtain the state equation of the Bose gas,
$$ P = -\frac{T}{V_D} \ln(1 - z) + \frac{2g_D}{D} \Gamma(D/2+1) \mathrm{Li}_{D/2+1}(z) T^{D/2+1}\,,$$
where the first term is negligible in the thermodynamic limit, above an below $T_c$ (below $T_c$ it goes to zero as $\ln V/ V \rightarrow 0$). Therefore, the equation of state, in parametric form, with parameter the fugacity is,
$$P = \frac{2g_D}{D} \Gamma(D/2+1) \mathrm{Li}_{D/2+1}(z) T^{D/2+1}\,,$$
and, for $T > T_c$,
$$n = g_D \Gamma(D/2) \mathrm{Li}_{D/2}(z) T^{D/2}\,,$$
which can be written,
$$P = nT \frac{\mathrm{Li}_{D/2+1}(z)}{\mathrm{Li}_{D/2}(z)}\,,$$
to stress the difference with respect to the ideal gas. Below $T_c$, the pressure is ($z = 1$),
$$P = g_D\Gamma(D/2) \mathrm{Li}_{D/2+1}(1) T^{D/2+1}$$
The internal energy is,
$$E = - \frac{\partial \ln Z}{\partial (1/T)} = \frac{D}{2} PV_D\,,$$
or, equivalently ,
$$E = \int_0^\infty \D \epsilon \, \frac{g(\epsilon) \epsilon}{z^{-1} \E^{\epsilon/T} - 1}\,,$$
for $T>T_c$ and $z=1$ for $T<T_c$, which gives,
$$E = \frac{D}{2} V_D g_D \Gamma(D/2) \mathrm{Li}_{D/2+1}(z) T^{D/2+1}\,.$$
The heat capacity per unit volume is thus, 
$$c_V = \left. \frac{\partial E}{\partial T} \right|_{N,V_D,z} + \left. \frac{\partial E}{\partial z}\right|_{N,V_D,T} \left. \frac{\partial z}{\partial T} \right|_{N,V_D}\,,$$
giving,
$$c_V = \frac{D}{2} g_D \Gamma(D/2) T^{D/2} \left[ \left( \frac{D}{2} + 1 \right) \mathrm{Li}_{D/2+1}(z) + \frac{T}{z} \left. \frac{\partial z}{\partial T} \right|_{N,V_D} \mathrm{Li}_{D/2}(z) \right]\,.$$
To calculate the last derivative we use the expression of the density,
$$n = \frac{1}{V_D} \frac{1}{1-z} + g_D \Gamma(D/2) \mathrm{Li}_{D/2}(z) T^{D/2}\,,$$
(which is fixed) and derive it with respect to the temperature, to obtain
$$ \frac{T}{z} \left. \frac{\partial z}{\partial T} \right|_{N,V_D} = - \frac{(D/2)g_D \Gamma(D/2) \mathrm{Li}_{D/2}(z) T^{D/2}}{g_D \Gamma(D/2) \mathrm{Li}_{D/2-1}(z) T^{D/2} + \frac{1}{V_D} \frac{z}{(1-z)^2}} \,.$$
In the thermodynamic limit for $T>T_c$ the term in $1/V_D$ vanishes ($z<1$) and fot $T<T_c$ it diverges, giving $\partial z/\partial T \rightarrow 0$. For $T>T_c$,
$$c_V = \frac{D}{2} n\, \left[ \left( \frac{D}{2} + 1 \right) \frac{\mathrm{Li}_{D/2+1}(z)}{\mathrm{Li}_{D/2}(z)} - \frac{D}{2} \frac{\mathrm{Li}_{D/2}(z)}{\mathrm{Li}_{D/2-1}(z)} \right]\,,$$
which tends to the classical result $c_V \rightarrow Dn/2$ at high temperature ($T \gg T_c$). For low temperatures $T < T_c$,
$$c_V =  \frac{D}{2} \left( \frac{D}{2} + 1 \right) n\, \frac{\mathrm{Li}_{D/2+1}(1)}{\mathrm{Li}_{D/2}(1)} \left( \frac{T}{T_c} \right)^{D/2}\,,$$
it grows as $T^{D/2}$.

The behavior around the condensation transition, can be studied by computing the $c_V$ difference across $T_c$ is,
$$\Delta c_V = \lim_{z \to 1} n(T) \left( \frac{D}{2} \right)^2 \frac{\mathrm{Li}_{D/2}(z)}{\mathrm{Li}_{D/2-1}(z)}\,.$$
If $D/2 - 1 > 1$ the polylogarithm tends to the zeta function at $z=1$, then a jump of the specific heat is expected, otherwise, if $D/2 \le 2$ the specific heat is continuous at the condensation temperature $T_c$. Indeed, near $z=1$ for $s<1$, we know that
$$\mathrm{Li}_s(z) \approx \Gamma(1 - s) (1 - z)^{s - 1}\,,$$
diverges, making the ratio $\mathrm{Li}_{D/2}/\mathrm{Li}_{D/2-1}$ to vanish.


> <img src="{static}/images/PS-bc.svg" height="200">
>
> Schema of the specific heat showing a cusp at $T=T_c$ for $D=3$.

To demonstrate the existence of a cusp in the $c_V$ for $D=3$ at $T=T_c$, we compute the jump in its derivative. For $T>T_c$ and fixed $n$,
$$T \left. \frac{\partial c_V}{\partial T} \right|_{N,V} = \frac{T}{z} \left. \frac{\partial z}{\partial T} \right|_{N,V_D} z \left. \frac{\partial c_V}{\partial z} \right|_{N,V}\,,$$
and using,
$$\frac{T}{z} \left. \frac{\partial z}{\partial T} \right|_{N,V} = - \frac{3}{2} \frac{\mathrm{Li}_{3/2}(z)}{\mathrm{Li}_{1/2}(z)}$$
we obtain,
$$T \left. \frac{\partial c_V}{\partial T} \right|_{N,V} = \frac{9}{4} n \, \left[ \frac{5}{2} \frac{\mathrm{Li}_{5/2}(z)}{\mathrm{Li}_{3/2}(z)} - \frac{\mathrm{Li}_{3/2}(z)}{\mathrm{Li}_{1/2}(z)} - \frac{3}{2} \frac{\mathrm{Li}_{3/2}^2(z) \mathrm{Li}_{-1/2}(z)}{\mathrm{Li}_{3/2}^3(z)} \right]\,.$$
Below $T_c$, we have,
$$T \left. \frac{\partial c_V}{\partial T} \right|_{N,V} = \frac{45}{8} n\, \frac{\mathrm{Li}_{5/2}(1)}{\mathrm{Li}_{3/2}(1)} \,.$$
Therefore,
$$T \Delta \left. \frac{\partial c_V}{\partial T} \right|_{N,V} = \frac{27}{16\pi} \zeta^2(3/2) \frac{n}{T_c}\,.$$


### 5

A fermion gas is confined in a two dimensional device. Compute the fermi energy, and the chemical potential as a function of the temperature.

The momentum in a system of size $L$ is quantized to $p = (2m\epsilon)^{1/2} = 2\pi \hbar k/L$, where $k$ is an integer; the number of modes of energy smaller than $\epsilon$ is $N(\epsilon) = g \pi k^2(\epsilon)/(2\pi)^2$, with $g=2$ the multiplicity of the spin $1/2$:
$$N(\epsilon) = \frac{L^2}{\pi} \frac{m}{\hbar^2} \epsilon$$
and the density of state,
$$g(\epsilon) =  \frac{L^2}{\pi} \frac{m}{\hbar^2}$$
is constant.

The number of fermions is,
$$N = \int_0^\infty \D \epsilon \, \frac{g(\epsilon)}{\E^{(\epsilon - \mu)/T} + 1}\,.$$
The integral is elementary:
$$N = \frac{L^2}{\pi} \frac{m T}{\hbar^2} \ln \big(\E^{\mu/T} +1\big)\,,$$
from which we obtain the fermi level,
$$\epsilon_F = \mu(T=0) = \frac{\pi \hbar^2}{m} n,\; n = N/L^2\,.$$
It is determined by the gas density $n$. With this definition, the chemical potential writes,
$$\mu(T) = T \ln \big( \E^{\epsilon_F/T} - 1 \big)\,.$$
For $T \ll \epsilon_F$,
$$\mu \approx \epsilon_F - T \E^{-\epsilon_F/T}\,,$$
which is almost constant. At very high temperatures, the chemical potential is negative and tends to $-\infty$.


### 6

White dwarf. Compute, using relevant physical approximations, the gravitational equilibrium of a sphere of degenerate electrons in the non-relativistic case. Establish the mass-radius relation. Discuss the orders of magnitude and the validity of the approximations. Show that in the limit of ultra-relativistic electrons there is a mass limit for stability.

Non-relativistic

$$N_e = M/2m_p, \quad n = \frac{N_e}{V}, \; V = \frac{4\pi}{3}R^3$$

$$g(\epsilon)= \frac{\sqrt{2}}{\pi^2}\left( \frac{m}{\hbar^2}\right)^{3/2} V \sqrt{\epsilon}$$

$$\mu = \epsilon_F = (3\pi^2)^{2/3} \frac{m}{\hbar^2} n^{2/3}$$

$$E_e(R) = \int_0^{\epsilon_F} \D \epsilon \, g(\epsilon) \epsilon$$

$$E_G(R) = -G \rho^2 \int_0^R 4\pi r^2 \D r \, \left(\frac{4\pi}{3}R^3\right) \frac{1}{r}$$

$$R_\star = \frac{\alpha}{M^{1/3}},\quad \alpha = \frac{(9\pi^2)^{2/3}}{8G} \frac{\hbar^2}{mm_p^{5/3}}$$


Ultra-relativistic

$$g(\epsilon) \sim \epsilon^2$$

$$E_e = \frac{3^{5/3} \pi^{1/3}}{2^4} \left( \frac{M}{m_p} \right)^{4/3} \frac{\hbar c}{R}$$

$$E_e + E_G = 0$$

$$M_\star = \frac{3\pi^{1/2}}{2^6m_p^2} \left( \frac{5\hbar c}{G} \right)^{3/2} \approx 1.7 M_\odot$$



