Title: Quantum chaos
Slug: qc
Date: 2017-01-20
Category: Lectures
Tags: quantum, chaos
Authors: Alberto Verga
Summary: Chaos arises in quantum systems beyond their semiclassical counterpart: randomly distributed energy levels of (deterministic) Hamiltonians, localization transition driven by a periodic perturbation, irregular (fractal) eigenfunctions in many body systems.
status: hidden

$\newcommand{\I}{\mathrm{i}} \newcommand{\E}{\mathrm{e}} \newcommand{\D}{\mathop{}\!\mathrm{d}}$

[&raquo;chaos]({filename}CH-index.md)

The idea that the complex spectrum of heavy nucleons could be associated with a random (and correlated) distribution of levels given by the eigenvalues of a *random matrix* Hamiltonian, comes back to Wigner and Landau in the fifties:

> From very general considerations one expects that levels with the same spin are distributed in such a way that the probability of a very small spacing will be very small--the levels act as though *repelling* each other. This problem merits investigation ([Landau & Smorodinsky]).

The important point about this idea is that it relates *deterministic* quantum systems (Hamiltonian) to a seemingly stochastic behavior (energy spectrum and eventually, dynamics). Random behavior of deterministic systems is usually referred as *chaos*.

However, the first investigations of chaos in quantum systems dealt with systems whose corresponding classical companions were chaotic. The question was about the existence (or not) of quantum signatures of classical chaos. This bridge between quantum and classical systems can be defined, in principle, only in the *semiclassical* limit. In fact even in this limit essential differences may arise: chaotic classical systems can correspond to regular quantum systems, and classical integrable systems may have irregular quantum counterparts. Two conjectures guided the early research for chaos in quantum systems:

* The level spacings distribution of a quantum system close to an *integrable* classical system, is Poissonian ([Berry & Tabor]).
* For quantum systems corresponding to chaotic classical systems, the irregular part of the spectrum is well described by the random matrix ensembles ([Bohigas et al.]).

We first investigate the relationship between classical and quantum chaos through the simple [kicked rotator]({filename}CH-kicked.md) model. The kicked rotator exhibits a rich phenomenology, and in particular, contrary to the standard map in the global chaotic regime for which the particle undergoes a diffusive motion, the spreading of the quantum particle is stopped by a [dynamical localization]({filename}CH-kicked-localization.md) effect, analogous to the Anderson localization metal-insulator transition of a particle in a disordered potential. We end with a discussion of the [random matrices ensembles]({filename}CH-rm.md), in order to relate the symmetry properties of the quantum hamiltonian to the statistical properties of its spectrum. 

The interest in quantum chaos was recently renewed because it is related to the fondations of statistical machanics, as first investigated by von Neumann who discused the ergodic hypothesis in the quantum context, and to a variety of phenomena in many-body systems undergoing a localization transition (see the review of [D'Alessio, 2016](http://dx.doi.org/10.1080/00018732.2016.1198134)).

### Bibliography

* Berry, *Semiclassical mechanics of regular and irregular motion*, Les Houches, 1983. ([.pdf]({static}/pdfs/Berry-1983fv.pdf))
* Bohigas, *Chaotic motion and random matrix theories*, Springer, 1984. ([.pdf]({static}/pdfs/Bohigas-1984fk.pdf))
* Casati et al., *Stochastic behavior of a quantum pendulum under a periodic perturbation*, Lecture Notes in Physics, Springer, 1979. ([.pdf]({static}/pdfs/Casati-1979kx.pdf))
* D'Alessio et al., *From quantum chaos and eigenstate thermalization to statistical mechanics and thermodynamics*, Adv. Phys. 2016. ([.pdf]({static}/pdfs/DAlessio-2016fj.pdf)) 
* Wigner, *Random matrices in physics*, SIAM Review, 1967. ([.pdf]({static}/pdfs/Wigner-1967ve.pdf))

[&raquo;chaos]({filename}CH-index.md)[&raquo;kicked rotator]({filename}CH-kicked.md)[&raquo;dynamical localization]({filename}CH-kicked-localization.md)[&raquo;quantum walk]({filename}CH-qrw.md)[&raquo;random matrices]({filename}CH-rm.md)

[Landau & Smorodinsky]:http://link.springer.com/book/10.1007/978-1-4899-6457-1
[Berry & Tabor]:http://dx.doi.org/10.1098/rspa.1977.0140
[Bohigas et al.]:http://dx.doi.org/10.1103/PhysRevLett.52.1

