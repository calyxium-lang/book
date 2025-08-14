## Installation

The first step is to install Calyxium. We'll download Calyxium through `calyxup`, a command line tool for managing Calyxium versions and associated tools. You’ll need an internet connection for the download.

> Note: if you prefer not to use `calyxup` for some reason, please see the
> [Alternative Calyxium Installation Methods page](ch01-alternative-installation.md) for more options.

The following steps install the latest stable version of Calyxium, which is compatible with all of the book's examples.
Some program outputs may vary from the book because Calyxium often improves error messages and warnings. 
In other words, any newer, stable version of Calyxium you install using these steps should work as expected with the content of this book.

> ### Command Line Notation
>
> Throughout the book, we’ll show some commands.
> Lines entered in the terminal all start with `$` or `>`.
> You don’t need to type either character; it’s the command line prompt shown to
> indicate the start of each command. Lines that don’t start with `$` typically
> show the output of the previous command. Unless stated otherwise, PowerShell-specific
> examples will use `>` rather than `$`.

### Calyxium Installer

Currently Calyxup isn't finished so you are going to have to install
the latest version semi manually from the [downloads page](https://calyxium-lang.github.io/downloads/)

### Installing `Calyxium` and `calyxup` on Windows, Linux and MacOS

> PowerShell is required for calyxup
> you can find instructions on how to install [PowerShell here](https://learn.microsoft.com/en-us/powershell/scripting/whats-new/migrating-from-windows-powershell-51-to-powershell-7?view=powershell-7.5)

Open a PowerShell terminal and enter the following command:

```console
> curl --proto '=https' --tlsv1.2 <add link> | pwsh -Command -
```
The command downloads a script and starts the installation of the `calyxup`
tool, which installs the latest stable version of Calyxium. You might be prompted
for your password.

#### TODO add install instructions when calyxup is done 

### Installing the `calyxium-lang` Extension

It is **highly recommended** to install the `calyxium-lang` extension by following the instructions [here](ch01-02-useful-development-tools.md#installing-the-calyxium-lang-extension).

