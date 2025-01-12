# funl

Rough prototype of what could become a fun functional language.

> ⚠️ funl is currently in the unstable, incomplete version **a-3**.

Take a look at the [changelog](./changelog.md) to see what the current development stage is.

## Example

```lua
println("Did you know that...")
i = int(0)
loop = {
    println("funl is considered to be *perfect*?")
    i = add(i(), int(1))
    eval(i(),"<",10,loop)
}
loop()
```