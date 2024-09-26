class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums_map = {}
        current_max_number = 0
        for n in nums:
            nums_map[n] = nums_map.get(n, 0) + 1

            if nums_map[n] > nums_map.get(current_max_number, 0):
                current_max_number = n

        return current_max_number


def main() -> None:
    s = Solution()

    nums = [3, 2, 3]
    print(s.majorityElement(nums))


if __name__ == "__main__":
    main()
