''' Segment Tree '''
class SegmentTreeSum:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (2 * self.n)
        self.build_tree(data)
    
    def build_tree(self, data):
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

    def update(self, index, value):
        pos = index + self.n
        self.tree[pos] = value
        while pos > 1:
            pos //= 2
            self.tree[pos] = self.tree[2 * pos] + self.tree[2 * pos + 1]

    def range_sum(self, left, right):
        result = 0
        left += self.n
        right += self.n + 1
        while left < right:
            if left % 2:
                result += self.tree[left]
                left += 1
            if right % 2:
                right -= 1
                result += self.tree[right]
            left //= 2
            right //= 2
        return result
    
class SegmentTreeMin:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [float('inf')] * (2 * self.n) #difference from Treesum, initialize -inf
        self.build_tree(data)
    
    def build_tree(self, data):
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = min(self.tree[i * 2], self.tree[i * 2 + 1]) #difference, build value as min

    def update(self, index, value):
        pos = index + self.n
        self.tree[pos] = value
        while pos > 1:
            pos //= 2
            self.tree[pos] = min(self.tree[2 * pos], self.tree[2 * pos + 1]) #diff

    def range_min(self, left, right):
        result = float('inf')
        left += self.n
        right += self.n + 1
        while left < right:
            if left % 2:
                result = min(result, self.tree[left]) # diff
                left += 1
            if right % 2:
                right -= 1
                result = min(result, self.tree[right]) # diff
            left //= 2
            right //= 2
        return result

class SegmentTreeProduct:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [1] * (2 * self.n)
        self.build_tree(data)
    
    def build_tree(self, data):
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i * 2] * self.tree[i * 2 + 1]

    def update(self, index, value):
        pos = index + self.n
        self.tree[pos] = value
        while pos > 1:
            pos //= 2
            self.tree[pos] = self.tree[2 * pos] * self.tree[2 * pos + 1]

    def range_product(self, left, right):
        result = 1
        left += self.n
        right += self.n + 1
        while left < right:
            if left % 2:
                result *= self.tree[left]
                left += 1
            if right % 2:
                right -= 1
                result *= self.tree[right]
            left //= 2
            right //= 2
        return result
    
class LazySegmentTree: #rangesum
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (2 * self.n)
        self.lazy = [0] * (2 * self.n)
        self.build_tree(data)
    
    def build_tree(self, data):
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

    def update_range(self, left, right, value): #Outer function for update
        self._update_range(left, right, value, 0, self.n - 1, 1)

    def _update_range(self, left, right, value, start, end, node): #Inner function for update, lazy
        if self.lazy[node] != 0:
            self.tree[node] += (end - start + 1) * self.lazy[node]
            if start != end:
                self.lazy[node * 2] += self.lazy[node]
                self.lazy[node * 2 + 1] += self.lazy[node]
            self.lazy[node] = 0

        if left > end or right < start:
            return None

        if left <= start and end <= right:
            self.tree[node] += (end - start + 1) * value
            if start != end:
                self.lazy[node * 2] += value
                self.lazy[node * 2 + 1] += value
            return None

        mid = (start + end) // 2
        self._update_range(left, right, value, start, mid, node * 2)
        self._update_range(left, right, value, mid + 1, end, node * 2 + 1)
        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def range_sum(self, left, right):
        return self._range_sum(left, right, 0, self.n - 1, 1)

    def _range_sum(self, left, right, start, end, node):
        if self.lazy[node] != 0:
            self.tree[node] += (end - start + 1) * self.lazy[node]
            if start != end:
                self.lazy[node * 2] += self.lazy[node]
                self.lazy[node * 2 + 1] += self.lazy[node]
            self.lazy[node] = 0

        if left > end or right < start:
            return 0

        if left <= start and end <= right:
            return self.tree[node]

        mid = (start + end) // 2
        left_sum = self._range_sum(left, right, start, mid, node * 2)
        right_sum = self._range_sum(left, right, mid + 1, end, node * 2 + 1)
        return left_sum + right_sum
    
N, M, K = isi()
data = [ii() for _ in range(N)]
seg_tree = SegmentTreeSum(data)