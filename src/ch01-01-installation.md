## Installation

The first step is to install Calyxium. We'll download Calyxium through `calyxup`, a command line tool for managing Calyxium versions and associated tools. You’ll need an internet connection for the download.

> Note: if you perfer not to use `calyxup` for some reason, please see the
> [Other Calyxium Installation Methods page](#) for more options.

The following steps install the latest stable version of Calyxium, which is compatible with all of the book's examples.
Some program outputs may vary from the book because Calyxium often improves error messages and warnings. 
In other words, any newer, stable version of Calyxium you install using these steps should work as expected with the content of this book.

> ### Command Line Notation
>
> Throughout the book, we’ll show some commands.
> Lines entered in the terminal all start with `$` or `>`.
> You don’t need to type either character; it’s the command line prompt shown to
> indicate the start of each command. Lines that don’t start with `$` typically
> show the output of the previous command. Generally, PowerShell-specific
> examples will use `>` rather than `$`.

### Installing `Calyxium` and `calyxup` on Windows, Linux and MacOS

> PowerShell is required for clayxup
> you can find instructions on how to install [PowerShell here](https://learn.microsoft.com/en-us/powershell/scripting/whats-new/migrating-from-windows-powershell-51-to-powershell-7?view=powershell-7.5)

Open a PowerShell terminal and enter the following commnad:

```console
> curl --proto '=https' --tlsv1.2 <add link> | pwsh -Command -
```
The command downloads a script and starts the installation of the `calyxup`
tool, which installs the latest stable version of Calyxium. You might be prompted
for your password.

# TODO add install instructions when calyxi is done 
