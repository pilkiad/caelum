# Reference

## Keywords

Found below are all funl keywords in alphabetical order.

| Name  | Parameters    | Returns       | Description   |
| ---   | ---           | ---           | ---           |
| add | `[int, ...]` | `int` | Adds `param[0..]` |
| assert | `any`, `any` | `bool` | Asserts that `param[0]` is equal to `param[1]`. Returns `1` if parameters are requal, `0` otherwise. |
| eval | `any`, `str`, `any`, `str` | Return value of `param[3]()` if evaluated as `1`, `none` otherwise | Evaluates a statement `param[0..2]` and calls `param[3]` if statement evaluates as `1`. |
| exit |  |  | Exits the application |
| in |  | `str` | Reads stdin. Returns the users input. |
| int | `int` | `int` | Integer value. Returns whatever was given as `param[0]` |
| print | `[str, ...]` | `str` | Prints `param[0..]` to console. Returns the resulting `str` |
| println | `[str, ...]` | `str` | Prints `param[0..]` to console while adding a newline (`\n`) behind every parameter. Returns the resulting `str` |
| return | `any` | `any` | Returns out of the function. Returns `param[0..]` |
| rint | `int`, `int` | `int` | Generates a random `int` between `param[0]` and `param[1]` |
| version | `str`       | `bool` | Check if the application is being run on the correct version. Returns `1` if correct, `0` otherwise. |