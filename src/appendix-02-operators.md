# Appendix B: Operators and Symbols

This appendix contains a glossary of Calyxium's syntax, including operators and other symbols that appear by themselves or in the context of paths, comments, tuples, brackets.

### Operators

Table B-1 contains the operators in Calyxium, an example of how the operator would appear in context, a short explanation.

<span class="caption">Table B-1: Operators</span>

| Operators                 | Example                                                 | Explanation                                                           |
| ------------------------- | ------------------------------------------------------- | --------------------------------------------------------------------- |
| `not`                     | `not expr`                                              | logical complement.                                                   |
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
| `lsl`                     | `expr lsl expr`                                         | Left-shift.                                                           |
| `lsr`                     | `expr lsr expr`                                         | Right-shift.                                                          |
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
| `lor`                     | `expr lor expr`                                         | Bitwise OR.                                                           |
| `lxor`                    | `expr lxor expr`                                        | Bitwise XOR.                                                          |
| `lnot`                    | `lnot expr`                                             | Bitwise NOT.                                                          |
| `land`                    | `expr land expr`                                        | Bitwise AND.                                                          |
| `->`                      | `pat -> expr`                                           | Part of match arm syntax.                                             |
| `\|>`                     | `var \|> expr`, `expr \|> expr`                         | Passes left-hand value as input to right-hand expression.             |
| `\|`                      | `\| pat`                                                | Part of match arm syntax.                                             |
| `!`                       | `!var`                                                  | Dereference mutable copy.                                             |
| `^`                       | `string ^ string`                                       | String concatenation.                                                 |
| `@`                       | `array @ array`                                         | Array concatenation.                                                  |
| `..`                      | `1..10`, `1..`                                          | Range operator (inclusive).                                           |
| `?`                       | `cond ? expr : expr`                                    | Part of ternary conditional operator.                                 |
| `:`                       | `var: type`, `cond ? expr : expr`, `array[start:end]`   | Type ascription or ternary branch separator, or slice range separator.|
| `;`                       | `expr; expr`                                            | Expression separator.                                                 |
| `.`                       | `object.field`                                          | Member access.                                                        |
| `_`                       | `match x with \| _ -> ...`                              | Wildcard pattern.                                                     |
| `,`                       | `(a, b)`                                                | Comma separator (lists, tuples, args).                                |
| `:=`                      | `var := expr`                                           | Mutable copy assignment.                                              |

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