## Installation

The first step is to install Calyxium. We'll download Calyxium through `calyxi`, a command line tool for managing Calyxium versions and associated tools. You’ll need an internet connection for the download.

> Note: if you perfer not to use `calyxi` for some reason, please see the
> [Other Calyxium Installation Methods page](#) for more options.

The following steps install the latest stable version of the Calyxium interpreter. Calyxium's stability guarantees ensure that all the examples in the book that
compile will continue to compile with newer Calyxium versions. The output might
differ slightly between versions because Calyxium often improves error messages and
warnings. In other words, any newer, stable version of Calyxium you install using
these steps should work as expected with the content of this book.

> ### Command Line Notation
>
> In this chapter and throughout the book, we’ll show some commands used in the
> terminal. Lines that you should enter in a terminal all start with `$`. You
> don’t need to type the `$` character; it’s the command line prompt shown to
> indicate the start of each command. Lines that don’t start with `$` typically
> show the output of the previous command. Additionally, PowerShell-specific
> examples will use `>` rather than `$`.

### Installing `calyxi` on Linux or macOS

If you're using Linux or macOS, open a terminal and enter the following commnad:

```console
$ curl --proto '=https' --tlsv1.2 <add link> -sSF | sh
```
The command downloads a script and starts the installation of the `calyxi`
tool, which installs the latest stable version of Calyxium. You might be prompted
for your password. If the install is successful, the following line will appear:

```text
Calyxium is installed now. Great!
```