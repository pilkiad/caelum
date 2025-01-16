# a-3

This alpha version is meant to further implement scopes and improve debugging capabilities.

- funl now finally supports a working fibonacci program! Take a look at `examples/fibonacci.funl`
- Added `new()` and `pop()` to `environment` to create / remove a new environment (used when calling or returning functions to create a local scope)
- `environment` now strictly only allows functions to be declared or updated in the local environment
- Behaviour of `eval` changed: instead of calling the provided function, it will execute a provided code block in the local environment
- Added assert statement, usage: `assert(actual, expected, [error message])`