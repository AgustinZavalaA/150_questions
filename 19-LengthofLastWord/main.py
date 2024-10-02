class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip(" ").split(" ").pop())


def main() -> None:
    s = Solution()

    text = "Hello worldaesigifdvjshj     "

    print(s.lengthOfLastWord(text))


if __name__ == "__main__":
    main()
