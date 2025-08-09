# Data Types

> Under Construction

In calyxium there are 5 primitive data types

### Int

This is an integer number (whole number) and is used to store numbers without decimals, it can be positive and negative.
It ranges between `LOWEST` and `HIGHEST`. If you try to make it bigger or smaller than these ranges you will get unintended results.

For example `10` or `-3000`

To specify an int in code you can just type out the number.

### Float

This is any number and is used to store numbers with decimals, it can be positive and negative.
It ranges between `LOWEST` and `HIGHEST`. If you try to make it bigger or smaller than these ranges you will get unintended results.
The term _float_ refers to the fact that the decimal can "float" between positions. Its full name is Floating Point Number.

For example `10.009` or `-3000.33`

To specify a float in code you can add `.0` to the end of the number.

One interesting property of floats is that the higher the number the less precise the number will be because there isn't enough room to store the digits after the decimal point.

Say a the max size of a float is 7 characters, when the numbers before the decimal are only 3 characters `200.457` you will have enough room for 3 more numbers, however if there are 5 characters `20000.1` you only have enough room for 1 number after the decimal making the number much less precise, and you can start to get artifacts in your computations. This is what causes graphical artifacts in games where the players position can become high enough to start allowing floating point precision problems.

### String

This is a string (sequence) of [chars](#byte) and is used to store any word, phrase, paragraph you can think of!
The term string comes from "stringing" a sequence of characters together. The longest string you can make is `HIGHEST`.
Although some devices may not be able to display them, strings can hold **any** character you will come across; that is,
if they are within the [char](#byte) size limit.

For example `"Hello world!"` or `"جبن"` or even `"😎👍"`

To specify a string in code you just surround anything you want to write with a `"` character

### Byte

This is a **single** character and is want a [string](#string) is composed of. Again, it can be any character you can think of.
It can also be referred to as a char. The biggest character you can make is `BYTES` bytes. Once again, although some devices may
not be able to display them, chars can be any character you will come across, as long as they are within the limit.
If you try and put more than one character in a char you will get an error, so just make it a [string](#string) if you are unsure.

For example `'ö'` or `'ب'` or even `'😎'`

To specify a byte in code you just surround a **single** character you want to write with a `'` character

### Bool

Short for boolean, this data type has 2 states `true` or `false`. Sort of like a yes or no.\
By doing `not my_boolean` you can reverse a boolean. These are used to control the flow of a program.
The name comes from English mathematician [George Boole](https://en.wikipedia.org/wiki/George_Boole) who developed [Boolean algebra](https://en.wikipedia.org/wiki/Boolean_algebra).\
These are the least memory intensive only taking a single bit of storage.

To write a boolean simply write `true` or `false`.