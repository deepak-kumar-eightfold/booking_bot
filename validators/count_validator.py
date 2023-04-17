

class CountValidator:
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end

    def is_count_valid(self, count: int) -> bool:
        return self.start <= count <= self.end
