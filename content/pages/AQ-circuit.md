Title: Quantum circuits
Slug: AQ-circuit
Date: 2020-09-26
Category: Lectures
Tags: teaching, advanced quantum mechanics
Authors: Alberto Verga
Summary: Circuit model of quantum computation, gates, universality and simple circuits.
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

# Circuit computational model

## Quantum gates

Quantum gates are simple one and two qubits unitary operators that allow the construction of much more complex, in fact arbitrary, unitary operators acting on a $N$-qubit system. The ability to model an arbitrary $U$ by a product of single and two qubits unitary operators is known as universality, and the corresponding set of gates as universal.

One qubit gates are essentially constructed from the pauli matrices, which generate arbitrary rotations in the natural $SU(2)$ space of the qubit (bloch sphere),[^bb]
$$R(\varphi,\theta,\psi) = \E^{-\I \psi Z/2} \E^{-\I \theta Y/2} \E^{-\I \varphi Z/2} = R_z(\psi) R_y(\theta) R_z(\phi)\,,$$
where
$$R_n(a) = \E^{-\I \hat{\bm n} \cdot \bm \sigma \, a/2}\,,$$
is the rotation matrix of angle $a$ and axis $\hat{\bm n}$. Some particular cases are physically important. For instance the Hadamard gate,
$$H = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$$
represents, in quantum optics, a lossless symmetric beam splitter. Logical "not" can be implemented by the $X$ matrix that exchanges $\ket{0}$ and $\ket{1}$:
$$X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}\,.$$
The action of the hadamard gate can be also written,
$$H: \ket{x} \rightarrow \frac{1}{\sqrt{2}} (\ket{0} + (-1)^x \ket{1})$$
where $x = 0, 1$, analogously
$$X: \ket{x} \rightarrow \ket{1 \oplus x}$$
where $\oplus$ is for the addition modulo 2.

An important two qubit gate is the controlled not:
$$\mathsf{CNOT}: \ket{x} \otimes \ket{y} \rightarrow \ket{x} \otimes \ket{y \oplus x}\,.$$
Its matrix representations is,
$$\mathsf{CNOT} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix}\,,$$
which exchange the values of the second qubit if the first one is in the 1 state, without modifying the first qubit.

A general controlled unitary $U$ has the form given by the circuit,

<img src="{static}/images/AQ-ccu.svg" alt="control U" style="width: 250px;"/>

note the power $x$: if $x=0$ the input state do not change, otherwise $x=1$ we apply $U$ to de second qubit.

### Universal gate set

One qubit gates and the $\mathsf{CNOT}$ two qubits gate form a set of *universal* gates: any $n$-qubit operator can be written as a circuit of this set of gates.

The general expression of a qubit unitary is
$$U = \E^{\I \alpha} \mathsf{R}(\varphi, \theta, \psi)\,.$$
In fact, we need at most four complex numbers to write any two by two matrix; however, the unitary condition restrict the number to independent parameters to four reals $\alpha, \varphi, \theta, \psi \in \mathbb{R}$. In addition to the global phase $\alpha$, the three euler angles allow a general rotation $SU(2) \sim SO(3)$:
$$U = \begin{pmatrix} \E^{ \I (\alpha - \psi/2 - \phi/2) } \cos \theta/2 & -\E^{ \I (\alpha - \psi/2 + \phi/2) } \sin \theta/2 \\ \E^{ \I (\alpha + \psi/2 - \phi/2) } \sin \theta/2 & -\E^{ \I (\alpha + \psi/2 + \phi/2) } \cos \theta/2 \end{pmatrix}\,,$$
that can be written as the $\mathsf{R}$ product of rotations <strong style="color:DarkSlateBlue; background-color:LightGray;">EX</strong>.

A useful particular form of the general decomposition of $U$ is
$$U = \E^{\I \alpha} A X B X C, \quad ABC = 1\,,$$
as can be verified writing 
\begin{align*}
A &= R_z(\psi) R_y(\theta/2)\\
B &= R_y(-\theta/2) R_z\left( -\frac{\phi + \psi}{2}\right)\\
C &= R_z\left( \frac{\phi - \psi}{2}\right)
\end{align*}
<strong style="color:DarkSlateBlue; background-color:LightGray;">EX</strong>, which we use to write a general controlled $U$ two qubit operator:

<img src="{static}/images/AQ-ccuU.svg" alt="control U universal" style="width: 400px;"/>

where the last gate $\Phi$ takes into account the phase $\alpha$:
$$\Phi(\alpha) = \begin{pmatrix} 1 & 0 \\ 0 & \E^{\I \alpha} \end{pmatrix}\,.$$
Therefore, any controlled operation can be implemented using the $\mathsf{CNOT}$ gate with well chosen one qubit operators.

One possible demonstration of the universality of the set mentioned is using the classical result that the toffoli gate is universal, and showing that the toffoli gate can be written in terms of the cnot gate, together with one quibit gates.

## Quantum Circuits

We show through some simple circuits the entanglement mechanisms and we illustrate the related notion of entanglement as a resource. We also discuss the measurement process in the context of quantum circuits.

### Deutsch algorithm

The Deutsch algorithm circuit aims at determining if a boolean function is balanced or constant. We take $f$ to be a function whose range and domain are one bit:
$$f: \{0,1\} \rightarrow \{0,1\}\,.$$
One says that a general boolean function (with domain $n$ bits and range one bit) $f$ is *balanced* if $f(x)$ evaluates to 0 for half of the inputs, and 1 for the other half; in addition, one says that $f$ is constant if, whatever the input, the output is 0 or 1, exclusively. In the case of a one bit to one bit function, it is balanced if $f(0) \ne f(1)$ and constant if $f(0) = f(1)$. Therefore,
$$f(0) \oplus f(1) = \begin{cases} 0 & \text{if constant} \\ 1 & \text{if balanced} \end{cases}\,.$$
The circuit is shown below. It is implemented with a controlled unitary operator $U_f$:
$$U : \ket{xy} \rightarrow \ket{xy\oplus f(x)}\,.$$ 

<img src="{static}/images/AQ-cdeutsch.svg" alt="Deutsch circuit" style="width: 400px;"/>

It is easy to show that <strong style="color:DarkSlateBlue; background-color:LightGray;">EX</strong>:
$$\ket{\psi_3} = \pm \ket{f(0) \oplus f(1)}\otimes \ket{-}, \quad \ket{-} = \frac{\ket{0} - \ket{1}}{\sqrt{2}}\,.$$
As a consequence, a measurement of the first qubit gives information about a *global* property $f$: the result 0 means that it is constant and the result 1 that it is balanced. This answers the question computing $U_f$ only once: a unique (quantum) evaluation of $f$ is then enough. Classically we would had to use two evaluations of $f$ to determine if $f$ is balanced or constant. This circuit illustrates a quantum advantage over the classical one, where the extra resource is the inherent quantum parallelism (superposition and interference of states). Remark that this result is obtained without resorting to entanglement of the two qubits.

### Bell states

The bell state can be generated using a simple circuit with one hadamard gate, which prepares the qubit into a superposition, and a cnot gate, which is responsible of the entanglement:

<img src="{static}/images/AQ-cbell.svg" alt="Bell states circuit" style="width: 200px;"/>

or in a compact notation
$$\ket{b_{xy}} = \frac{1}{\sqrt{2}} \left( \ket{0y} + (-1)^x \ket{1 y \oplus 1} \right)$$
The bell states correspond to
$$\ket{\Phi_+} = \ket{b_{00}} \,, \quad \ket{\Phi_-} = \ket{b_{10}}$$
and
$$\ket{\Psi_+} = \ket{b_{01}} \,, \quad \ket{\Psi_-} = \ket{b_{11}}$$

### Dense coding

It is possible to communicate two bits of classical information using only one qubit from a pair of entangled qubits. Dense coding provides the simplest example showing entanglement as a computational resource; with $n$ qubits we can code $2^n$ bits of information (the dimension of their hilbert space), thus opening the way to an exponential increase in the performance of the quantum information processing.

<img src="{static}/images/AQ-cdc.svg" alt="dense coding" style="width: 350px;"/>

Two qubits are initialized in the $\ket{0}$ state and entangled to form a bell state $\ket{\Phi_+}$; this entangled state is shared by Alice and Bob. Alice want to send a two bits message to Bob, then she applies the following operator to her first qubit:
$$Z^{b_2} X^{b_1}$$
as a result, the initial bell state change into one of the four basis states:
\begin{align*}
00 & \rightarrow 1 &\rightarrow \ket{\Phi_+} \\
01 & \rightarrow Z &\rightarrow \ket{\Phi_-} \\
10 & \rightarrow X &\rightarrow \ket{\Psi_+} \\
11 & \rightarrow ZX &\rightarrow \ket{\Psi_-}
\end{align*}
After applying a different operator for each possible message, she send her qubit to Bob. Bob applies the inverse transformation $\mathsf{CNOT} \, \mathsf{H}$ to *disentangle* them, and finally he measures the two qubits: the result of the measurement is the message. In conclusion, using one operation on only one qubit, Alice send a message of two bits through a quantum channel to Bob; the last operation is a measurement of the two qubits.

### Teleportation

An interesting and enlightening application of the entanglement of two qubits, like in the bell states, is the possibility of quantum state teleportation. It is easy to demonstrate that the linearity of quantum laws forbids to copy a state, or state *cloning*.

Indeed, we can use as a resource the entanglement of Bell states, to teleport an unknown qubit $\ket{\psi}$, as shown it the circuit below. 

<img src="{static}/images/AQ-ctele.svg" alt="teleportation" style="width: 350px;"/>

We observe that the entanglement is created by a mechanism of *interaction* of the two qubits. To show this, let us write the cnot unitary as a product of one qubit operators and one ising-like unitary <strong style="color:DarkSlateBlue; background-color:LightGray;">EX</strong>:
$$\E^{\I Z \otimes Z \pi/2},$$
we get,
$$\mathsf{CNOT} = U(1, Y, \pi/2)\, \mathsf{CZ}\, U(1, Y, -\pi/2)\,,$$
where
$$\mathsf{CZ} = \E^{\I \pi/4} U(Z,Z, -\pi/2) U(Z,1,\pi/2) U(1,Z,\pi/2)\,,$$
is the control-$Z$ or controlled phase two qubit gate, and
$$U(A,B,\theta) = \exp\left( -\I A \otimes B \,\theta/2 \right) \,.$$
We observe that, up to one qubit rotations, the interaction between the two qubits has the generic form of the ising hamiltonian $H \sim Z \otimes Z$ of two spins. Is just this type of interacting mechanism which is at the origin of the two qubits entanglement.


### Exercises

1. Show that the following circuit represents a generalized measurement; $U_M$ is unitary, its eigenvalues are supposed to be $1$ and $-1$ (for the states $\ket{0}$ and $\ket{1}$, respectively)

    <img src="{static}/images/AQ-cm.svg" alt="measurment U" style="width: 300px;"/>

2. Demonstrate that cloning a quantum state is in contradiction with quantum mechanics.

3. Compute the successive states of the teleportation circuit; analyze in particular how are used the measurement results.

4. Show that the modified teleportation circuit with deferred measurement (figure below), transfers an unknown quantum state $\ket{\psi}$ from one quantum channel to another one; explain why this version, even if equivalent to the bell measurement based teleportation from the quantum point of view, cannot be considered as a real teleportation.

    <img src="{static}/images/AQ-cteleU.svg" alt="teleportation U" style="width: 350px;"/>

5. Write the $\mathsf{CZ}$ two qubits gate in terms of an effective hamiltonian $\hat{H}$ (not to be confused with the hadamard gate),
    $$\mathsf{CZ} = \E^{-\I \hat{H}}$$
    and discuss the result.

6. Show that,
    $$\mathsf{CNOT} = (1\otimes H) \mathsf{CZ} (1\otimes H)$$
    and write the corresponding circuit.

## Notes

An interesting account of teleportation in the language of quantum computing can be found in the web site [Qiskit](https://qiskit.org/textbook/ch-algorithms/teleportation.html). You can also find a practical implementation of the [dense coding](https://qiskit.org/textbook/ch-algorithms/superdense-coding.html) algorithm, showing the influence of errors in the transmitted message.

The diagrams of quantum circuits were drawn using the latex package [``quantikz``](https://ctan.org/pkg/quantikz) written by Alastair Kay [arXiv:1809.03842](https://arxiv.org/abs/1809.03842) v.4 (2020)

[^bb]: Barenco, A., Bennett, C. H., DiVincenzo, D., Margolus, N., Shor, P. Sleator, T., Simolin, J., and Weinfurter, H., *Elementary gaters for quantum computation,* Phys. Rev. A **52**, 3457 (1995) [.pdf]({static}/pdfs/Barenco-1995.pdf)
