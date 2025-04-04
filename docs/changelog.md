# a-5

This alpha version introduces the quality-of-life feature *imports* as well as a working example of convays game of life:
- Renamed from *funl* to *caelum*
- Added logo
- Added example for convay's game of life: `examples/convay.clm`, also added gif showing that
- Added `clear()` to clear all content in console
- Added logical operators `and()`, `or()`, `xor()`
- Added `import()` to import files by interpreting them in the current environment
- Added `std/data.clm` with some functions for array generation, importable by `import(std/data)`
- Added `std/tui.clm` with some functions for array pretty printing, importable by `import(std/tui)`
- Added `arr_len` to get the length of an array

# a-4

This alpha version adds many new datatypes, improves syntax and introduces the first drawing prototype.

- Added datatypes: `float`, `rfloat`, `bool`, `rbool`, `arr`, `str`, `meh`
- Added `arr_push()` and `arr_set()` to append to an array and set an element at a specific index respectively
- Added `div()` to divide numbers. Returns `float` by default
- Added `eq()` (equals), `gt()` (greater-than) and `lt()` (less-than) as boolean operations
- Added `draw()` call for either `arr(bool)`, `arr(int)` or `arr(float)` to quickly visualize arrays
- Updated `eval` syntax: `eval(statement, { ... })`

# a-3

This alpha version is meant to further implement scopes and improve debugging capabilities.

- funl now finally supports a working fibonacci program! Take a look at `examples/fibonacci.funl`
- Added `new()` and `pop()` to `environment` to create / remove a new environment (used when calling or returning functions to create a local scope)
- `environment` now strictly only allows functions to be declared or updated in the local environment
- Behaviour of `eval` changed: instead of calling the provided function, it will execute a provided code block in the local environment
- Added assert statement, usage: `assert(actual, expected, [error message])`
