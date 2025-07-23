from typing import Callable, Iterable, Any

def has_collisions(func: Callable[[Any], Any], input_space: Iterable[Any]) -> bool:
    """
    Checks if `func` has any output collisions over the given `input_space`.

    Args:
        func: The function to evaluate.
        input_space: A finite iterable of inputs to test.

    Returns:
        True if any two inputs produce the same output (collision), else False.
    """
    seen_outputs = set()
    for x in input_space:
        y = func(x)
        if y in seen_outputs:
            return True  # Collision found
        seen_outputs.add(y)
    return False
