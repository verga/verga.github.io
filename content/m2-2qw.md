Title: Master project (2017)
Authors: Alberto Verga
Date: 2017-01-12
Category: teaching
Tags: quantum
slug: m2-2qw
Summary: Scientific computing and master project internships: interacting quantum walks and entanglement.


## Interacting quantum walks on graphs 
### scientific computing internship
* proposed by Alberto Verga (Alberto.Verga@univ-amu.fr)
* Institut: Centre de Physique Théorique (CPT), bureau 623

> The recent discovery of area laws for the entanglement entropy in many-body systems, shed a new light into the complex problem of nontrivial states of matter, in particular topological order (spin liquids, quantum Hall states, many-body localization). Entanglement and interaction are intimately related, however, entanglement is a nonlocal property and interaction is essentially local in most physical systems. This project aims at investigating quantum correlations arising from the interaction of two walkers evolving by a local unitary operator on a graph. Specifically, we study the entanglement of the quantum state (von Neumann entropy, negativity,…) for different graphs topologies, with the goal of answering the following questions: are the measures of entanglement sufficient to distinguish the graph topology? how does entanglement depend on the graph topology?

> The student will develop the numerical tools (algorithms, code, data analysis) using standard languages (python, fortran or C) and modern computations frameworks (jupyter notebooks).

* Prerequisites: none

### References

* A. Ahlbrecht, A. Alberti, D. Meschede, V. B. Scholz, A. H. Werner, and R. F. Werner. Molecular binding in interacting quantum walks. New Journal of Physics, 14(7):073050, 2012. [url](https://arxiv.org/abs/1105.1051)

* G. R. Carson, T. Loke, and J. B. Wang. Entanglement dynamics of two-particle quantum walks. Quantum Information Processing, 14(9):3193–3210, 2015. [url](http://dx.doi.org/10.1007/s11128-015-1047-4)

##  Graph states and quantum walks
### master internship

A deep and far reaching idea relates matter and information through the concept of entropy. Trying to understand the measurement process in quantum mechanics as first thoroughly discussed by Niels Bohr, von Neumann associated an entropy to a quantum state, described by the density matrix. Later, in one of the most influential papers of the twenty century, Shanon found a definition of the information as the negative of the entropy: precisely the same entropy Boltzmann used to assess the second principle of thermodynamics. 

Entanglement, that can be measured by the von Neumann entropy, is a central concept in quantum mechanics. On one hand, it is this property of quantum states that reveals the existence of correlations in physical systems that cannot arise from classical mechanisms. On the other hand, from the quantum computing point of view, entanglement constitutes a supplemental resource without equivalent in classical computing, allowing us to think that a quantum computer might solve problems of higher complexity than their classical counterpart.

In parallel to its relation to information, entanglement, is important in the characterization of topological phases of matter, as encountered in many-body interacting systems (spin liquids, fractional quantum Hall states, many-body localization). One of the goals of this project is just to exploit this relation between information, quantum states, and physical properties of condensed matter systems.

We are in particular interested in the link between *entanglement and interactions*. Indeed, the physical mechanism by which entanglement develops is particle interactions. As a specific system suitable to reveal the influence of interactions on entanglement, we investigate a two particle system evolving on general networks (quantum walk on graphs), whose interaction can be easily modified by choosing different "collision" operators (coin). We can in this way play, for instance, on the internal degree of freedom (spin) of the particles. Comparison between the free evolution (non interacting) and interacting one, can discriminate between quantum correlations related to the graph topology and quantum walk dynamics (swap and coin operators) and genuine interaction effects. The candidate will use analytical and numerical tools to explore the phenomenology of the interacting quantum walk, develop the appropriated information-theoretic measuring quantities, characterize the system's topology (for instance using an effective Hamiltonian or the symmetries of the unitary evolution operator), and eventually describe the behavior of the quantum states.


### General references

* B. Zeng, X. Chen, D.-L. Zhou, and X.-G. Wen. Quantum Information Meets Quantum Matter – From Quantum Entanglement to Topological Phase in Many-Body Systems. ArXiv e-print:1508.02595, 2015. [url](http://arxiv.org/abs/1508.02595)

* T. Kitagawa. Topological phenomena in quantum walks: elementary introduction to the physics of topological phases, Quantum Information Processing, 11, 1107 (2012). [url](http://dx.doi.org/10.1007/s11128-012-0425-4)
