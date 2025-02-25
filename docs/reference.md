# Reference

## Keywords

Found below are all funl keywords in alphabetical order.

| Name  | Parameters    | Returns       | Description   |
| ---   | ---           | ---           | ---           |
| add       | `[int, ...]` | `int` | Adds `param[0..]` |
| arr       | `T, [value: T, ...]` | `[value: T, ...]` | Array. Expects type `T` as `param[0]` and values of type `T` as `param[1..]`. Returns `param[1..]`. |
| assert    | `any`, `any` | `bool` | Asserts that `param[0]` is equal to `param[1]`. Returns `1` if parameters are requal, `0` otherwise. |
| bool      | `0` or `1` | `0` or `1` | Boolean value. Integer limited to range `[0, 1]` for type safety. Returns whatever was given as `param[0]` |
| eval      | `any`, `str`, `any`, `str` | Return value of `param[3]()` if evaluated as `1`, `none` otherwise | Evaluates a statement `param[0..2]` and calls `param[3]` if statement evaluates as `1`. NOTE `param[3]` will be executed as a code block in the same environment as the caller function. |
| exit      |  |  | Exits the application. |
| float     | `float` | `float` | Floating point value. Returns whatever was given as `param[0]` |
| in        |  | `str` | Reads stdin. Returns the users input. |
| int       | `int` | `int` | Integer value. Returns whatever was given as `param[0]` |
| meh       | | `meh` | Meh value. Always returns `meh`. |
| print     | `[str, ...]` | `str` | Prints `param[0..]` to console. Returns the resulting `str` |
| println   | `[str, ...]` | `str` | Prints `param[0..]` to console while adding a newline (`\n`) behind every parameter. Returns the resulting `str` |
| rbool     | | `0` or `1` | Generates a random `bool` that can be either `0` or `1` |
| return    | `any` | `any` | Returns out of the function. Returns `param[0..]` |
| rfloat    | `float`, `float` | `float` | Generates a random `float` between `param[0]` and `param[1]` |
| rint      | `int`, `int` | `int` | Generates a random `int` between `param[0]` and `param[1]` |
| str       | `str` | `str` | String value. Returns whatevers was given as `param[0]` |
| version   | `str`       | `bool` | Check if the application is being run on the correct version. Returns `1` if correct, `0` otherwise. |