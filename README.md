# Ruby_Lexer

This is the delivery for the second homework assignment of Compilers
Construction of Innopolis University, Fall 2018

# Description
**Ruby_Lexer** is a project that makes a full lexical analysis for _Ruby_
programming language. Analyzer is implemented as standalone function
working on demand: each call detects next token from the input stream
and returns its representation. Analyzer detects all kinds of tokens:
delimiters, operators, keywords, identifiers, literals.

# Basic workflow

Lexer reads the file `in.txt` and looks at each symbol sequentially.
It determines the kind of token by some first symbols that it encounters:
if it is a letter, then it is either a keyword or identifier, if it is a
digit, then it may be an int or a float, and so on. If it meets the
comment, it skips it. When it finishes analysis of the input, it writes
in `out.txt` the tokens and their representation.

# How to use

**Run program**

`python main.py` 

**Run tests**
 
 `python test_lexer.py`

# Tokens
We have several kinds of tokens - keywords, identifiers,
string literals (any string between single or double quotes), numbers
(can be integer, float, hex, bin, oct), parentheses, delimiters, and
operators (arithmetic, logical, relational, etc). We do not distinguish
between different kinds of operators (if needed, it can be easily done,
because we store not only the token, but its representation).

