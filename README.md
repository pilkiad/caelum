<img src="./resources/caelum-logo.png" width="100px" height="100px">

Caelum is a functional, eval-driven programming language with recursive constructs, suitable for mathematical simulations, formal modeling, and experimental programming approaches.

> ⚠️  caelum is currently in the unstable, incomplete version **a-5**.

## Reference

[Changelog](./docs/changelog.md)

[Reference](./docs/reference.md)

## Installation

Under debian:

```bash
git clone https://github.com/pilkiad/caelum.git
cd caelum
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 -m src.main
```

## Example

```lua
version("a-5")

-- Constants
SIZE = int(20)
MIDDLE = int(div(SIZE(), int(2)))
ITERATIONS = int(5)

-- Generates an empty array
-- IN   i     int(0)      Current iteration
-- IN   max   int         Size of the array
-- OUT        arr(bool)   The resulting empty array
gen_empty_state = (i, max) {
    eval(eq(i(), int(0)),   { res = arr(bool) })
    eval(gt(i(), int(0)),   { res = arr_push(res(), int(0)) })
    eval(lt(i(), max()),    { res = gen_empty_state(add(i(), int(1)), max()) })
    return(res())
}

-- Applies "Rule 30" rulebook to input array
-- IN   current_state   arr(bool)   Current state of the system
-- OUT                  arr(bool)   Next state of the system
gen_next_state = (current_state) {
    res = arr(bool)

    -- Iterates over the cells of the system
    iter = (i, max) {
        updated_state = bool(0) -- new state cell defaults to bool(0)

        -- Check bounds
        eval(and(
            gt(i(), int(0)),
            lt(i(), max())), {
                -- Apply rule 30
                updated_state = xor(
                    current_state(sub(i(), int(1))),
                    or(
                        current_state(i()),
                        current_state(add(i(), int(1)))
                    )
                )
        })

        -- Append updated cell and repeat process
        res = arr_push(res(), updated_state())
        eval(lt(i(), max()), {
            res = iter(add(i(), int(1)), max())
        })

        return(res())
    }
    res = iter(int(0), sub(SIZE(), int(1)))

    return(res())
}

-- Simulates Rule 30 for n amount of iterations
-- https://en.wikipedia.org/wiki/Rule_30
-- IN   current_state   arr(bool)   Current state of the system
-- IN   i               int(0)      Current iteration
-- IN   n               int()       Maximum amount of iterations
rule_30 = (current_state, i, n) {
    new_state = gen_next_state(current_state())
    draw(new_state())

    eval(lt(i(), n()), {
        rule_30(new_state(), add(i(), int(1)), n())
    })
}

-- Setup the initial state
initial_state = gen_empty_state(int(0), SIZE())
initial_state = arr_set(initial_state(), MIDDLE(), int(1))

-- Draw initial state and simulate Rule 30
draw(initial_state())
rule_30(initial_state(), int(0), ITERATIONS())
```
