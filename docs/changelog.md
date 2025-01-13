# a-3

This alpha version is meant to further implement scopes and improve debugging capabilities.

- Added `new()` and `pop()` to `environment` to create / remove a new environment (used when calling or returning functions to create a local scope)
- Added assert statement, usage: `assert(actual, expected, [error message])`