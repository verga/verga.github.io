Title: Leçon de physique théorique: Quantum phase transitions
Slug: L3-qphase
Date: 2023-03-02
Category: Blog
Tags: teaching
Authors: Alberto Verga
Summary: We explore in these introductory notes, quantum phase transitions with a focus on dynamics.

$\newcommand{\I}{\mathrm{i}} 
\newcommand{\E}{\mathrm{e}} 
\newcommand{\D}{\mathop{}\!\mathrm{d}} 
\newcommand{\bra}[1]{\langle{#1}|}
\newcommand{\ket}[1]{|{#1}\rangle}
\newcommand{\braket}[1]{\langle{#1}\rangle}
\newcommand{\bbraket}[1]{\langle\!\langle{#1}\rangle\!\rangle}
\newcommand{\bm}[1]{\boldsymbol{#1}}$

> This lecture is intended for students of the "Licence de physique", and in particular to those interested in theoretical physics.


# Quantum phase transitions

At zero temperature $T=0$ an isolated quantum system, described by a hamiltonian operator $H(\lambda)$, should be in its ground state $\ket{0\lambda}$. In general the hamiltonian depends on a set of parameters, labelled by $\lambda$, which characterize the state of the system. A quantum phase transition refers to a drastic qualitative change of the ground state physical properties when the parameter $\lambda$ is smoothly changed around a *critical* value $\lambda_c$.

The quantum phase transition can also manifest dynamically, for instance after the quench of a system initially in the ground state of a hamiltonian, say $H_0$, which subsequently evolves with another hamiltonian, $H_1$, possessing a different ground state.

Driven systems, in which energy is no longer conserved, quantum phase transition can be also present. In this case the natural evolution, for an isolated system, is towards an infinite temperature ergodic state. However, ergodicity breaking dynamical transitions may lead the system towards a stationary quantum phase, whose properties are not related to its thermodynamic equilibrium phases. 

In this *Leçon* we explore the notion of quantum phase transition, with a focus on dynamics.

## Bifurcation

The simplest model of a qualitative change driven by the continuous tuning of a parameter is the dynamical system $x(t)$ described by the one-dimensional ordinary differential equation
\begin{equation}\label{e:xt}
\dot{x}(t) = \lambda x(t) - x(t)^3.
\end{equation}
In this model $x$ represents the state of the system, which evolves in time $t$ and depends on the value of the (external) parameter $\lambda$. There is a unique fixed point for $\lambda <0$ and three for $\lambda>0$:
\begin{equation}\label{e:x0}
x(\infty) = x_\lambda = \begin{cases} 0 & \text{if } \lambda>0 \\ \pm\sqrt{\lambda} & \text{if } \lambda>0 \end{cases}.
\end{equation}

> <img src="{static}/images/L3-qp_bifurcation.svg" alt="Bifurcation" style="height: 200px;"/>
>
> Bifurcation diagram.

Here the "critical" behavior is related to the behavior of the roots of the polynomial $\lambda x - x^3$: the two complex conjugate roots present when $\lambda<0$ collide on the real axis at the critical point $\lambda_c=0$ and start to follow the real axis for $\lambda>0$. 

## Quantum transition: Landau-Zener

Consider the hamiltonian $H(\lambda)$ of a spin in a longitudinal ($z$) magnetic field, here proportional to $\lambda$, superposed to a fixed transversal ($x$) field of intensity $\Delta$
\begin{equation}
  \label{e:Hl}
  H(\lambda) = \Delta \sigma_x + \lambda \sigma_z.
\end{equation}
When $\Delta = 0$, $H$ describes a two energy levels system $\pm \lambda$. The term in $\Delta$ mixes the two levels leading to the spectrum
\begin{equation}
  \label{e:sp}
  H(\lambda) \ket{\pm} = E_\pm \ket{\pm}, \quad E_\pm = \pm \sqrt{\lambda^2 + \Delta^2},
\end{equation}
and corresponding eigenstates
\begin{equation}
  \label{e:spv}
  \ket{+} = \begin{pmatrix} \cos\theta/2 \\ \sin\theta/2
  \end{pmatrix}, \quad
  \ket{-} = \begin{pmatrix} -\sin\theta/2 \\ \cos\theta/2
  \end{pmatrix},
\end{equation}
where,
\begin{equation}
  \label{e:th}
  \cos \theta = \frac{\lambda}{\sqrt{\lambda^2 + \Delta^2}}, \quad
  \sin \theta = \frac{\Delta}{\sqrt{\lambda^2 + \Delta^2}}.
\end{equation}
See the figure below.

> <img src="{static}/images/L3-qp_LZ.svg" alt="Landau-Zener" style="height: 200px;"/>
>
> Spectrum of the spin hamiltonian. In the absence of the transverse field the two levels $\ket{0}$ and $\ket{1}$ crosses at $\lambda=0$. For any other value of $\Delta$, the level crossing is avoided. The two levels $E_\pm$, corresponding to the eigenstates $\ket{\pm}$, are separated by a gap $2\Delta$.

We observe that the topology of the spectrum change between the two cases $\Delta=0$ and $\Delta \ne 0$; in the former case there is level crossing which disappears for any finite transversal field. As in the case of the bifurcation there is a loss of analyticity, here in the spectrum of the hamiltonian, for a particular value of the parameters. Note however that when $\Delta \ne 0$ transition between the positive and negative energy levels is impossible.

Now assume that $\lambda=\lambda(t)$ becomes a time dependent parameter
\begin{equation}
  \label{e:lt}
  \lambda(t) = \frac{vt}{2}
\end{equation}
where $v$ characterizes the variation of $\lambda$ by time unit (we take $\hbar=1$). The time dependence of the hamiltonian allows the emergence of a new effect, the transition between the two levels $E_+$ and $E_-$, absent in the static case. This is the effect discovered by Landau, Zener, Majorana and Stückelberg (1932), independently. They found that the transition probability between the two adiabatic levels $E_\pm$ (for the linear time dependency of $\lambda$) is exponentially small
\begin{equation}
  \label{e:lz}
  p_{+-} = \E^{-\pi \Delta^2/v}.
\end{equation}
This expression gives the transition probability at infinite time ($t \rightarrow \infty$), when the initial state was on one of the $E_\pm$ levels, at $t\rightarrow -\infty$. 

## Quantum phase

A quantum phase is a state of matter at zero temperature. It can be an equilibrium state that naturally connects with a thermal phase at finite temperature. For example, the superfluid phase of liquid helium extends to $T=0$: there, changing the pressure a transition to a solid (supersolid) state is possible.

Quantum phases are ground states with specific correlations, and in particular, specific entanglement properties. Consider the case of a ferromagnet, a material whose spins are aligned at $T=0$ (the ground state is twice fold degenerated, the full up and the full down states having the same energy). When it is placed in a external transverse magnetic field of enough strength (the $\lambda$ parameter), intense tunneling (between up an down states) destroy the magnetic order, leading the system to a paramagnetic state. Therefore, the strength of the applied field controls a transition between ferro- and paramagnetic states.

### Transverse field Ising model

The hamiltonian describing this order-disorder transition, in its simplest form, can be written as
\begin{equation}
  \label{e:tih}
  H = -\sum_x Z_x Z_{x+1} - \lambda \sum_x X_x, \quad x \in \mathbb{Z}
\end{equation}
where we denote by $XYZ$ the three pauli matrices. The first term, the quantum Ising hamiltonian, describes the ferromagnetic interaction between neighboring spins in the one-dimensional lattice; the second term describes the applied field (in the $x$ direction).

For $\lambda = 0$ the ground state is ordered,
\begin{equation}
  \label{e:ti0}
  \ket{\uparrow} = \prod_x \ket{0},
\end{equation}
where $\ket{0}$ and $\ket{1}$ are the eigenvectors of $Z$; while when $\lambda \rightarrow \infty$ the ground state is disordered
\begin{equation}
  \label{e:ti1}
  \ket{\uparrow} = \prod_x \frac{1}{\sqrt{2}} \big( \ket{0} + \ket{1}  \big);
\end{equation}
between these extreme cases, a transition produces at $\lambda = 1$, which corresponds then to the critical point. Note that in the state $\ref{e:ti1}$ the spatial correlation function satisfy
\begin{equation}
  \label{e:tic}
  \braket{Z_xZ_y} = \delta_{xy}
\end{equation}
which differs to its value in the ordered state $\braket{Z_x Z_y}=1$, showing that the $Z$ spins are, in this phase, perfectly independent. At finite values of $\lambda$, the generic behavior of the correlation function is exponential 
\begin{equation}
  \label{e:tix}
  \braket{Z_xZ_y} = \E^{-|x-y|/\xi},
\end{equation}
where $\xi$ is called the correlation length. On important property of the critical point is that in its neighborhood the correlation length diverges as a *power law*
\begin{equation}
  \label{e:tixx}
  \xi \sim |\lambda- \lambda_c|^{-\nu}
\end{equation}
characterized by the exponent $\nu$. A detailed calculation gives $\nu = 1$.[^S]

### Symmetry breaking

Quantum phases, as classical thermodynamic phases, possess specific symmetry properties that, at the transition, change. In the previous example the disordered phase is isotropic (the paramagnet do not have a privileged orientation of the spins), while the ferromagnetic phase broke the rotation symmetry (here privileging the $z$-direction). In addition, although the ground state is degenerate, allowing in principle both $\pm z$-orientations, the interaction of the system with the environment can select one particular unique ground state, even in the limit of a vanishing coupling strength. The non analytic behavior of the ground state (the equivalent of the free energy at $T=0$) at the transition is strictly valid only in the $N \rightarrow \infty$ thermodynamic limit. A remarkable consequence of this limit, is that two states (in our case $\ket{\uparrow}$ and $\downarrow$) unitary related for finite hilbert space, may become unitary unrelated in the infinite hilbert space.

To see the unitary inequivalence of two states when the number of degrees of freedom tends to infinity, let us rotate the ferromagnetic state $\ket{\uparrow}$ by an angle $\theta$ around the $y$-axis,
\begin{equation}
  \label{e:sbr}
  \ket{\theta} = U(\theta) \ket{\uparrow}, \quad U = \exp\left[- \frac{\I \theta}{2} \sum_{x=1}^N Y_x \right],
\end{equation}
where $\theta \in (0,\pi]$. We compute now the overlap of the two states
\begin{equation}
  \label{e:sbo}
  \braket{0|\theta} = \left( \cos \frac{\theta}{2} \right)^N \rightarrow 0 \; (N \rightarrow \infty )
\end{equation}
and find that it vanishes for arbitrary small $\theta$. In fact, using the lowering operator $\sigma_- = (X-\I Y)/2$ one can build a complete basis of the hilbert space from the up state, and equivalently we can buid another hilbert space from $\ket{\theta} = U(\theta) \ket{\uparrow}$, using the rotated pauli matrices
$$
\bm \tau = U(\theta) \bm \sigma U^\dagger(\theta).
$$
These two hilbert spaces are then inequivalent: any scalar product between vectors of the two spaces should vanish in the limit $N \rightarrow \infty$ (remember that unitary operators preserve the value of the scalar product). 

## Dynamical transition

We consider a $N$-body system initially in the ground state $\ket{0}$ of some hamiltonian $H_0 = H(\lambda_0)$. At time zero we change $\lambda$ to a new value, and let the system evolve with the new hamiltonian $H(\lambda)$, therefore 
\begin{equation}
  \label{e:dt0}
  \ket{t} = \E^{-\I H t} \ket{0}
\end{equation}
is the state at time $t$, evolved from the ground state of $H_0$. The square of the transition amplitude 
\begin{equation}
  \label{e:dtl}
  \mathcal{L}(t) = \big| \braket{0| t} \big|^2 = \big| \braket{0| \E^{-\I H t} |0} \big|^2 
\end{equation}
is called the *Loschmidt echo*, and 
\begin{equation}
  \label{e:dtr}
  r(t) = -\lim_{N \rightarrow \infty} \frac{1}{N} \ln \mathcal{L}(t)
\end{equation}
the *rate function*, which can be viewed as a well defined intensive quantity (contrary to $\mathcal{L}$, which generically tends to zero in the thermodynamic limit). The rate function represents the probability density to return to the initial states after a time $t$.

It is interesting to note the analogy of the return (echo) amplitude with the partition function in thermodynamics $Z(T) = \mathrm{tr}\, \E^{-H T}$,
$$G(t) = \braket{0| t} = \braket{0|\E^{-\I t H}|0}$$
if one replaces $T \rightarrow \I t$ (formally considering complex temperatures). In the same way that zeros of the partition function correspond to critical points separating different thermodynamic phases, zeros of the amplitude would indicate *dynamical* quantum phase transitions.[^H]


### Discrete time cluster model

One of the challenges in quantum information is to create quantum states that can be used as resources, for instance, in the measurement-based model of quantum computing. For instance, one can imagine that the successive application of a local unitary operator can entangle neighboring spins (in the simplest case on a one-dimensional lattice), and can then transform an initial product state into a useful entangled one. 

An example of the basic entanglement mechanism can be illustrated by the quantum circuit where the entangling gate is the controlled not $\mathsf{cnot}$,

<img src="{static}/images/AQ-cbell0.svg" alt="bell state" style="height: 80px;"/>

where the unitary operator that transforms the initial $\ket{00}$ state into the bell state is the product of the hadamard $\mathsf{h} = (X+Y)/\sqrt{2}$, and controlled not gates:
$$ U = (1\otimes \mathsf{h}) \exp\left[ \I \pi \frac{1-Z}{2} \otimes \frac{1-X}{2} \right].$$
A similar entangled state can be obtained using the basic circuit using the controlled phase gate $\mathsf{cz}$
$$\mathsf{cz} \ket{++} = \exp\left[ \I \pi \frac{1-Z}{2} \otimes \frac{1-Z}{2} \right] \ket{+} \ket{+},$$
that can be translated into the circuit

<img src="{static}/images/AQ-cbell1.svg" alt="cluster state CZ" style="height: 80px;"/>

which create the two qubits *cluster* state. The generalization of this state to a two-dimensional square lattice, provides a universal resource to quantum computing. It is in fact the ground state of the hamiltonian,
\begin{equation}
  \label{e:cmh0}
  H_C = -J\sum_x Z_{x-1} X_x Z_{x+1}.
\end{equation}

> <img src="{static}/images/L3-qp_ll.svg" alt="loschmidt rate" style="height: 200px;"/>
>
> Behavior of the loschmidt rate in two different quantum phases as a function of time in the Floquet cluster model. The non-analytic time evolution occurs when $J>B$, which corresponds to the cluster phase. The trivial phase is present when $B>J$, leading to a smooth regular loschmidt rate.

To construct the unitary operator we complement this hamiltonian with an external field term:
\begin{equation}
  \label{e:cmUx}
  U(J,B) = \E^{\I \Delta t J \sum_x Z_{x-1} X_x Z_{x+1}} \E^{\I \Delta t B \sum_x X_x}.
\end{equation}
In the limit $\Delta t \rightarrow 0$, this evlution operator reduces to the evolution of the cluster hamiltonian in a field $B$. For $\Delta t = 1$, the model descibes a discret time (Floquet) dynamics. 

If the apllied field becomes dominant ($J<B$) the entangled cluster state is destroyed and the system enters a low entanglement magnetic phase. In the opposite case ($J>B$), the cluster state prevails. This "disordered", albeit highly entangled state, is called a topopogical phase. The dynamical transition between the two is illustrated in the above figure, wher we plot the loschmidt ratio for the two cases.[^V]

### Notes 

[^S]: Sachdev, S. *Quantum Phase Transitions* (Cambridge, 1999); see also Dutta, A. et al. *Quantum Phase Transitions in Transverse Field Spin Models* (2015) [arXiv:1012:0653](https://arxiv.org/abs/1012.0653)

[^H]: Heyl, M. *Dynamical Quantum Phase transition* Rep. Prog. Phys. **81**, 054001 (2018) [arXiv:1709.07461](https://arxiv.org/abs/1709.07461)

[^V]: Verga, A.D. *Entanglement dynamics and phase transitions of the Floquet cluster spin chain* Phys. Rev. B **107**, 085116 (2023) [arXiv:2208.01706](http://arxiv.org/abs/2208.01706)
