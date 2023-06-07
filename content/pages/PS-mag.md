Title: Magnetism of the fermi gas
Slug: PS-mag
Date: 2018-08-08
Category: Lectures
Tags: teaching, statistical physics
Authors: Alberto Verga
Summary: Paramagnetism and diamagnetism of free fermions
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

A magnetic field not only interacts with the orbital motion of charged particles through their angular momentum $\boldsymbol L$, but also interacts with the particle's spin $\boldsymbol S$, even if their charge is zero. The origin of these interactions is quantic and relativistic (Dirac, 1928). 

Let us consider, to be specific, a free electron in the limit of small velocities with respect to the light speed: its hamiltonian in the presence of a magnetic field $\boldsymbol B$, is,
$$\mathcal{H} = \frac{(\boldsymbol p + e \boldsymbol A)^2}{2m} + \frac{1}{2}g \mu_\mathrm{B} \boldsymbol \sigma \cdot \boldsymbol B$$
where $m=9.1093\,8356\times 10^{-31}\,\mathrm{kg}$ is the electron mass, $e=1.6021\,7662\times 10^{-19}\,\mathrm{C}$ is the elementary charge, $\boldsymbol A$ the vector potential,
$$\boldsymbol B = \nabla \wedge \boldsymbol A\,,\quad 
\boldsymbol A(\boldsymbol x) = \frac{1}{2} \boldsymbol B \wedge \boldsymbol x\,,$$
where the second equation holds for a constant magnetic field, $\mu_\mathrm{B} = e\hbar/2m = 0.9274\,764\times 10^{-23} \,\mathrm{J\,T^{-1}}$ is the Bohr magneton, $g=2.0023\,1930\,43618$ the g-factor, and $\boldsymbol \sigma$ is the vector of pauli matrices:
$$\sigma_x = \begin{pmatrix}0 & 1 \\ 1 & 0 \end{pmatrix}\,, \quad
\sigma_y = \begin{pmatrix}0 & -\I \\ \I & 0 \end{pmatrix}\,, \quad
\sigma_z = \begin{pmatrix}1 & 0 \\ 0 & -1 \end{pmatrix}\,.$$
$\mathcal{H}$ is the Pauli hamiltonian (corrected with the g-factor $g\ne2$). Generalization of $\mathcal{H}$ to many electrons in a potential is straightforward (to model for example, atom magnetism). The Pauli work demonstrated that elementary particles possess an intrinsic magnetic momentum related to their spin $\boldsymbol S$:
$$\boldsymbol \mu = - g\mu_\mathrm{B} \frac{\boldsymbol S}{\hbar},$$
explaining the Stern-Gerlach experiment (1922). Note that the spin and momentum are in opposite directions. For an electron, the spin operator is,
$$\boldsymbol S = \frac{\hbar}{2} \boldsymbol \sigma\,,$$
whose eigenvalues are the two spins $\pm\hbar/2$, up and down.

In classical mechanics the second term of the hamiltonian containing the spin would be absent; moreover, the potential vector and the momentum are simple real variables. When integrating over the phase space to calculate the classical partition function, the vector potential appears as an irrelevant shift of the momentum, disappearing in the computation of the thermodynamic properties; this result, the Bohr-van Leeuwen theorem, demonstrate that in classical mechanics magnetic system are impossible: the thermal average of the magnetization always vanishes. Magnetism is therefore an entire quantum effect. The non commutativity of position and momentum in quantum mechanics invalidates the theorem hypothesis, open the possibility of a magnetic effect due to the orbital motion: the Landau *diamagnetism* (1930). The spin term is responsible for the splitting of the degenerated energy levels according to their quantum magnetic number, the Zeeman splitting, which leads to a paramagnetic response first described by Pauli (1927). In summary, the orbital term, modifying the electron momentum, gives rise to diamagnetism, and the spin term leads to *paramagnetism*.

The contribution of each effect to the energy spectrum can be considered separately. The first term in $H$, associated with the orbital motion, is related to the harmonic oscillator, because it is quadratic in momentum and position, leads to a spectrum containing a continuous part related to the kinetic energy, and a discrete part 
$$\epsilon(p_z,n) = \frac{p_z^2}{2m} + \hbar \omega_B \left(n + \frac{1}{2} \right)\,,\quad n = 0,1,\ldots$$
where we assumed the magnetic field in the $z$ direction, $\omega_B$ is the cyclotron frequency; the energy states labeled by $n$, are called *Landau levels*, and are highly degenerate. The second term, related to the particle's spin, corresponds to a two bands system (the momentum term has, as in the previous case, a continuous spectrum), one band is associated to the spin up polarization $1/2$, and the other band to the spin down polarization $-1/2$. 

It is convenient to introduce units such that $\hbar = m = e = 1$; in these units $g\mu_{\mathrm{B}} = 1$ (with $g=2$), and the dimensions of mass, length and time are,
$$ m =1, \quad L = \sqrt{\frac{\hbar}{eB}} = \frac{1}{\sqrt{B}}, \quad T = \frac{m}{eB} = \frac{1}{B}\,.$$
The unit of magnetization is $[M] = g\mu_\mathrm{B}/V = 1/V$, proportional to the magnetic moment of the electron per unit volume, and the energy unit is $g\mu_\mathrm{B} B =\omega_B \hbar$, with $\omega_B = eB/m$ the cyclotron frequency. The advantage of this unit system is that all the physical quantities are expressed in terms of the magnetic field, the experimental control parameter.

Now we investigate the thermodynamic behavior of a gas of electrons whose orbital motion and spin are coupled to an external constant magnetic field.


## Pauli paramagnetism

Under the action of an external magnetic field different materials, insulators or metals, develop a macroscopic magnetization. If the magnetization is in the direction of the applied field, the material is said to be paramagnetic; if it is in the opposite direction to the applied field, the response is then diamagnetic. The quantity that describes the material response is the ratio between the generated magnetization and the applied field $H$:
$$\chi = \frac{M}{H}\,,\quad (H \rightarrow 0)$$
the magnetic *susceptibility*, which is nondimensional in SI ($\mu_0 = 4\pi \times 10^{-7}\, \mathrm{T\,m/A}$). Insulators may have a large paramagnetic susceptibility, in contrast to metals whose paramagnetic response is weaker. The weak paramagnetic effect of metals is related to the fermi statistics obeyed by the electrons, as demonstrated by Pauli: only the electrons possessing energies near the fermi energy $\epsilon_F$ may contribute to the paramagnetic susceptibility. In normal conditions the fermi energy, which is of the order of $10^4\,K$, is much larger than the thermodynamic temperature, making the electrons a degenerate quantum gas.

A simple estimation of the paramagnetic pauli susceptibility, is obtained in the limit $T=0$; in absence of magnetic field, the density of states has a cut at the fermi level $\epsilon_F$:
$$\epsilon_F = (3\pi^2)^{2/3} \frac{\hbar^2 n^{2/3}}{2m}\,.$$
The magnetic field introduces a splitting of $2\mu_0\mu_\mathrm{B} H$ (where $-g \mu_\mathrm{B}/2 \approx -\mu_\mathrm{B}$ is the electron magnetic moment, opposite to the spin direction). The number of electrons in the up-spin band is $N_+ =  N_0 - \frac{1}{2}\nu(\epsilon_F)\mu_0\mu_\mathrm{B} H$, and in the down-spin band, $N_- =  N_0 + \frac{1}{2} \nu(\epsilon_F)\mu_0\mu_\mathrm{B} H$ (note that $\nu(\epsilon)/2$ is the band density of states), where we accounted for the fact that the band with the magnetic moment aligned with the magnetic field is more populated. Therefore, we find that the magnetization is proportional to the magnetic field,
$$M= -\frac{\mu_\mathrm{B}}{V}(N_+ - N_-) = \chi H, \quad \chi = \frac{\mu_0
\mu_\mathrm{B}^2}{V} \nu(\epsilon_F)$$
and the proportionality coefficient is the pauli susceptibility.

> <img src="{static}/images/PS-mag-para.svg" height="250">
>
> Schema of the density of states showing the splitting between up and down spins induced by the applied magnetic field $H$. Energy states are occupied up to the fermi energy $\epsilon_F$.

In the general case, for arbitrary temperature, it is appropriated to work in the grand canonical ensemble. To describe fermions with spin, we use the creation $c^\dagger_{\boldsymbol p, s}$ and annihilation $c_{\boldsymbol p, s}$ operators of a particle with momentum $\boldsymbol p$ and spin $\hbar/2$, $s=1$ (spin up), or spin $-\hbar/2$, $s=-1$ (spin down). The electron hamiltonian becomes,
$$\mathcal{H} = \sum_{\boldsymbol p,s} \epsilon_{\boldsymbol p,s} c_{\boldsymbol p,s}^\dagger c_{\boldsymbol p,s}\,,\quad \epsilon_{\boldsymbol p,s} = \frac{p^2}{2m} + \frac{s}{2}g\mu_\mathrm{B} B\,.$$
The grand partition function, in this context a function of the magnetic field, is,
$$Z_F(T, \mu, V, B)= \mathrm{Tr}\,\prod_{\boldsymbol p, s} \exp\left(-\frac{\epsilon_{\boldsymbol p, s} - \mu}{T} c^\dagger_{\boldsymbol p, s} c_{\boldsymbol p, s}\right)\,, $$
which, after exchanging the trace and the product, and using the fermion occupation numbers, becomes
$$Z_F(T, \mu, V, B) = \prod_{\boldsymbol p}\left[1+ \E^{-(p^2/2 + B/2 - \mu)/T}\right] \left[1+ \E^{-(p^2/2 - B/2 - \mu)/T}\right]\,.$$
in convenient units (note that $H=B/\mu_0$). As a result, the grand potential splits into two contributions differing in their effective chemical potential $\mu + s B/2$ (noting only the dependence on $\mu$ and $B$, which are here the relevant thermodynamic variables, $T$ and $V$ can be considered as fixed parameters),
$$\Phi(\mu, B) = \Phi_0(\mu - B/2) + \Phi_0(\mu + B/2)$$
where $\Phi_0(\mu) = \Phi(\mu, B=0)/2$ is the grand potential of free electrons (with $B=0$), up to a factor $1/2$ necessary to avoid counting twice each state (corresponding to the degeneracy factor $g_s=2$, included in the definition of $\Phi$),
$$\Phi_0(\mu) = - T \sum_{\boldsymbol p} \ln \left( 1 + \E^{-(p^2/2 - \mu)/T} \right)\,.$$
The corresponding density of states is hence,
$$\nu_0(\epsilon) = \frac{\nu(\epsilon)}{2} = \frac{1}{2} \frac{3N}{2} \frac{\epsilon^{1/2}}{\epsilon_F^{3/2}}\,.$$

Note that we can obtain, using the results already computed for free fermions, the exact value of $\Phi_0$,
$$\Phi_0(\mu, \pm B) = \frac{VT}{\lambda^3} \mathrm{Li}_{5/2}(-z\E^{\pm B/2T})\,,\quad
z = \E^{\mu/T}\,,$$
however, to obtain the susceptibility, which corresponds to the response of the fermion gas to a *small* magnetic field ($B\rightarrow0$), it is more suitable to expand $\Phi(B)$ in powers of the magnetic field.

We start by calculating the number of particles as a function of the effective chemical potential. The derivative with respect to the chemical potential $-\partial \Phi(\mu, B)=N$, gives the desired number of particles,
$$N = N_+ + N_-\,, N_\pm = \int_0^\infty \D \epsilon\, \frac{\nu(\epsilon)}{2} n_\epsilon(\mu \mp B/2)\,,$$
where, as in the elementary derivation, we introduced the spin dependent populations $N_\pm$. The magnetization is (in units of $[g\mu_B]$),
$$M = -\frac{N_+ - N_-}{2V} = -\frac{1}{2V}\int_0^\infty \D \epsilon\,\frac{\nu(\epsilon)}{2} [n_\epsilon(\mu - B/2) - n_\epsilon(\mu + B/2)]\,,$$
where the factor $1/2$ comes from the magnetic moment of the electron ($g\mu_\mathrm{B}/2 = 1/2$). Expanding in powers of $B$,
$$M \approx \frac{1}{4V} \int_0^\infty \D \epsilon\,\nu(\epsilon) \frac{\partial n_\epsilon}{\partial \mu} B = \frac{1}{4V} \frac{\partial N(\mu)}{\partial \mu} B\,.$$
At low temperatures, the usual case for a metal, $T \ll \epsilon_F$, the derivative of the fermi distribution is picked around $\epsilon = \epsilon_F$:
$$\frac{\partial n_\epsilon}{\partial \mu} = - \frac{\partial n_\epsilon}{\partial \epsilon} \approx \delta(\epsilon_F-\epsilon)\,.$$
thus, putting the original units, 
$$M = \chi H\,, \quad \chi = \mu_0(g\mu_\mathrm{B})^2 \frac{\nu(\epsilon_F)}{4V} = \frac{\mu_0}{4V} (g\mu_\mathrm{B})^2 \frac{3N}{2\epsilon_F}\,.$$
or ($g^2\approx4$),
$$\chi = \frac{3\mu_0\mu_B^2}{2} \frac{n}{\epsilon_F} \sim n^{1/3}\,.$$

We can also use the small magnetic field expansion to compute the susceptibility in the high temperature regime, suitable to describe independent (classical) magnetic moments:
$$n_\epsilon \sim \E^{-(\epsilon - \mu)/T}, \quad \frac{\partial n_\epsilon}{\partial \mu} = \frac{n_\epsilon}{T}$$
which immediately gives,
$$\chi = \mu_0 \mu_\mathrm{B}^2 \frac{n}{T}$$
which is the *Curie susceptibility* of a classical paramagnet. Note that one recovers  the Curie susceptibility, up to a numerical factor, from the pauli susceptibility formula, by the substitution of the fermi level by the temperature. This shows that the existence of an extra *energy scale* in the quantum regime, build from the planck constant and the mean distance between electrons,
$$\epsilon_F \sim \frac{\hbar^2}{m n^{-2/3}}$$
deeply modify the low energy $T \ll \epsilon_F$ physical properties of the gas.


## Landau diamagnetism

To investigate the effect of the orbital motion of the electron we will ignore its spin, already taken into account in the computation of the paramagnetic susceptibility. The motion of a classical particle in a magnetic field is characterized by the cyclotron frequency $\omega_B$ and the Larmor radius $R$:
$$\omega_B = \frac{eB}{m}, \quad R^2 = \frac{2\epsilon}{m \omega_B^2} \,,$$
where $\epsilon$ is the particle's energy. The quantification of the energy, the Landau levels $n = 0, 1,\ldots$, has a radical consequence: the area enclosed by the cyclotron motion $2\pi R^2$ is quantified. Therefore, the number of electrons in a Landau level, that can be accommodated in a plane perpendicular to the direction of the magnetic field, is constrained by its surface. As a consequence, the electron gas possesses a kind of rigidity or incompressibility, which strongly affects its thermodynamic (and transport) properties.

The hamiltonian reads,
$$\mathcal{H} = \sum_{p_z,n} \left[ \frac{p_z^2}{2m} + \hbar \omega_B \left(n + \frac{1}{2}\right) \right] c^\dagger_{p_z, n} c_{p_z, n}$$
where the $c^\dagger_{p_z,n}$ creates a particle of momentum $p_z$ at the energy level $n$. The degeneracy of a Landau level $n$ is given by the number of magnetic flux quanta $h/2e=2\pi\hbar / 2 e = 2.0678\,3383\times 10^{-15}\, \mathrm{T\, m^2}$ in $L^2B$,
$$g_B = 2 \times \frac{L^2 eB}{2\pi\hbar}\,,$$
(the factor $2$ is *here* the spin degeneracy; in fact, included in the original definition of the flux quantum as the charge of a superconducting electron pair), which gives the number of states in the interval $[p_z,p_z+\D p_z]$,
$$g_B \frac{L \D p_z}{2\pi \hbar} =2V \frac{eB}{(2\pi\hbar)^2} \D p_z \,.$$

The grand potential, in the units defined above, is:
$$\Phi = -T \frac{VB}{2\pi^2} \sum_{n = 0}^\infty \int_{-\infty}^\infty \D p_z\,\ln\big[1 + \E^{-[p_z/2+ B(n + 1/2) - \mu]/T}\big]$$
which is a function of the thermodynamic variables $\Phi = \Phi(T, \mu, V, B)$. We may use the [Euler-MacLaurin](https://en.wikipedia.org/wiki/Euler–Maclaurin_formula) formula,
$$\sum_{n=a}^b f(n) = \int_a^b \D x \, f(x) + \frac{1}{2} [f(a) + f(b)] - \frac{1}{12}[f'(a) - f'(b)] + \ldots$$
to compute $\Phi$ at low temperatures. Taking $a=0$, $b=\infty$ and shifting $n \rightarrow n + 1/2$, the formula becomes,
$$\sum_{n=0}^\infty f(n+1/2) = \int_0^\infty \D x \, f(x) + \frac{1}{24} f'(0)\,,$$
where we used the interpolation, valid for small fields $B \ll T$, $f(x) \approx f(0) + x f'(0)$ in the interval $-1/2 \le x \le 0$. It is easy to see that the first term do not depend on the magnetic field <strong style="color:DarkSlateBlue; background-color:LightGray;">EX</strong>, then only the second term do contribute to the susceptibility. The corresponding term of the grand potential, we denote $\phi$, is
$$\phi(B) = \frac{VB^2}{2\pi^2} \frac{1}{24} \int_{-\infty}^\infty \D p_z \frac{1}{\E^{(p_z^2/2 - \mu)/T} + 1}\,$$
or changing the variable,
$$\phi(B) = \frac{VB^2}{2\pi^2} \frac{1}{24} \sqrt{2T} \int_{0}^\infty \D x \frac{x^{-1/2}}{\E^{-\mu/T}\E^x + 1}\,,$$
which is given in terms of the polylogarithm function $\mathrm{Li}_{1/2}$:
$$\phi(B) = - \frac{VB^2}{\pi^2} \frac{1}{24} \frac{\sqrt{\pi T}}{\sqrt{2}} \mathrm{Li}_{1/2}(-\E^{\mu/T}) \approx \frac{V}{24} \frac{\sqrt{2}}{\pi^2} \epsilon_F^{1/2} B^2\,.$$
where we replaced in the last expression, the low temperature asymptotics of $-\mathrm{Li}_{1/2}(-z) \approx (\ln z)^{1/2}/\Gamma(3/2)$ and the chemical potential by the fermi energy $\mu \approx \epsilon_F$. The susceptibility is derived from the derivative with respect to the field of the grand potential (in the original units),
$$\chi = -\frac{\mu_0}{VB} \frac{\partial \phi(B)}{\partial B} = -\frac{\mu_0 (g\mu_\mathrm{B})^2}{12\pi^2}  \frac{m}{\hbar^2}\left(\frac{2m\epsilon_F}{\hbar^2}\right)^{1/2} \,.$$
After a little transformation, using $(2m\epsilon_F/\hbar^2)^{3/2}/3\pi^2 = N/V$, it leads to the final formula,
$$\chi = -\frac{\mu_0}{12}(g\mu_\mathrm{B})^2 \frac{3n}{2\epsilon_F}\,.$$
Remarkably, the diamagnetic susceptibility is one third of the pauli paramagnetic susceptibility, and of course, of opposite sign:
$$\chi_{\text{dia}} = -\frac{1}{3} \chi_{\text{para}}\,,$$
which means that the effective susceptibility of the free fermion degenerate gas is given by (in the original units):
$$\chi_F = \chi_{\text{para}} + \chi_{\text{dia}} = \mu_0\mu_B^2 \frac{n}{\epsilon_F}\,.$$

