class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        smallest_size = min([len(s) for s in strs])

        prefix = ""
        for i in range(smallest_size):
            common_prefix = strs[0][i]
            for s in strs:
                if s[i] != common_prefix:
                    return prefix

            prefix += common_prefix
        return prefix


def main() -> None:
    s = Solution()

    strs = ["flower", "flow", "flight"]

    print(s.longestCommonPrefix(strs))


if __name__ == "__main__":
    main()
