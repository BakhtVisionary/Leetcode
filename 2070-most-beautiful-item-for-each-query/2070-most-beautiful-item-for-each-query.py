class Solution(object):
    def maximumBeauty(self, items, queries):
        """
        :type items: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        # Sort items by price
        items.sort()

        # Pair queries with their indices and sort by price
        queries = sorted((q, i) for i, q in enumerate(queries))

        max_beauty = 0
        j = 0

        # Initialize result list
        res = [0] * len(queries)

        # Process each query
        for q, i in queries:
            while j < len(items) and items[j][0] <= q:
                max_beauty = max(max_beauty, items[j][1])
                j += 1
            res[i] = max_beauty

        return res
