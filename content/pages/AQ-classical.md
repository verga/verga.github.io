Title: Classical information
Slug: AQ-classical
Date: 2020-09-07
Category: Lectures
Tags: teaching, advanced quantum mechanics
Authors: Alberto Verga
Summary: Information is physical (Landauer), Shannon entropy
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

# Information is physical

A discussion about Maxwell demon, the Szilard model, the Landauer principle, and the Bennett[^Bennett] solution of the paradox can be found in the [Leçon de physique]({filename}/L3-demon.md). For completeness I reproduce here the main point.

Maxwell devised an "intelligent being" that can distribute the molecules to the left or to the right of a vessel with two separated compartments, according to their velocities: to the left the faster ones and to the right the slower ones; hence obtaining from an initially equilibrium system a difference of temperature that can be used to push from the left to the right a piston. This is in contradiction with the second principle. Szilard simplified the problem to a system composed by a unique molecule and the demon a simple logical register that can store one bit, as in the figure:

> <img src="{static}/images/PS-szilard-2.svg" alt="Szilard engine plus demon" style="width: 320px;"/>
> 
> In the initial state (a) the particle is somewhere inside the box and the demon register is empty $(0,0)$, in the second panel (b) the demon identifies the position of the particle filling its left register $(0,1)$ (the three possible states of the register are empty, left, or right). It then applies a logical operation to put the piston on the correct side to gain work from the gas (c) *or* (c'). Finally (d), the particle recovers its initial state. Note however that the demon register is filled (one bit of information is stored), meaning the (d) is not equivalent to (a). Note the branching from (b) to (c), (c').

One important point of the Bennett argument to solve the paradox is based on the fact that logical operations can be donne reversibly (the step (c) in the figure). We know that logical circuits are build from elementary logical operators (gates in an electronic device). For instance the *not* gate takes an input bit and outputs a single bit implementing the logical table:

<blockquote>
<table style="width:200px;">
<caption>NOT gate</caption>
<tr>
<th>in</th>
<th></th>
<th>out</th>
</tr>
<tr>
<th>T</th>
<th>\(\rightarrow\)</th>
<th>F</th>
</tr>
<tr>
<th>F</th>
<th>\(\rightarrow\)</th>
<th>T</th>
</tr>
</table>
</blockquote>

where T stands for true and F for false; equivalently we may write,
\begin{align*}
  0 &\rightarrow 1\\
  1 &\rightarrow 0
\end{align*}
and the *nand* gate ("not and"):

<blockquote>
<table style="width:200px;">
<caption>NAND gate</caption>
<tr>
<th>in</th>
<th>in</th>
<th></th>
<th>out</th>
</tr>
<tr>
<th>T</th>
<th>T</th>
<th>\(\rightarrow\)</th>
<th>F</th>
</tr>
<tr>
<th>T</th>
<th>F</th>
<th>\(\rightarrow\)</th>
<th>T</th>
</tr>
<tr>
<th>F</th>
<th>T</th>
<th>\(\rightarrow\)</th>
<th>T</th>
</tr>
<tr>
<th>F</th>
<th>F</th>
<th>\(\rightarrow\)</th>
<th>T</th>
</tr>
</table>
</blockquote>

which takes two input bits $x, y \in \{0,1\} = \{\mathrm{F}, \mathrm{T}\}$ and outputs one:
$$(x,y) \rightarrow 1 \oplus xy$$
the output bit is the addition modulo 2 of 1 and the product $xy$. (Using the same operation the not gate is $x \rightarrow 1 \oplus x$.)

We see that while the not operation is reversible (you can infer the input form the output), the nand gate is irreversible: information of the input is lost under this operation. The Landauer principle states that erasing a bit increases the entropy by an amount $k_B \ln 2$ (in joules$/$kelvin). Therefore, if the Maxwell demon uses a logical circuit to decide if a given molecule must go to the left or to the right chambers, some dissipation would arise because of the irreversibility of the logical operation. However, it is not so difficult to show that a complete set of gates, a set which allows build any circuit, can be done reversibly. As a consequence, irreversibility will only appear in the last step of the Szilard cycle, when the demon register must be *erased* to recover its initial empty state. Under erasure entropy increases:
$$\Delta S = k_\mathrm{B} \ln 2 \quad (\text{demon}) \,,$$
which is *Landauer principle*.

One may argue that the necessity of erasing comes from the necessity to merge the two branches created after (b), (c) and (c'); and, physically, the necessity of branching in (b) comes from the random character of the particle motion.

In fact a reversible version of the nand gate was found by Toffoli gate; the main idea is to add two input bits in order to keep track of the initial state:
$$(x,y,z) \rightarrow (x,y,z \oplus xy)$$
when the third bit is 1 we recover the nand result. Note that the output is also a set of 3 bits, to ensure that we can recover the initial input. The Toffoli gate can be represented by a matrix:
$$\mathrm{toffoli} = \begin{pmatrix} 
  1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
  0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\
  0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\
  0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\
  0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\
  0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\
  0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 \\
  0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 \end{pmatrix}$$
that can be applied to the canonical base corresponding the 8 input bits: $000, 001,\ldots,111$; for example:
$$010 \rightarrow \begin{pmatrix} 0 \\ 0 \\ 1 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \end{pmatrix}\,.$$
You may find its inverse <strong style="color:DarkSlateBlue; background-color:LightGray;">EX</strong>.

In summary, the Maxwell demon establishes an interesting relationship between thermodynamics and information, through the Landauer principles (which is itself a form of the second principle applied to the unit of information, the bit).[^l]

# Shannon entropy[^s]

The basic model of information consists in an information *source*, a transmission *channel*, and destination *receiver*. These three components are build on a physical support. The source produces a *message* that is translated into a *signal* such that it can be sent using the channel to the receiver, which transforms the signal into the original message (perfect channel communication).

Consider a message as a sequence of events $x$ whose probability is $p(x)$. For instance, the events can be a string of $N$ binary digits, or a sequence of letters in the set $\{x_1, \ldots, x_K\}$, chosen from an alphabet of $K$ symbols. For the binary alphabet we have the probability distribution $p(0) = p$ and $p(1) = 1-p$. A classical physical system with two distinguishable states can encode a *bit* of information. A bit is the elementary unit of information.

In the Shannon model, information is related to a set of messages emitted by a source, encoded using an alphabet whose letters $x$ are distributed according with some probability distribution $p(x)$. A measure of the information might be the effective number of symbols needed to faithfully encode the message $NH$, with $N$ is the number of events in the message. The optimal length per symbol $H$ is the Shannon entropy. We require the following properties to by satisfied by $H$:

* $H$ depends only on the probability $p(x)$; 
* $H = H(p)$ is a continuous function;
* if the probability $p$ is uniform (for example $p_k = 1/K,\, \forall k \in \{1, \ldots, K\}$), $H$ should be a monotonic increasing function of alphabet length ($K$);
* $H$ is *additive*: if the choice of $\{p_1,p_2,\ldots\}$ can be subdivided into successive choices, then $H$ is the weighted sum of the individual values of $H$; take for instance,
$$p = \{p_1, p_2, p_3\}$$
    and
$$q = \{p_1, q_1, q_2, q_3 | q_1 = 1 - p_1, q_1q_2 = p_2, q_1q_3=p_3\}$$
    then,
$$H(p) = H(p_1,q_1) + q_1 H(q_2,q_3)$$
    (see the figure below for an example)

> <img src="{static}/images/AQ-tree.svg" width="300">
> 
> The information measure of the two trees are equivalent, but with different distributions:
> $$H(1/2,1/3,1/6) = H(1/2,1/2) + \frac{1}{2} H(2/3,1/3)$$
> Note that the sum of the arguments of $H$ is always 1.

This last property means that there exists a function $I(p_n)$ for fixed $p_n$, satisfying,

* $I = I(p_n)$ is continuous and,
* it is additive $I(p_n,p_m) = I(p_n) + I(p_m)$
* such that,
    
    $$H(p) = \braket{I} = \sum_n I(p_n) p_n\,.$$

It is straightforward to demonstrate that $I = -\text{const.} \log(p_n)$ <strong style="color:DarkSlateBlue; background-color:LightGray;">EX</strong>, and thus that
\begin{equation}
    H(p) = -\sum_n p_n \log p_n
    \label{e:Hp}
\end{equation}
the Shannon *entropy*. The constant is determined by the condition $\log 2 = 1$, which fixes the entropy of a bit to be one (in accordance with the definition of the information unit). Therefore, $\log \cdot = \log_2 \cdot$ stands for the base 2 logarithm (base $\E$ logarithm is denoted by $\ln$).

The shannon entropy allows a rigorous definition of the unit of information: a bit corresponds to the entropy of a random variable taken two values with equal probability.

### Exercises

1. Demonstrate that $H(pq) = H(p) + H(q)$.
2. Calculate and draw $H(p)$ for a bipartite system with distribution $\{p, 1-p\}$.
3. Consider two random variables $x$ and $y$ whose joint distribution is $p(x,y)$; show that:
$$H(p) \le H_x(p) + H_y(p)$$
    where $p(x) = \sum_y p(x,y)$, and
    $$H_x(p) = -\sum_{xy} p(x,y) \log p(x) = -\sum_x p(x) \log p(x),$$
    and similar definitions for $p(y)$ and $H_y$. You may use the fact that $\log x \le (x-1)/ln 2$.
4. Define the conditional probabilities:
$$p(x|y) = \frac{p(x,y)}{p(y)},\; p(y|x) = \frac{p(x,y)}{p(x)}\,.$$
    Show that
$$H(x,y) = H(x) + H(y|x) = H(y) + H(x | y)\,,$$
    where we use the notation $H(x) = H_x(p)$, $H(y) = H_y(p)$, and the conditional entropy is defined by,
$$H(y | x) = -\sum_{xy} p(x,y) \log p(y | x),\; H(x | y) = - \sum_{xy} p(x,y) \log p(y)\,.$$
   Deduce the inequality,
$$H(y) \ge H(y | x)\,.$$
5. A message is written in an alphabet of 4 characters $\{a,b,c,d\}$, whose frequencies are
$$\{p(a) = 1/2, p(b) = 1/4, p(c) = 1/8, p(d) = 1/8\}$$
    It is possible to code these four characters using two bits by
    $$\{00, 01, 10, 11\},$$
    however this code is not optimal. Compute the length per character in bits of a typical message coded with
    $$\{0,10,110,111\},$$
    in which we use fewer bits to code the liker characters (Answer: $7/4$), and show that it corresponds to the Shannon entropy. Compare the result with the 2 bits code.

    Find the messages coded by the string $001001100010111$.

## The Turing machine

An algorithm can be defined as a series of instructions aiming at solving a given problem. A constructive way to mathematically specify an algorithm is through specific models of computation. A problem itself can be viewed as the computation of a general boolean function, a functions which takes and gives binary values $f: \{0,1\}^{n} \rightarrow \{0,1\}^{m}$ (in the case $m=1$ the algorithm solves questions that can be answered by yes or no). For instance, a universal set of gates provides a way to compute any boolean function (definition of universal); actually, the nand gate is universal: any other gate can be implemented by a convenient set of nand gates. The computation of $f$ can then be implemented by a circuit defined as a sequence of gates which transforms input bits into an output, the answer.

Another universal model of computation was devised by Turing in the form of a machine consisting in a tape and a read-write head, a set of internal states and a program. The thesis put forward by Turing (Church-Turing thesis) states that

> a Turing machine can solve any algorithmic problem, or equivalently, the class of Turing machine computable functions corresponds to the class of functions computable by means of algorithms.

Elements of the Turing machine (figure below):

1. A *tape* divided into cells numbered from 0 to infinity $0, 1, 2, \ldots$, containing a finite number of letters from an alphabet $a$, typically $\{0,1\}$ and a symbol for a blank cell $b$, which can separate numeric cells, or fill the rest of the tape.
2. A *control unit*, which can be in any of a finite set of internal states $s_1,s_2, \ldots, s_n$. In addition, there are two special states, the starting state $s_0$ and the halting state $s_h$.
3. A head that can *read* the cell content and *write* a new character into it; the head can also move to the left ($L$) or to the right ($R$).
4. During the computation the internal state changes according to a series of statements or instructions called a *program*, which in addition control the motion of the head together with the read and write operations. Each instruction has the structure:
$$s, a, \bar{s}, \bar{a}, m$$
    where $s$ is the actual state of the cell containing $a \in \{0,1,b\}$, $\bar{s}$ is the new state of the cell, in which the head writes the new letter $\bar{a}$, and $m = L, R$ is the motion of the head to the left or to the right.

> <img src="{static}/images/AQ-turing_m.svg" alt="transition state diagram" style="width: 320px;"/>
> 
> Turing machine: each cell of the tape contains a character from an alphabet, here the numers 0 and 1, and blank "b" (empty cell), the head read and writes characters according to the instructions of a program; as a result the internal state of the machine changes.

A program instruction is then of the form $(s_1,a_1,s_2,a_2,m)$ corresponding to the code

```python
read(current_state, current_letter)
if (current_state == s_1) and (current_letter == a_1):
    new_state = s_2
    write(a_2)
    move(m)
```

where $s_1$ is the cell's current state and $a_1$ the current letter of the alphabet $a$; then the program changes the internal state to $s_2$ and writes the new value $a_2$ in the cell tape, finally it moves the head one step in the direction $m$.

A set of such rules can be conveniently represented by a "transition diagram" in which a state is a labeled circle, and the transition between states are arrows labeled with the current and new letters, and the direction of the head motion ($a_1,a_2,m$ in the previous example). The transition graph contains all the information of the program.

An example of a program is given by the transition state diagram below. It solves the question: is the number of ones in a given binary string even or odd? It consists on two states $s_1$ which represents "odd", and $s_2$ which represents "even"; the initial state is on the leftmost character and $s_1$. Once the head reach a blank cell, it writes $1$ if the machine last state was $s_1$, and 0 if it was $s_2$. Reading the last cell we get the answer to the question.

> <img src="{static}/images/AQ-turing_tsd.svg" alt="transition state diagram" style="height: 200px;"/>
> 
> This transition diagram describes a program to compute the parity of a binary string: if the number of 1 is odd it writes 1 and it writes 0 otherwise, at the end of the string. The initial state is $s_1$, and the initial position is on the leftmost number. The arrows correspond to the program instructions, for instance $1,0,R$ means that the cell is in state 1, one writes 0 and move to $R$.

### Exercice

Write the program corresponding to the previous transition diagram.

## Notes

[^Bennett]: Bennett, "The thermodynamics of computatio," Int. J. Theor. Phys. **21**, 905 (1982) ([.pdf]({static}/pdfs/Bennett-1982fk.pdf))

[^s]: C. E. Shannon, *A mathematical theory of communication*, Bell syst, J., **27**, 379 (1948) [.pdf]({static}/pdfs/shannon.pdf)

[^l]: R. Landauer, *Information is physical*, Phys. Today **44**, 23 (1991) [.pdf]({static}/pdfs/Landauer-1991.pdf)

