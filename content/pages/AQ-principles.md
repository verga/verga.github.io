Title: Quantum principles
Slug: AQ-principles
Date: 2020-09-20
Category: Lectures
Tags: teaching, advanced quantum mechanics
Authors: Alberto Verga
Summary: Generalized quantum principles for mixed states; density matrix, measurement.
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

# Principles of quantum mechanics

The basic postulates of quantum mechanics set the concepts of a quantum system, its state and evolution, and define the nature of observables.

* The *state space* of a, possibly composite, quantum system is a vectorial space over complex numbers, the hilbert space $\mathcal{H}$. The *state* of a general, possibly mixed, quantum system is given by its *density operator* $\rho$:
    $$\rho = \sum_n p_n \ket{\psi_n} \bra{\psi_n}$$
    where $\ket{\psi_n} \in \mathcal{H}_n$ and $p_n \in [0,1]$ satisfying
    $$\sum_n p_n = 1\,.$$
    Each $n$ can be interpreted in two equivalent ways: (i) as a member of a composite quantum system; (ii) as a subsystem of a larger system, the whole system being in a *pure* state 
    $$\ket{\psi} \in \mathcal{H} = \bigotimes_n \mathcal{H}_n\,.$$
    A state which is not pure, is *mixed*. The hilbert state of an ensemble is then the kronecker product of the hilbert spaces of its elements.

* Physical quantities are hermitian operators over the system's hilbert space. Examples are the position and momentum of an oscillator, the total angular momentum of an atom or the spin of the electron; they are usually called *observables*. The spectrum $o_n$ of a hermitian operator $O$ is real and its eigenvectors form an orthonormal basis of the hilbert space:
    $$O \ket{o_n} = o_n \ket{o_n}, \quad \braket{o_n|o_m} = \delta_{nm}\,.$$
    The expected value of an observable of a system in state $\rho$ is,
    $$\braket{O} = \Tr O \rho\,,$$
    which reduces to $\braket{O} = \braket{\psi|O|\psi}$ in the case of a pure state $\ket{\psi}$.

* The evolution of the quantum state is *unitary*
    $$\rho(t) = U(t,t_0) \rho(t_0) U^\dagger(t,t_0) \,;$$
    the unitary operator $U(t,t_0)$ evolves the system from time $t_0$ to $t$. In the case that the quantum system is described by a hamiltonian $H$, independent of time,
    $$U(t) = \E^{-\I H t}\,.$$
    In this case the quantum state satisfies the Schrödinger equation:
    $$\I \frac{\partial }{\partial t} \rho = [H,\rho],.$$

This basic principles are complemented with an empirical theory of the *measurement*. In addition, for systems of identical particles, one distinguishes bosons and fermions according to the symmetry of the quantum state under particle permutations: fermion states are completely antisymmetric; boson states are completely symmetric.


## Measurement

In the case of a quantum system in a pure state we have the usual Born rule:

* A projective or *orthogonal measurement* of a system in a quantum state $\ket{\psi}$, is the projection $P_n$ into an eigenstate $o_n$ of the observable $O$:
    $$P_n \ket{\psi} = \psi_n\ket{o_n}\,,$$
    where $\psi_n$ is the complex amplitude corresponding to the state $o_n$. It is important to note that the projected "state" resulting is not normalized (obviously $P$ is not unitary). A projection operator satisfies $P^2 = P$; its eigenvalues are then $0$ or $1$. The result of the projective measurement is the eigenvalue $o_n$ with probability (Born rule):
    $$p(o_n) = p_n = \braket{\psi|P_n|\psi} = |\braket{o_n|\psi}|^2 = |\psi_n|^2\,.$$
    The post-measurement state ("collapse") becomes,
    $$\ket{\psi} \rightarrow \frac{P_n\ket{\psi}}{\braket{\psi|P_n|\psi}} = \ket{o_n}\,.$$

This rule generalizes trivially to mixed states: the probability to measure the property $n$ in the state $\rho$ is simply,
$$p_n = \Tr P_n\rho \,,$$
and the quantum state becomes, after the measurement,
$$\rho_n = \frac{P_n \rho P_n}{\Tr P_n \rho}\,,$$
if the outcome is $o_n$. The measurement action itself changes the state into:
$$\rho \rightarrow \rho_M = \sum_n p_n \rho_n = \sum_n P_n \rho P_n\,.$$

More generally, we consider a measurement to be the result of the interaction of the system of interest with an apparatus. The total hilbert space is then the product of the system's space and an "ancilla" space which is spanned by the measuring basis. This is essentially the von Neumann model of the measurement *process*.[^p] A "measurement" $M$ can then be made via a unitary operator $U_M$ which acts on a product space $\mathcal{H}_S \otimes \mathcal{H}_A$ of the system $S$ and an ancilla space $A$ spanned by the set $\ket{n}$, which is in one to one correspondence with the set of the possible measurement outcomes $\ket{o_n}$. Therefore, the measurement consists in the action:
$$U_M\ket{\psi} \otimes \ket{0} = \sum_n M_n \ket{\psi} \otimes \ket{n}\,,$$
here $\ket{\psi}$ is the state of $S$ and $\ket{0}$ is a fixed state of $A$. The system state after selection of the outcome, say $\ket{m}$ for some $n=m$, transforms into the post-measurement state:
$$\ket{\psi} \rightarrow \ket{\psi}_M =  \frac{M_m \ket{\psi}}{\braket{\psi | M^\dagger_m M_m | \psi}}\,.$$
In addition, unitarity of $U_M$ implies that the set of operators $M_n$ is complete:
$$\sum_n M_n^\dagger M_n = \sum_n E_n = 1$$
where 1 is here the identity operator; $M_n$ are called Kraus operators, and the set of *positive* operators $E_n = M_n^\dagger M_n$ form a complete set that generalizes the set of projectors $P_n$ of the orthogonal measure.

Previous to the selection, if initially the system's state was $\rho$, the interaction with the apparatus leaves the system in a mixed state:
$$\rho_M = \sum_n M_n \rho M_n^\dagger\,;$$
after selection, the outcome $n$ of the measurement is the state
$$\rho_n = \frac{M_n \rho M_n^\dagger}{\Tr M_n \rho M_n^\dagger}\,,$$
which generalizes the projective measurement to the case of a set of measurement operators $M_n$.

Let us illustrate the measurement process through a unitary transformation. We consider an initial state $\ket{\psi} = a \ket{0} + b \ket{1}$, with $|a|^2 + |b|^2 = 1$, and complement it with an ancilla state:
$$\ket{\mathrm{in}} = \ket{\psi} \otimes \ket{0},$$
We also introduce a unitary operator $Z$
$$Z = \mathrm{diag}(1, -1)$$
with eigenvalues $\pm1$ (it is both unitary and hermitian, then it also is an observable). Instead of applying a projector, as for example $\ket{0}\bra{0}\ket{\psi}$ to obtain, with probability $p(1)=|a|^2$, the eigenvalue 1 state $\ket{0}$, we will use a controlled version of the $Z$ operator:
$$U_M = \mathrm{ctrl}Z: \begin{cases}\ket{00}  \rightarrow & \ket{00}\\ 
\ket{01} \rightarrow & \ket{01}\\ \ket{10} \rightarrow & \ket{10}\\ \ket{11} \rightarrow & -\ket{11} 
\end{cases} \,.$$
The first step ($s_1$), in the measurement protocol, is to apply the operator $H$ defined by
$$H: \begin{cases} \ket{0} \rightarrow \frac{\ket{0} + \ket{1}}{\sqrt{2}} \\  \ket{1} \rightarrow \frac{\ket{0} - \ket{1}}{\sqrt{2}}  \end{cases}\,,$$ 
which transform a vector of the twodimensional ancilla basis into a superposition, to the ancilla state $\ket{0}$:
$$\ket{\mathrm{in}} \rightarrow \ket{s_1} = 1\otimes H \ket{\psi}\otimes\ket{0}$$
In the second step $s_2$, we apply $U_M$
$$\ket{s_1} \rightarrow \ket{s_2} = \mathrm{ctrl}Z \ket{s_1},$$
and then third, $s_3$, we apply $1\otimes H$ again:
$$\ket{s_2} \rightarrow \ket{s_3} = 1\otimes H \ket{\psi}\otimes\ket{0}.$$
We finally get <strong style="color:DarkSlateBlue; background-color:LightGray;">EX</strong>:
$$\ket{s_3} = \ket{\mathrm{out}} = (a \ket{0}) \otimes \ket{0} + (b \ket{1}) \otimes \ket{1} \,. $$
Therefore, a projective measurement of the ancilla gives us a post-measurement output state $\ket{0}$ with probability $|a|^2$, or $\ket{1}$ with probability $|b|^2$. As we will study later, the output state is an *entangled* state; its entanglement allows the measurement protocole using a unitary operator.

In summary, for a pure or mixed system in state $\rho$, a quantum measurement is realized with the aid of a Kraus operator $M_n$, which measures property $n$ with probability,
$$p_n = \Tr M_n \rho M_n^\dagger = \Tr E_n \rho\,.$$
The measurement modifies the state into,
$$\rho_M = \sum_n M_n \rho M_n^\dagger\,,$$
and the post-measurement state is,
$$\rho_n = \frac{M_n \rho M_n^\dagger}{\Tr E_n \rho}\,,$$
therefore, one may say that the Kraus operators $M_n$ are the generators of the post-measurement state, they are sometimes called the detection operators. In the quantum information literature the complete set $E_n$ is called a *positive operator valued measure* or POVM.

### Ideal measurement, Cini model

One interesting and thorough example of non-intrusive measurement is the Cini[^c] model: a two state system $\sigma_z = Z$ ($S$, up and down) is in contact with an apparatus ($A$) consisting in a set of $N$ bosons (eventually macroscopic) that can occupy a ground state $0$ or an excited one $1$ (see figure).

<img src="{static}/images/AQ-cini.svg" alt="cini model" style="width: 250px;"/>
>
> A two level system $S$ (atom) is put in interaction with an apparatus $A$ (ancilla space) consisting in $N$ bosons that can be in two states $0$ and $1$. The interaction is tuned in such a way that the population of the excited level depends on the amplitude of the up atom state.

The interaction hamiltonian is,
$$H_{SA} = \frac{J}{2\sqrt{N}} (1 + Z) (a^\dagger_0 a_1 + a_0 a^\dagger_1)\,,$$
where $J$ is the coupling constant and $a^\dagger_s,a_s$ are creation and annihilations operators of the states $s = 0,1$, they satisfy the usual boson commutation relations,
$$[a_s,a^\dagger_s] = 1, \quad [a_0,a_1] = [a_0^\dagger,a_1^\dagger] = 0\,.$$
Note that in the $S$ down state the interaction energy vanishes and is proportional to $J$ in the up state. Therefore, the apparatus can distinguishes between the up and down states, which is precisely the goal a measuring device. An ancilla state depends on the number $n$ of bosons in the ground state:
$$\ket{n, N-n} = \frac{(a^\dagger_0)^n (a^\dagger_1)^{N-n} }{\sqrt{n!(N-n)!}}\ket{00}\,.$$
The energy associated to the excitation of one mode is given by the matrix element,
$$\bra{N,0}\braket{\uparrow|H_{SA}|\uparrow}\ket{N-1,1} = J\,,$$
which justifies the $\sqrt{N}$ factor in the definition of the coupling interaction; indeed, using the uncertainty energy relation we obtain that the one mode excitation time is $\tau \sim 1/J$, independent of $N$, as it should.

We compute now the evolution of the initial product state,
$$\ket{\psi(0)} = \big(c_\uparrow \ket{\uparrow} + c_\downarrow \ket{\downarrow}\big) \ket{N0}$$
in which the system is in an arbitrary superposition and the apparatus in its ground state. After a time $t$ the state evolves to <strong style="color:DarkSlateBlue; background-color:LightGray;">EX</strong>:[^cini]
$$\ket{\psi(t)} = c_\uparrow \ket{\uparrow} \sum_{n=0}^N A_n(t) \ket{n\,N-n} + c_\downarrow \ket{\downarrow}\ket{N0}\,,$$
where
$$A_n(t) = \frac{\I^{N-n} \sqrt{N!}}{\sqrt{n!(N-n)!}} \cos^n \frac{Jt}{\sqrt{N}} \sin^{N-n} \frac{Jt}{\sqrt{N}} \,.$$
The probability $P_n = |A_n|^2$ of finding $n$ bosons in the ground state is,
$$P_n = \binom{N}{n} p(t)^n q(t)^{N-n}\,,$$
where
$$p_n(t) = \cos^2 \frac{Jt}{\sqrt{N}}, \quad q_n(t) = \sin^2 \frac{Jt}{\sqrt{N}}\,.$$
The binomial distribution is strongly concentrated around its maximum: for large $N$ its approaches a gaussian distribution ([de Moivre-Laplace](https://en.wikipedia.org/wiki/De_Moivre-Laplace_theorem) theorem). Therefore, at some time, when $n(t) = N p(t) = \braket{n}$, one finds
$$P_\braket{n} = \binom{N}{\braket{n}} \left( \frac{\braket{n}}{N} \right)^\braket{n} \left( \frac{N - \braket{n}}{N} \right)^{N-\braket{n}} \sim \mathcal{N}(Np,Npq)\,,$$
or using the stirling formula <strong style="color:DarkSlateBlue; background-color:LightGray;">EX</strong>:
$$P_\bar{n} \approx 1\,.$$
Therefore, the contribution to the total probability of the states other than those near $n \approx \braket{n}$ is negligible. Initially $t=0$, $P_n(0)=\delta_{nN}$, and at $t^\star = (\pi/2) N^{1/2}/J$, the whole set of bosons is in the excited state
$$P_n(t^\star) = \delta_{n0},\; t^\star \sim \sqrt{N}\,,$$
which gives us an order of magnitude of the needed time to populate macroscopically the excited state. However, the time to correlate the system with apparatus is much smaller, of the order of $1/J$. As a consequence, for large $N$ the combined system state can be written as,
$$\ket{\psi(t)} = c_\uparrow \ket{\uparrow} \ket{\braket{n}(t), N - \braket{n}(t)} + c_\downarrow \ket{\downarrow} \ket{N,0}\,.$$
This state establishes a one to one correspondance between system and apparatus: an excited apparatus corresponds to the system in the up state, and the apparatus in the ground state corresponds to the system in the down state. Note that the final state is not a product state, as it would be in the case of collapse, it is entangled; however, the interference terms, which are proportional to the overlap,
$$\sum_n A_n \braket{n,N - n|N,0} \sim \braket{\braket{n}, N- \braket{n}|N,0}=0$$
are vanishingly small. We may see the measuring process as a way to amplify the microscopic state of the system, into a macroscopically distinguishable superposition of states.

### Exercises

1. Demonstrate the following properties of the density matrix

    * $\rho = \rho^\dagger$
    * $\Tr \rho =1$
    * $\rho$ is positive
    * $\Tr \rho^2 \le 1$

2. Consider a bipartite system $AB$ of two two level atoms, and the unitary operator:
    $$U: (a\ket{0} + b\ket{1})_A \otimes \ket{0} \, \rightarrow \, a\ket{0}_A \otimes \ket{0}_B + b \ket{1}_A \otimes \ket{1}_B$$
    Find a matrix representation of $U$. Calculate the probability $p_A(0)$ to find the atom $A$ in the ground state, using a measure of the second atom $B$.

    If the measure of the $B$ atom is made in the basis of $\sigma_x = X$, $\ket{\pm}$, what are the post-measurement states of $A$?

    Show that the operator $U$ can be also defined by the rule
    $$U: \ket{\psi}_A \otimes \ket{0}_B \,\rightarrow \, M_+ \ket{\psi}_A \otimes \ket{+}_B + M_- \ket{-} \ket{\psi}_A \otimes \ket{-}_B\,,$$
    where
    $$M_+ = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}\,,
      M_- = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}\,,$$
    Show that the set $M$ is complete. Compute $M_\pm^\dagger \ket{\psi}_A$ and compare with the post-measurement states obtained before. Calculate the norm of these two vectors $|M_\pm^\dagger\ket{\psi}_A|^2$ and compare the results with $p_A(\pm)$.


## Notes

A concise and useful book is,

* J. A. Bergou, and M. Hillery, *Introduction to the Theory of Quantum Information Processing* (Springer, 2013)

[^p]: J. Preskill, *Lecture notes on Quantum Information* (Caltech, 1997-) [web](http://theory.caltech.edu/~preskill/ph219/index.html)

[^c]: M. Cini, *Quantum theory of measurment without wave packet collapse*, Nuovo Cimento B **73**, 27 (1983) [.pdf]({static}/pdfs/Cini-1983yq.pdf)

[^cini]: Note that the bosonic part of the interaction hamiltonian,
$$H \sim a^\dagger_0 a_1 + a_0 a^\dagger_1$$
is diagonalized by the linear transformation (with unit jacobian, then preserving the commutation relations),
$$a_0 = \frac{b_0 - b_1}{\sqrt{2}}, \quad a_1 = \frac{b_0 + b_1}{\sqrt{2}}.$$
The new hamiltonian is
$$\bar{H} \sim b^\dagger_0 b_0 - b^\dagger_1 b_1\,.$$
Its eigenvalues are integers $\bar{n}$, and its eigenvectors are (it is enough to change $n$ by $\bar{n}$ in the expression of the harmonic oscillator eigenvectors):
$$\ket{\bar{n}, N - \bar{n}} = \frac{(b^\dagger_0)^\bar{n} (b^\dagger_1)^{N-\bar{n}}}{\sqrt{\bar{n}!(N-\bar{n})!}} \ket{0}$$
Now we want to express the old eigenvectors in terms of the new ones; the initial state reads,
\begin{align*}
\ket{N,0} &= \frac{(a^\dagger_0)^N}{\sqrt{N!}} \ket{0} \\
  &= \frac{1}{\sqrt{N!}} \frac{(b_0 - b^\dagger_1)^N}{\sqrt{2}} \ket{0} \\
  &= \frac{1}{2^{N/2} \sqrt{N!}} \sum_{\bar{n}} \binom{N}{\bar{n}} (-1)^{N-\bar{n}} (b^\dagger_0)^\bar{n} (b^\dagger_1)^{N-\bar{n}} \ket{0} \\
  &= \frac{1}{2^{N/2} \sqrt{N!}} \sum_{\bar{n}} \frac{N! (-1)^{N - \bar{n}}}{\bar{n}! (N - \bar{n})!} \sqrt{\bar{n}!} \sqrt{(N-\bar{n})!} \ket{\bar{n}, N - \bar{n}} \\
  &= \frac{1}{2^{N/2}} \sum_{\bar{n}} \frac{(-1)^{N-\bar{n}} \sqrt{N!}}{\sqrt{\bar{n}!} \sqrt{(N - \bar{n})!}} \ket{\bar{n}, N - \bar{n}}
\end{align*}

