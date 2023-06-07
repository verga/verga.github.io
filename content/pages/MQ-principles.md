Title: Principles of quantum mechanics
Slug: MQ-principles
Date: 2020-01-26
Category: Lectures
Tags: teaching, quantum mechanics, undergraduates
Authors: Alberto Verga
Summary: Undergraduate course on quantum mechanics: principles
status: hidden

$\newcommand{\I}{\mathrm{i}} 
\newcommand{\E}{\mathrm{e}} 
\newcommand{\D}{\mathop{}\!\mathrm{d}} 
\newcommand{\Tr}{\mathrm{Tr}} 
\newcommand{\bra}[1]{\langle{#1}|}
\newcommand{\ket}[1]{|{#1}\rangle}
\newcommand{\braket}[1]{\langle{#1}\rangle}
\newcommand{\bbraket}[1]{\langle\!\langle{#1}\rangle\!\rangle}$

# Principles of quantum mechanics

We call quantum those phenomena involving the [Planck constant](https://physics.nist.gov/cgi-bin/cuu/Value?hbar|search_for=universal_in!),
$$\hbar = 1.054\, 571\, 817 \times 10^{-34} \mathrm{kg\,m^2\,s^{-1}} = 1$$
The first equality is the international system definition, and the second one means that this value is exact; it can thus be used as a relation between the energy unit J (joule) and the frequency unit s$^{-1}$:
$$1\,\mathrm{J} = 0.848\,252\,156 \times 10^{34} \,\mathrm{s^{-1}}$$
The Planck constant has the dimensions of an action. The classical action is related to the lagrangian of a mechanical system by the formula
$$S[q] = \int_{t_1}^{t_2} \D t L(q,\dot{q}), \; q(t_1)=q_1,\, q(t_2)=q_2$$
where $q(t)$ is the trajectory between the fixed points $q_1,q_2$. Observables in physics correspond to *local* dimensional quantities, such as position, angular momentum, energy, temperature, electromagnetic field, etc. The action $S$, which is a *functional* of the trajectory $q(t)$, is therefore nonlocal. The fundamental consequence is that quantum phenomena has not a specific (length, energy) scale. In this respect *nature is quantum*.

The first observed experimental phenomenon explicitly showing $\hbar$, was the thermal radiation emitted by any material at a fixed temperature. This radiation results from the equilibrium established at this temperature, between matter and photons, and cannot be described at any energy scale, by the laws of classical thermodynamics: the emission covers the entire range of energies, from zero to infinity.

Magnetism is also a macroscopic manifestation of a quantum property of matter: the intrinsic angular momentum of electrons, protons and neutrons, called *spin*.

Even in perfectly classical systems, possess quantum properties, hidden into their physical parameters. The motion of an incompressible fluid like water, for instance, is governed by Navier-Stokes equations. Their qualitative behavior is determined by the reynolds number $Re = LU/\nu$, a nondimensional combination of the characteristic flow length $L$ and velocity $U$ scales, and the viscosity $\nu$. The viscosity is one example of a transport coefficient, like the thermal conductivity, the resistivity of a metal, or the polarization of a dielectric. All these coefficients are related with the scattering cross section, which is ultimately quantum.

The most fundamental experimental facts about quantum systems are that the quantum states are a kind of information resource, their superposition is also a quantum state and their evolution preserves the amount of information; in addition, elementary particles, like photons or electrons, are identical.

In classical physics information is related to thermodynamics through the entropy and its relation to the Shannon entropy, and the fundamental Landauer principle, which states that erasing a bit of information amounts to an increase of $k_\mathrm{\small B}\ln 2$ (where $k_\mathrm{\small B} = 1.380\, 649 \times 10^{-23} \mathrm{J\,K^{-1}} = 1$ is the [Boltzmann constant](https://physics.nist.gov/cgi-bin/cuu/Value?k), which establishes a proportionality between energy an temperature). In quantum mechanics, it is the state itself that carries information.
