Title: Kitaev toric code
Slug: AQ-toric
Date: 2021-06-15
Category: Lectures
Tags: teaching, advanced quantum mechanics
Authors: Alberto Verga
Summary: Toric code, stabilizer formalism and topology
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

# Toric Code

We summarize the main ideas of the stabilizer formalism.[^G] Errors on individual qubits can be represented by the action of the pauli matrices (spin flip, phase and amplitude errors). The pauli matrices are the generators of the pauli group:
\begin{equation}
\mathcal{P} = \braket{\I 1_2, X, Y, Z}
\end{equation}
The physical information of $K$ qubits is encoded into $K$ logical states $\ket{i_L} \in \mathcal{L} \subset \mathcal{H}_L$, of an extended hilbert space of dimension $\mathrm{dim}(\mathcal{H}_L) = 2^N$.

To detect and eventually correct the pauli errors, a set of $N-K$ independent operators, the stabilizer $\mathcal{S} \subset \mathcal{P}$, is necessary:
\begin{equation}
\mathcal{S} = \braket{g_1, \ldots, g_{N-K}}
\end{equation}
where the stabilizers $g_n$ commute, $[g_n, g_m] = 0$. The logical states (code words) satisfy,
\begin{equation}
g_n \ket{i_L} = \ket{i_L}, \quad \forall g_n \in \mathcal{S}
\end{equation}
Therefore, the logical qubits are the common eigenstates of the stabilizer operators with eigenvalue one. The operators acting on the subspace spanned by the logical states, are the logical operators. Typically they are products of pauli matrices we denote $X_L$ and $Z_L$, such that
$$X_L \ket{0_L} = \ket{1_L},\quad X_L \ket{1_L} = \ket{0_L}$$
and
$$Z_L \ket{0_L} = \ket{0_L},\quad Z_L \ket{1_L} = -\ket{1_L}$$
The *centralizer* group of the stabilizers, the set of operators commuting with the stabilizers, is
\begin{equation}
\mathcal{C} = \braket{ \{g \in \mathcal{P} \mid [g,g_n] = 0, \; \forall g_n \in \mathcal{S}\} }
\end{equation}
has a rank $N + K = (N - K) + 2K$, with $N-K$ stabilizers and $2K$ logical operators (of type $X$ and $Z$); the $2K$ logical operators commute with the stabilizers but act non trivially on the logical qubits:
\begin{equation}
\mathcal{C} = \left\langle \begin{matrix} X_L^{(1)}, \ldots,  X_L^{(K)} & g_1, \ldots g_{N-K} \\ Z_L^{(1)} , \ldots , Z_L^{(K)} & \end{matrix} \right\rangle
\end{equation}
where the operators in the same column anticommute, while the operators on different columns, commute each other.

The physical realization of a quantum error correcting system was first proposed by Kitaev (1997),[^K] using the degenerated ground state of a local hamiltonian as a logical code; the hamiltonian itself is build up using a set of stabilizers (see table below).


<blockquote>
<table class="table table-striped" style="width: 500px">
<thead class="thead-dark">
<caption> Physical realization of an error correction code. Information concepts, like code or error can be translated into a physical system governed by a hamiltonian. </caption>
<tr>
<th>Information concept</th>
<th>Physical system</th>
</tr>
</thead>
<tbody>
<tr>
<td>stabilizer code</td>
<td>frustration free hamiltonian</td>
<tr>
<td>code space</td>
<td>degenerated ground state protected by a gap</td>
</tr>
<tr>
<td>errors</td>
<td>excitations</td>
</tr>
</tbody>
</table>
</blockquote>

## Hamiltonian and ground state

We consider a set of $N = 2 L^2$ spins laying on the links $\ell$ of a square lattice of size $L$ with periodic boundaries, equivalent to a torus.

The hamiltonian is defined in terms of mutually commuting star $A_s$ and plaquette $B_p$ operators (figure below),
\begin{equation}
\label{e:H}
H = -J_s \sum_s A_s - J_p \sum_p B_p
\end{equation}
where
\begin{equation}
\label{e:AB}
  A_s = \prod_{\ell \in s} X_\ell,  \quad  
  B_p = \prod_{\ell \in p} Z_\ell\,,
\end{equation}
and $J_s,J_p$ the coupling energies (we use normal product notation for tensor product of operators).

> <img src="{static}/images/AQ-toric_AB.svg" alt="toric operators" style="width: 280px;"/>
>
> The toric code is defined on a square lattice with periodic boundary conditions; the spins live on the links and interact via  four-body coupling operators $A_s$ (star) and $B_p$ (plaquette).

For example, applying $A_s$ to a star gives $A_s\ket{0010} = \ket{1101},$ (flip), and $B_p$ to a plaquette gives $B_p \ket{0010} = - \ket{0010}$ (odd parity).

The ground state of $H$ is easy to find because its terms commute, implying that a state $\ket{00}$
\begin{equation}
\label{kAB}
A_s \ket{00} = \ket{00}, \quad B_p \ket{00} = \ket{00}
\end{equation}
(we explain below the labels) which is a simultaneous eigenvector of the stabilizers $A_s$ and $B_p$, minimizes the energy. However, the system ($\ref{kAB}$) involves only $2L^2 - 2$ equations, because not all the operators are independent:
\begin{equation}
\prod_s A_s = 1,\quad \prod_p B_p = 1
\end{equation}
Therefore, the logical space has dimension $2^2=4$, since the stabilizer space contains $N-2$ independent generators, or $K = 2$. The ground state of $H$ is then four times degenerated, and can be written as a superposition of the type:
$$\ket{\psi_L} = \sum_{b_1,b_2 = \{0,1\}} a_{ij} \ket{b_1b_2}, \quad a_{b_1b_2} \in \mathbb{C}$$
where $b_1,b_2$ label the four basis states of the ground state subspace. The states $\ket{b_1b_2}$ span then the logical space.

Equation ($\ref{kAB}$) has an interesting geometrical interpretation based on the duality of the square lattice: star operators become plaquette operators in the dual lattice. The dual of a square lattice is also a square lattice whose vertices are at the centers of the original faces (plaquettes). We may construct the ket $\ket{00}$ (in the ground state of $H$) from the product state with all spins up $\ket{0}^{\otimes N}$, using the fact that application of multiple star operators
$$A_s \ket{0}^{\otimes N}, A_{s_1} A_{s_2} \ket{0}^{\otimes N}, \ldots$$
represents a loop in the dual lattice of the torus; one $A_s$ gives a plaquette loop in the dual lattice, two successive stars form a two plaquettes loop in the dual lattice, etc. In addition, the action of the plaquette operators is trivial, $B_p \ket{0}^{\otimes N} = \ket{0}^{\otimes N}$ (remember that $[A_s,B_p]=0$). Therefore, an equal superposition of all of these loops:
\begin{equation}
\label{e:k00}
\ket{00} = \frac{1}{2^{(L^2-1)/2}}\prod_s (1 + A_s) \ket{0}^{\otimes N}
\end{equation}
must be a ground state (note that $A_s(1+A_s) = 1 + A_s$), the one composed by contractible loops $\ket{00}$ (see figure).

> <img src="{static}/images/AQ-toric_loops.svg" alt="tore contractible loops" style="width: 300px;"/>
>
> The ground state $\ket{00}$ is a superposition of contractible loops in the torus, generated by the successive application of the stabilizer operators (c.f. $\eqref{e:k00}$). We show two loops on the dual lattice $\bar{\ell}$, of reversed spins by a cycle of stars operators $A_s$.

Indeed, as shown in the figure below, on a torus we can have contractible loops $\ell$ and non contractible ones, encircling the torus longitudinally $\ell_\parallel$ (polar angle) or perpendicularly $\ell_\perp$ (azimutal angle). 

> <img src="{static}/images/AQ-toric_XZ.svg" alt="tore loops" style="width: 300px;"/>
>
> The ground state of the toric code is a superposition of loops; $\ell$ is a contractible loop, and $\ell_\perp, \ell_\parallel$ are two topologically distinct non contractible loops.

The star operators create contractible loops (on the dual lattice). However, non contractible loops can be created using the so called string operators:
\begin{align*}
X_\parallel &= \prod_{n \in \bar{\ell}_\parallel} X_n, \quad &
X_\perp &= \prod_{n \in \bar{\ell}_\perp} X_n \\
Z_\parallel &= \prod_{n \in \ell_\parallel} Z_n , \quad &
Z_\perp &= \prod_{n \in \ell_\perp} Z_n 
\end{align*}
associated to the loops around the two directions in the torus, on the lattice $\ell$ and the dual lattice $\bar{\ell}$ (see figure).

> <img src="{static}/images/AQ-toric_LL.svg" alt="tore loops and duals" style="width: 280px;"/>
> 
> Non contractible loops on the square lattice and its dual. One associates a logical operator $X_L$ (dual, dashed lines) and $Z_L$ (solid lines), on each path.

Note that the logical operators commute with the stabilizers but act non trivially on the ground state; for instance, the state $\ket{b_1b_2}$ defined by
$$X^{b_1}_{\parallel}  X^{b_2}_{\perp} \ket{00} = \ket{b_1b_2}, \quad b_1,b_2 = 0, 1$$
represents a ground state with $b_1$ non contractible loops in the longitudinal direction, and $b_2$ non contractible loops in the perpendicular direction.

An interesting observation is that the structure of the logical operators reflects the underlying geometry of the torus: the support of the logical operators is a non contractible cycle on the torus. Moreover, the logical operators, given that they commute with the hamiltonian, are thus related to non trivial symmetries. However, at variance with the stabilizers (which also are symmetries of $H$), the logical operator symmetries are spontaneously broken in the ground states.

Summarizing the above results, we conclude that the ground state $\ket{\psi_L}$ of the toric code is four times degenerated and can be spanned by the two logical qubits basis $\ket{b_1b_2}$, of the possible superpositions of closed paths on the torus.



## Notes

[^G]: Gottesman, D., *Stabilizer Codes and Quantum Error Correction,* Thesis (1997); arXiv:quant-ph/9705052 [.pdf]({static}/pdfs/Gottesman-1997.pdf)

[^K]: Kitaev, A., *Fault-tolerant quantum computation by anyons,* Ann. Phys. **303**, 2 (2003); arXiv:quant-ph/9707021 [.pdf]({static}/pdfs/Kitaev-2003fk.pdf)
