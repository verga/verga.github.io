Title: Exercises
Slug: CH-exercises
Date: 2019-11-12
Category: Lectures
Tags: teaching, chaos, quantum
Authors: Alberto Verga
Summary: Problems, exercises and selected applications of advanced quantum mechanics and chaos.
status: hidden

$\newcommand{\I}{\mathrm{i}} 
\newcommand{\E}{\mathrm{e}} 
\newcommand{\D}{\mathop{}\!\mathrm{d}} 
\newcommand{\bra}[1]{\langle{#1}|}
\newcommand{\ket}[1]{|{#1}\rangle}
\newcommand{\braket}[1]{\langle{#1}\rangle}
\newcommand{\bbraket}[1]{\langle\!\langle{#1}\rangle\!\rangle}$
$\newcommand{\bm}{\boldsymbol}$

## Topics

* Quantum principles, density matrix and entanglement
* Random quantum states and Don Page entropy formula
* Gates and simple circuits, superdense coding, teleportation, Deutsch algorithm, Grove search algorithm
* Quantum walks
* Quantum chaos: the kicked rotator and dynamical localization

## Problems

### 1
Density matrix. A quantum system consists in two parts A and B. Show that the expected value of an operator $O$ acting on A,

$$O = O_A \otimes I_B$$

where $I_B$ is the identity in the B hilbert spaca $\mathcal{H}_B$, is given by the partial trace, over B, of the AB density matrix $\rho$,

$$\rho_A = \mathrm{Tr}_B \rho\,.$$

As an application take a two spins state:

$$\ket{\psi} = \frac{1}{\sqrt{2}}\left( \ket{0} \otimes \ket{1} + \ket{1} \otimes \ket{0} \right)\,,$$

and compute the expected value of $X$ and $Z$ (the A pauli matrix in the $x$ and $z$ directions). Compare with the single spin state $(\ket{0} + \ket{1})/\sqrt{2}$.

### 2
Bell state entanglement. Consider a bipartite system AB, and the dichotomic variables $a,c=\pm1$ of A and $b,d=\pm1$ of B. Show that,

$$x = ab + ad + cb - cd = \pm 2\,.$$

Demonstrate that the expected value $\braket{x}$ satisfies $\braket{x} \le 2$.

Now consider a quantum equivalent system:

$$|\braket{X}| = \left| \braket{ \bm \sigma_A \cdot \bm n_a \bm \sigma_B \cdot \bm n_b + \bm \sigma_A \cdot \bm n_a \bm \sigma_B \cdot \bm n_d + \bm \sigma_A \cdot \bm n_c \bm \sigma_B \cdot \bm n_b - \bm \sigma_A \cdot \bm n_c \bm \sigma_B \cdot \bm n_d } \right|$$

Demonstrate that,

$$|\braket{X}| \le 2\sqrt{2}$$

in contradiction to the classical result. Compute the expected value of $X$ in the state,

$$\ket{AB} = \frac{1}{\sqrt{2}} \left( \ket{01}- \ket{10} \right)\,,$$

where the measure axes are in the plane $xz$ with angles with respect to the $z$ axis $\theta_a = 0$, $\theta_b = \pi/2$, $\theta_c = \pi/4$, and $\theta_d = -\pi/4$.

### 3
The Greenbergm Horne and Zeilinger paradox. Consider the state GHZ of a three parts system ABC:

$$\ket{GHZ} = \frac{1}{\sqrt{2}} \left( \ket{000} + \ket{111} \right).$$

Show that the operators in the set $\mathcal{S}$, have eigenvalue 1:

$$\mathcal{S} = \{111, ZZ1, 1ZZ, Z1Z, XXX, -YYX, -YXY, -XYY\},$$

where, for instance, $YXY = Y_A \otimes X_B \otimes Y_C$ and $ZZ1 = Z_A \otimes Z_B \otimes I_C$.

Consider now a classical equivalent system for which the value of the observables in $\mathcal{S}$ can take the values $m(\mathcal{S}) = \pm 1$. Show then that,

$$m(X_A) m(X_B) m(X_C) = ?$$
$$-m(Y_A) m(Y_B) m(X_C) = ?$$
$$-m(Y_A) m(X_B) m(Y_C) = ?$$
$$-m(X_A) m(Y_B) m(Y_C) = ?$$

leads to a contradiction $-1=1$.

### 4
Teleportation. Alice and Bob share the bell state,

$$\ket{\Phi_-} = \frac{1}{\sqrt{2}} \left( \ket{01}- \ket{10} \right)\,,$$

In addition, Alice possesses an arbitrary state $\ket{\psi} = a \ket{0} + b \ket{1}$. Show that the three qubit state can be written as,

$$\ket{\psi} \ket{\Phi_-} = \frac{1}{2} \left[ \ket{\Phi_+} (-Z) \ket{\psi} + \ket{\Phi_-} (-\ket{\psi}) + \ket{\Psi_+} (-XZ \ket{\psi}) + \ket{\Psi_-} (X \ket{\psi}) \right]$$

a decomposition in the bell states:


$$\ket{\Phi_\pm} = \frac{1}{\sqrt{2}} \left( \ket{01} \pm \ket{10} \right)\,,$$
$$\ket{\Psi_\pm} = \frac{1}{\sqrt{2}} \left( \ket{00} \pm \ket{11} \right)\,.$$

Explain how the information in possession of Alice (the bell states) may lead Bob to recover the initially Alice $\ket{\psi}$ state.

Answer: $\ket{\Phi_+} \rightarrow Z$, $\ket{\Phi_-} \rightarrow I$, $\ket{\Psi_+} \rightarrow ZX$, and $\ket{\Psi_-} \rightarrow X$. 

### 5
The Deutsch-Jozsa algorithm. We want to determine if certain boolean function $f$ of $n$ bits,

$$f(x_1,\ldots,x_n), \quad x \in \{0,1\}$$

is "constant" or "balanced". In the first case, the constant value of $f$ can be either 0 or 1, whatever the set of input bits. In the second case, $f=0$ for exactly half of the possible input values of $\{x_1,\ldots,x_n\}$, and $f=1$ for the other half.

* How many evaluations of $f$ are necessary to decide classically if it is constant or balanced?

Deutsch devised a quantum algorithm which only needs one evaluation of $f$, using the circuit:

> <img src="{static}/images/CH-dj.png" style="width:400px;" />

where the unitary operator $U_f$ is defined by

$$U_f \ket{x}\otimes \ket{b} = \ket{x}\otimes \ket{f(x) \oplus b}$$

with the notation $\ket{x}$ for the state of the first $n$ qubits (top wire of the circuit), and $\ket{b}$ for the last qubit (bottom wire). Initially the $n+1$ qubits are in the state $\ket{0}$

* Compute the state $\ket{\psi_0}$ after the application of the operator $X$ to the last qubit.

* Compute the state $\ket{\psi_1}$ after the application of the Hadamard operator to all qubits.

* Show that the state of the last qubit remains the same, up to a *phase factor*,

    $$ \ket{-} = \frac{\ket{0}-\ket{1}}{\sqrt{2}}  $$

    after the $U_f$ step. The phase factor depends on the value of $f$.

    Determine the state $\ket{\psi_2}$ after applying $U_f$.

* Demonstrate that after the last application of the Hadamard operator to the first $n$ qubits, the final state is,

    $$\ket{\psi_3} = \frac{1}{2^{n}} \sum_{x,y\in\{0,1\}^n} (-1)^{\langle x,y \rangle + f(x)} \ket{y} \otimes \ket{-} $$

    *Hint*. As an intermediate computation you may demonstrate that,

    $$H^{\otimes n} \ket{0} = \frac{1}{\sqrt{2^n}} \sum_{x\in\{0,1\}^n} \ket{x}$$

    (which gives you $\ket{\psi_1}$), and

    $$H^{\otimes n} \ket{x} = \frac{1}{\sqrt{2^n}} \sum_{y\in\{0,1\}^n} (-1)^{\langle x,y \rangle} \ket{y}$$

    which will give you the $\ket{\psi_3}$ state.

* Explain how one may distinguish between the two cases, constant or balanced, using the properties of the final quantum state. Can we answer the question with certainty?


### 6
Quantum walk. Investigate the pseudo-energy spectrum of a one dimensional quantum walk defined by the step operator $U = SC$ with coin,

$$C=R_y(\theta) = \E^{-\I \theta Y/2}$$

and motion,

$$S = \sum_x \left( \ket{x+1} \bra{x} \otimes \ket{0} \bra{0} +  \ket{x-1} \bra{x} \otimes \ket{1} \bra{1} \right) \,.$$

Find the expression of the effective hamiltonian in the limit $k \rightarrow 0$ and compare the result with the Dirac hamiltonian.
