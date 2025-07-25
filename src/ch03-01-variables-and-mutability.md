# Variables and Mutability

By default, variables are immutable. This is one of the many nudges Calyxium gives you to write your code in a way that takes advantage of the safety that Calyxium offers. However, you still have the option to make your variables mutable. Let’s explore how and why Calyxium encourages you to favor immutability and why sometimes you might want to opt out.

When a variable is immutable, once a value is bound to a name, you can't change that value. To illustrate this, generate a new file called `variables.cx` in your `projects` directory.

Then, open `variables.cx` and add it's following code which won't interpret just yet:

<span class="filename">Filename: `variables.cx`</span>

```calyxium
let x: int = 10
x := 12
```

Save and run the program using `calyxium variables.cx`. You should receive an error message regarding an immutability error, as shown in this output:

This example shows how the interpreter helps you find errors in your programs.
interpreter errors can be frustrating, but really they only mean your program
isn’t safely doing what you want it to do yet; they do _not_ mean that you’re
not a good programmer! Experienced <add word for what we call people that use calyxium> still get interpreter errors.

You received the error message:
`` random `x` `` because mutable doesn't exist `x` yet **add later**.