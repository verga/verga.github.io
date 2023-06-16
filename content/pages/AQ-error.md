Title: Quantum error correction
Slug: AQ-error
Date: 2021-06-08
Category: Lectures
Tags: teaching, advanced quantum mechanics
Authors: Alberto Verga
Summary: Error correction, stabilizer codes
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

# Error Correction

We know from the theory of open systems that the interaction with the environment destroys the intrinsic coherence of the unitary evolution. In terms of quantum information the modification of the state of a qubit due to different forms of decoherence, and not to the normal operation of the unitary gates, defines an *error*. Protecting the quantum channels from the effects of noise is the goal of error correction codes. For instance, we may consider an imperfect channel that introduces a qubit flip with probability $p$, leading to the mixed state
$$\mathcal{E_f}(\ket{\psi}\bra{\psi}) = (1-p)\ket{\psi}\bra{\psi} + p X \ket{\psi}\bra{\psi} X \,,$$
from an arbitrary initial one qubit state $\ket{\psi}$. Schematically,

> <img src="{static}/images/AQ-ec_1.svg" alt="error flip" style="width: 150px;"/>

The flip error is related to the kraus operator $M = \sqrt{p} X$; therefore, if the initial state is $\ket{\psi}$, the channel output is $\rho$ and the flip error probability is
$$p_f = 1 - \braket{\psi| \rho | \psi} = \alpha p, \quad \alpha = 1-\braket{\psi|X|\psi}^2$$
is proportional to $p$. An error correction code is a strategy to reduce the error probability, and ideally, to detect and correct the errors.

The idea of quantum correction codes is to use entanglement of the information carrying qubits (the message) with supplementary qubits, and to use a set of local operators whose action on the total space vectors, allow the identification of the modified qubits, without altering the original message subspace.

As an example, to correct errors due to spin flips, we start by creating the entangled state:
$$(a \ket{0} + b \ket{1}) \otimes \ket{0} \otimes \ket{0} \rightarrow \ket{i_L} = a \ket{000} + b \ket{111}$$
using the circuit

> <img src="{static}/images/AQ-ec_2.svg" alt="error flip GHZ" style="width: 200px;"/>

where $\ket{\psi} = a \ket{0} + b \ket{1}$ is the "message" state, and $\ket{i_L} \in \mathcal{H}_L$ is then the *logical* input state, and $\mathcal{H}_L$ the logical hilbert space.[^l] In the input state $\ket{i_L}$ the message qubit states $\ket{0}$ and $\ket{1}$ are encoded using the logical qubits:
$$\ket{0_L} = \ket{000},\quad \ket{1_L} = \ket{111}\,,$$
which encodes each original qubit into three qubits. This redundancy allows the reduction of the error probability (see exercise), as in the classical error correction codes using majority voting. The qubits building the logical states are the physical qubits processed in the computer. The set $\{\ket{0_L}, \ket{1_L}\}$ is our first example of a quantum code space.

Flipping one qubit of the encoded state $\ket{i_L}$, can lead to one of the following three output states:
$$\ket{i_L} \rightarrow \ket{o_1} = a\ket{100} + b \ket{011}$$
if it is the qubit the one that is reversed,
$$\ket{i_L} \rightarrow \ket{o_2} = a\ket{010} + b \ket{101}$$
if qubit two is reversed, and
$$\ket{i_L} \rightarrow \ket{o_3} = a\ket{001} + b \ket{110}$$
if it is qubit three. Therefore, considering that it is also possible that no qubit at all is reversed, we have four different output states. A method to identify these four possibilities form the information contained in the logical state, is to apply successively the operators
$$Z_1 Z_2 = Z \otimes Z \otimes 1_2$$
and
$$Z_2 Z_3 = 1_2 \otimes Z \otimes Z$$
to the output state and to record the eigenvalue:

<blockquote>
<table class="table table-striped" style="width: 300px">
<thead class="thead-dark">
<caption> Error correction code </caption>
<tr>
<th>State</th>
<th>\(Z_1 Z_2\)</th>
<th>\(Z_2 Z_3\)</th>
<th>Apply</th>
</tr>
</thead>
<tbody>
<tr>
<td>\(\ket{i}\)</td>
<td>\(+\)</td>
<td>\(+\)</td>
<td>\(1_2\)</td>
</tr>
<tr>
<td>\(\ket{o_1}\)</td>
<td>\(-\)</td>
<td>\(+\)</td>
<td>\(X_1\)</td>
</tr>
<tr>
<td>\(\ket{o_2}\)</td>
<td>\(-\)</td>
<td>\(-\)</td>
<td>\(X_2\)</td>
</tr>
<tr>
<td>\(\ket{o_3}\)</td>
<td>\(+\)</td>
<td>\(-\)</td>
<td>\(X_3\)</td>
</tr>
</tbody>
</table>
</blockquote>

We observe that the operators $ZZ$ check the parity of the encoded states. The set of their eigenvalues, when applied to the faulty states, is called the error *syndrome*. In order to detect the $\pm 1$ eigenvalues of the $ZZ$ gates, we may use the circuit of [Ex. 1]({filename}AQ-circuit.md), in the circuits lecture, in which the ancilla controlled unitary operator, put in between two hadamard gates, has precisely eigenvalues $\pm 1$. A complete implementation of the error correcting code is given by the circuit:

> <img src="{static}/images/AQ-ec_3.svg" alt="ZZ circuit" style="width: 450px;"/>

We distinguish three steps to achieve error correction: (i) a preparation step in which the initial state is encoded, followed by (ii) the syndrome step in which a set of gates is used to detect the errors, and (iii) a final *correction* step. The correction step may use information provided by the measurement of the ancilla qubits (syndrome measurement), or might be implemented by a set of unitary multi-controlled cnot gates to obtain a self-correction algorithm.

An interesting observation is that applying the two operators $Z_1Z_2$ and $Z_2Z_3$, to the basis vectors of the extended $\mathcal{H}^{\otimes 3}$ hilbert space, we find that the set
$\{\ket{000}, \ket{111}\}$ remains unchanged; this invariant set is the *quantum code* to correct spin flip errors.

If instead of a spin flip, the error was a phase flip:
$$\ket{\psi} = a \ket{0} + b \ket{0} \rightarrow a \ket{0} - b \ket{0}\,, $$
we may use an analogous strategy to encode $\ket{\psi}$ into a state $\ket{i_L}$,
$$\ket{\psi} \rightarrow \ket{i_L} = a \ket{0_L} + b \ket{1_L}$$
using the quantum code:
$$\ket{0_L} = \ket{+++}, \quad \ket{q_L} = \ket{---}\,,$$
where $\ket{\pm}$ are, as usual, the eigenvectors of $X$. The idea behind this encoding is that the phase error is related to a $Z$ kraus operator, instead of the flip $X$, and the transformation:
$$Z = HXH$$
transform then a flip into a phase error; as a consequence we also transform the basis vectors:
$$\ket{+} = H \ket{0}, \quad \ket{-} = H \ket{1}\,.$$

In 1995 Shor demonstrated that the code:[^sh]
\begin{align*}
  \ket{0} & \rightarrow \ket{0_L} = \frac{1}{8^{1/2}} \big( \ket{000} + \ket{111} \big)^{\otimes 3}\,, \\
  \ket{1} & \rightarrow \ket{1_L} = \frac{1}{8^{1/2}} \big( \ket{000} - \ket{111} \big)^{\otimes 3}\,,
\end{align*}
allows the correction of any one qubit error. If more than one qubit is modified the redundancy leads to a probability of error which is the product $O(p^2)$ of one error probabilities.

In summary, we showed a procedure to encode a message qubit into a logical qubit in an extended hilbert space, allowing an arbitrary state $\ket{\psi}$ 
$$\ket{\psi} \rightarrow \ket{i_L}\,,$$
to be manipulated through its logical counterpart $\ket{i_L}$, in such a way that the errors $\mathcal{E}(\ket{i_L})$ (the noisy channel), can eventually be corrected. A *quantum code* is then a well chosen subspace of the expanded hilbert space, such that its vectors are not affected by the errors, implying that the information encoded within this subspace can be recovered even after being corrupted by a specific set of discrete errors.

### Error correction conditions

We saw that the spin flip error was related with the $X$ kraus operator; similarly, the phase flip error is related with the $Z$ pauli matrix, and the more general depolarizing error, which combines flips, phase and amplitude changes, is related with the set of kraus operators:
$$M_0 = \sqrt{1-p} 1_2, \; M_1 = \sqrt{\frac{p}{3}} X, \; M_2 = \sqrt{\frac{p}{3}} Y, \; M_3 = \sqrt{\frac{p}{3}} Z\,.$$
Generally, errors $E$ on a one qubit channel can be expressed in the pauli matrices basis:
$$E \in \{1_2, X, Y , Z\}$$
the pauli group (we may add the constants $\{\pm1, \pm\I\}$ to close the products); this is a simple consequence of the fact that any operation on twodimensional hilbert vectors can be decomposed as a linear combination of this set.

A general error operator $E_n$, in a $N$ dimensional space, is a tensor product of pauli matrices (including the identity) acting on the set of $N$ qubits. Therefore, a schematic way to write the action of the environment is,
$$\ket{\psi} \ket{e} \rightarrow \sum_n E_n \ket{\psi} \ket{e_n} \,,$$
where $\ket{e}$ refers to the initial environment state, $\ket{e_n}$ are the environment related states; the sum spans the set of possible errors.

Then an error $n$ transforms $\ket{\psi}$ into $E_n\ket{\psi}$; correction of this error consists in transforming back $E_n\ket{\psi}$ into $\ket{\psi}$, which amounts at correcting $X$, $Z$ and $XZ$ type errors: the linear nature of quantum states leads to the fact that correcting spin and phase errors will correct all errors (even such for which the mixed state is subject to nonunitary relaxation).

A quantum code $\mathcal{C} = \{\ket{i_L}, i = 0,1,\ldots\}$ allows correction of a set $\{E_1, E_2, \ldots\}$ of errors if the code words $\ket{i_L}, \ket{j_L} \in \mathcal{C}$ satisfy,
$$\braket{i_L | E_1E_2 | j_L} = 0$$
and
$$\braket{i_L | E_1E_2 | i_L} = \braket{j_L | E_1E_2 | j_L}\,.$$
The first condition ensures discrimination between errors: the overlap of two errors over two different code words vanishes; the second condition says that the overlap of two errors on each word is independent on the code word. Then, even if two erroneous versions $E_1\ket{i_L}$ and $E_2\ket{i_L}$ of the same word may overlap, as long as this overlap is the same for all code words, the code can correct the set of errors.

Let us denote $R$ the recovery procedure:
$$R\ket{a_1}E_1\ket{i_L} = \ket{A_1}\ket{i_L}$$
where $\ket{a}$ and $\ket{A}$ are the initial and final ancilla states; $R$ is a unitary operator acting on the whole code space, including the message, noise and ancilla systems. We have, $R\ket{a_2}E_2\ket{j_L} = \ket{A_2}\ket{j_L}$
$$\bra{i_L} E_1 \braket{a_1|R^\dagger R|a_2} E_2 \ket{j_L} = \braket{A_1|A_2} \braket{i_L|j_L} = 0$$
and also
$$\bra{i_L} E_1 \braket{a_1|R^\dagger R|a_2} E_2 \ket{j_L} = \bra{i_L} E_1 E_2 \ket{j_L}\,,$$
(for the case $\braket{a_1|a_2} = \braket{a|a} = 1$, which must be included as a possible recovery case) leading to the first condition. Similarly, the second condition results from,
$$\bra{i_L} E_1 \braket{a|R^\dagger R|a} E_2 \ket{i_L} = \bra{i_L} E_1 E_2 \ket{i_L} = \braket{A_1|A_2}\,,$$
which is independent of $\ket{i_L}$, thus, we can replace $\ket{i_L}$ by another $\ket{j_L}$, everywhere. 

### The stabilizer code

A stabilizer is an operator such that, when applied to a given state $\ket{\psi}$ in the logical hilbert space $\mathcal{H}_L$, leaves the state invariant
$$g \ket{\psi} = \ket{\psi}\,,$$
$\ket{\psi}$ is then an eigenvector of $g$ with eigenvalue 1. We observe that two such operators $g_1, g_2$:
$$g_1 \ket{\psi} = \ket{\psi} \,, \quad g_2 \ket{\psi} = \ket{\psi}\,,$$
commute $g_1 g_2 = g_2 g_1$, and their product $g = g_1 g_2$ is also a stabilizer. Therefore, we can define the generators set
\begin{align*}
  \mathcal{S} & = \braket{g_1, g_2, \ldots} \\
  & = \{g_n \mid g_n \ket{\psi} = \ket{\psi}, \, [g_n, g_m] = 0, \forall (n,m)\}
\end{align*}
of the stabilizer group $\mathcal{S}$. The important point is that $\mathcal{S}$ defines a set of states $\ket{i_L}$, the code states, as the invariant set under the action of the given $g_n$. Therefore, instead of using the code states, which depend on $2^N$ parameters for $N$ qubits, we use the generators of the stabilizer group, whose size is essentially of the order of $N$.

More precisely, we define $\mathcal{L}$, the code space, as a subset of the logical hilbert space $\mathcal{L} \subset \mathcal{H}_L$ such that:
$$\mathcal{L} = \{\ket{i_L} \in \mathcal{H}_L \mid g_n \ket{i_L} = \ket{i_L}, \; \forall n\}\,.$$
Error correction using the stabilizers results form the fact that, either the error operator $E$ commutes with the stabilizer
$$g E = E g $$
or it anti-commutes
$$g E = - E g\,.$$
Remember that pauli matrices commute or anti-commute, e.g. $X_1X_2 - X_2X_1 = 0$, $X_1Z_1 + Z_1X_1 = 0$). Correcting an error reduces then to the detection of the eigenvalue $\pm 1$, as we found in the case of the spin flip example:
$$g_n E \ket{\psi} = \pm E g_n \ket{\psi} = \pm E \ket{\psi}\,.$$
If the error is in the set of stabilizers, its eigenvalue is $+1$, correction is the identity, since these errors do not change the logical basis. If instead, the eigenvalue is $-1$, we may identify the error through the measurement of the generator $g_n$, the observables in the stabilizer space. In the case of the spin flip code, measurement of $Z_1Z_2$ and $Z_2Z_3$, gave us the necessary information to apply $X$ to the correct qubit.

More specifically, consider a message space of $K$ dimensions and a code space of $N>K$ dimensions. A set of independent observables $g$ of dimension $N-K$ should be enough to detect the errors (syndrome extraction). Using the formalism of the previous section, we note that a noisy state has the form:
$$\ket{0_A} \sum_n E_n \ket{i_L} \ket{e_n}$$
(the first term corresponds to the ancillary space, of dimension $N-K$). To extract the eigenvalue associated to the generator $g_n$, we may follow the steps (see the circuit above):

* put the ancilla in the $\ket{+}$ state by applying the hadamard gate $H$,
* use the ancilla qubit to control the action of the stabilizer $g_n$ on the logical space,
* apply the hadamard gate to the ancilla to put it in the state:
    $$\frac{1+s_n}{2}\ket{0} + \frac{1-s_n}{2}\ket{1} = \ket{b_n} \,, \; b_n = \frac{1 \pm 1}{2} \,,$$
    where $s_n$ is the eigenvalue of $g_n$.

The string of $N-K$ bits $b_n = 0, 1$ allows the syndrome extraction,
$$\ket{0_A} \sum_n E_n \ket{i_L} \ket{e_n} \rightarrow \sum_n \ket{b_n} \big(E_n \ket{i_L}\big) \ket{e_n} \rightarrow \big(E_\bar{n} \ket{i_L}\big) \ket{e_\bar{n}}\,,$$
where the first step is the syndrome extraction procedure, and the second the ancilla measurement projecting the message state to the corresponding error $E_\bar{n} \ket{i_L}$ state. Note that this projected state is disentangled, applying the operator $E^\dagger_\bar{n}$ to it we recover the original state $\ket{i_L}$ (or any superposition of logical states).

### The Steane code[^st]

Quantum codes are labeled by the number of qubits $N$ in the code words, the number of original qubits $K < N$, and the minimal hamming distance between two code words $d$: $[\![N,K,d]\!]$. The hamming distance between two binary strings of length $N$ is the number of different bits ($d(01101,01001) = 1$), the weight of a string $b$ is its number of ones $\mathrm{wt}(b) = d(0,b)$; note that $d(b_1,b_2) = \mathrm{wt}(b_1 + b_2)$, where the addition is in $\mathbb{Z}_2$.

The Steane code $[\![7,1,3]\!]$, derived from the classical [hamming](https://en.wikipedia.org/wiki/Hamming(7,4)) $(7,4,3)$ code, encodes one qubit $K=1$ into seven $N=7$, and can correct any one qubit error $t = (d-1)/2 = 1$; its two logical words are:
\begin{multline*}
\ket{0_L} = \frac{1}{8^{1/2}}\big( \ket{0000000} + \ket{1010101} + \ket{0110011} + \ket{1100110} + \\
\ket{0001111} + \ket{1011010} + \ket{0111100} + \ket{1101001}
\end{multline*}
and
$$\ket{1_L} = X_1X_2X_3X_4X_5X_6X_7 \ket{0_L}\,.$$
The total dimension of the logical hilbert space is $2^7$; the seven qubits might be subject to individual errors,
$$E \in \{X_1,\ldots,X_7,Z_1,\ldots,Z_7,X_1Z_1,\ldots,X_7Z_7\}\,.$$
However, only the two logical codewords are important, because their superposition carries the message information (that depends on only two amplitudes $\ket{\psi} = a \ket{0} + b \ket{1} \rightarrow \ket{i_L} = a \ket{0_L} + b \ket{1_L} \in \mathcal{H}_L$). This means that we can shrink the number of relevant states, and this can be accomplished by using a set of six stabilizers of the logical qubits:
\begin{array}{lll}
g_1 = 111XXXX, & g_2 = X1X1X1X, & g_3 = 1XX11XX, \\
g_4 = 111ZZZZ, & g_5 = Z1Z1Z1Z, & g_6 = 1ZZ11ZZ,
\end{array}
the number of code words is found observing that $2^{7-6}=2$, which corresponds to the dimension of the invariant subset of $2^7$ states under the action of $\mathcal{S} = \braket{g_1,\ldots,g_6}$. Remark that since any two stabilizers commute, they divide the $2^7$ hilbert space into $2^6$ subspaces of dimension 2. In general, the number of stabilizers is such that $N-|\mathcal{S}| = K$, the number of encoded qubits (or the number of original qubits). Note that the operator $\bar{X} = XXXXXXX$ exchange the two logical states:
$$\bar{X} \ket{0_L} = \ket{1_L}$$
and $\bar{Z} = ZZZZZZZ$, distinguishes between these two states by their phase:
$$\bar{Z} \ket{0_L} = \ket{0_L}, \; \bar{Z} \ket{1_L} = - \ket{1_L}\,.$$

The encoding of the logical states is:
$$\ket{0_L} = \frac{1}{8^{1/2}} (1 + g_1)(1 + g_2)(1 + g_3) \ket{0}^{\otimes 7}$$
The circuit for error syndrome is:
$$H_A \prod_{n=1}^6 \Lambda_n(g_n) H_A$$
where we introduced the notations $H_A$ for the hadamard gates applied to the 6 ancilla qubits,
$$H_A = H^{\otimes 6} \otimes 1_7\,,$$
and the controlled gate operator $O$ with control $n$ and target the logical space, 
$$\Lambda_n(O) \ket{b} \ket{i_L} = \ket{b_1 \ldots b_6} O^{b_n}\ket{i_L}\,,$$
where $\ket{b}$ is an ancilla basis state $b = b_1 \ldots b_6$, $b_n = 0, 1$. The measurement of the ancilla space identifies the error for subsequent correction.

## Exercises

1. Apply the flip channel $\mathcal{E_f}$, conveniently generalized to 3 qubits, to the $\ket{i} = a \ket{0_L} + b \ket{1_L})$. The resulting state $\rho$ contains 8 terms corresponding to the 8 flips. Perform a projective measurement $\sigma_m = P_m \rho P_m$ ($m=0,1,2,3$), with,
    $$P_0 = \ket{000} \bra{000} + \ket{111} \bra{111},\; P_1 = X_1 P_0 X_1,\;P_2 = X_2 P_0 X_2,\; P_3 = X_3 P_0 X_3,$$
    where each $X_n$ applies to the $n=1,2,3$ qubit, respectively; note that $\sigma_m$ is not normalized; thus, its trace gives the corresponding probability. What is the meaning of $P_m$? Calculate the (non normalized) state:
    $$\bar{\sigma} = \sigma_0 + X_1 \sigma_1 X_1 + X_2 \sigma_2 X_2 + X_3 \sigma_3 X_3$$
    and compute the error probability (which is the sum of probabilities for the four cases, just contained in $\bar{\sigma}$)
    $$p_f = 1 - \braket{i| \bar{\sigma} | i}$$
    and show that it is
    $$p_f = p^2 (3-2p)(1 - \braket{i | X_1 X_2 X_3 | i}^2\,.$$
    Therefore we reduced the flip error in the final state to second order in $p$.

    Remark. The generalization of the one qubit channel $\mathcal{E}$ to $N$ qubits is $\mathcal{E}^{\otimes N}$. The matrices $X_1,X_2,X_3$ commute.

    Hint. The density matrix reads,
    $$\rho = (1-p)^3 \ket{i}\bra{i} + (1-p)^2p ( X_1\ket{i}\bra{i} X_1 + X_2 \ket{i}\bra{i} X_2 + X_3 \ket{i}\bra{i} X_3) + \ldots$$
    The projected states are of the form,  
    \begin{align*}\sigma_0 &= (1-p)^3 \ket{i}\bra{i} + p^3 X_1 X_2 X_3 \ket{i}\bra{i} X_1 X_2 X_3 \\ \sigma_1 &= (1-p)^2p X_1 \ket{i}\bra{i} X_1 + (1-p)p^2 X_2 X_3 \ket{i}\bra{i} X_2 X_3 \\ \text{etc.} \end{align*}

2. Replace the measurement of the ancilla qubits in the circuit correcting one flip errors by a unitary operation in order to obtain a self-correcting algorithm. The idea is to insert two controlled cnot gates and a multi-controlled cnot.

3. Show that the set,
    \begin{multline*}
    \{Z_1Z_2,\, Z_2Z_3,\, Z_4Z_5,\, Z_5Z_6,\, Z_7Z_8,\, Z_8Z_9, \\
    X_1X_2X_3X_4X_5X_6X_7,\, X_4X_5X_6X_7X_8X_9\}
    \end{multline*}
    stabilizes the Shor code.

4. Find the equivalent of the pauli and cnot gates acting on the Steane logical states $\ket{0_L}$ and $\ket{1_L}$. For example, $X \rightarrow \bar{X} = X^{\otimes 7}$, since $\bar{X} \ket{0_L} = \ket{1_L}$. For the cnot case, consider two logical (seven qubit) states $\ket{0_L}$ and $\ket{1_L}$. Give your answer in the form of a circuit.


## Notes

[^l]: Sometimes the original, uncoded, qubits are called "logical", and the encoded qubits "physical"; we adopt here the convention that the unecoded qubits are the "message" or "original" ones, while the labelled "$L$" states are the "encoded" or "logical" qubits. Note however that the number of encoded qubits corresponds to the number of original ones, generally denoted by $K$. We denote $N$ the dimension of the encoded qubits.

[^sh]: Shor, P. A., *Scheme for reducing decoherence in quantum computer memory,* Phys. Rev. A **52**, R2493 (1995)

[^st]: Steane, A. M., *A Tutorial on Quantum Error Correction,* (Proceedings of the International School of Physics "Enrico Fermi", 2006) [.pdf]({static}/pdfs/Steane-2006.pdf)
