## Hello, world!

Now that you've installed Calyxium, it's time to write your first Calyxium program. It's traditional when learning a new language to write a little program that prints the text Hello, world! to the screen, so we’ll do the same here!

### Creating a Project Directory

You'll start by making a directory to store your Calyxium code. It doesn't matter to Calyxium where your code lives, but for the exercises and projects in this book, we suggest making a _projects_ directory in your home directory and keeping all
your projects there.

Open a terminal and enter the following commands to make a _projects_ directory
and a directory for the `“Hello, world!”` project within the _projects_ directory.

For Linux, macOS and PowerShell on Windows, enter this

```console
$ mkdir ~/projects
$ cd ~/projects
$ mkdir hello_world
$ cd hello_world
```
For Windows CMD, enter this:

```cmd
> mkdir "%USERPROFILE%\projects"
> cd /d "%USERPROFILE%\projects"
> mkdir hello_world
> cd hello_world
```

### Writing and Running a Calyxium Program

Next, make a new source file and call it `main.cx`. Calyxium files always end with
the `.cx` extension. If you’re using more than one word in your filename, the
convention is to use an underscore to separate them. For example, use
`hello_world.cx` rather than `helloworld.cx`.

Now open the `main.cx` file you just created and enter the code in listed below.

<Listing number="1-1" file-name="main.cx" caption="A program that prints `Hello, world!`">

```calyxium
println("Hello, world!")
```

</Listing>

Save the file and go back to your terminal in the
`~/projects/hello_world` directory. On Linux or macOS, enter the following
commands to run the file:

```console
$ calyxium main.cx
Hello, world!
```

Regardless of your operating system, the string `Hello, world!` should print to
the terminal.

If `Hello, world!` did print, congratulations! You’ve officially written a Calyxium
program. That makes you a Calyxium programmer—welcome!

Let’s review this “Hello, world!” program in detail.

```calyxium
println("Hello, world!")
```

This line does all the work in this little program: it prints text to the screen. There are two important details to notice here.

First, `println` calls the function to display contents to you're terminal.

Second, you see the `"Hello, world!"` string. We pass this string as an argument to `println`, and the string is printed to the screen.