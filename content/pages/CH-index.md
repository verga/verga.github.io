Title: Chaos
Slug: CH-index 
Date: 2015-12-31 16:23
Modified: January 24, 2015
Category: Lectures
Tags: chaos
Authors: Alberto Verga
Summary: Classical and quantum chaos
status: hidden

$\newcommand{\I}{\mathrm{i}} 
\newcommand{\E}{\mathrm{e}} 
\newcommand{\D}{\mathop{}\!\mathrm{d}} 
\newcommand{\Di}[1]{\mathop{}\!\mathrm{d}#1\,} 
\newcommand{\Dd}[1]{\frac{\mathop{}\!\mathrm{d}}{\mathop{}\!\mathrm{d}#1}} 
\newcommand{\kB}{k_\textsc{b}} 
\newcommand{\NA}{N_\textsc{a}}$

Graduate course on classical chaos, plasmas, and quantum chaos. The approach is phenomenological, with a brief presentation of the theoretical concepts in parallel with computations (mostly numerical) of specific systems. Given at the Aix-Marseille University, January - February 2016-2018, "Master de physique théorique" [P3TMA](http://physique-sciences.univ-amu.fr/master2-physique/P3TMA).

# Chaos, classical and quantum 

* Alberto Verga, [alberto.verga@univ-amu.fr](mailto:alberto.verga@univ-amu.fr)
* CPT bureau 623

## Summary

1. [Maps]({filename}CH-map.md)
    * dyadic map and the sensitivity to initial conditions
    * logistic map, stable and instable orbits, bifurcations, periodic orbits, chaotic orbits
    * [Hamiltonian formalism]({filename}CH-hamilton.md): Liouville, KAM and PB theorems.
    * standard map: a chaotic Hamiltonian system, fixed points and Chirikov stochasticity criterion; quasilinear diffusion.
    * [Stability and bifurcation]({filename}CH-cds.md) of dynamical systems
2. [Plasmas]({filename}CH-plasma.md)
    * Vlasov equation, Landau damping
    * Numerical simulation of the collisionless plasma (particle in cell)
    * [Quasilinear diffusion]({filename}CH-plasma-ql.md)
3. [Quantum chaos]({filename}CH-qc.md)
    * [kicked rotator]({filename}CH-kicked.md), [dynamical localization]({filename}CH-kicked-localization.md) (localization length)
    * [random matrices, level statistics]({filename}CH-rm.md)
    * [quantum random walk]({filename}CH-qrw.md)
    * [Quantum entanglement]({filename}CH-entangle.md)
4. [Exercises]({filename}CH-exercises.md)

Among different possible classifications of classical physical systems, we may distinguish dynamics and thermodynamics; although both are related to changes driven by forces, *dynamics* refers to the change in time of mechanical systems, while *thermodynamics* refers to the change of state without reference to time. In some sense, time is external in dynamic systems, but it is intrinsic in thermodynamic systems. Of course, these two categories are related by the laws of statistical physics: the dynamics of a large number of microscopic systems manifests macroscopically as a thermodynamic system. 

However, in the case of a *quantum system*, we must be cautious about their description within the conceptual framework of dynamical systems. Indeed, a quantum system cannot be reduced to the paradigm of *dynamics*, even if one principle of quantum mechanics is its unitary evolution (with time as a parameter). The state of the system cannot be defined by a set of initial conditions, but it is necessary to specify the Hilbert space and a set of observables, without equivalent in classical systems. In addition, the state of a quantum system has associated a von Neumann *entropy* that grows in the measurement process. Classical mechanical system do not have an entropy *naturally* associated with them; it is necessary to introduce same coarse-graining into the phase space to define a probability distribution (Kolmogorov). Under this perspective, quantum systems share some fundamental properties of thermodynamic systems, in particular both are related to *information*.

It is the purpose of this course to explore dynamical systems, from the logistic map to plasmas, and to enlarge the perspective to investigate complex behavior in quantum systems, from kicked rotators to quantum walks. In addition to the more traditional description in terms of sensitivity to initial conditions, we show that *classical chaos* is basically related to statistical properties of trajectories. This point of view will allow us to extend some notions to the realm of *chaotic quantum systems*. 

The simple idea behind *chaos* is that deterministic systems behave as stochastic systems:

* nuclear levels can be described by hermitian random matrices (quantum chaos)
* Lyapounov exponents in chaotic systems can be modeled by products of identically distributed random matrices (classical chaos)

### Bibliography

* Wimberger (2015) "Nonlinear Dynamics and Quantum Chaos"
* Stöckmann (1999) "Quantum Chaos"
* Haake (2010) "Quantum Signatures of Chaos"
* Boyd (2003) "The Physics of Plasma"

#### Miscellaneous papers

* [Floss (2015)](http://dx.doi.org/10.1103/PhysRevLett.115.203002) experiments demonstrating dynamical localization [.pdf]({static}/pdfs/Floss-2015kx.pdf)
* [Robinson (1999)](http://dx.doi.org/10.1103/PhysRevLett.74.3963) kicked rotator experiment
* [Izrailev (1990)](http://dx.doi.org/10.1016/0370-1573(90)90067-C) "Simple models of quantum chaos: Spectrum and eigenfunctions" [.pdf]({static}/pdfs/Izrailev-1990yg.pdf)
* [Kitagawa (2012)](http://dx.doi.org/10.1007/s11128-012-0425-4) "Topological phenomena in quantum walks" [.pdf]({static}/pdfs/Kitagawa-2012fk.pdf)

### Index

* [Maps]({filename}CH-map.md)
* [Stability, bifurcations, ...]({filename}CH-cds.md)
* [Hamiltonian formalism]({filename}CH-hamilton.md)
* [Plasmas]({filename}CH-plasma.md)
* [Plasmas, quasilinear theory]({filename}CH-plasma-ql.md)
* [Quantum chaos]({filename}CH-qc.md)
* [Kicked rotator]({filename}CH-kicked.md)
* [Dynamical localization]({filename}CH-kicked-localization.md)
* [Random matrices]({filename}CH-rm.md)
* [Quantum walk]({filename}CH-qrw.md)
* [Quantum entanglement]({filename}CH-entangle.md)
* [Exercises]({filename}CH-exercises.md)
