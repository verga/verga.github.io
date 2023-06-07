Title: Applications: Boltzmann distribution
Slug: PS-A_boltz
Date: 2018-10-07
Category: Lectures
Tags: teaching, statistical physics
Authors: Alberto Verga
Summary: Solution of selected exercices, mainly about classical systems described by the boltzmann distribution.
status: hidden

$\newcommand{\I}{\mathrm{i}} 
\newcommand{\E}{\mathrm{e}} 
\newcommand{\D}{\mathop{}\!\mathrm{d}} 
\newcommand{\bra}[1]{\langle{#1}|}
\newcommand{\ket}[1]{|{#1}\rangle}
\newcommand{\braket}[1]{\langle{#1}\rangle}
\newcommand{\bbraket}[1]{\langle\!\langle{#1}\rangle\!\rangle}
\newcommand{\bm}{\boldsymbol}$

> [Lectures]({filename}PS-index.md) on statistical mechanics.

### 1 

A system, satisfying Boltzmann statistics, consists in $N$ two level atoms (with energies $E_1 < E_2$); the system is in contact with a reservoir at temperature $T$. If the emission of a quanta into the reservoir occurs, the level populations change $n_2 \rightarrow n_2 - 1$ and $n_1 \rightarrow n_1 + 1$. Assuming $n_1 \gg n_2$, calculate the entropy change for the two level system and the reservoir; eventually derive the Boltzmann relation for the ration $n_2/n_1$.

**1** Two levels population ratio. The boltzmann entropy is given by the logarithm of the number of microscopic configurations $\Omega$ compatible with the macroscopic state. For a two level subsystem,
$$\Omega_\text{i} = \frac{N!}{n_1!n_2!},\quad N = n_1 + n_2.\; E_\text{i} = E_1 n_1 + E_2 n_2$$
where $n_1$ is the number of particles in state $1$ of energy $E_1$ and $n_2$ in state with energy $E_2$. The initial state change by a transition from level $E_2$ to level $E_1$:
$$\Omega_\text{f} = \frac{N!}{(n_1+1)! (n_2-1)!}\,,\; E_\text{f} = E_\text{i} + E_1 - E_2$$
the variation of entropy of the system is then,
$$\Delta S_{\text{subsystem}} = \Delta S = \ln \frac{\Omega_\text{f}}{\Omega_\text{i}}= \ln \frac{n_2}{n_1+1}$$
Simultaneously, the entropy change in the state of the surrounding system due to a change in energy is:
$$-\Delta S_\text{reservoir} = \Delta S = \frac{E_1 - E_2}{T} = - \frac{\Delta E}{T}$$
where the minus sign ensures that the total entropy change is zero $\Delta S_\text{subsystem} + \Delta S_\text{reservoir} = 0$, for an insolated system, which leads to,
$$\frac{n_2}{n_1} \approx \E^{-\Delta E/ T}$$
the boltzmann distribution (we used $n_1 \gg n_2$).

### 2

Show that an ideal gas, in the diluted, high temperature limit $n \lambda^3 \ll 1$, the fermi distribution reduces to the boltzmann one ($n$ is the density, $\lambda^2=2\pi \hbar^2/mT$, with $m$ the atom's mass, and $T$ the temperature). Using the free particles density of states in a volume $V$, demonstrate that the ideal gas chemical potential $\mu$ is given by
$$\E^{\mu/T} = \frac{1}{2} n\lambda^3.$$

**2** We know that the population $n(\epsilon)$ of a level of energy $\epsilon$ of a fermi gas ($n_\epsilon \in [0,1]$) is given by,
$$n(\epsilon) = \frac{1}{\E^{(\epsilon-\mu)/T} + 1} \approx \E^{\mu/T} \E^{-\epsilon/T}$$
where the approximation is valid if $z=\E^{\mu/T} \ll 1$, or chemical potential negative and large with respect to the temperature). 

The relation between the density and the chemical potential is given by the relation:
$$N = \int_0^\infty \D \epsilon \nu(\epsilon) n(\epsilon)\,,$$
where $\nu(\epsilon)$ is the density of states, and $n(\epsilon)$ is the (number) density of particles as a function of the energy.

This result can be justified by computing the density of states of an ideal gas:
$$\nu(\epsilon)\D \epsilon = g_s V 4\pi k^2 \frac{\D k}{(2\pi)^3} = \frac{V}{\pi^2} k^2 \D k\,, \quad \epsilon = \frac{\hbar^2 k^2}{2 m}$$
where $g_s = 2$ is the spin degeneracy ($g_s =2s+1$, $s=1/2$, for electrons), and,
$$\D k = \frac{m}{\hbar^2} \sqrt{\frac{\hbar^2}{2m \epsilon}} \D \epsilon\,.$$
Putting these results together,
$$\nu(\epsilon) = \frac{\sqrt{2}V}{\pi^2} \left(\frac{m}{\hbar^2}\right)^{3/2}\sqrt{\epsilon}\,.$$ 
Therefore, the total number of particles is the integral over the energies of the density of states weighted by the boltzmann distribution (this is our assumption):
\begin{align*}N & = 2\E^{\mu/T} V \int_{\mathbb{R}^3} \frac{\D \boldsymbol k}{(2\pi)^3} \E^{-\hbar^2 k^2/2 m T} \\ 
&= \E^{\mu/T} \int_0^\infty \D \epsilon\, \nu(\epsilon) \, \E^{-\epsilon/T} \\ 
& = \frac{\sqrt{2}V}{\pi^2} \left(\frac{m}{\hbar^2}\right)^{3/2} \int_0^\infty \D \epsilon \, \sqrt{\epsilon} \E^{-\epsilon/T} \E^{\mu/T} \\
& = \frac{2V}{\lambda^3} \E^{\mu/T}\end{align*}
which leads to the expression,
$$\mu = T \ln \left(\frac{n\lambda^3}{2}\right)\,,\quad \lambda = \left(\frac{2\pi\hbar^2}{mT}\right)^{1/2}\,.$$
In conclusion, the approximation is justified if the fermi gas is extremely diluted and hot:
$$n\lambda^3 \ll 1\,.$$

* Note that the one particle energy is $\epsilon(k) = (\hbar k)^2/2m$, where the wavenumber
$$\bm k = \big( \frac{2\pi n_x}{L_x}, \frac{2\pi n_y}{L_y},\frac{2\pi n_z}{L_z} \big)\,,$$
is quantified such that $n_x,n_y,n_z$ are integers and $V=L_xL_yL_z$ is the volume. Therefore, the number of modes inside a small "volume" in $\bm k$ space is,
$$\Delta n_x \Delta n_y \Delta n_z = V\frac{\Delta k_x \Delta k_y \Delta k_z}{(2\pi)^3}\,.$$
Now, using the fact that for a given energy $\epsilon$ the possible wavenumvers are inside a sphere of radius proportional to $\sqrt{\epsilon}$, we obtain the total number of states inside this sphere:
$$N(\epsilon) = \frac{V}{(2\pi)^3} \frac{4\pi}{3} k^3, \quad k = \frac{1}{\hbar}\sqrt{2m\epsilon}.$$
The density of states is simply $\nu(\epsilon) = \D N(\epsilon)/\D \epsilon$:
$$\sum_{\bm n} \ldots \rightarrow V \int_{-\infty}^\infty \frac{\D \bm k}{(2\pi)^3} \ldots = \int_0^\infty \D\epsilon \, \nu(\epsilon) \ldots$$
If the energy states are degenerated, we multiply this result by the degeneracy $g_s$.

### 3

Disordered material. An alloy contains a small fraction of impurities that can be in two energy states $\Delta_x > 0$ or $-\Delta_x$, according to their position $x$ in the crystal lattice. We assume that the impurities are independent. We are interested in the low temperature limit $T \ll \Delta$.

* In the case that each impurity atom has the same levels $\pm\Delta$ (independent of position), calculate their contribution to the heat capacity (neglect all other possible contributions).
* In the inhomogeneous case, write the total heat capacity summing up the individual contributions. Assuming now that the distribution of energy levels is exponential,
$$\rho(\Delta) = \frac{\E^{-\Delta/\Delta_0}}{\Delta_0}\,,$$
replace the sum by an integral, and investigate the low temperature behavior of the heat capacity. Compare with the homogeneous case.

**3** Taking first $\Delta>0$ fixed, we compute the specific heat for a two level system:
$$E = -N \tanh \frac{\Delta}{T}$$
and,
$$c_V = \left(\frac{\Delta}{T}\right)^2 \cosh^{-2}\frac{\Delta}{T}$$
or at low temperature,
$$c_V \approx \left(\frac{\Delta}{T}\right)^2 \E^{-2\Delta/T}$$
In the presence of disorder, the mean specific heat is given by,
$$\braket{c_V} = \int_0^\infty \D \Delta\,p(\Delta) c_V(\Delta)$$
The interesting results is that, for low temperature, we find
$$\braket{c_V} \sim T$$
instead of the exponential behavior of the ordered case.

### 6

A high temperature hydrogen plasma contains a fraction ($T < m_\mathrm{e}c^2$) of positrons created through electron collisions $\mathrm{e}^{-} + \mathrm{e}^{-} \rightarrow 2\mathrm{e}^{-} + (\mathrm{e}^{+} + \mathrm{e}^{-})$, or proton-electron collisions $\mathrm{e}^{-} + \mathrm{p} \rightarrow \mathrm{e}^{-} + \mathrm{p} + ( \mathrm{e}^{+} + \mathrm{e}^{-})$ (note that the total charge is conserved). The proton density is $n_\mathrm{p} = 1\,10^{16}\,\mathrm{m^{-3}}$. Find the chemical potential for $\mathrm{e}^{-}$ and $\mathrm{e}^{+}$ and estimate the temperature at which the positron density is $n_+ = 1\,10^{6}\,\mathrm{m^{-3}} \ll n_\mathrm{p}$ and $n_+ = 1\,10^{16}\,\mathrm{m^{-3}} \approx n_\mathrm{p}$. Assume the plasma non relativistic and non degenerated.

**6** The equilibrium condition is given by $\mu_- = - \mu_+ = \mu$, the chemical potential of the positrons $\mu_+$, is negative and has the opposite value of the electron chemical potential $\mu_-$:
$$\frac{n_+}{n_-} = \E^{-2\mu/T}\,.$$
This is due to the fact that the *difference* $N_+ - N_+$ of the number of electrons and positrons is conserved (particles are created by pairs).

### 7

An ideal gas of polar polar molecules is placed in a uniform electric field $\mathcal{E}$. The dipolar moment of each molecule is $p$, whose energy is $-p\mathcal{E} \cos \theta$, where $\theta$ is the angle between the applied field and the dipole. Compute the classical partition function $Z$ in the canonical ensemble, the mean polarization and the dipolar susceptibility $\chi = \D \braket{p}/ \D \mathcal{E}$, and the specific heat at constant volume. Find the high temperature asymptotics, where the classical approximation is valid.

**7** The $N$ particles partition function is simply the product of one-particle partition functions because the dipoles are free:
$$Z = Z_1^N\,,\quad Z_1 = \int_\Omega \D \Omega \E^{\epsilon \cos \theta/T}$$
where $\epsilon = p \mathcal{E}$ is the typical energy of one dipole. We are interested in the electrical properties of the system, therefore we neglect the kinetic part of the partition function. The integral is readily calculated,
$$Z_1 = 2\pi\int_{-1}^1 \D(\cos\theta) \E^{\epsilon \cos\theta/T} = \frac{4\pi T}{\epsilon} \sinh \frac{\epsilon}{T}$$
The free energy is then,
$$F = - NT \ln \left(\frac{4\pi T}{\epsilon} \sinh \frac{\epsilon}{T}\right)$$
the energy $E= -T\partial F/\partial T + F$, is
$$E = NT - N\epsilon \coth \frac{\epsilon}{T} = - N \braket{p\cos\theta} \mathcal{E}$$
The mean dipole moment is,
$$\braket{p\cos\theta} = -\frac{T}{\mathcal{E}} + p \coth\left( \frac{p \mathcal{E}}{T}\right)$$
from which we derive the dielectric susceptibility:
$$\chi = \frac{T}{\mathcal{E}^2} - \frac{p^2}{T} \sinh^{-2}\frac{p \mathcal{E}}{T}$$
At weak applied field $p\mathcal{E} \ll T$, we obtain,
$$\chi \approx \frac{p^2}{3T}$$
in accordance with the Curie law.

### 8

Surfactant gas. A surfactant is diluted in an aqueous solution; the molecules binding energy in volume is $\epsilon$ and on the surface is $\epsilon_s$, the difference $\Delta \epsilon = \epsilon - \epsilon_s >0$. Suppose the surfactant molecules as an ideal gas of dimension $D$ and compute the partition function $Z(T,\mu_D,V_D)$ in the grand canonical ensemble; calculate the number $N_3$ of molecules in the volume $V_3 =V$ and $N_2$ of molecules on the surface $V_2 = A$. Find the ratio $N_2/N_3$ and discuss your result.

**8** We note $D=2,3$ the spatial dimension, $\epsilon_2 = \epsilon_S$ and $\epsilon_3 = \epsilon$ are the surfactant surface and bulk energies. The fact that the particles are non interacting allows the grand partition function to be written in the power series form,
$$Z(T,\mu_D,V_D) = \sum_{N_D=0}^\infty \E^{\mu_D N_D} \E^{-N_D\epsilon_D} \frac{Z_D^{N_D}}{N_D!}$$
where,
$$Z_D= \frac{V_D}{(2\pi\hbar)^3} \int_{V_D} \D^D p\, \E^{-p^2/2mT}=\frac{V_D}{\lambda^D}$$
is the kinetic energy part of the partition function, identical to the ideal gas expression. Therefore,
$$Z(T,\mu_D, V_D) = \exp\left( \E^{-(\epsilon_D-\mu_D)/T} \frac{V_D}{\lambda^D}\right)\,,$$
or, in terms of the thermodynamical potential,
$$\Phi(T,\mu_D,V_D) = - T \E^{-(\epsilon_D-\mu_D)/T} \frac{V_D}{\lambda^D}\,.$$
The particle numbers $N_D$ are readily obtained using the formula $N_D = -\partial \Phi/\partial \mu_D$:
$$N_D = \frac{V_D}{\lambda^D} \E^{-\epsilon_D/T} \E^{\mu_D/T} \,.$$
And, inverting this last equation, we obtain the chemical potentials as a function of the concentrations:
$$\mu_D = \epsilon_D + T \ln (n_D \lambda^D)\,.$$
In particular, the ratio $N_2/N_3$ of the surface with respect to the bulk surfactant particles, is
$$\frac{N_S}{N} = \frac{V_2\lambda}{V_3} \E^{(\epsilon - \epsilon_S)/T}$$
at equilibrium, $\mu_2 = \mu_3$. Finally, the surface density $n_S = N_2/V_2$ is given by,
$$n_S = n \lambda \E^{(\epsilon - \epsilon_S)/T}\,.$$ 
It is interesting to note that the final formula includes the microscopic parameter $\lambda$, which gives the relevant length scale to compare the bulk and the surface densities. The nondimensional ratio $n_S/n\lambda \gg 1$, is exponentially large ($\epsilon > \epsilon_S$).
