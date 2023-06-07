Title: Exams (November 2022)
Slug: PS-exams_1
Date: 2022-11-08
Category: Lectures
Tags: teaching, statistical physics
Authors: Alberto Verga
Summary: Solutions to the 2022 midterm exam problems
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

# Midterm November 2022


## Bosons

### 1.
Black Body. Use dimensional analysis to find the energy density of a gas of photons at temperature $T$ (Stefan law). Apply the experimental fact that $E/V$ only depends on $T$ ($E$ and $V$ are the thermodynamic energy and volume of the black body).

### Solution
We must determine the function
$$\epsilon = E/V = \epsilon(T)$$
for a noninteracting photon gas. A photon is a quantum ($\hbar$ planck constant) of the electromagnetic field ($c$ light speed); therefore we assume that 
$$\epsilon=\epsilon(T)=f(T; \hbar, c).$$
The dimensions are:
$$[\epsilon]=EL^{-3}, \; [\hbar c]=E L, \; [k_BT]= E$$
where $E$ and $L$ are dimensions of energy and length, respectively. Noting that to make a volume we need a factor $(\hbar c)^3$, and compensating for the extra powers of $E$, we obtain that
$$\epsilon=\text{const.} \frac{(k_BT)^4}{(\hbar c)^3}$$
has the correct dimensions ($\text{const.}$ is a number). This is the Stefan law.

### 2.
Debye phonons. Use dimensional analysis to find the maximum energy $\epsilon_M$ a phonon can take in a solid of $N$ atoms and volume $V$; the sound velocity $c_s$ is isotropic. (Hint: assume that the energy is a function of the density $n=N/V$.) Compute $\epsilon_M$ using the exact density of states. Compare the two results.

### Solution

A phonon is the quantum of cristal lattice excitations of energy $\epsilon = \hbar \omega$: its frequency $\omega$ is related to its wavenumber $k$ by the sound velocity $c_s$, $\omega=c_s k$. The Debye cutoff frequency is a function of the density:
$$\omega_M=\epsilon_M/\hbar=\omega_M(n)=f(n; c_s).$$
To determine $f$ we analyze the parameter dimensions: 
$$[\omega_M]=T^{-1}, \; [c_s] = LT^{-1}, \; [n] = L^{-3}.$$
From these relations we find that 
$$\omega_M = \text{const.} c_s n^{1/3},$$
because $n^{-1/3}$ has dimension of length.

To compute the unknown constant, we use the definition of the cutoff frequency:
$$\text{number of modes} = \text{number of dof} = 3N$$
which states that the number of phonons must not exceed the number of degrees of freedom (dof) $3N$ (for $N$ lattice sites). Therefore,
$$3 V \frac{4\pi}{3} \left( \frac{\omega_M}{2\pi c} \right)^3 = 3N,$$
where the first term is $3$ times (for the longitudinal and transversal phonon polarizations) the volume of a sphere of radius $\omega/2\pi c_s$. We finally obtain,
$$\omega_M = (6\pi^2 n)^{1/3} c_s\,.$$

## Rigid rotator

We consider a material formed in first approximation, by independent rotators of inertia moment $I$. We are interested in the low temperature limit and assume a Boltzmann distribution.

1. Write the hamiltonian of the set of \emph{fixed} rotators.

2. Use dimensional analysis to determine the low temperature condition. (Hint: compare the temperature with a characteristic energy of a rotator.)

3. Write the exact expression of the one particle partition function and compute its low temperature expansion. (Remark: take into account the degeneracy of the angular momentum.)

4. Find the specific heat at low temperature.

5. Plot the specific heat as a function of the temperature. Discuss the result (compare with the classical expectation.) 

### Solution

The hamiltonian of a rigid rotator of inertia moment $I$ and angular momentum $L$ is
$$H = \frac{L^2}{2I}\,.$$
The eigenspectum is given by the spherical harmonics $\ket{lm}$ of orbital number $l=0,1,\ldots$ and magnetic number $-l\le m \le l$:
$$H\ket{lm} = \frac{\hbar^2}{2I} l(l+1) \ket{lm}.$$
The energy levels are then given by
$$\epsilon_l = \frac{\hbar^2}{2I} l(l+1).$$
This leads to a characteristic energy of the rotator $\hbar^2/I$, which combined with the temperature defines the nondiemnsional parameter:
$$\theta = \frac{\hbar^2}{Ik_BT}\; ;$$
the low temperature regime corresponds to $\theta\gg 1$.

The one particle partition function $Z_1 = \sum_s \exp(-\epsilon_s/T)$ ($k_B=1$ from now on), where the quantum state here is determined by $s=\{l,m\}$, writes
$$Z_1 = \sum_{l=0}^\infty \sum_{m=-l}^l \E^{-\theta l(l+1)/2}= \sum_{l=0}^\infty (2l+1) \E^{-\hbar^2 l(l+1)/2IT} \,,$$
where we took into account the degeneracy of $\epsilon_l$ (just the sum over $m$). At low temperature each term of the sum is exponentially small (for $l>0$), therfore up the first relevant term we have
$$Z_1 = 1 + 3\E^{-\theta},$$
and, to the same order,
$$F=-3 T \E^{-\hbar^2/IT},$$
for the free energy.

The thermodynamic energy is
$$\frac{E}{N} = \frac{\partial (F/T)}{\partial (1/T)} = \frac{3\hbar^2}{I} \E^{-\hbar^2/IT},$$
and the specific heat per particle,
$$c_v = \frac{\partial E}{N \partial T} = 3 \left( \frac{\hbar^2}{IT} \right)^2 \E^{-\hbar^2/IT}.$$

To plot $c_v(T)$ we note that it tends to zero when $T \rightarrow 0$ and that, for high temperatures, it must match the classical result $c_v = 1$, in units of the boltzmann constant; the change between the two regimes occurs about $\theta=1$.

> <img src="{static}/images/PS-exam_cv.svg" alt="cv" style="width:300px;"/>

## van der Waals

Find the van der Waals equation of state of parameters $a$ and $b$
\begin{equation}
\label{e:vdW}
\left( P + N^2a/V^2 \right)(V - Nb) = Nk_B T
\end{equation}
where $P$ is the pressure, $V$ the volume, $N$ the number of atoms and $T$ the temperature ($k_B$ is the Boltzmann constant), corresponding to the interaction energy
\begin{equation}
\label{e:wr}
w(r) = \begin{cases} \infty & r < r_0\\ -\epsilon & r_0<r<r_1 \\ 0 & r>r_1 \end{cases}\,.
\end{equation}
Here $r_0,r_1$ have the dimension of a length and $\epsilon > 0$ is an energy.

1. Plot $w$ and explain the significance of the dimensional parameters appearing in its definition.

2. Compute the second virial coefficient:
\begin{equation}
\label{e:B}
B(T) = 2\pi \int_0^\infty r^2 \D r \left[ 1 - \E^{-w(r)/T} \right]\,. 
\end{equation}

3.Show that one can write 
\begin{equation}
\label{e:ab}
B(T) = v_0 - \frac{a(T)}{T}, \quad v_0 = \frac{2\pi r_0^3}{3}\,,
\end{equation}
and demonstrate that $a(T)$ is independent of the temperature at high $T$.

4. Show how to obtain the excluded volume term and compute the van der Waals parameters $a$ and $b$.

### Solution

We use $k_B=1$. The interaction energy is piecewise constant, repulsive for $r<r_0$, attractive for $r \in (r_0,r_1)$ with a characteristic energy $\epsilon$, and free for $r>r_1$; it can be considered as a crude approximation of the lennard-jones potential.

> <img src="{static}/images/PS-exam_vdw.svg" alt="vdw" style="width:300px;"/>

The second virial coefficient
$$B(T) = 2\pi \int_0^\infty \D r r^2 \left[ 1 - \E^{-w(r)/T} \right] $$
is (the integrals give the volume of a sphere over 2):
$$B(T) = \frac{2\pi}{3}r_0^3 + \frac{2\pi}{3} (r_1^3 - r_0^3)\big(1-\E^{\epsilon/T}\big) \,.$$
It can be written as $B=v_0-a/T$,
$$v_0 = \frac{2\pi}{3}r_0^3, \; a(T) = -\frac{2\pi}{3} (r_1^3 - r_0^3)\big(1-\E^{\epsilon/T}\big)T \,.$$

We note that when $T \gg \epsilon$ (high temperature case) we have $\E^{\epsilon/T}\approx 1 + \epsilon/T$, which leads to
$$a(T) = \frac{2\pi}{3} (r_1^3 - r_0^3)\epsilon = \text{const.} \,,$$
independent of $T$

Putting $B(T)$ in the virial formula $PV = NT (1+ B N/V)$, we obtain
$$PV = NT (1 + \frac{N}{V} v_0) - \frac{N^2}{V} a(T)$$
or
$$\left[ P + a(T) \frac{N^2}{V^2} \right] V = NT(1 +Nv_0/V) \approx \frac{NTV}{V-Nv_0}$$
where, in the last equality we used that $Nv_0 \ll V$. Therefore, we found the van der Waals equation of state with the microscopic parameters:
$$b = Nv_0, \; \text{and} \; a(T) = a(T) = \frac{2\pi T}{3} (r_1^3 - r_0^3)\big(\E^{\epsilon/T} - 1 \big) \,.$$ 
