# Appendix A: Keywords

The following list contains keywords that are reserved for current or future use by Calyxium. As such, they cannot be used as identifiers. Identifiers are names of functions, variables, parameters, structs fields, modules, types.

## Keywords Currently in Use

The following is a list of keywords currently in use, with their functionality described.

- `rec` - define a recursive function
- `if` - branch based on the result of a conditional expression
- `then` - fallback for `if` control flow constructs
- `else` - fallback for `then` and `if` control flow constructs
- `let` - bind a variable or function
- `match` - match a value to patterns
- `with` - branch based on the value of match
- `use` - in a module path, refers to the modules root
- `mod` - define a module
- `true` - Boolean true literal
- `false` - Boolean false literal
- `enum` - define an enumeration

* ~~`for` - loops over items~~ Superseded by `rec`

### Keywords Reserved for Future Use

The following keywords do not yet have any functionality but are reserved by
Calyxium for potential future use.

- `struct`
- `class`
- `extends`
- `fn`
- `ref`