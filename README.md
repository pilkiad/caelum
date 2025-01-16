# funl

Rough prototype of what could become a fun functional language.

> ⚠️ funl is currently in the unstable, incomplete version **a-3**.

Take a look at the [changelog](./docs/changelog.md) to see what the current development stage is.

Also there is a [reference](./docs/reference.md).

## Example

```lua
version("a-3")

-- recursive fibonacci function
fib = (n) {
    case_0 = { return(int(0)) }
    case_1 = { return(int(1)) }

    res = int(0)

    -- 0, 1 and 2 are special cases
    eval(n(), "==", int(0), "res = case_0()")
    eval(n(), "==", int(1), "res = case_1()")
    eval(n(), "==", int(2), "res = case_1()")

    -- if no special case matched, run fib(n-1)+fib(n-2)
    eval(n(), ">", int(2), "
        fib_1 = fib(sub(n(), int(1)))
        fib_2 = fib(sub(n(), int(2)))
        res = add(fib_1(), fib_2())
    ")

    return(res())
}

-- calls fibonacci function n times
main = (n, c) {
    print(fib(c()), ",")
    eval(c(), "<", n(), "main(n(), add(c(), int(1)))")
}

println("Calculate the fibonacci sequence up until n", "https://en.wikipedia.org/wiki/Fibonacci_sequence")
print("n = ")
input = int(in())

main(input(), int(0))
```