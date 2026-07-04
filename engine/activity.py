from dataclasses import dataclass


@dataclass
class Activity:
    key: str
    name: str
    complete: int
    total: int
    percent: float

    @property
    def remaining(self) -> int:
        return self.total - self.complete

    @property
    def is_complete(self) -> bool:
        return self.remaining == 0