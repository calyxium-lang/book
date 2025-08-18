# Control Flow

> Under Construction

The ability to run some code depending on whether a condition is `true` and to run some code repeatedly while a condition is `true` are basic building blocks in most programming languages. The most common constructs that let you control the flow of execution of Calyxium code are `if` expressions and loops.

### `If` Expressions

An `if` expression allows you to branch your code depending on conditions. You
provide a condition and then state, “If this condition is met, run this block
of code. If the condition is not met, do not run this block of code.”

```calyxium,no
let number = 3 in

if number < 5 then print("condition was true") else print("condition was false")
```

All `if` expressions start with the keyword `if`, followed by a condition. In
this case, the condition checks whether or not the variable `number` has a
value less than 5. The block of code to execute if the condition is true follows immediately after the then keyword. Similarly, the block to execute if the condition is false follows the optional else keyword. These blocks of code are sometimes called arms.

Optionally, we can also include an `else` expression, which we chose to do
here, to give the program an alternative block of code to execute should the
condition evaluate to `false`. If you don’t provide an `else` expression and
the condition is `false`, the program will just skip the `if` block and move on
to the next bit of code.

Try running this code; you should see the following output:
```
condition was true
```

Let’s try changing the value of `number` to a value that makes the condition
`false` to see what happens:
```calyxium,no
let number = 7 in

if number < 5 then print("condition was true") else print("condition was false")
```

Run the program again, and look at the output:
```
condition was false
```

It’s also worth noting that the condition in this code _must_ be a `bool`. If
the condition isn’t a `bool`, we’ll get an error. For example, try running the
following code:
```calyxium,no
let number = 3 in

if number then print("condition was true") else print("condition was false")
```

The `if` condition evaluates to a value of `3` this time, and Calyxium throws an
error:
```
.\main.cx: Type error in `if` expression condition:
  Expected: bool
  Found:    int
```

The error indicates that Calyxium expected a `bool` but got an integer. Unlike
languages such as Ruby and JavaScript, Calyxium will not automatically try to
convert non-Boolean types to a Boolean. You must be explicit and always provide
`if` with a Boolean as its condition. If we want the `if` code block to run
only when a number is not equal to `0`, for example, we can change the `if`
expression to the following:

```
let number = 3 in

if number != 0 then print("number was something other than zero")
```

Running this code will print `number was something other than zero`.

> Note: `if` expressions in Calyxium are expression based, which means they evaluate
> to a value. You can assign their result to a variable or use them directly in larger expressions.