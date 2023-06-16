Title: Quantum entanglement
Slug: CH-entangle
Date: 2019-09-22
Category: Lectures
Tags: teaching, quantum, chaos
Authors: Alberto Verga
Summary: Quantum algorithms, von Neumann entropy, random density matrices
status: hidden

$\newcommand{\I}{\mathrm{i}} 
\newcommand{\E}{\mathrm{e}} 
\newcommand{\D}{\mathop{}\!\mathrm{d}} 
\newcommand{\bra}[1]{\langle{#1}|}
\newcommand{\ket}[1]{|{#1}\rangle}
\newcommand{\braket}[1]{\langle{#1}\rangle}
\newcommand{\bbraket}[1]{\langle\!\langle{#1}\rangle\!\rangle}$

[&raquo;Lectures: quantum chaos]({filename}CH-index.md)


# Quantum state and entanglement

We start by exploring numerically some properties of simple quantum states. We use a python implementation to create both, product and entangled states, and to compute the von Neumann entropy of a bipartite system in Hilbert space.

We start by importing the plotting and numerical libraries into a ``jupyter notebook``:

    :::python
    %matplotlib inline
    import matplotlib.pyplot as plt
    import numpy as np
    # scipy
    from scipy.linalg import eigvals

Next, we create a product state:
$$ \ket{++} = \frac{1}{2} \left( \ket{00} + \ket{01} + \ket{10} + \ket{11} \right)$$
and the corresponding density matrix
$$\rho_0 = \ket{++}\bra{++}$$
where
$$\ket{+} = \frac{\ket{0} + \ket{1}}{\sqrt{2}}$$

    :::python
    # qubit
    b0 = np.array([1,0])
    b1 = np.array([0,1])
    # balanced state 00 + 01 + 10 + 11
    b00 = np.kron(b0, b0)
    b01 = np.kron(b0, b1)
    b10 = np.kron(b1, b0)
    b11 = np.kron(b1, b1)
    bb = ( b00 + b01 + b10 + b11 )/2
    # density matrix
    rho0 = np.kron(bb.reshape(4,1), bb.reshape(1,4))

We partition the hilbert space into two equal parts, corresponding to qubit 1 and qubit 2. The density matrix can be viewed as a four rank tensor $\rho_{ij,kl} = \bra{i}\otimes\bra{j}\rho\ket{k}\otimes\ket{l}$.

    :::python
    # bipartition and partial trace over 2
    rho0_12 = rho0.reshape((2,2,2,2))
    # contraction of axis 1, 3 (n2) gives rho_1
    rho0_1 = np.einsum('ijkj -> ik', rho0_12)

Using the $\mathrm{CZ}$ (controled $Z$ operator
$$\mathrm{CZ} = \mathrm{diag}(1,1,1,-1)$$
we define a new state $\ket{\psi} = \mathrm{CZ} \ket{++}$
$$\ket{\psi} = \frac{1}{2} \left( \ket{00} + \ket{01} + \ket{10} - \ket{11} \right)$$
and the first $1$ qubit density matrix,
$$\rho_1 = \mathrm{Tr}_2\, \ket{\psi} \bra{\psi}$$
is the partial trace over qubit $2$.

    :::python
    # apply cphase gate
    cphase = np.diag([1,1,1,-1])
    bm = np.dot(cphase, bb)
    rho = np.kron(bm.reshape(4,1), bm.reshape(1,4))
    rho_12 = rho.reshape((2,2,2,2))
    rho_1 = np.einsum('ijkj -> ik', rho_12)

The von Neumann entropy of a general state $\rho$ is
$$S = - \mathrm{Tr}\, \rho \log \rho$$
where we use the convention that $\log$ denote base 2 logarithm (this definition differs from the usual one by a factor $1/\ln 2$).

    :::python
    # von Neumann entropy of a bipartite system
    def vn_ent(rho):
        """ computes von Neumann entropy, from the eigenvalues of rho"""
        pn = np.real(eigvals( np.einsum( 'ijkj->ik', rho ) ))
        n = pn > 0
        if len(n) > 0:
            S = -np.sum( pn[n] * np.log2(pn[n]) )
        else:
            S = 0.0 # p log p = 0 if p = 0
        return S

We then compute the entanglement entropy of the first qubit (in state $\rho_1$) with the second one
$$S_1 = - \mathrm{Tr}\, \rho_1 \log \rho_1\,.$$
Note that for a $1,2$ bipartite system one has $S_1 = S_2$, whatever the respective dimensions.

    :::python
    vn_ent(rho0_12) # output 0
    vn_ent(rho_12) # output 1

These results show that the product state $\ket{++}$, as expected, has zero entropy, while the transformed state by the "interaction" gate CZ, lead to a maximally entangled state.

## Density matrix

In 1927 [Landau]({static}/pdfs/Landau-1927.pdf) introduced the concept of *density matrix* (or density operator) $\rho$ to describe the *entanglement* of a composite quantum system:

* $\rho = \rho^\dagger$ is hermitian,
* $\rho$ is positive, for all $\ket{\psi} \in \mathcal{H}$, we have $\braket{\psi| \rho |\psi} > 0$, and
* $\mathrm{Tr}\, \rho = 1$, it has unit trace (normalization of the state),
* the expected value of an operator is given by $\braket{O} = \mathrm{Tr}\, \rho O$.

Indeed, in general the state of a composite system cannot be expressed as a product state of the components. This essential property of a quantum state was called *entanglement* by [Schrödinger]({static}/pdfs/Schrodinger-1935.pdf).

The density matrix satisfies:

* $\mathrm{Tr \rho^2 = 1}$ for a *pure* state, or equivalently $\rho = \ket{\psi} \bra{\psi}$

* $\mathrm{Tr \rho^2 < 1}$ for a *mixed* state. In this case, $\rho$ takes the general form:
    $$\rho = \sum_{i} p_i \ket{\psi_i}\bra{\psi_i}, \; i = 1,2,\ldots \; \ket{\psi_i} \in \mathcal{H}_i$$
    where $i$ labels a component of the composite system $\mathcal{H} = \otimes_{i} \mathcal{H}_i$ in the state $\ket{\psi_i}$, and
$$\sum_i p_i = 1\,,$$
    to satisfy the trace condition.

### Bipartite systems

The state of a *bipartite* system $AB$ is given by the superposition,
$$\ket{\psi} = X \ket{A} \otimes \ket{B} = \sum_{ij} x_{ij} \ket{a_i} \otimes \ket{b_j},$$ 
where $X \in \mathcal{H}_A \otimes \mathcal{H}_B$ ($i=1,\ldots,N_A$, $j=1,\ldots,N_B$ with $N_A \le N_B$) is a matrix formed with the amplitudes of the $AB$ states, its is of dimension $N_A \times N_B$. From the density matrix of this pure state 
$$\rho = \ket{\psi}\bra{\psi},$$
we compute the reduced density matrix of part $A$, taking the partial trace over part $B$:
$$\rho_A = \mathrm{Tr}_B \, \rho = \ket{A} XX^\dagger \bra{A} = \sum_{ii'} (XX^\dagger)_{ii'} \ket{a_i}\bra{a_{i'}}.$$
Equivalently, the part $B$ density matrix is given by $X^\dagger X$. The hermitian matrix $XX^\dagger$ can be diagonalized:
$$XX^\dagger = U P U^\dagger, \; U^{-1} = U^\dagger, \; P = \mathrm{diag}(p_i)$$
where $U$ is unitary and $P$ diagonal of dimension $N_A$. Therefore,
$$\rho_A = \ket{u^A} P \bra{u^A} = \sum_i p_i \ket{u^A_i} \bra{u^A_i}$$
where $u_i$ are the $N_A$ eigenvectors of $XX^\dagger$,
$$XX^\dagger \ket{u^A_i} = p_i \ket{u^A_i},\; i = 1,\ldots,N_A.$$
Or, in the same way for $B$,
$$\rho_B = \ket{u^B} P \bra{u^B} = \sum_i p_i \ket{u^B_i} \bra{u^B_i}$$
where $u^B_i$ are the $N_A$ *nonzero* eigenvectors of $X^\dagger X$. Using these eigenvalues and eigenvectors, we can express the bipartite state in the form:
$$\ket{\psi} = \sqrt{P} \ket{u^A} \otimes \ket{u^B} = \sum_i \sqrt{p_i} \ket{u^A_i} \otimes \ket{u^B_i} \,,$$
called the Schmidt decomposition of a pure bipartite state.

## Random density matrix

We consider a bipartite pure system in a random state.

    :::python
    # create a random state of n qubits
    n = 12
    # normal distributed complex amplitudes
    a = np.random.normal(0, 1, [2, 2**n])
    a = a[0] + 1j*a[1]
    psi = a/np.linalg.norm(a) # random state
    rho = np.kron( psi.reshape([len(psi),1]),\
                  np.conjugate(psi.reshape([1, len(psi)])) )
    
    # split the systems into two equal parts
    n2 = 2**(n//2)
    vn_ent( rho.reshape([n2,n2,n2,n2]) ) # output 5.2742
    # select first spin
    vn_ent( rho.reshape([2,2**(n-1),2,2**(n-1)]) ) # output 1

These results show that one spin in a generic random state is maximally entangled with the other spins, and that one half of the system is highly entangled with the other half; in our case with 12 spins the von Neumann entropy is $S_A \approx 5.3$, near the maximum value of $6$.

In 1993 Don Page conjectured a formula,
$$S_A = \log N_A - \frac{N_A^2-1}{2N_AN_B\ln2}, \tag{DP}$$
for the entanglement entropy of a random pure state $N=N_AN_B$, that perfectly fit the numerical result, $S_A = 5.2788 \approx 5.2742$.

    :::python
    # Don Page entropy:
    da = 2**(n//2)
    db = 2**(n//2)
    np.log2(da) - (da**2 - 1)/(2*da*db*np.log(2))  # output 5.2788


### Hilbert-Schmidt measure [^BZ]

In order to demonstrate the Page conjecture, we start by defining the appropriated probability distribution of the random state density matrix eigenvalues $p$. The basic idea is to use random matrix theory, that is to associate a probability measure to the metric induced by a class of matrices, in our case, the density matrix induced distance:
$$\mathrm{dist}(\rho_1,\rho_2) = \sqrt{\mathrm{Tr}\, (\rho_1 - \rho_2)^2 }$$
from which we may define the element of length,
$$ds^2 = \frac{1}{2} \mathrm{Tr}\, \D \rho^2$$
(the scaling factor is for convenience). Using the decomposition $\rho = UPU^\dagger$, we find
$$\D \rho = \D U P U^\dagger + U \D P + U P \D U^\dagger$$
taking into account that $U \D U^\dagger + \D U U^|dagger = 0$, or $U\D U^\dagger = - \D U U^\dagger$,
$$\D \rho = U \left( \D P + [U^\dagger \D U, P] \right) U^\dagger$$
squaring,
$$\mathrm{Tr}\, \D \rho^\dagger \D \rho = \mathrm{Tr}\, \left(\D P^\dagger + [P, \D U^\dagger U] \right) \left(\D P + [U^\dagger \D U, P] \right)$$
defining $A = U^\dagger \D U$ and canceling the term in $[P, \D P]$, we have,
$$\D s^2 = \frac{1}{2} \left( \mathrm{Tr}\, |\D P|^2 + \mathrm{Tr}\, |[P, \D A]|^2 \right)\,$$
noting that
$$[P, \D A]_{ij} = (p_i - p_j) \D A_{ij}$$
one finally obtains,
$$\D s^2 =  \frac{1}{2} \sum_i (\D p_i)^2 + \sum_{i<j} (p_i-p_j)^2 |\D A_{ij}|^2\,.$$

The idea now is to relate the metric $ds^2 = G \D X \D X$ (where the dimension of $dX$ is given by the number of independent degrees of freedom) with the volume measure,
$$\D \mathrm{Vol} \sim \sqrt{\det G} \D X \sim \D P(\rho)\,. \tag{1}$$

The probability distribution of the random density matrix is, using the matrix $X$ to represent the bipartite state,
$$P(\rho_A) \sim \int_B \D X \delta(\rho_A - XX^\dagger) \delta(\mathrm{Tr}\,\rho_A - 1)$$
where the first dirac delta stands for the constraint of having a pure state, the second one is for the normalization of this state, and the integral over the random vectors corresponds to the partial trace. Making the change of variable,
$$X = \sqrt{\rho_A} Y$$
one obtains,
$$P(\rho_A) = \det\rho_A^{N_B-N_A} \Theta(\rho_A) \delta(\mathrm{Tr}\,\rho_A -1)\,. \tag{2}$$
We used:
$$\int_B \D X \rightarrow  \D Y \det\big( \rho_A^{N_B} \big)$$
and
$$\delta(\sqrt{\rho_A}(1 - YY^\dagger)\sqrt{\rho_A}) \rightarrow \det\big( \rho_A^{-N_A} \big) \delta(1 - Y Y^\dagger).$$

Now, combining (1) and (2), we obtain,
$$P_{N_AN_B}(p_1,\ldots,p_{N_A}) = C_{N_AN_B} \delta\left(1 - \sum_i p_i \right) \prod_i^{N_A} p_i^{N_B - N_A} \Theta(p_i) \prod_{i < j}^{N_A} (p_i - p_j)^2, \tag{P}$$
the probability distribution of a pure state random matrix in terms of its eigenvalues. The computation of the normalization constant needs the calculation of the $\mathrm{Vol}(U(N)$ which is essentially the product of the volume of $2N-1, 2N-3, \ldots, 1$ dimensional spheres.

### Page formula[^DP]

To characterize the entanglement of a random state we can compute the von Neumann entropy of the reduced matrix of part $A$ of the bipartite system $AB$, using 
$$S_A = \braket{- \mathrm{Tr}\, \rho_A \ln \rho_A}\,,$$
where the mean is taken over $P_{N_AN_B}(p_1,\ldots,p_{N_A}) \equiv P(p)$. The computation of this integral[^S] gives formula (DP). To this end it is convenient to transform the $p_i$ variables to new variables taking any positive value $q_i = rp_i$ ($r>0$), and to introduce exponential weights to satisfies the normalization condition:
$$\delta\left( 1 - \sum_i p_i \right) \D_{N_A}p = r^{N_A-1} \delta\left( r - \sum_i q_i \right) \D r\D_{N_A-1}q,$$
where $\D_n x = \D x_1 \ldots \D x_n$,
\begin{align*}Q(q)\D_{N_A}q &\equiv \prod_{i<j}^{N_A} (q_i - q_j)^2 \prod_{i=1}^{N_A} \left( \E^{-q_i} q_i^{N_B-N_A} \D q_i \right) \\ 
&= r^{N_AN_B} \E^{-r \sum_i p_i} \prod_{i<j}^{N_A} (p_i - p_j)^2 \prod_{i=1}^{N_A} \left( p_i^{N_B-N_A} \D p_i \right) \\
&= C r^{N_AN_B-1} \E^{-r} P(p) \D r \D_{N_A-1}p \,.\end{align*}
The proportionality constant $C$, is given by,
$$\int_0^\infty \D_{N_A} q\, Q(q) = C \Gamma(N_AN_B) \int_0^1 \D_{N_A-1} p\, P(p)\,.$$
Therefore,
\begin{align*} -\int_0^\infty \D_{N_A} q \, & Q(q)  \left( \sum_i q_i \ln q_i \right) =\\
&= -C \int_0^1 \D_{N_A-1} p \int_0^\infty \D r\, r^{N_AN_B-1} \E^{-r} r P(p) \left( \sum_i p_i \ln p_i + \ln r \right) \\
&= - \left[ C\int \D_{N_A-1} p \, P(p) \right] \, \Gamma(N+1) \psi(N+1) \\
& \quad + \left[ C \int \D_{N_A-1} p \, P(p) \right] \frac{ \int \D_{N_A-1} p \, P(p) S_A}{\int \D_{N_A-1} p \, P(p)}\\
&= N \int \D_{N_A} q\, Q(q) \left[ -\psi(N+1) + \braket{S_A}  \right] \end{align*}
($\psi(z)=\Gamma'(z)/\Gamma(z)$ is the psi, or [digamma](https://dlmf.nist.gov/5.9), function) or, finally,
$$\braket{S_A} = \psi(N_AN_B+1) - \frac{ \int_0^\infty \D_{N_A} q \, Q(p) \left( \sum_i q_i \ln q_i \right)}{N_AN_B\int_0^\infty \D_{N_A} q \, Q(q)}\,,$$
which can be evaluated by the Sen[^S] straightforward, albeit difficult, calculation.


## Notes

[^BZ]: I. Bengtsson and K. Zyczkowski, *Geometry of quantum states* (Cambridge, 2017)
[^DP]: [D. Page]({static}/pdfs/Page-1993nr.pdf), *Average entropy of a subsystem*, Phys. Rev. Lett. **71**, 1291 (1993)
[^S]: [S. Sen]({static}/pdfs/Sen-1996gx.pdf), *Average entropy of a quantum subsystem*, Phys. Rev. Lett. **77**, 1 (1996)

