Title: LaTeX recipes: graphics
Slug: TP-latex2
Date: 2019-11-16
Category: Lectures
Tags: teaching, latex
Authors: Alberto Verga
Summary: A practical introduction to the numerical tools for scientific writing: graphics
status: hidden

$\newcommand{\I}{\mathrm{i}} 
\newcommand{\E}{\mathrm{e}} 
\newcommand{\D}{\mathop{}\!\mathrm{d}}
\newcommand{\bra}[1]{\langle{#1}|}
\newcommand{\ket}[1]{|{#1}\rangle}
\newcommand{\braket}[1]{\langle{#1}\rangle}$

> [Workshop]({filename}ON-index.md) on scientific typesetting.

# Graphics tools

You may find a large choice of [graphic python libraries](https://pyviz.org/):

* ``matplotlib`` is the basic package to plot functions in 1D and 2D, basic histograms, contour and density plots, including text tools (you may use latex for the labels). See the [gallery of examples](https://matplotlib.org/gallery/index.html). It can be associated with other libraries such [``pandas``](https://pandas.pydata.org/) for data analysis, or [``networkx``](https://networkx.github.io/) for graph theory.
* [``holoviews``](http://holoviews.org/) which aggregates many graphic tools and allow for interacting pictures integrated in [``jupiter notebooks``](https://jupyter.org/).

There are also graphic libraries oriented to be used in $\TeX$ documents:

* [``TikZ``](http://www.texample.net/tikz/examples/) is the best solution to insert figures directly using the text source; it has a large variety of libraries to be used in various domains, as for instance elementary geometry, graph theory, networks or quantum circuits, see the [gallery](http://www.texample.net/tikz/examples/).
* [``Asymptote``](http://asymptote.sourceforge.net/) a sophisticated graphic language, which includes 3D tools.

The python libraries are included in the [anaconda distribution](https://www.anaconda.com/distribution/). The $\TeX$ tools are included in the TeX Live distribution, you do not need to install them.

## Matplotlib example

The Lennard Jones potential depends on two parameters, the hard core lenght $r_0$ and the binding energy $\epsilon$:

$$ w(r) = 4\epsilon \left[ \left(\frac{r_0}{r}\right)^{12} - \left(\frac{r_0}{r}\right)^{6}   \right]$$<Paste>

```python
x = linspace(0.95, 2.5, 128) # x-points
y = 4*(1/x**12 - 1/x**6) # LJ
# plot
plot(x, y, 'k-')
plot([0,2.7], [0,0], ':', color = '0.35')
plot([0.8,1.4], [-1,-1], ':', color = '0.35')
plot([1,1], [-0.7,0.7], ':', color = '0.35')
# labels and text
xlabel(r'$r/r_0$')
ylabel(r'$w(r)/\epsilon$')
text(1.05,0.13, r"$r_0$")
text(0.6,-1, r"$-\epsilon$")
savefig('lj.pdf') # save figure in pdf format
```

> <img src="{static}/images/TP-lj.svg" style="width:250px;"\img>

Note that it is possible to embed python code directly in the tex source file using the package [``pythontex``](https://github.com/gpoore/pythontex) (included in the texlive distribution).

In order to obtain compatible styles between matplotlib graphics and latex text, you may create a matplotlib style file:

```python
lines.linewidth : 1.0
text.usetex : True
font.family : serif
font.weight : normal
font.size : 20.0
font.serif : STIX Two Text, DejaVu Serif, Computer Modern Roman, serif
mathtext.fontset : stix
mathtext.rm : serif
axes.titlesize : 24
axes.labelsize : 24
xtick.top : True
ytick.right : True
xtick.direction : out
ytick.direction : out
figure.figsize : 6.0, 4.5
savefig.bbox : tight
savefig.dpi : 300
```

where we use $\LaTeX$ for the figure labels, define the figure size $6\times 4.5$ (aspect ratio 4:3), and suitable font sizes. For the fonts we use ``stix``. However, the standard choice, available in every operating system, is Computer Modern Roman (serif) and cm (math fonts). This file must be created inside the ``.config/matplotlib/stylelib`` folder and have the extension ``.mplstyle``; it is invoked within python with ``plt.style.use('name')``, if your file name is ``name.mplstyle``.

## TikZ ist kein Zeichenprogramm

[TikZ](https://mirrors.chevalier.io/CTAN/graphics/pgf/base/doc/pgfmanual.pdf) and [pgfplots](https://mirrors.chevalier.io/CTAN/graphics/pgf/contrib/pgfplots/doc/pgfplots.pdf) are popular graphics packages. Tikz is specially useful for schematic drawing, diagrams, graphs with nodes and links, geometry, and in general it is perfect to illustrate mathematical and physical concepts. At variance, pgfplots needs often external programs (like gnuplot) and can be replaced by standard graphical programming libraries (matplotlib is an example).

**tikz**. The package is loaded with ``\usepackage{tikz}`` you may also need to load specialized libraries like: ``\usetikzlibrary{calc,positioning,scopes,shapes}``.

```tex
\documentclass{article}
\usepackage{tikz}
\usetikzlibrary{calc,positioning,scopes,shapes}
...
%
\begin{document}
...
\begin{tikzpicture}
   ...
\end{tikzpicture}
...
\end{document}
```

**tikzpicture**. The picture environment, where you put your tikz code, is ``tikzpicture``. You may choose many options, for instance  ``scale=2`` or ``node distance=5mm``, etc. The style of the pictures can be globally defined by ``\tikzset{every picture/.style={line width=2pt, color=red!80}}``; if instead of ``every picture``, which is pre-defined, you use a name, this name is globally available; styles can also be defined as option of tikzpicture; options can also be defined inside the tikzpicture using the ``scope`` environment; a convenient way to use ``scope`` is to load the ``scopes`` library.

**path**. The drawing commands are ``\path``, ``\draw``, ``\fill`` and ``\clip``. Path and clip do not draw anything by themselves, but for example ``\path[draw]`` is equivalent to ``\draw``. A path is basically a sequence of coordinates; the linking operator can be ``--`` (segment) or ``..`` (curve).

Coordinates can be given as an ordered pair $(x,y)$ (canvas) or $(\phi:r)$ (canvas polar), or by name ``(node name)``; relative coordinates with respect to the current position are given bi $+(,)$ (without update) or $++(,)$ (with position update):

* to draw a rectangle: ``\path[draw] (0,0)--(0,1)--(1,1)--(1,0)--cycle`` ('cycles' ensures a closed path), or a shifted one ``\draw (1,3) -- +(0,1) -- +(1,1) -- +(1,0) --cycle``, or equivalently ``\draw (1,3) -- ++(0,1) -- ++(1,0) -- ++(0,-1) --cycle``

    ![tikz]({static}/images/TP-r.svg)

```tex
\begin{tikzpicture}
\path[draw] (0,0)--(0,1)--(1,1)--(1,0)--cycle;
\draw[fill=blue!60] (1,1.2) -- +(0,1) -- +(1,1) -- +(1,0) --cycle;
\draw[fill=red!60] (1,-1.2) -- ++(0,1) -- ++(1,0) -- ++(0,-1) --cycle;
\end{tikzpicture}
```

**node**. It is the tikz basic construction. It can be specified by ``\node['options'] ('name') at 'coordinate' {'label'}``, or as a part of a path:

``\path (0,0) node {A} (1,0) node {B} (1,1) node {C} (1,-1) node {D};`` 

![tikz]({static}/images/TP-n.svg)

A more complicate example, using fine positioning:


```tex
\begin{tikzpicture}[
  every node/.style={draw, minimum size=1cm, fill=gray!25, rounded corners},
  ]
\node[minimum width=5cm] (M) {$M$};
\node[above=of M.north west, anchor=south west] (A) {$a$};
\node[above=of M] (B) {$b$};
\node[above=of M.north east, anchor=south east] (C) {$c$};
\draw[->] (M.north -| A) -- (A);
\draw[->] (M) -- (B);
\draw[->] (M.north -| C) -- (C);
\draw[-] (M.west) -- +(-1,0);
\draw[-] (M.east) -- +(1,0);
\end{tikzpicture}
```

![tikz]({static}/images/TP-nn.svg)

Observe the relative positions in this case: ![tikz]({static}/images/TP-rel.svg)

```tex
\begin{tikzpicture}
  \fill[gray!50] (0,0) circle (2pt)
    node[anchor=south,black] {$S$} 
    node[anchor=north] {$N$} 
    node[anchor=east] {$E$} 
    node[anchor=west] {$W$};
\end{tikzpicture}
```

You see that the dot (filled circle), which is the drawn *object*, is located to the south of the node labeled $S$, the node is then anchored to the north of the object, and similarly for the other nodes.

Some node options are: shape (rectangle, circle, etc.), anchor (above, below, left, right, etc.), ``every node/.style={...}``, inner sep, outer sep (separation), minimum height, minimum width, and many others!

Nodes can be used as 'coordinates', this is useful to connect them by paths and edges:

```tex
\begin{tikzpicture}
  \path (-1,0) node[circle,draw] (a) {$\uparrow$}
        (0,1) node[circle,draw] (b) {$\downarrow$}
        (1,0) node[rectangle,draw,red!80!black] (c) {$\uparrow$};

      \path[<->] (a) edge node[above left] {$-J$} (b)
            edge[red!50!black] node[below] {$+J$} (c)
        (b) edge node[above right] {$-J$} (c);
\end{tikzpicture}
```

``edge`` inherits the options form the surrounding path ![tikz]({static}/images/TP-f.svg)

A sequence of similar path commands can be obtained using the **foreach** operation, ``\path ... foreach 'variables' ['options'] in {'path commands'} ... ;``

```tex
\begin{tikzpicture}
  \foreach \x in {0,1,2,3}
    \draw (\x,0) -- (\x,3);
  \foreach \y in {0,1,2,3}
    \draw (0,\y) -- (3,\y);
  \foreach \x in {0,1,2,3}
    \foreach \y in {0,1,2,3}
      \path (\x,\y) node[circle, fill=gray!20, 
                       rotate=180*(0.5*rand+1), 
                       draw] {$\rightarrow$} ;
\end{tikzpicture}
```

![tikz]({static}/images/TP-s.svg)

where we used ``rand`` for a random orientation of the node arrows.

### Example: quantum circuit

The following circuit describes the Deutsch algorithm, which allows to determine using a single evaluation of $f(x)$, if the boolean function is balanced. We use the package [``quantikz`` by Alastair Kay](https://arxiv.org/abs/1809.03842):

```tex
\documentclass{standalone}
\usepackage{tikz}
\usetikzlibrary{external,quantikz}
\tikzexternalize % create pdf of figures with the
                 % external library 
                 % compile with the -shell-escape option
%
\begin{document}
\tikzset{ slice/.append style={gray}}
\begin{quantikz}
\lstick{$\ket{0}^{\otimes n}$} & 
\gate{H^{\otimes n}} \slice{$\ket{\psi_1}$} &
  \ctrl{1} \slice{$\ket{\psi_2}$} & 
  \gate{H^{\otimes n}} \slice{$\ket{\psi_3}$} &
  \qw\\
\lstick{$\ket{1}$} &
  \gate{H} &
  \gate{y \otimes f(x)} &
  \qw &
  \qw
\end{quantikz}
\end{document}
```

![tikz]({static}/images/TP-c.svg)
