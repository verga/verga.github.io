Title: Outils numériques: Unix
Slug: ON-unix 
Date: 2020-12-16
Category: Lectures
Tags: teaching, numerical methods
Authors: Alberto Verga
Summary: Commandes unix usuelles, outils de base, vim
status: hidden

$\newcommand{\I}{\mathrm{i}} 
\newcommand{\E}{\mathrm{e}} 
\newcommand{\D}{\mathop{}\!\mathrm{d}}$

# Commandes unix de base

Le système d'exploitation linux, dérivé libre d'unix, est particulièrement adapté pour le travail en sciences. Les langages de programmation comme C, fortran, python, les compilateurs (e.g. gcc), les bibliothèques (e.g. linpack), ainsi que les technologies web (e.g. html), ou les outils d'édition scientifique come TeX, ont tous été développés dans le cadre d'unix.

À la différence des systèmes dont le but est essentiellement de faire tourner une série (fixe) de logiciels, comme Windows par exemple pour le travail administratif avec Office, le système linux est ouvert: il permet de controller complètement le fonctionnement de votre ordinateur.

L'interaction de l'utilisateur avec le système unix se fait à travers un terminal; le terminal  execute  un programme appelé `shell`, lequel interprète et exécute à son tour les commandes introduites par l'utilisateur avec le clavier. Les commandes unix de base sont généralement des mots de deux lettres: ls, cd, mv, rm, qui effectuent des tâches comme afficher la liste de fichiers, changer de dossier, déplacer un fichier ou le supprimer. Les commandes peuvent aussi ouvrir des logiciels, compiler un code, effectuer des mises à jour, ou par exemple, se connecter à un site extérieur pour récupérer des données.

#### Exercices:

* Ouvrez le terminal et tapez la commande d'aide `man man`, ici le commande `man` affiche les informations à propos de la commande `man`. Répondez aux questions: common avance-t-on d'une page? comment revient-on en arrière d'une page? comment quit-on la commande?

* Tapez la commande `ls` et notez la différence avec `ls -al`

## Fichiers

Le système de fichiers d'unix est organisé selon une structure arborescente, la racine `/` est le "parent" de tous les autres dossiers, elle contienne, entre autres, les répertoires `/usr` avec les bibliothèques et les exécutable, et le dossier `/home` qui est la base des utilisateurs: par exemple le répertoire `/home/dupont` est le "home directory" de l'utilisateur Dupont (attention, unix distingue les majuscules). Un autre répertoire important est `/usr/bin`, lequel regroupe notamment les commandes du système. Le répertoire `/etc` contient les fichiers de configuration du système.

En unix, les fichiers n'ont pas nécessairement d'extension (comme txt, pdf, c, png,...), pour afficher leur type on utilise la commande `file` suivie du nom du fichier.

Le nom d'un fichier peut être absolu, quand il est spécifié par son chemin depuis la racine, par exemple `/home/dupont/Documents/Textes/notes.txt`, ou relatif, quand son chemin commence par le dossier courant; dans l'exemple précédent si on se trouve sur Documents, ce serait `Textes/notes.txt`. 

### `ls, cd, pwd, du`

`ls` liste les fichiers du répertoire courant; pour savoir dans quel dossier vous êtes, tapez `pwd` (present working directory); pour changer de dossier tapez `cd` suivi du chemin de votre dossier (path). Le dossier présent est désigné par un point `.`, le dossier parent par `..`, le dossier parent du parent `../..`, la racine par `/`; le dossier home par `~`. Par exemple, le chemin vers votre dossier Documents est `/home/dupont/Documents` ou `~`. 

La commande `du` sert à afficher la taille des répertoires: `du -sh Documents/*` donne la taille totale (option -s) en unités lisibles (option -h); l'étoile (\*) liste tous les sous-dossiers et fichiers dans Documents.

#### Exercices:

* Tapez successivement `cd / <CR>` (`<CR>` c'est return --retour chariot), `pwd <CR>`, `cd <CR>` et enfin `pwd` Où est allez vous vous promener?

| CMD | &nbsp; OPT &nbsp; |  description |
| :--- | :---- | :---- |
| ls   |  | liste les fichiers du répertoire courant |
| | -a | liste les fichiers cachés |
| | -l | propriétés des fichiers, liste détaillée |
| | -t | les plus récents en premier |
| | | `ls -lh *.pdf` liste les fichiers pdf avec la taille exprimée en Kb, Mb, Gb (`-h`)
| cd path |  | change de répertoire selon le chemin |
| | ~ | répertoire personnel (home) |
| | .. | parent |
| | | `~/.config/nvim`  va au sous-dossier nvim du répertoire caché .config de `/home/$USER`|
| pwd| | affiche le répertoire courant |
| du | | liste la taille des fichiers et dossiers donnés comme arguments |
| | -s | (summarize) taille totale, autrement vous obtenez une liste exhaustive |
| | -h | utilise les unités en K, M, G octets (bytes)
| | -d n | (depth) descend l'arborescence de n niveaux; -s est équivalent à -d 0 |

### `mkdir, cp, mv, rm, touch, source`

Pour créer un dossier il suffit de taper `mkdir nomdudossier`. Si vous faites `mkdir nom du dossier` vous créez trois dossiers... Un nom avec espaces doit être mis entre guillemets, ou utiliser le caractère d'échappement `\` comme dans `nom\ du\ dossier`.

`cp fichier1 fichier2` crée le deuxième fichier, copie du premier; la commande `cp imgage1.png images/` copie "image1.png" dans le dossier "images" avec le même nom (notez, c'est important, que le chemin fini par un slash, ou barre, qui est le caractère de séparation des dossiers).

Pour renommer ou transférer un fichier "file1.txt" vers un autre dossier on utilise `mv`: `mv file1.txt ../.` met le fichier dans le dossier parent; `mv file1.txt fichier1.txt` change le nom (en français).

Le caractère `*` (wildcard pattern) remplace zero ou plus des caractères: par exemple, `*.pdf` désigne tous le noms de fishier avec extension `.pdf` (portable document file). Si vous voulez nommer les fichiers `a1, a2, a2, a4` vous pouvez ne pas répéter la partie commune avec `a{1,2,3,4}` ou encore `a{1..4}`. Ces raccourcis peuvent être utilisés avec les commandes de fichiers.

La commande `rm` efface irréversiblement fichiers et dossiers: `rm *.pdf` efface du répertoire courant les fichiers dont le nom termine par `.pdf`; `rm -rf rep1/` efface l'arborescence commençant par le repertoire rep1 (sous-répertoire du répertoire courant).

Pour créer un fichier vide on peut faire `touch nom` (cette commende actualise la date si nom existe déjà); un autre façon de créer un fichier vide est d'utiliser la redirection `>`, par exemple `> nom.txt` crée le fichier nom.txt en y ajoutant rien. Cette dernière recette vous permet par exemple, de créer un fichier contenant la sortie de ls: `ls -l Documents/* > "liste de mes dossiers.txt"`


| CMD | &nbsp; OPT &nbsp; |  description |
| :--- | :---- | :---- |
| mkdir | | (make directory) crée le répertoire donné en argument |
|  | -p | crée les parents aussi: mkdir -p rep1/rep2 crée rep1 et rep2 |
| cp | | copie des fichiers et dossiers |
| | -r | copie récurrente des dossiers et tous ses sous-dossiers | 
| mv | | (move) déplace, ou renomme, fichiers et répertoires |
| rm | | (remove) efface fichiers et dossiers *définitivement* |
| | -rf &nbsp; | efface récursivement le dossier dans l'argument |
| touch | | crée un fichier vide: `touch note.txt` |
| source | | sert à mettre à jour un script shell: `source ~/.config/nvim/init.vim` |
| | | `source ~/.bashrc` execute le script de configuration de votre session shell |


### `tar, gzip`

Pour créer un archive des fichiers et le compresser on utilise la commande `tar`; son format est `tar -options tarfile /path/dossier/` avec les options `-cf` pour créer (c) l'archive tar (f) nommé tarfile, avec les fichiers contenus dans /path/dossier/ (notez le slash final!). Si vous voulez compresser l'archive tarfile il suffit d'ajouter l'option `z`, qui applique la commande gzip automatiquement:

```bash
    tar -cvzf mes_codes.tar.gz ~/codes/
```

crée l'archive mes_codes (avec les extensions correspondant a `tar` et `gzip`) avec les fichiers dans votre dossier codes. La commande:

```bash
    tar -xvf mes_codes.tar.gz
```

extrait les fichiers et les mets dans le dossier courant; si vous voulez décompresser dans un autre dossier vous pouvez utiliser l'option -C:

```bash
    tar -xvf mes_codes.tar.gz -C codes_1
```

crée le dossier codes_1 avec les fichiers dans l'archive mes_codes.tar. L'option `-v` (verbose) affiche des information sur le résultat de la commande.

### `cat, more, head, tail`

Souvent on veut inspecter le contenu d'un fichier sans l'ouvrir. `cat` affiche dans le terminal la totalité du fichier, `more` affiche page para page (on peut aussi utiliser `less` qui est plus souple); `head` and `tail` montrent le début et la fin du fichier (par défaut 10 ligne, avec l'option -n 12, vous affichez 12 lignes).

Si vous avez deux fichiers f1.txt et f2.txt et vous voulez créer un fichier contenant f1 et f2 à la suite vous faites:

```bash
    cat f1.txt f2.txt > f3.txt
```

### `find, grep`

`find` cherche fichiers dans la hiérarchie des dossiers:

```bash
    find Documents/codes -name f1.txt
```

suit le chemin 'Documents/codes' et affiche les fichiers dont le nom est 'f1.txt', y compris dans tous les sous-dossiers de l'arborescence. Le nom du fichier peut contenir des jokers:

```bash
    find . -type f -name "*.dat" -print
```

'find' est la commande, '.' est le chemin (ici), '-type' est le type (f fichier, d dossier), '-name pattern' est le nom suivie du motif '"*.dat"': les guillemets tiennent compte des espaces dans le nom des fichiers avec extension finale '.dat', '-print' est une action (d'autres actions sont possible, par exemple -delete efface tout en dessous de ce qu'il trouve--danger!-- ou '-exec command' pour exécuter la commande 'command')

`grep -options pattern path` cherche dans le fichiers dans 'path' le motif donnée (pattern), les options les plus communes sont:

* `-i` ignorer la case (cherche également Dossier et dossier)
* `-r` cherche récursivement dans les sous-répertoires
* `-l` affiche uniquement le nom du fichier où 'pattern' est trouvé

Le chemin peut être spécifié avec des wildcards: 

```bash
    grep -l "<strong>" codes/*.html
```

affiche la liste des fichiers .html contenant le tag '&lt;strong&gt;' (les guillemets sont nécessaires), du dossier 'codes'.

## Shell

Le shell, c'est-à-dire le logiciel qui tourne sur votre terminal (pour simplifier), vous permet de contrôler votre ordinateur. Comme on l'a vu vous pouvez explorer le système de fichiers, vous pouvez lancer l'exécution des applications, ou la compilation des vos codes python, fortran, C ou latex; vous pouvez créer des nouveaux fichiers en utilisant l'éditeur (par exemple `vim` ou `nvim`, si neovim est installé).

Chaque programme actif est, sous unix, un processus contrôlé par le système (linux ou macos); pour obtenir une liste des processus on peut faire `top` ('q' pour quitter). `top` affiche le PID (process identifier), que vous permet de tuer un processus bloqué: `kill -9 1234` arrête le processus 1234 (où 1234 est, par exemple, le navigateur, ou la commande que vous avez lancée et que ne réponds plus).


## Éditeur: vim

L'éditeur `vim` est accessible depuis le terminal; il est présent dans toute distribution unix. C'est l'éditeur de choix de beaucoup de développeurs, particulièrement adapté à la programmation (python, fortran, latex, par exemple). Sa caractéristique distinctive c'est qu'il possède différents modes:

* le mode normal, auquel on accède en tapant vim dans le shell, attend des commandes; les commandes ont souvent la forme `ncm` avec `n` un nombre, `c` une commande (ou action) et `m` un mouvement (ou objet: ligne, mot, paragraphe...).  Par exemple, `3dw` efface (deletes) 3 mots (words). La commande `i` change en mode insertion;

* le mode insertion, qui correspond en fait au mode dans lequel on écrit son texte comme dans un éditeur usuel; on quite le mode d'insertion en frappant `<ESC>` (touche escape)
      
* le mode visuel, qui permet de sélectionner du texte (horizontalement et verticalement), auquel on accède depuis le mode normal en tapant `v`;

* le mode commande, accessible par `:`, qui sert à faire des recherches et remplacements, manipuler les lignes, ouvrir ou fermer des fichiers (buffers, windows, tabs)

On quite vim avec la commande `:wq` (on sauve `w` et on se sauve `q`). Notez que les commandes élémentaires n'ont qu'un caractère: en les combinant on peut effectuer des tâches complexes. Certaines commandes, commençant par `g` ou `z`, comportent deux caractères.

#### Exercice

Asseyez-vous. Tapez `vim` et une fois le logiciel ouvert (cet instantané) tapez `:Tutor` Levez vous une heure après.

#### Commandes basiques

`<ESC>` 
: $-$ passe au mode normal (commande), depuis par exemple le mode d'insertion

`i a I A` 
: $-$ passe au mode insertion, à la position du curseur (i), ou après le curseur (a), ou au début de la ligne (I), ou enfin à la fin de la ligne (A)

`o O`
: $-$ insère une ligne en dessous (o) ou au dessus (O), de la ligne courante

`h j k l`
: $-$ déplace le curseur un caractère vers la gauche (h) ou vers la droite (l), ou vers la ligne précédente (k) ou suivante (j)

`H M L` 
: $-$ positionne le curseur en haut (H), au milieu (M) ou en bas (L) de l'écran.

`^u ^d ^b ^f` 
: $-$ control u (^u) déplace le texte d'un demi écran vers le haut, (^l) le fait vers le bas; (^b) et (^f) font pareil, mais le déplacement se fait par écran entier (vers le haut et vers le bas, respectivement)

`gg G` 
: $-$ début du document (gg), fin du document (G)

`^ $` 
: $-$ début de la ligne (^) et fin de la ligne (\$)

`w b e W B E` 
: $-$ permettent de déplacer le curseur d'un mot en avant (w), en arrière (b), ou à la fin (e) du mot; les versions majuscules définissent le mot comme une succession des caractères entre deux espaces

`f F t T` 
: $-$ effectuent des mouvements du curseur sur la ligne: (fa) avance jusqu'au premier 'a', (F) va dans le sens opposé; (ta) avance jusqu'au caractère qui précède, et (T), va dans la direction opposée.

`x dd d` 
: $-$ efface un caractère (x) ou n caratères (nx); (dd) efface la ligne, et (d) suivi d'un mouvement efface jusqu'à la nouvelle position du curseur: pour effacer un mot on fait `dw`, pour effacer 3 mots contenant de nombres `d3W` 

`r s c C`
: $-$ (r) remplace un caractère et reste en mode normal, (s) substitue le caractère sous le curseur et passe en mode insertion; pour changer le mot entier on utilise `c` ou `C` pour une chaîne alpha-numérique.

`y yy p P`
: $-$ pour sélectionner un texte on fait `y` suivi d'un mouvement, par exemple `y$` copie le texte jusqu'à la fin de la ligne courante; `p` colle le texte sélectionné par `y` après le curseur et `P` à partir de la position du curseur; (yy) copie la ligne. Grosso modo, y correspond à copier et p a coller.

`u ^r`
: $-$ (undo) remonte la liste de tous les changements en remettant le texte dans son état précédent; control r remet l'état à l'état présent


## Notes

Voici quelques liens utiles sur unix:

* [Linux guide](https://en.wikibooks.org/wiki/Linux_Guide)
* [Bash shell scripting](https://en.wikibooks.org/wiki/Bash_Shell_Scripting)
* [Vim help](https://vimhelp.org/)
