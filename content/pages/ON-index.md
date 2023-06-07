Title: Outils numériques
Slug: ON-index
Date: 2020-12-16
Category: Lectures
Tags: teaching, numerical methods
Authors: Alberto Verga
Summary: Travaux pratiques sur les méthodes numériques, unix, python, introduction aux algorithmes de calcul
status: hidden

$\newcommand{\I}{\mathrm{i}} 
\newcommand{\E}{\mathrm{e}} 
\newcommand{\D}{\mathop{}\!\mathrm{d}}$

> Work in progress

# TeX: scientific typesetting

This course consists in three tutorials on the $\LaTeX$ typesetting system, with focus on the structure of a scientific report and the use of the corresponding tools, necessary to build a bibliography data base, draw sketchy diagrams and plots.

* Introduction to LaTeX, [scientific typesetting]({filename}TP-latex_0.md)
* Guidelines to write a [scientific document]({filename}TP-latex_1.md)
* [Graphic tools]({filename}TP-latex_2.md) (tikz, matplotlib)
* [Presentations with beamer]({filename}TP-latex_3.md)

**Exam**: report of 4-6 pages, about, preferentially, a subject on a simple physical system or mathematical tool (oscillator, lenses, coulomb, carnot cycle, fourier transform, special functions, etc.), including a tikz diagram, a matplotlib figure, bibtex references, and code listings.

# Outils numériques

Cette série de travaux pratiques sur ordinateur ont pour but de nous familiariser avec l'environnement de travail numérique utilisé en laboratoire, et d'introduire le langage python pour l'appliquer au calcul scientifique et au traitement des données.

Programme des séances de travaux pratiques (30h):

* Révisions - environnement UNIX et commandes shell, notions de bases en programmation Python: types de base et les collections; structures de contrôle de condition et de répétition; fonctions; modules [numpy](https://numpy.org/doc/stable/), [scipy](https://docs.scipy.org/doc/scipy/reference/) et [matplotib](https://matplotlib.org/contents.html);

* Application à des calculs numériques élémentaires sur, e.g. des suites définies par récurrence, des séries de fonction;

* Tableaux du module numpy et fonctions associées, manipulations de tableaux et slicing, et exemple d'application manipulation d'images;

* Calcul d’intégrale avec les méthodes usuelles: rectangles, trapèze, Simpson, introduction de la méthode de Monte Carlo. Importance de la discrétisation et notion de convergence.

* Méthode des moindres carrés. Application à la régression linéaire;

* Équations différentielles ordinaires. Schéma d'intégration explicite-implicite. Les méthodes méthodes de Newton et de Runge Kutta d'ordre 2 sont reprogrammées et appliquées à un problème de type ballistique. Introduction des fonctions ad hoc du module scipy;

* Décomposition en série de Fourier, illustration du phénomène de Gibbs;

* Générateur nombre aléatoire, marche aléatoire, diffusion.


Ressources en ligne: [unix]({filename}ON-unix.md), [python]({filename}ON-python.md)

