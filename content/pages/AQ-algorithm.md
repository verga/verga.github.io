Title: Quantum algorithms
Slug: AQ-algorithm
Date: 2020-11-15
Category: Lectures
Tags: teaching, advanced quantum mechanics
Authors: Alberto Verga
Summary: Fourier transform and phase detection quantum algorithms, error correction
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

# Quantum Algorithms

## Fourier transform and phase estimation

The classical fourier transform has an inverse: applying the transform to a function and then applying its inverse, lead to the identity; the fact that the inverse is related to the complex conjugate of the direct transformation, naturally leads to the observation that the fourier transformation can be seen as a *unitary* operator. The quantum algorithm is simply an implementation of this unitary operator acting on a space of dimension $2^N$, as a circuit of one and two qubits gates.

Let us start with the fourier transform of the basis states. We denote a basis state of the $N$ qubits hilbert space,
$$\ket{s} \in \mathcal{H}^{\otimes N}$$
by the binary string
$$s = s_1 \ldots s_{N} = \sum_{n=1}^{N} s_n 2^{N-n},\; s_n = \{0,1\}\,.$$
Therefore,
$$\ket{s} = \frac{1}{\sqrt{2^N}} \sum_{k=0}^{2^N-1} \E^{2\pi \I s k/2^N} \ket{k}$$
is the fourier transform of $\ket{s}$. Knowing the transformation of the basis vector we can compute the transformation of any superposition. The basic idea is to transform the unitary operator, here defined a s *sum* over the basis vectors in fourier space $\ket{k}$, into a product. This can be achieved using the decomposition of $s$ and $k$ into its binary digits:
\begin{align*}
\ket{s} &= \frac{1}{\sqrt{2^N}} \sum_{k=0}^{2^N-1} \exp\left( 2\pi \I \frac{s k}{2^N} \right) \ket{k} \\
  & = \frac{1}{\sqrt{2^N}} \sum_{k_1=0,1} \ldots \sum_{k_{N}=0,1} \exp\left( 2\pi \I s \sum_{n=1}^{N} \frac{k_n}{2^n} \right) \ket{k_1 \ldots k_{N}} \\
  & = \frac{1}{\sqrt{2^N}} \sum_{k_1=0,1} \ldots \sum_{k_{N}=0,1} \bigotimes_{n=1}^{N} \exp\left( 2\pi \I \frac{k_n}{2^n} \right) \ket{k_n} \\
  & = \frac{1}{\sqrt{2^N}} \bigotimes_{n=1}^{N} \sum_{k_n=0,1} \exp\left( 2\pi \I \frac{k_n}{2^n} \right) \ket{k_n} \\
  & = \frac{1}{\sqrt{2^N}} \bigotimes_{n=1}^{N} \left[ \ket{0} + \exp\left( 2\pi \I \frac{s}{2^n} \right) \ket{1} \right]
\end{align*}
The exponent selects the fractional part of $s/2^n$ for $n=1,\ldots,N$:
$$\{s/2^n\} = 0.s_{N-n+1}\ldots s_N\,,$$
which allows the previous product to be written in the simple form,
$$\ket{s_1 \ldots s_N} = \frac{1}{2^{N/2}} \left(\ket{0} + \E^{2 \pi \I 0.s_N} \ket{1} \right) \otimes \ldots \otimes \left(\ket{0} + \E^{2 \pi \I 0.s_1 \ldots s_N} \ket{1} \right)\,.$$

Consider the last exponential, each term $s_n/2^n$ of the phase $2\pi 0.s_1\ldots s_N$,
$$0.s_1 \ldots s_N = \frac{s_1}{2} + \cdots + \frac{s_N}{2^N}$$
can be obtained by a rotation of an angle $2\pi/2^n$ if $s_n = 1$, otherwise it remains $0$; this operation can be implemented by the rotation matrix
$$R_n = \begin{pmatrix} 1 & 0 \\ 0 & \E^{2 \pi \I/ 2^n} \end{pmatrix}\,,$$
controlled by $s_n$ and applied to the first qubit state (initially $\ket{s_1}$). We observe that this term depends on the values of all qubits, leading to a decomposition in at least $N$ operators (one qubit or with one control qubit). The first decimal can be simply obtained from the initial $\ket{s_1}$ by the application of an hadamard gate
$$H \otimes^{N-1} 1_2 \ket{s_1 \ldots s_N} = \left(\ket{0} + \E^{2 \pi \I 0.s_1} \ket{1} \right) \ket{s_2 \ldots s_N}\,,$$
note $\E^{2 \pi \I s_1/2} = -1$ only if $s_1=1$. Now, applying $R_2$ controlled by the second qubit, we obtain
$$\left(\ket{0} + \E^{2 \pi \I 0.s_1s_2} \ket{1} \right) \ket{s_2 \ldots s_N}\,.$$
Iterating this last step $N-1$ times, up to applying $R_N$, we get the last term in the product:
$$\left(\ket{0} + \E^{2 \pi \I 0.s_1s_2 \ldots s_N} \ket{1} \right) \ket{s_2 \ldots s_N}\,.$$
For the other qubits we use the same recipe, $N-1$ times for $0.s_2 \ldots s_N$, $N-3$ on $0.s_3 \ldots s_N$, and so on: the total number of steps is then $N(N-1)/2$. We represent the whole algorithm in the circuit of the figure.

> <img src="{static}/images/AQ-cfourier.svg" alt="fft" style="width: 550px;"/>

The classical algorithm, the fast fourier transform, needs instead $2^N N$ steps, which is exponential in $N$, compared to the $N^2$ quantum algorithm. This speed up in the computation of the fourier transform is at the origin of the Shor algorithm performance, which allows the factorization of large integers in polynomial time.

### Phase estimation

The quantum fourier transform may be used to compute the phase $\theta \in (0,1)$, related to the eigenvalue of a unitary $U$ by,
$$U \ket{u_\theta} = \E^{2 \pi \I \theta} \ket{u_\theta}$$
where $\ket{u_\theta}$ is a known eigenvector (of dimension $D$). The circuit

> <img src="{static}/images/AQ-cphase.svg" alt="fft phase" style="width: 550px;"/>

implements the first part of the algorithm (Cleve et alia, 1998).[^C] One register, whose input is $\ket{u_\theta}$, is used to compute the iterates $U^{2^n}$ ($n=0,\ldots,N-1$) which do not modify the eigenstate, and an ancilla register of $N$ qubits, which are used to control the $U$ iterates; the value of $N$ is chosen in order to get $\theta$ with a $N$ bit precision. The state obtained after the circuit application corresponds to the fourier transform of the state <strong style="color:DarkSlateBlue; background-color:LightGray;">EX</strong>:
$$\ket{2^N \theta} = \frac{1}{2^{N/2}} \sum_{k=0}^{2^N - 1} \E^{2\pi \I \theta k} \ket{k}\,.$$ 

Applying the inverse fourier transform
$$\ket{k} = \mathcal{F^\dagger} \ket{s} = \frac{1}{2^{N/2}} \sum_{s=0}^{2^N - 1} \E^{-2\pi \I s k/2^N} \ket{s}\,.$$
to this state, one obtains,
$$ \frac{1}{2^N} \sum_{s=0}^{2^N - 1} \left[ \sum_{k=0}^{2^N - 1} \E^{-2\pi \I k (s - 2^N \theta)/2^N} \right] \ket{s} \approx \ket{2^N \theta}\,.$$
The expression in brackets is picked at $\theta = s/2^N$, therefore, after this inverse transformation, measurement of the ancilla qubits gives us $s$, a $N$ bit approximation of $\theta$.

### Eigenvectors and eigenvalues finding

An influential paper of Abrams and Lloyd[^L] adapted the phase estimation algorithm to calculate the eigenvector $\ket{\bar{\theta}}$ of $U$ and its eigenvalue $\E^{\I \bar{\theta}}$.  They assumed an initial state $\ket{\theta}$ possessing a substantial overlap with the true eigenvector $\ket{\bar{\theta}}$; this means that the expansion
$$\ket{\theta} = \sum_k \theta_k \ket{k}, \quad U \ket{k} = \E^{\I \bar{\theta}_k} \ket{k} \,,$$
contains essentially order one amplitudes
$$\theta_k = \braket{\bar{\theta}_k|\theta}\,.$$
The idea is to define a circuit using a set of $N$ ancilla qubits such that their measure leads with probability
$$p_k = |\braket{\bar{\theta}_k | \theta}|^2$$
to the correct eigenvector $\ket{\bar{\theta}_k}$. Consider the circuit,

> <img src="{static}/images/AQ-cphase-2.svg" alt="Lloyd" style="width: 400px;"/>

We note that instead of applying the successive $U$, $U^2$, $U^4$, $\ldots$ controlled gates as in the phase estimation algorithm, here we simply they use the sequence $U,U^2,U^3,\ldots, U^{2^N-1}$ ($N$ is the dimension of the ancilla register). The state after the application of the hadamard gates and the ancilla controlled $U^n$ gates ($n=0, \ldots, 2^{N}-1$), is 
$$\ket{\psi} = \sum_k \theta_k \left( \sum_n \E^{\I \bar{\theta}_k n} \ket{n} \right) \ket{k} \,.$$
As shown in the above circuit, this needs to control the application of $U$ on the set of ancilla qubits, choosing at each step a different combination of $\ket{0}$ (black) or $\ket{1}$ (white dots) as control qubit states (the gray box in the circuit).

Now, we assume for simplicity that the eigenvalues are $N$-decimal binary digits; in such a case, applying the inverse quantum fourier transform to the ancilla register state (as in the figure above), we obtain <strong style="color:DarkSlateBlue; background-color:LightGray;">EX</strong>
$$\ket{\psi} = \sum_k \theta_k \ket{\theta_k} \ket{k} \,,$$
where, in the present approximation the phases $\theta_k$ coincides with the exact ones $\bar{\theta}_k$. As a consequence, a measurement of the first register gives the binary digits $n$ of the phase $n = 2^N\theta_k$, and the state of the second register is projected into its corresponding eigenvector $\ket{k}$.

## Shor

## Grover

## Exercises

1. Compute the final state after the application of the first part of the phase estimation algorithm (see the circuit figure). Investigate the performance of the algorithm.

2. Analyze the circuit,

    <img src="{static}/images/AQ-cphase-1.svg" alt="phase measure" style="width: 400px;"/>

    where $H$ is the hadamard gate,
    $$Z_\varphi = \mathrm{diag} \left(1, \E^{\I \varphi} \right)$$
    is a phase gate, and $L$ an integer, and show that it transforms the initial state $\ket{0} \otimes \ket{u_\theta}$, $\ket{u_\theta}$ is an eigenvector of $U$, into $\ket{L, \varphi, \theta} \otimes \ket{u_\theta}$,
    $$\ket{L,\varphi,\theta} = \frac{1}{2} \left( 1 + \E^{2\pi \I L \theta + \I \varphi} \right) \ket{0} + \frac{1}{2} \left( 1 - \E^{2\pi \I L \theta + \I \varphi} \right) \ket{0}$$
    Compute the probabilities of measuring the ancilla qubit to be in state $0$ or $1$. (*Hint* $P_{L,\varphi}(0, \theta) = |\braket{0|L,\varphi, \theta}|^2$)

    Show that with a choice of $\varphi$ one can accurately estimate 
    $$\cos(2\pi L \theta) \; \text{and} \; \sin(2\pi L \theta)$$
    from which one finally gets an approximate value of the phase $\theta$.


## Notes

The [qiskit.org](https://qiskit.org/) website contains complete documentation on the quantum [fourier transform](https://qiskit.org/textbook/ch-algorithms/quantum-fourier-transform.html) and its application to the [phase estimation](https://qiskit.org/textbook/ch-algorithms/quantum-phase-estimation.html).

The diagrams of quantum circuits were drawn using the latex package [``quantikz``](https://ctan.org/pkg/quantikz) written by Alastair Kay [arXiv:1809.03842](https://arxiv.org/abs/1809.03842) v.4 (2020)

[^C]: Cleve et al. *Quantum algorithms revisited,* Proc. R. Soc. Lond. A **454**, 339 (1998) [.pdf]({static}/pdfs/Cleve-1998.pdf)

[^L]: Abrams, D., and Lloyd, S., *Quantum algorithm providing exponential speed increase for finding eigenvalues and eigenvectors,* Phys. Rev. Lett. **83**, 5162 (1999)
