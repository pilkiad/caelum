# Reference

## Primitive datatypes

Datatypes in funl are functions who return whatever value was given as a parameter.

---

`int()` is used to denote integers. Use `rint(min, max)` to generate a random integer: `rint(2, 5) = eg. int(4)`.

`float()` is used to denote floating point numbers. Use `rfloat(min, max)` to generate a random float: `float(3.0, 9.3) = eg. float(5.83927465...)`.

`str()` is used to denote strings: `str("Hello, world!")`.

`bool()` is used to denote boolean values. Use `rbool` to generate a random boolean: `rbool() = eg. bool(1)`. Internally, these are just typesafe `int`s.

## Complex datatypes

In funl, complex datatypes are datatypes that have corresponding functions.

---

`arr()` is used to denote an array. The first parameter indicates the type of array: `arr(int, 1, 2, 3)`. Access an element at a given index using `my_arr(1) = int(2)`.

`arr_push()` can be used to append an element to an array: `arr_push(arr(int, 1, 2, 3), 4) = arr(int, 1, 2, 3, 4)`.

`arr_set()` can be used to set a specific element of an array: `arr_set(arr(int, 1, 2, 3), 1, 4) = arr(int, 1, 4, 3)`.

## Maths

`add()` can be used to add all given parameters: `add(int(3), int(2)) = int(5)`.

`sub()` can be used to substract the parameters from each other in the order they were given: `sub(int(3), int(2)) = int(1)`.

`div()` can be used to devide two given parameters: `div(int(11), int(2)) = float(5.5)`. This returns a `float` by default.

## Boolean operations

`eq()` can be used to check equality between two parameters: `eq(bool(1), sub(int(3), int(2))) = bool(1)`.

`gt()` can be used to check whether the first parameter is greater than the second parameter: `gt(int(3), int(2)) = bool(1)`.

`lt()` can be used to check whether the first parameter is less than the second parameter: `lt(int(3), int(2)) = bool(0)`.

## Input

`in()` can be used to capture user input as string.

## Output

`print()` can be used to print all parameters to console.
`println()` will place a newline after each parameter.

`draw()` can be used to visualize `arr` using *matplotlib*.

## Function declaration

A function is declared like this: `func_name = (params, ...) { ... }`.

Example:

```lua
my_func = (msg) {
    println(msg)
}

my_func(str("Hello, world!"))
```

Produces:

```
Hello, world!
```

## Conditional statements

There are no conditional statements.
`if`, `when` and `else` are syntactical sugar for the weak, funl uses only `eval`.

`eval()` can be used to evaluate arbitrary statements and execute anonymous inner functions upon the previous statement being evaluated as `bool(1)`.

Example:

```lua
eval(gr(int(3), int(2)), {
    println("Who would have thought that 3 is greater than 2?")
})
```

Produces:

```
Who would have thought that 3 is greater than 2?
```

## Loops

There are no loops - the only true saviour shall be recursion.

Example:

```lua
println("I feel empty - ")
loop = (i, m) {
    println("Recursion will save me...")
    eval(lt(i(), m()), { loop(add(i(), int(1)), m()) })
}
loop(int(0), int(2))
```

Produces:
```
I feel empty - 
Recursion will save me...
Recursion will save me...
Recursion will save me...
```

Due to the excessive use of recursion, funl may not execute most code as it reaches maximum recursion depth quickly.