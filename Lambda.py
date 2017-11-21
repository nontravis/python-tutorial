# NOTE:
# - single one line expression, not a block of statements.
# - We can only squeeze design, to limit program nesting for coding simple function
#   but def handles the larger tasks.


def square(num): return num**2  # == lambda num: num**2


square(10)


def rev(s): return s[::-1]  # == lambda s: s[::-1]


rev         # NOTE: return <function rev at 0x1005e2410>
