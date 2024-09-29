import cases


class Solution:
    def __init__(self) -> None:
        self._checked_lengths: set[int] = set()

    def canJump(self, nums: list[int]) -> bool:
        if len(nums) == 1:
            return True

        jump = nums[0]
        while jump:
            if len(nums) in self._checked_lengths:
                return False
            if jump >= len(nums):
                jump -= 1
                continue
            # print("PJ", self._checked_lengths, jump, nums[jump], len(nums[jump:]))
            if not self.canJump(nums[jump:]):
                jump -= 1
            else:
                return True

        self._checked_lengths.add(len(nums))
        return False

    def canJumpRobado(self, nums: list[int]) -> bool:
        gas = 0
        for n in nums:
            if gas < 0:
                return False
            elif n > gas:
                gas = n
            gas -= 1
        return True


def main() -> None:
    s = Solution()

    nums = cases.nums  # [2, 3, 1, 1, 4]
    print(s.canJump(nums))
    nums = cases.nums2  # [2, 3, 1, 1, 4]
    print(s.canJumpRobado(nums))
    nums = [3, 2, 1, 0, 4]
    print(s.canJump(nums))


if __name__ == "__main__":
    main()
