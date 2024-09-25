class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        initial_len = len(nums)

        while True:
            try:
                nums.remove(val)
            except ValueError:
                break

        removed_count = initial_len - len(nums)
        nums.extend([0] * removed_count)

        return initial_len - removed_count

        # as leet code does not care what comes after the number of items we can ignore the extend step so a better version would be
        #
        while True:
            try:
                nums.remove(val)
            except ValueError:
                break

        return len(nums)


def main():
    s = Solution()

    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2

    x = s.removeElement(nums, val)

    print(nums, x)


if __name__ == "__main__":
    main()
