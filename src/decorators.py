from functools import wraps
from typing import Any, Callable


def log(filename: str = "None") -> Callable:
    """
    Декоратор для логирования функций.
    """

    def decorator(func: Callable) -> Callable:
        """
        Обертка декоратора.
        """

        @wraps(func)
        def wrapper(*args: tuple, **kwargs: dict) -> Any:
            """
            Обертка функции, которая выполняет логирование.
            """
            try:
                res = func(*args, **kwargs)
            except Exception as e:
                res = f"Error {e} input data: {args}, {kwargs}"

            if filename != "None":
                with open(filename, "a") as file:
                    file.write(f"{func.__name__} ok")
            else:
                print(f"{func.__name__} ok")

            return res

        return wrapper

    return decorator
