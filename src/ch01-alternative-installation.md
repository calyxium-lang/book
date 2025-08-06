# Alternative Installation methods

> Note: It is **highly** recommend that you use `calyxup`.
> [Standard Installation Method page](ch01-01-installation.md).\
> This guide is not for the faint hearted. You have been warned!\
> Currently this is the only method to install Calyxium

## Building it yourself

This method may not always result in a successful install as the version of Calyxium on Github may have some compatibility issues; especially if you use the dev branch. It is recommend that you stay on the the main branch which has less updates but should remain compatible for all devices. Of course, because you are using a more up to date version of Calyxium that has not been publicly released yet there may be new breaking changes that have not yet been documented in the books. With that out of the way, lets start with cloning the repository:

### Cloning the repository

The first thing you want to do to build calyxium yourself is to clone the [repository](https://github.com/calyxium-lang/calyxium)

> You will need some form of Git to clone the repository. [See methods here](https://github.com/git-guides/install-git#install-git-on-windows)

If you have [Github Desktop](https://github.com/apps/desktop) installed you can go to the [repository](https://github.com/calyxium-lang/calyxium)
and click the `Code` Button, then press the `Open with Github Desktop` button and Github Desktop should open asking you if you would like to clone the repository, press the blue `Clone` button.

---

If you do not have Github Desktop but do have Git installed you can enter the following command into any terminal.

Make sure you are in the target parent directory of where you want the repository to be cloned.\
This is normally located at `%USERPROFILE%\Documents\Github\` for Windows users. To ensure the repository is cloned to that location enter this command into your terminal.

```console
> git clone https://github.com/calyxium-lang/calyxium %USERPROFILE%\Documents\Github\calyxium
```

If you are not a Windows user or are already in the target parent directory run this command instead.

```console
> git clone https://github.com/calyxium-lang/calyxium
```

### Installing OCaml

Now that you have cloned the repository you will need to go through the process of installing OCaml onto your system.

You can download and install OCaml from the [official site](https://ocaml.org/install#win).

### Installing Dune

Once you have installed OCaml you will need to install Dune using the following command.

```console
$ opam install dune
```

---

If you are having issues with opam, remember to activate the opam switch with the following command on cmd.

```console
$ for /f "tokens=*" %i in ('opam env') do @%i
```

and for PowerShell use this command.

```console
> (& opam env) -split '\r?\n' | ForEach-Object { Invoke-Expression $_ }
```

> Please note that on Windows if you want to use the `dune` or `calyxium` commands you will need to run either of the above commands whenever you start a new terminal. `opam` should not require this. The book will assume you have ran the command above.

If you want to circumvent this you have 2 options, either add `dune` and `calyxium` to the [system environment variables](#adding-to-system-variables), or make a new [terminal profile](#creating-terminal-profile) which automatically runs the command when opened. It is recommend to do the latter approach because you don't have to do this same process if you use other opam tools, you should also add `calyxium` to the system variables so its accessible to all terminal processes; `calyxup` would normally do this for you.

#### Adding to system variables

To add `calyxium` to the system environment variables run this command in PowerShell. This is assuming you cloned the repository to the recommended path. 

For those curious `USERPROFILE` is just your `C:\Users\NAME\` Folder, but it works for everybody, so no need to change anything!

```console
> $target = "$env:USERPROFILE\Documents\GitHub\calyxium\_build\default\bin"; $old = [Environment]::GetEnvironmentVariable("Path", "User"); if (-not ($old -split ';' | ForEach-Object { $_.Trim() } | Where-Object { $_ -eq $target })) { [Environment]::SetEnvironmentVariable("Path", "$old;$target", "User") }
```

#### Creating terminal profile

To create a new terminal profile which automatically runs the command afore mentioned whenever opened begin by pressing `Windows` and then typing out `terminal` and pressing `enter`. This should open a new terminal. Now press the <code style="transform: scale(-1, -1);display: inline-block">^</code> button next to the `+` button. This should open a menu. Press the `Settings` button. Then down in the bottom left corner press the `Open JSON file` button. This should now open notepad. In here add the following JSON block in the list of profiles.

```json
{
    "colorScheme": "CGA",
    "commandline": "cmd.exe /k for /f \"tokens=*\" %i in ('opam env') do @%i",
    "guid": "{f79c35ac-42f6-4755-82db-da7e34ac0399}",
    "hidden": false,
    "icon": "%USERPROFILE%\\Documents\\Apps\\ocaml-logo.png",
    "name": "OPAM",
    "startingDirectory": "%USERPROFILE%"
},
```

You can put it anywhere you like in the list to determine which order it shows up on the menu.

To give the terminal an icon like the rest you can download [this](https://ocamlverse.net/assets/img/ocaml-logo.png) picture.\
This JSON specifies the logo to be located at `Documents\Apps\` however you can put it wherever you like. You can also use a different icon if you wish. You can also use a different theme or even a different profile name, but keep the `commandline` the same.


---

##### Bonus tip

If you didn't know, in Windows Explorer you can click the directory bar, type `cmd`, and hit enter. This handy shortcut allows you to open a terminal right within the directory, so you don't have to `cd` to whichever folder you want to be in. 

This bonus tip is going to show you how you can do this with this new profile you created with whatever keyword you want.

---

To do this make a new `.bat` file named what you want to type in to open this new profile terminal. For example `opt` (opam terminal)
then enter the following code into the file and save it to where you want. In this instance we will use the directory where we put our icon earlier.

```batch
@echo off
setlocal
set "cwd=%cd%"
wt -p "OPAM" -d "%cwd%"
```

---

Alternatively with your new found shortcut abilities go into this directory in explorer and enter `pwsh` into the directory bar and hit enter.
Now paste this code to generate the `opt.bat` script for you, and you can simply rename it after if you wish by hitting `F2`. Do not set the name to any pre existing command names or shortcuts as this will not work.

```console
> Set-Content -Encoding ASCII opt-launch.bat "@echo off`nsetlocal`nset `"cwd=%cd%`"`nwt -p `"OPAM`" -d `"%cwd%`""; $s=(New-Object -ComObject WScript.Shell).CreateShortcut("$PWD\opt.lnk"); $s.TargetPath="$PWD\opt-launch.bat"; $s.WindowStyle=7; $s.Save()
```

After you've done this you can run the following script to add the path to your environmental variables. Again use PowerShell and note that this will assume you have put the `.bat` in the same directory as the `.png` icon.

```console
> Set-Content -Encoding ASCII opt.bat "@echo off`nsetlocal`nset `"cwd=%cd%`"`nwt -p `"OPAM`" -d `"%cwd%`""
```

Now you can use the `opt` shortcut in Windows Explorer and on the start menu, that means you can press `Windows` and type `opt` press `enter` and it will also open the terminal profile. Neat!

---

### Running Dune

Now that you've installed Dune and hopefully made a new terminal profile and completed the bonus tip we can `opt` into the `%USERPROFILE%\Documents\GitHub\calyxium` directory and run the following 2 commands in sequence.

```console
$ dune build --profile release
```

```console
$ dune install
```

Pretty self explanatory right? Thats it! You've completed this tutorial. You deserve a pat on the back!
If you ever pull a new commit from the base repository, before you try and use Calyxium, run the following command 
to stop anything strange from happening (speaking from experience). Then run both commands again.

```console
$ dune clear
```