class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        last_seen_number = (
            100000  # we know the list is sorted so it probable it is a small number
        )

        i = 0
        while True:
            if i >= len(nums):
                break

            new_number = nums[i]

            if new_number == last_seen_number:
                nums.pop(i)
            else:
                i += 1

            last_seen_number = new_number
        return len(nums)

    def optimizedRemoveDuplicates(self, nums: list[int]) -> int:
        new_list = []

        for v in nums:
            if v not in new_list:
                new_list.append(v)

        nums[:] = new_list[:]
        return len(new_list)


def main():
    s = Solution()

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    unique_numbers = s.removeDuplicates(nums)
    unique_numbers2 = s.optimizedRemoveDuplicates(nums2)

    print(nums, unique_numbers)
    print(nums2, unique_numbers2)


if __name__ == "__main__":
    main()
