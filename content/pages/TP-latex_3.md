Title: LaTeX recipes: presentations
Slug: TP-latex3
Date: 2019-12-01
Category: Lectures
Tags: teaching, latex
Authors: Alberto Verga
Summary: A practical introduction to the numerical tools for scientific writing: beamer presentations
status: hidden

$\newcommand{\I}{\mathrm{i}} 
\newcommand{\E}{\mathrm{e}} 
\newcommand{\D}{\mathop{}\!\mathrm{d}}
\newcommand{\bra}[1]{\langle{#1}|}
\newcommand{\ket}[1]{|{#1}\rangle}
\newcommand{\braket}[1]{\langle{#1}\rangle}
\newcommand{bm}{\boldsymbol}$

> [Workshop]({filename}ON-index.md) on scientific typesetting.

# Beamer presentations

[Beamer](https://en.wikibooks.org/wiki/LaTeX/Presentations) is a latex class for technical presentations. The [manual (.pdf)](https://www.ctan.org/pkg/beamer) contains a full description of the package.

## Beamer template

A typical beamer source file is:

```tex
\documentclass[utf8, xcolor={table}]{beamer}
%
% theme
\usetheme{Rochester}
\usecolortheme{dove}
\setbeamertemplate{navigation symbols}{}  % no navigation bar
\usepackage{multimedia} % display movies
%
\usepackage{tikz} % add libraries if needed
%
\begin{document}
%
\title{your title}
\author[short name]{long name}
\institute[short address]{your institution full name}
\date[short date]{long date}

\begin{frame}
\titlepage % makes the first slide
\end{frame}
%
% ABSTRACT
\begin{frame}{Abstract}
your abstract
\end{frame}

\begin{frame}{Outline}
\tableofcontents % make an index based on \section
\end{frame}
%
% TEXT
\section{your section}
%
%
% FRAMES
\begin{frame}{your frame title}
your text
\end{frame}
% more sections, subsections, ...
% more frames
\end{document}
```

### Theme

A theme ([see the theme matrix](https://mpetroff.net/files/beamer-theme-matrix/)) is defined by the theme name and the theme color:

```tex
\usetheme{Theme name}
\usecolortheme{color theme name}
```

A combination of theme and color gives you a large variety of possibilities; however, it is rather easy to customize your theme with, for instance, your choice of colors (see the manual).

### Frame formatting

Frames can be formatted using standard latex structures. For instance, you may use two columns slide, to separate text and figures:

```tex
\begin{frame}{frame title}
%
\begin{columns}[c]
\begin{column}{0.65\textwidth} % you may change the column width
\includegraphics[width=0.99\textwidth]{figure name}
\end{column}
%
\begin{column}{0.35\textwidth} % 0.65 + 0.35 = 1
your text
\end{column}
\end{columns}
%
\end{frame}
```

It is also possible to display multimedia contents. A *movie frame* uses the ``multimedia`` package which defines the ``\movie`` command:

```tex
\begin{frame}{frame title}
\begin{center}
\movie[externalviewer,height=7cm]{%
\includegraphics[height=7cm]{figure mask}}{%
movie file.mp4}
\end{center}
\end{frame}
```

You may use boxes for important text, and other similar structures for theorems, examples, or remarks; their appearance depends on the theme, and can alose be fully customized:

```tex
...
\begin{block}{important result}
Use nondimensional parameters
\end{block}
...
```

You may navigate inside your presentation using hyperlinks:

```tex
\label{XXX} % somewhere inside a frame
...
\hyperlink{XXX}{\beamerbutton{click here} to find XXX}
```

The command ``\beamerbuttom`` creates a cliquable button on your pdf. Note that the command ``\frame`` accepts the option ``label=name``, which can be used in a hyperlink.

### Effects

You may display the presentation table of contents at each new section to recall the structure of your talk:

```tex
% Outline sections
\AtBeginSection[]{\begin{frame}{Outline}
  \tableofcontents[currentsection]
\end{frame}}
```

Beamer allows the creation of *overlays*, to control the way a slide contents is displayed. For example, you may uncover items of a list step by step:

```tex
...
\begin{itemize}
\item <1-> this item is visible when the slide starts
\item <2-> this item appears after a click
\item <3-> next one
\end{itemize}
...
```

Use ``tikz`` in your slides!

> <img src="{static}/images/TP-sch.png" style="width : 250px;" />

```tex
\begin{frame}{Schrödinger equation}
\begin{tikzpicture}
\uncover<1->{
\node[draw, rectangle, fill=gray!20] (S) at (0,0)
  {$\displaystyle \I \frac{\partial }{\partial t} \ket{\psi} =
    H(t) \ket{\psi}$};
}
\uncover<2->{
\node[draw,rectangle] (U) at (3,2)
  {$\displaystyle U(t,0) =
    \mathbb{T} \E^{-\I\int_0^t \D t_1 H(t_1)}$};
\draw (S) -| (U);
}

\bigskip

\uncover<3>{
\BLC{Note the time ordered product}}
\end{tikzpicture}
\end{frame}
```

In this example we defined a color text style (uses the ``xcolor`` package, invoked as a class option):

```tex
\definecolor{colLight}{RGB}{255, 255, 235} % light yellow
\definecolor{colDark}{RGB}{90, 40, 19} % dark sienna
\newcommand{\BLC}[1]{\colorbox{colDark}{\textcolor{colLight}{#1}}}
\newcommand{\BDC}[1]{\colorbox{colLight}{\textcolor{colDark}{#1}}}
```

and used the macros:

```tex
\usepackage{braket}
\newcommand{\I}{\mathrm{i}}
\newcommand{\E}{\mathrm{e}}
\newcommand{\D}{\mathrm{d}}
```

you may insert in the preamble. Note the use of ``uncover`` to show first the Shrödinger equation, then the evolution operator, and eventually the remark (colored text).

## Modes

Beamer can be set in different modes: presentation, handouts, transparencies, and article modes:

* ``presentation`` is the default mode, it creates the slides (defined by the ``\frame`` command);
* ``handouts`` creates supplementary material the audience can read during the presentation;
* ``trans`` creates a stack of slides without the overlays, in fact a printable version of your talk;
* ``article`` ignores frames and transfers the scope to other document class (article, book); in this case you change the class to "article" and load ``\usepackage{beamerarticle}``

Thus, playing with the presentation and article mode, you can have one source (.tex) file with your paper and your talk:

* mode presentation ``\documentclass[ignorenonframetext]{beamer}``
* mode article 
```tex
    \documentclass{article}
    \usepackage{beamerarticle}
```

The commands ``\mode<article>{some text}`` and ``\mode<presentation>{some text`` make "some text" available only in the specified mode.

### Notes

You may also add notes inside your slides: ``\note{your text}`` creates a separate page just after your slide page, with the note text. It is also possible to use the command outside a specific frame:

```tex
\begin{frame}
    slide text...
\end{frame}
\note{ note text... }
```

Notes are ignored in article mode.

