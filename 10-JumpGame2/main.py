class Solution:
    def jump(self, nums: list[int]) -> int:
        current_index = 0
        jumps = 0
        nums[-1] = max(nums)

        while True:
            jump_candidates = [
                index + value
                for index, value in enumerate(
                    nums[current_index + 1 : current_index + nums[current_index] + 1]
                )
            ]
            if not jump_candidates:
                break
            jumps += 1
            current_index += len(jump_candidates) - jump_candidates[::-1].index(
                max(jump_candidates)
            )

        return jumps


def main() -> None:
    s = Solution()

    nums = [2, 3, 0, 1, 4]  # [2, 3, 1, 1, 4]

    print(s.jump(nums))


if __name__ == "__main__":
    main()
