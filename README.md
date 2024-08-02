# funl

Silly experimental language where absolutely everything is a function.

I developed this idea while talking to a coworker about how greate the idea
of tcl is - to build a complex language from incredibly simple rules.

So, I decided to try the same as a prototype and here are some ideas I came
up with:

- Everything is either a function declaration or a function call - Syntax
should be as minimal as possible, if you know how to call a function you
know pretty much everything about funl - Strongly typed variables - because
this helps with preventing errors - Interpreted (because that was easiest)

I am using [textx](https://pypi.org/project/textX/), here is the only thing
I got working so far:

```
a = int(2)
b = int(3)
res = add(a(), b())
print("a + b = ", cast(res(), str))
```

Output:

``` a + b = 5 ```

(stunning, I know)

## TODO

(there are more todos within the code, this is the only acceptable way to
manage open issues)

Ranked in order of priority;

- fix mypy typing
    - make mypy not accept any untyped variable declarations
- comment coverage - add project structure - add pylint (and pep8?)
