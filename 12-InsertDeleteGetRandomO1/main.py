import random


class RandomizedSet:
    def __init__(self):
        self._set: set[int] = set()

    def insert(self, val: int) -> bool:
        is_present = val in self._set
        self._set.add(val)
        return not is_present

    def remove(self, val: int) -> bool:
        is_present = val in self._set
        if is_present:
            self._set.remove(val)
        return is_present

    def getRandom(self) -> int:
        return random.choice(tuple(self._set))


def main() -> None:
    rs = RandomizedSet()

    print(rs.insert(1))
    print(rs.insert(1))
    print(rs.insert(2))
    print(rs.remove(1))
    print(rs.remove(1))
    print(rs.insert(1))
    print(rs.getRandom())


if __name__ == "__main__":
    main()
