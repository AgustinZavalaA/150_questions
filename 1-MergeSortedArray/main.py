class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for _ in range(n):
            nums1.pop()
        nums1.extend(nums2)
        nums1.sort()

        print(nums1)
        # nums1 = nums1[: n + m]


def main() -> None:
    s = Solution()

    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    s.merge(nums1, m, nums2, n)

    print(nums1)


if __name__ == "__main__":
    main()
