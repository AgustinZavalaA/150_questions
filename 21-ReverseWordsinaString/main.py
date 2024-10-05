class Solution:
    def reverseWords(self, s: str) -> str:
        # return " ".join(s.split()[::-1])
        reversedString = ""

        word = ""
        for c in s[::-1]:
            if c == " ":
                if word:
                    reversedString += " " + word[::-1]
                    word = ""
            else:
                word += c

        if word:
            reversedString += " " + word[::-1]

        return reversedString[1:]


def main() -> None:
    s = Solution()

    text = "   hello world   "

    print(s.reverseWords(text))

    text = "the sky is blue"

    print(s.reverseWords(text))


if __name__ == "__main__":
    main()
