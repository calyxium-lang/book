# Appendix B: Operators and Symbols

This appendix contains a glossary of Calyxium's syntax, including operators and other symbols that appear by themselves or in the context of paths, comments, tuples, brackets.

### Operators

Table B-1 contains the operators in Calyxium, an example of how the operator would appear in context, a short explanation.

<span class="caption">Table B-1: Operators</span>

| Operators                 | Example                                                 | Explanation                                                           |
| ------------------------- | ------------------------------------------------------- | --------------------------------------------------------------------- |
| `!`                       | `!expr`                                                 | logical complement.                                                   |
| `!=`                      | `expr != expr`                                          | Nonequality comparison.                                               |
| `==`                      | `expr == expr`                                          | Equality comparison.                                                  |
| `>`                       | `expr > expr`                                           | Greater than comparison.                                              |
| `<`                       | `expr < expr`                                           | Less than comparison.                                                 |
| `>=`                      | `expr >= expr`                                          | Greater than or equal to comparison.                                  |
| `<=`                      | `expr <= expr`                                          | Less than or equal to comparison.                                     |
| `&&`                      | `expr && expr`                                          | Short-circuiting logical AND.                                         |
| `+`                       | `expr + expr`                                           | Arithmetic addition.                                                  |
| `-`                       | `expr - expr`                                           | Arithmetic subtraction.                                               |
| `-`                       | `- expr`                                                | Arithmetic negation.                                                  |
| `*`                       | `expr * expr`                                           | Arithmetic multiplication.                                            |
| `/`                       | `expr / expr`                                           | Arithmetic division.                                                  |
| `%`                       | `expr % expr`                                           | Arithmetic remainder.                                                 |
| `**`                      | `expr ** expr`                                          | Arithmetic power.                                                     |
| `<<`                      | `expr << expr`                                          | Left-shift.                                                           |
| `>>`                      | `expr >> expr`                                          | Right-shift.                                                          |
| `>>>`                     | `expr >>> expr`                                         | Logical Right-shift.                                                  |
| `=`                       | `var = expr`                                            | Assignment.                                                           |
| `+=`                      | `var += expr`                                           | Arithmetic addition and assignment.                                   |
| `-=`                      | `var -= expr`                                           | Arithmetic subtraction and assignment.                                |
| `*=`                      | `var *= expr`                                           | Arithmetic multiplication and assignment.                             |
| `/=`                      | `var /= expr`                                           | Arithmetic division and assignment.                                   |
| `&=`                      | `var &= expr`                                           | Bitwise AND and assignment.                                           |
| <code>&#x60;=</code>      | <code>var &#x60;= expr</code>                           | Bitwise OR and assignment.                                            |
| `$=`                      | `var $= expr`                                           | Bitwise XOR and assignment.                                           |
| `<<=`                     | `var <<= expr`                                          | Left-shift and assignment.                                            |
| `>>=`                     | `var >>= expr`                                          | Right-shift and assignment.                                           |
| `++`                      | `var++`, `expr++`                                       | Incrementation.                                                       |
| `--`                      | `var--`, `expr--`                                       | Decrementation.                                                       |
| <code>&#x60;</code>       | <code>expr &#x60; expr</code>                           | Bitwise OR.                                                           |
| `$`                       | `expr $ expr`                                           | Bitwise XOR.                                                          |
| `~`                       | `~ expr`                                                | Bitwise NOT.                                                          |
| `->`                      | `pat -> expr`                                           | Part of match arm syntax.                                             |
| `\|>`                     | `var \|> expr`, `expr \|> expr`                         | Passes left-hand value as input to right-hand expression.             |
| `\|`                      | `\| pat`                                                | Part of match arm syntax.                                             | 

Table B-2 shows symbols that create comments.

<span class="caption">Table B-2: Comments</span>

| Symbol     | Explanation             |
| ---------- | ----------------------- |
| `--`       | Line comment            |
| `-- $`     | Inner line doc comment  |

Table B-3 shows the contexts in which curly braces are used.

<span class="caption">Table B-3: Curly Brackets</span>

| Context      | Explanation      |
| ------------ | ---------------- |
| `{...}`      | Block expression |

Table B-3 shows the contexts in which square brackets are used.

<span class="caption">Table B-3: Square Brackets</span>

| Context                                            | Explanation                                                                           |
| -------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `[...]`                                            | Array literal                                                                         |
| `expr[expr]`                                       | Collection indexing. Overloadable (`Index`)                                           |