## Comments

All programmers strive to make their code easy to understand, but sometimes
extra explanation is warranted. In these cases, programmers leave _comments_ in
their source code that the interpreter will ignore but people reading the source
code may find useful.

Here’s a simple comment:

```calyxium,no
-- hello, world
```

In Calyxium, the idiomatic comment style starts a comment with two dashes, and the
comment continues until the end of the line. For comments that extend beyond a
single line, you’ll need to include `--` on each line, like this:

```calyxium,no
-- So we're doing something complicated here, long enough that we need
-- multiple lines of comments to do it! Whew! Hopefully, this comment will
-- explain what's going on.
```

### Documentation Comments

Calyxium also supports a second kind of comment, **documentation comments**. These are used to provide structured, tool-readable documentation for your code, such as functions, constants, or modules.

Here’s a simple documentation comment:

```calyxium,no
-- $ hello, world i am a documentation comment $
```

In Calyxium, documentation comments follow the **same syntax rules** as normal comments, but with a special marker (`-- $ ... $`) to distinguish them. These comments are designed to integrate with your text editor to provide features like:

- Hover tooltips  

For example:

```calyxium
-- $ Returns the square of a number $
let square(x) {
    x * x
}
```

> To enable documentation comment support in your editor, install the [calyxium-lang Extension](ch01-02-useful-development-tools.md#installing-the-calyxium-lang-extension).

