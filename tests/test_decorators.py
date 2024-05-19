from src.decorators import log


def test_log() -> None:
    @log("test_log.txt")
    def test_func(a: int, b: int) -> int:
        return a + b

    test_func(2, 3)
    with open("test_log.txt", "r") as file:
        lines = file.readlines()
        assert lines[-1] == "test_func ok"
