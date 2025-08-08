# Appendix C: Built-in functions

This appendix contains a glossary of Calyxium's built-in functions.

> Under Construction

## Built-ins Currently in Use

The following is a list of built-ins currently in use, with their functionality described.

- `panic` - immediately terminates the program and displays the given error message
- `print` - prints to the terminal
- `to_float` - converts integers to floats
- `to_int` - converts floats to integers
- `to_bytes` - converts strings to an array of bytes
- `length` - returns the size of an array or string
- `input` - displays the prompt and reads a line of text from standard input, returning it as a unit.
- `assert` - fails if the boolean expression is false

### Built-ins Reserved for Future Use

The following built-ins do not yet have any functionality but are reserved by
Calyxium for potential future use.

- `map` -  applies a function to each element of an array, returning a new array with the results
- `filter` - returns a new array containing only the elements for which the function returns `true`
- `fold` - reduces an array to a single value by applying a function cumulatively
- `head` - returns the first element of an array
- `tail` - returns a new array containing all elements except the first
- `reverse` - returns a new array with elements in the opposite order