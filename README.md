# The Calyxium Programming Language

This repository contains the source of "The Calyxium Programming Language" book.

## Building the Book

We use [mdBook](https://github.com/rust-lang/mdBook) to generate the book website.

You can install `mdbook` in one of the following ways:

- **Using Scoop** *(recommended for Windows)*  
  If you're on Windows and have [Scoop](https://scoop.sh/) installed, run:

  ```sh
  scoop install mdbook
  ```

- **Manual installation**  
  Follow the [official installation guide](https://rust-lang.github.io/mdBook/guide/installation.html) for instructions.

### Using mdBook

To preview the book locally in your browser with live reload, run:

```sh
mdbook serve --open
```

This will start a local development server and automatically open the book in your default web browser.

### Testing the Syntax of Code Blocks

Code blocks labeled with `calyxium` will be automatically tested to ensure they contain valid syntax.

These tests will run automatically when you run:

```
mdbook serve
```

You can also run the tests manually with:

```
python run_tests.py
```

If you want to **exclude a code block from testing**, simply add `,no` to the end of the language tag.

## Useful VS Code Extensions

We recommend using the [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker) extension for spell checking.

The words `Calyxium` and `calyxup` have already been added to the allowed word list in `cspell.json`, so they won't be flagged as spelling errors.
