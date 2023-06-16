Title: Plasma: Quasilinear theory
Slug: plasma-ql
Date: 2016-01-24 12:00
Category: Lectures
Tags: plasma, diffusion, instability, Landau damping
Authors: Alberto Verga
Summary: Quasilinear theory of collisionless plasma instabilities.
status: hidden


$\newcommand{\I}{\mathrm{i}} 
\newcommand{\E}{\mathrm{e}} 
\newcommand{\D}{\mathop{}\!\mathrm{d}} 
\newcommand{\Di}[1]{\mathop{}\!\mathrm{d}#1\,} 
\newcommand{\Dd}[1]{\frac{\mathop{}\!\mathrm{d}}{\mathop{}\!\mathrm{d}#1}}$

[&raquo;chaos]({filename}CH-index.md)[&raquo;maps]({filename}CH-map.md)[&raquo;stability]({filename}CH-cds.md)[&raquo;hamiltonian systems]({filename}CH-hamilton.md)[&raquo;plasmas]({filename}CH-plasma.md)

# Quasilinear theory
## Nonlinear saturation of instabilities

The Landau theory of electrostatic fluctuations around a stationary state $F_0(v)$ shows that a state possessing for same velocity range, a positive slope $F'_0>0$, is unstable with a rate proportional to this slope,
$$
\gamma(k) =
  \frac{\pi \omega^3}{2k^2}  \left. \frac{\partial F_0(v) }{\partial v}
  \right|_{v=\frac{\omega}{k} }\,.
$$ 
As a consequence, the amplitude of a fluctuation with wavenumber $k$ will grow exponentially in time. To describe the evolution of the instability, and eventually its saturation, we must explore the nonlinear effects. The idea is to split the distribution function in two parts, a slow uniform one $f_0$, describing the dynamics of the mean value around a fluctuating part, the fast one $\delta f$:
$$
f(x,v,t) = f_0(v,t) + \delta f(x,v,t)\,, \quad
\langle f(x,v,t) \rangle = f_0(v,t)
$$
and to limit the nonlinear description to the slow part: $|\delta f| \ll |f_0|$. After substitution into the Vlasov equation, we have,
$$
\frac{\partial f_0}{\partial t} + 
\frac{\partial \delta f}{\partial t} +
v\cdot \frac{\partial \delta f}{\partial x} - 
\frac{e}{m} E \cdot \frac{\partial f_0}{\partial v} -
\frac{e}{m} E \cdot \frac{\partial \delta f}{\partial v} = 0\,,
$$
where the electric field arises from the fluctuating part,
$$
\nabla \cdot E = - \frac{e}{\epsilon_0} \int \Di{v} \delta f\,.
$$
Averaging the previous equation, and putting by definition $\langle \delta f \rangle = 0$, we obtain the slow equation:
\begin{equation}
  \label{ql}
  \frac{\partial f_0 }{\partial t} = \frac{e}{m} \left\langle
  E \cdot \frac{\partial \delta f}{\partial v} \right\rangle\,,
  \quad
  \langle \cdots \rangle = \frac{1}{\mathrm{Vol}} \int_{\mathrm{Vol}} \cdots
\end{equation}
Subtracting this equation from the Vlasov equation, and neglecting the nonlinear term in the fluctuations, we obtain the linearized equation for the rapid part,
$$
\frac{\partial \delta f}{\partial t} +
v\cdot \frac{\partial \delta f}{\partial x} -
\frac{e}{m} E \cdot \frac{\partial}{\partial v} f_0(t) = 0\,,
$$
which can be solved by Fourier transform, in most the same way as we proceeded for the derivation of the Landau damping. This is possible because of the time scale separation between $f_0$ and $\delta f$: during the characteristic time of variation of the fluctuations one can assume that the mean value is almost constant. Retaining only the resonant terms given by the imaginary part of the dispersion relation:
\begin{equation}
  \label{qle}
  \frac{\partial f_0}{\partial t} = \frac{\partial }{\partial v} \cdot D(t) \cdot \frac{\partial }{\partial v} f_0\,, \quad
  D_{ij}(t) = \frac{\pi e^2}{m \mathrm{Vol}} 
  \int dk \langle E_i(-k,t) E_j(k,t) \rangle \delta(\omega - k \cdot v)\,,
\end{equation}
where $D=D(t)$ is a time dependent diffusion coefficient that must be determined self-consistently. Considering a Fourier mode $E \sim \E^{\I k\cdot x - \I \omega t}$ we observe that only the imaginary part of the frequency (slow with respect to the waves frequencies) appears in the integral: 
$$
\langle E_i(-k,t) E_j(k,t) \rangle = |E_k|^2 \E^{2\gamma_k t} \delta_{ij}
$$
(we use the fact that the electrostatic fluctuations are isotropic, this is no more true in presence of a magnetic field) or in a more general form:
\begin{equation}
  \label{qlenergy}
  \frac{\partial }{\partial t} \mathcal{E}(k,t) =  2 \gamma_k[f_0] \mathcal{E}(k,t)\,,
\end{equation}
with 
$$
 W_\mathcal{E}(t) = \frac{\epsilon_0}{2} \langle E(x,t)^2 \rangle =
 \int \Di{k} \mathcal{E}(k,t) = \frac{\epsilon_0}{4\pi \mathrm{Vol} } 
 \int \Di{k} \langle E_i(-k,t) E_j(k,t) \rangle
$$
the electrostatic energy, and where we stressed the dependence of the growth instability rate $\gamma_k$ on the slow distribution function. 

It is interesting to verify that the total energy of the plasma:
$$
W = \int \Di{v} \frac{mv^2}{2} f_0(v,t) + \int \Di{k} \mathcal{E} = \text{const.}
$$
is conserved.

## Relaxation of the bump on tail instability

A plasma in thermal equilibrium is perturbed by a hot beam of fast particles: the typical form of its velocity distribution is a superposition of two gaussian functions, one centered at $v=0$, and one centered at the beam mean velocity $v=v_0$. The plasma will be unstable if the ratio of thermal velocities $v_{0T}/v_T \ll 1$ is small, ensuring the existence of a range of positive slope velocities in the distribution function $f_0=f_0(v,0)$. It is a one-dimensional effect, only the velocity in the direction of the beam velocity is important.

General considerations allows us deduce the form of the growth rate and the diffusion coefficient without a detailed computation. Indeed, the growth rate is proportional to the slope $2\gamma_k = B(v) f'_0(v)$ where $B(v)$ depends on the precise form of the distribution function. The diffusion coefficient is proportional to the electrostatic energy, computed at the particle-wave resonance: $D=A(v) \mathcal{E}(\omega/v, t)$. With these definitions of the functions $A(v)$ and $B(v)$, the quasilinear equations become,
\begin{align}
  \frac{\partial }{\partial t}f_0(v,t) &= 
  \frac{\partial }{\partial v}A(v) \mathcal{E}(\omega/v,t) 
  \frac{\partial }{\partial v}f_0(v,t)\,,  \\
  \frac{\partial }{\partial t} \mathcal{E} &= B(v) \mathcal{E}(\omega/v,t)
  \frac{\partial }{\partial v} f_0(v,t)\,.
\end{align}
The asymptotic, independent of time $t\rightarrow\infty$, solution is
\begin{align}
\mathcal{E}(\omega/v, t) \frac{\partial }{\partial v} f_0(v, t) &=0 \\
\frac{\partial }{\partial v} \frac{A(v)}{B(v)} \mathcal{E} & = f_0(v,0) - f_0(v, t)
\end{align}
Therefore, there exists a range of velocities where the electrostatic energy is finite $\mathcal{E}\ne 0$, and the distribution function is constant $f'_0=0$, and other region, outside this one, in which the system remains at equilibrium with $\mathcal{E}=0$ and a distribution with a stable slope.

In the range of velocities $v_- < v < v_+$, where the boundaries are determined by the conditions of continuity and conservation of the number of particles:
$$
f(v_-) = f(v_+)\,, \quad
\int_{v_-}^{v_+} \Di{v} f_0(v,0) = \int_{v_-}^{v_+} \Di{v} f_0(v,t)\,,
$$
the velocity distribution develops a plateau, by diffusion in velocity space around the initial region of unstable modes, for which the electrostatic waves are in resonance with the plasma particles.

### Bibliography

* [Vedenov](https://link-springer-com.lama.univ-amu.fr/chapter/10.1007/978-1-4615-7799-7_3) *Theory of a Weakly Turbulent Plasma*, Reviews of Plasma Physics, 1967. ([.pdf]({static}/pdfs/Vedenov-1967uq.pdf))


[&raquo;chaos]({filename}CH-index.md)[&raquo;maps]({filename}CH-map.md)[&raquo;stability]({filename}CH-cds.md)[&raquo;hamiltonian systems]({filename}CH-hamilton.md)[&raquo;plasmas]({filename}CH-plasma.md)
