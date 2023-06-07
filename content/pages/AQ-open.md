Title: Generalized quantum dynamics
Slug: AQ-open
Date: 2020-10-10
Category: Lectures
Tags: teaching, advanced quantum mechanics
Authors: Alberto Verga
Summary: Open quantum systems, Lindblad equation, quantum channels
status: hidden

$\newcommand{\I}{\mathrm{i}} 
\newcommand{\E}{\mathrm{e}} 
\newcommand{\D}{\mathop{}\!\mathrm{d}} 
\DeclareMathOperator{\Tr}{Tr}
\newcommand{\bra}[1]{\langle{#1}|}
\newcommand{\ket}[1]{|{#1}\rangle}
\newcommand{\braket}[1]{\langle{#1}\rangle}
\newcommand{\bbraket}[1]{\langle\!\langle{#1}\rangle\!\rangle}
\newcommand{\bm}{\boldsymbol}$

> [Lectures]({filename}AQ-index.md) on advanced quantum mechanics

# Open systems

An *open* system can be thought to be part of a larger isolated system; the actual system $S$ and its environment $E$. This is the framework we used to generalize the measurement process, when we introduced an ancilla space to describe the measurement by the unitary interaction between the system and the apparatus. Nonetheless, the physical properties of the environment are totally different to the measurement device: it is rather a bath whose state is only slightly affected by the system. A typical result of the interaction of the open system with its environment is some kind of relaxation from an out of equilibrium initial state. However, as in the case of the measurement, the system-environment interaction leads to their entanglement: the system's concomitant loss of information (leaked to the environment) is called *decoherence*.

<img src="{static}/images/AQ-se.svg" alt="S plus E" style="width: 250px;"/>

We are now interested in the dynamics of $S$, defined in the $\mathcal{H}_S$ subsystem of the total hilbert space $\mathcal{H}_{SE} = \mathcal{H}\otimes \mathcal{H}_E$ (figure above). The state of $S$ is described by the reduced density matrix,
$$\rho(t) = \Tr_E \rho_{SE}(t),$$
(we put  $\rho_S = \rho$); therefore, the problem is to find the evolution equation for $\rho$ knowing that $\rho_{ES}$ satisfies the von Neumann equation:
$$\I \frac{d}{dt}\rho_{SE}(t) = [H_{SE}, \rho_{SE}]\,.$$ 
The general form of the hamiltonian $H_{SE}$ of the total system is,
$$H_{ES} = H + H_E + V_{SE},\quad H = H_S$$
where $H$ and $H_E$ are the system's and environment hamiltonians and $V_{SE}$ their interaction energy. For the moment we are not interested in the particular form of the hamiltonian; we will use simply the total unitary operator $U(t,t_0)$ which evolves the total system state as:
$$\rho_{SE} = U_{SE}(t,t_0) \rho_{SE}(t_0) U_{SE}^\dagger(t,t_0)\,.$$

The evolution of the system is then,
$$\rho(t) = \Tr_E U(t)\rho_{SE}U^\dagger(t)$$
(simplifying the notation in an obvious way). The initial state is supposed to be a product state of the system $\rho(0) = \ket{\psi(0)} \bra{\psi(0)}$ and the bath, we note $\ket{0_E}$. Using the environment basis $\ket{n_E}$, we write,
$$\rho(t) = \sum_n \bra{n_E} U \ket{0_E} \rho(0) \bra{0_E} U^\dagger \ket{n_E}$$
We can define the system's operator,
$$M_n = \bra{n_E} U \ket{0_E}, \quad M_n \in \mathcal{H}_S$$
or
$$M_n(t) \ket{\psi_S} = \ket{n_E} U(t) \ket{\psi_S} \otimes \ket{0_E}, \quad \ket{\psi_S} \forall \mathcal{H}_S\,,$$
to obtain
$$\mathcal{E}(\rho(0)) = \rho(t) = \sum_n M_n(t) \rho(0) M^\dagger_n(t)\,.$$
The map $\mathcal{E}$ is referred as a "superoperator": it is linear and acts only on the system's state $\rho$, giving an operator in $\mathcal{H}_S$.  From the normalization of the state (the previous equation is exact: it contains the whole information on the system), we deduce that <strong style="color:DarkSlateBlue; background-color:LightGray;">EX</strong>
$$\sum_n M_n^\dagger M_n = 1\,,$$
are a set of Kraus operators from which we can define the positive hermitian operators $E_n = M_n^\dagger M_n$. The linear, trace preserving map $\mathcal{E}$ generalizes the unitary evolution to open system; it is itself unitary in an extended hilbert space.


## Master equation

Based on the previous theory of superoperators we incorporates the specific form of the hamiltonian and the physical properties of the environment, supposed to be a bath, or a source of noise, allowing us to neglect memory effects and deduce a markovian equation of motion.

We consider a short interval of time $\Delta t$, so that $\Delta t \ll \tau$ where $\tau$ is the characteristic time of the system's $S$ evolution. We also suppose $\Delta t \gg \tau_c$, the correlation time characterizing the interaction with the environment; this condition justifies the markovian approximation. During this interval the state changes
$$\rho \rightarrow \mathcal{E}(\rho) = \rho + \Delta \rho = \sum_n M_n \rho M^\dagger_n$$
according to the generalized evolution of a quantum open system. The system evolution is governed by the von Neumann equation, once one takes the partial trace over $E$:
$$\frac{\D}{\D t}\rho(t) = -\I \Tr_E [H_{SE}, \rho_{SE}] = -\I [H,\rho] - \I [H_E+V_{SE},\rho_{SE}]\,.$$
For $\Delta t$ small enough, we assume $\mathcal{E}$ near the identity,
$$\Delta \rho \sim \mathcal{O}(\Delta t),$$
thus, to linear order in $\Delta T$, we can write
\begin{align*}
M_0 &= 1 - \I H \Delta t + L_0 \Delta t \\
M_n &= L_n \sqrt{\Delta t}, \quad n \ne 0
\end{align*}
where, without loss of generality, we separated the near identity operator to be the $n=0$ kraus operator, in order to take exactly into account the first term of the von Neumann equation. Replacing this expansion into the linear map $\mathcal{E}(\rho)$, we obtain <strong style="color:DarkSlateBlue; background-color:LightGray;">EX</strong>
$$\frac{\D}{\D t}\rho = - \I [H, \rho] + \{L_0, \rho\} + \sum_{n>0} L_n \rho L_n^\dagger\,,$$
($\{\cdot,\cdot\}$ is the anticommutator) or, using $\Tr \rho = 1$
$$L_0 = - \frac{1}{2} \sum_{n>0}L_n^\dagger L_n\,,$$
we get the *Lindblad* equation:
$$\frac{\D}{\D t}\rho + \I [H, \rho] = \sum_{n>0} \left( L_n \rho L_n^\dagger - \frac{1}{2} \{L^\dagger_n L_n, \rho\} \right)\,.$$
We may rewrite the lindblad equation in the interaction representation:
$$\rho(t) \rightarrow \hat{\rho}(t) = \E^{-\I H t} \rho(t) \E^{\I H t}\,,$$
this eliminates the commutator in the left hand side to give
$$\frac{\D}{\D t}\hat{\rho} = \sum_{n>0} \left( \hat{L}_n \hat{\rho} \hat{L}_n^\dagger - \frac{1}{2} \{\hat{L}^\dagger_n \hat{L}_n, \hat{\rho}\} \right)\,.$$
where all operators are in the interaction representation. This equation describes the irreversible evolution of the system towards some set of stationary states. Stationary states are determined by the zero eigenvalues of the *lindbladian* $\mathcal{L}$:
$$\frac{\D}{\D t}\hat{\rho} = \mathcal{L} \hat{\rho}\,,$$
note that $\mathcal{L}$ is not unitary.

One important consequence of the non-unitary of $\mathcal{L}$ is that the system's entropy increases due to the interaction with the environment, under some general conditions on $L_n$. Inserting the lindblad equation into the von Neumann entropy evolution we have,
\begin{align*}
  \frac{\D}{\D t}S &= - \Tr \dot{\rho} \log \rho \\
  &= \sum_n \Tr (L^\dagger_n L_n \rho - L_n \rho L^\dagger_n) \log \rho \,,
\end{align*}
where we used the identity $\Tr f(\rho) [H,\rho] = 0$; now we introduce the density matrix diagonal expansion: 
$$\rho = \sum_k p_k \ket{k} \bra{k}$$
which allows us to rewrite the previous equation as,
\begin{align*}
  \frac{\D}{\D t}S &= \sum_{nkl} \left( L_n^\dagger L_n \ket{k}\braket{k|l} \bra{l} p_k \log p_l \right. \\
  & \quad - \left. L_n \ket{k} \bra{k} L^\dagger_n \ket{l} \bra{l} p_k \log p_l \right) \\
  & = \sum_{nkl} \left( \braket{k| L^\dagger_n L_n |k} p_k \log p_k - |\braket{l| L_n |k}|^2 p_k \log p_l \right) \\
  & = \sum_{nkl} |\braket{l| L_n |k}|^2 p_k \log \frac{p_k}{p_l} 
\end{align*}
The inequality $p\log(p/q) \ge p - q$, implies
\begin{align*}
  \frac{\D}{\D t}S & \ge \sum_{nkl} |\braket{l| L_n |k}|^2 (p_k - p_l) \\
  & = \sum_n \Tr \left( -L^\dagger_n \rho L_n + L_n \rho L^\dagger_n \right)
\end{align*}
We finally obtain the desired inequality for the entropy evolving according to the lindblad equation:
$$\frac{\D}{\D t}S \ge \sum_n \Tr \rho [L^\dagger_n, L_n]\,.$$
Therefore, if $L_n$ are normal operators (a normal operator commutes with its hermitian conjugate), the entropy always grows as a result of the interaction with the environment.

## Applications

In the context of information theory the action of the superoperator on the quantum state
$$\rho \rightarrow \mathcal{E}(\rho) = \sum_n M_n \rho M_n^\dagger,$$
which generalizes in the form of a complete positive map the usual unitary evolution, is referred as a *quantum channel*. Because this description includes open systems, it can describe transmission errors, such as amplitude damping of the qubits, or undesired phase changes or flips between up and down states.

### Kraus mapping for a depolarizing channel

Transmission of information through a quantum channel might be subject to errors generated by the interaction of the physical qubits with the environment. Consider for example an imperfect channel that introduces with probability $p/3$ a bit flip, a phase flip or both; the corresponding operators are the pauli matrixes $X$, $Z$ and $Y = \I XZ$, respectively. The whole system evolves according to the unitary operator acting on $SE$:
$$U_{SE} \ket{\psi} \otimes \ket{0_E} = \sqrt{1-p} \ket{\psi} \otimes \ket{0_E} + \sqrt{p/3} X\ket{\psi} \otimes \ket{1_E} + \sqrt{p/3} Y\ket{\psi} \otimes \ket{2_E} + \sqrt{p/3} Z\ket{\psi} \otimes \ket{3_E}\,,$$
where $\ket{\psi}$ is the transmitted qubit initial state. Tracing out the environment we obtain,
$$\mathcal{E}(\ket{\psi} \bra{\psi}) = (1-p) \ket{\psi} \bra{\psi} + \frac{p}{3} X \ket{\psi} \bra{\psi} X + \frac{p}{3} Y \ket{\psi} \bra{\psi} Y + \frac{p}{3} Z \ket{\psi} \bra{\psi} Z\,,$$
from which we identify the krauss operators:
$$M_0 = \sqrt{1-p} 1_2, \quad \bm M = (M_1, M_2, M_3) = \sqrt{p/3} \bm \sigma\,.$$
Using the relation $\sigma_i \sigma_j \sigma_i = -\sigma_j$ for $i \ne k$, we may compute the change in the general pure state $\rho = \ket{\psi} \bra{\psi} = (1_2 + \bm n \cdot \bm \sigma)/2$,
$$\mathcal{E}(\rho) = \frac{1}{2} \left[ 1_2 + \left( 1 - \frac{4}{3}p \right) \bm n \cdot \bm \sigma \right],.$$
As a result of the errors the initial qubit evolves into a mixed state, represented by a surface of radius $|1-4p/3|$ in the bloch sphere.[^bh]


### Phase damping

The idea is to associate the lindblad operator responsible for qubit dephasing, the random change of the relative phase between the $\ket{0}$ and $\ket{1}$ states of a qubit, the $Z$ pauli matrice. With $L = \sqrt{\nu} Z$, with $\nu>0$, the lindblad equation becomes (note that $Z^\dagger Z = Z^2 = 1$),
$$\frac{\D \rho}{\D t} = \nu (Z\rho Z - \rho)\,.$$
Using the bloch representation of the qubit state
$$\rho(t) = \frac{1}{2} + \frac{1}{2}\bm r(t) \cdot \bm \sigma$$
and noting that $ZXZ=-X$, $ZYZ=-Y$, one obtains the set of equations,
\begin{align*}
\frac{\D r_x}{\D t} &= -2 \nu r_x \\
\frac{\D r_y}{\D t} &= -2 \nu r_y \\
\frac{\D r_z}{\D t} &= 0
\end{align*}
leading to the solution,
$$\braket{0| \rho |0} = \braket{1| \rho |1} = \text{const.}$$
for the diagonal terms, and
$$\braket{0| \rho |1} = \rho_{01} \E^{-2 \nu t}$$
($\rho_{10} = \bar{\rho}_{01}$, by hermiticity). Therefore, the diagonal terms of $\rho(t)$ remain constant, while the nondiagonal ones decay. The diagonal terms are related to the ground and excited states populations; the nondiagonal terms are instead related to the coherence between these two states: their decay denotes the increasing with time of the decoherence of the two qubit states. In conclusion, the effect of random phase flips lead to the suppression of the quantum state coherence.

We may also express the density matrix at time $t$ in the form of a complete positive map applied to the initial state $\rho(0)$:
$$\rho(t) = \sum_{n=1}^2 M_n(t) \rho(0) M_n^\dagger(t)$$
where the krauss operators are <strong style="color:DarkSlateBlue; background-color:LightGray;">EX</strong>:
$$M_1 = \sqrt{1-p} 1_2, \; M_2 = \sqrt{p} Z \,,$$
where
$$p(t) = (1 - \E^{-2\nu t})/2\,.$$
These krauss operators completely characterize the phase damping channel.

## Amplitude damping

We consider a two level system in contact with a bath, whose hamiltonian is
$$
H = J Z\,,$$
Note that $\ket{e}=\ket{0}$ corresponds to the upper state and $\ket{g}=\ket{1}$ to the lower one. The interaction with the bath results in the absorption or emission of a boson accompanied with the excitation or decay of the atom, respectively. The excitation and decay operators are
$$\sigma_+ = \frac{X + \I Y}{2}, \quad \sigma_- = \frac{X - \I Y}{2}\,.$$
Therefore, we define $L = \sqrt{\nu} \sigma_-$ (the hermitian conjugate is $\sigma_+$) the lindblad operator describing the amplitude damping of the system (decay from the 0 excited state to the 1 ground state: $\sigma_- = \ket{g}\bra{e} = \ket{1}\ket{0}$). Indeed, the jump between the levels transfer part of their respective amplitudes to the bath. Another way to see what happens, is to say that during the interval $t, t + \Delta t$, the atom jumps to the exited level with probability $\nu \Delta t$, then we apply $\sigma_+$, and decays with probability $1-\nu \Delta t$, and then we apply $\sigma_-$; the markovian process consists, at each time step $\Delta t$, in applying randomly the creation and annihilations operators $\sigma_\pm$.

The lindblad equation reads,
$$\frac{\D \rho}{\D t} = \frac{\nu}{2} (2\sigma_- \rho \sigma_+ - \sigma_+ \sigma_- \rho - \rho \sigma_+ \sigma_-)\,.$$
Using as before the bloch representation we obtain the set of equations <strong style="color:DarkSlateBlue; background-color:LightGray;">EX</strong>:
\begin{align*}
  r_x(t) &= r_x(0) \E^{-\nu t/2}\\
  r_y(t) &= r_y(0) \E^{-\nu t/2}\\
  r_z(t) &= r_z(0) \E^{-\nu t} - 1 + \E^{-\nu t}
\end{align*}
or equivalently:
$$\braket{0| \rho |0} = \rho_{00} \E^{-\nu t}\,,$$
and
$$\braket{0| \rho |1} = \rho_{01} \E^{-\nu t/2}\,,$$
where we used the canonical basis order:
$$\begin{pmatrix} ee & eg \\ ge & gg \end{pmatrix} \,.$$
Both diagonal and nondiagonal terms decay with a rate proportional to $\nu$. From the geometrical point of view, we see that the bloch vector tends to $\bm r = (0,0,-1)$. The quantity $p(t) = 1 - \E^{-\nu t}$, which at short times is $p\approx \nu \Delta t$, corresponds to the spontaneous emission probability: it tends to 1 at large times $t \gg 1/\nu$, leading the system towards its "ground" state. In particular, if the initial state is mixed, the final one is a pure state.

The associated quantum channel operators $M$ can be obtained by noting that:
\begin{align*}
\ket{g}\ket{0_E} &\rightarrow \ket{g}\ket{0_E}\\ 
\ket{e}\ket{0_E} &\rightarrow \sqrt{1-p} \ket{e}\ket{0_E} + \sqrt{p} \ket{g}\ket{1_E}\\ 
\end{align*}
(Remind that $\ket{1}=\ket{g}$ and $\ket{0}=\ket{2}$ denote the ground and excited states, respectively.) After partial tracing the environment, we may then write the evolved state
$$\rho(t) = M_1(t) \rho(0) M_1^\dagger(t) + M_2(t) \rho(0) M_2^\dagger(t)\,,$$
in terms of the krauss operators
$$M_1(t) = \begin{pmatrix} \sqrt{1 - p(t)} & 0 \\ 0 & 1 \end{pmatrix}$$
and
$$M_2(t) = \begin{pmatrix} 0 & 0 \\ \sqrt{p(t)} & 0  \end{pmatrix} = \sqrt{p(t)} \sigma_- \,.$$
From these definitions we then have,
$$\rho(t) = \begin{pmatrix} (1-p(t))\rho_{00} & \sqrt{1-p(t)} \rho_{01} \\ \sqrt{1-p(t)} \rho_{10} & p(t) \rho_{00} + \rho_{11} \end{pmatrix}\,, $$
which leads to the identification $p(t) = 1 - \E^{-\nu t}$.

### Exercises

1. Demonstrate that the purity $\Tr \rho^2$ decreases under the lindblad dynamics, in the case where the $L_n$ are hermitian,
    $$\frac{1}{2}\frac{\D}{\D t} \Tr \rho^2 = \Tr \rho \mathcal{L} \rho \le 0\,,$$
    showing that the system evolves towards a mixed state, even if initially it was in a pure state, at variance with the von Neumann equation.[^M]

2. Show that the krauss operators for phase damping are,
    $$M_1 = \sqrt{1-p} 1_2,\; M_2 = \sqrt{p} \ket{0} \bra{0},\; M_3 = \sqrt{p} \ket{1} \bra{1}.$$
    where $p = 1-\E^{-2\nu t}$.

3. Show that the krauss operators for amplitude damping are,
    $$M_1 = \ket{0}\bra{0} + \sqrt{1-p} \ket{1}\bra{1}$$
    and
    $$M_2 = \sqrt{p} \ket{0} \bra{1}\,,$$
    where $p = 1-\E^{-\nu t}$.

4. Random phases.[^p] Consider a qubit initial state $\ket{\psi} = a \ket{0} + b \ket{1}$ that evolves to the state
   $$\ket{\psi(t)} = a \E^{\I \theta_1} \ket{0} + b \E^{\I \theta_2} \ket{1}$$
   with probability
   $$P(t, \theta_1, \theta_2) = P_t(\theta_1) P_t(\theta_2),$$
   with
   $$P_t(\theta) = \frac{\E^{-\theta^2/2\nu t}}{\sqrt{2\pi \nu}}$$
   a gaussian of zero mean and variance $\nu t$.
   Compute the density matrix:
   $$\rho(t) = \int_{-\infty}^\infty \D \theta_1 \D \theta_2 P(t, \theta_1, \theta_2) \ket{\psi(t)} \bra{\psi(t)}$$
   and show that it satisfies the equation,
   $$ \frac{\D \rho}{\D t} = - \nu ( \rho - M_1 \rho M_1 - M_2 \rho M_2 )$$
   where $M_n = \ket{n} \bra{n},\,n=0,1$; demonstrate that it is a Lindblad equation where
   $$L_n = \sqrt{2\nu} M_n\,.$$
   Discuss your results.

5. Unitary jump.[^p] A system evolves with probability $\nu\Delta t$ under the unitary $\E^{-\I J \theta}$, where $J$ is hermitian (it may represent the generator of rotations, or angular momentum), and $\theta$ a real parameter; thus $1 - \nu \Delta t$ is the probability that any change arises during $\Delta t$. We can write the density matrix as,
    $$\rho(t + \Delta t) = (1 - \nu \Delta t) \rho(t) + \nu \Delta t \E^{-\I J \theta} \rho \E^{\I J \theta} \,.$$
    Deduce the differential equation followed by $\rho(t)$ and show that it is of the lindblad form with
    $$L = \sqrt{\nu} \E^{-\I J \theta} \,.$$
    Solve the equation using the two eigenvalues of $J$, $j_1$ and $j_2$. Compute the decay rate.

## Notes

An interesting presentation of open systems, at an introductory level, can be found in the excellent book:

* B. Schumacher and M. Westmoreland, *Quantum Processes Systems, and Information,* Cambridge (2010)

A more complete treatment at the same level, is presented in:

* G. Auletta, M. Fortunato, and G. Parisi, *Quantum Mechanics,* Cambridge (2009)

[^bh]: Bergou, J., and Hillery, M., *Introduction to the Theory of Quantum Information Processing,* Springer (2013)

[^M]: Manzanaro, D., AIP Advances **10**, 025106 (2020) [.pdf]({static}/pdfs/Manzano-2020.pdf)

[^p]: Pearle, P., *Simple derivation of the Lindblad equation,* Eur. J. Phys. **33**, 805 (2012)

