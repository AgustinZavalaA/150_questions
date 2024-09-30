from collections import defaultdict


class Solution:
    def hIndex(self, citations: list[int]) -> int:
        cit_count = defaultdict(int)
        for c in citations:
            cit_count[c] += 1

        print(cit_count)
        sorted_cit_count_keys = sorted(cit_count.keys(), reverse=True)
        cum_count = 0
        h_index = sorted_cit_count_keys[0]
        while cum_count < h_index:
            cum_count += cit_count.get(h_index, 0)
            if cum_count >= h_index:
                break

            h_index -= 1
        return h_index

    def hIndex2(self, citations: list[int]) -> int:
        sorted_citations = sorted(citations, reverse=True)
        h_index = sorted_citations[0], 0
        while 0 in sorted_citations:
            sorted_citations.pop()
        for c in sorted_citations:
            print(h_index, c)
            if h_index[0] == c:
                h_index = h_index[0], h_index[1] + 1
            else:
                if h_index[1] >= h_index[0]:
                    break
                else:
                    h_index = (c, h_index[1] + 1)

        print(h_index)
        return min(h_index)


def main() -> None:
    s = Solution()

    citations = [3, 0, 6, 1, 5]
    print(s.hIndex(citations))

    citations = [100]
    print(s.hIndex(citations))

    citations = [4, 4, 0, 0]
    print(s.hIndex(citations))


if __name__ == "__main__":
    main()
