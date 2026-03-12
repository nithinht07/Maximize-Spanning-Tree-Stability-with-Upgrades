class Solution:
    def maxStability(self, n, edges, k):
        
        def can(T):
            parent = list(range(n))

            def find(x):
                while parent[x] != x:
                    parent[x] = parent[parent[x]]
                    x = parent[x]
                return x

            def union(a, b):
                pa = find(a)
                pb = find(b)
                if pa == pb:
                    return False
                parent[pb] = pa
                return True

            upgrades = 0
            count = 0
            optional = []

            for u, v, s, must in edges:
                if must == 1:
                    if s < T:
                        return False
                    if not union(u, v):
                        return False
                    count += 1
                else:
                    optional.append((u, v, s))

            for u, v, s in optional:
                if find(u) == find(v):
                    continue

                if s >= T:
                    union(u, v)
                    count += 1
                elif 2 * s >= T and upgrades < k:
                    union(u, v)
                    upgrades += 1
                    count += 1

                if count == n - 1:
                    break

            return count == n - 1

        left = 1
        right = 200000
        ans = -1

        while left <= right:
            mid = (left + right) // 2
            if can(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans