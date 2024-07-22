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
        self.tree = [float('inf')] * (2 * self.n)
        self.build_tree(data)
    
    def build_tree(self, data):
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = min(self.tree[i * 2], self.tree[i * 2 + 1])

    def update(self, index, value):
        pos = index + self.n
        self.tree[pos] = value
        while pos > 1:
            pos //= 2
            self.tree[pos] = min(self.tree[2 * pos], self.tree[2 * pos + 1])

    def range_min(self, left, right):
        result = float('inf')
        left += self.n
        right += self.n + 1
        while left < right:
            if left % 2:
                result = min(result, self.tree[left])
                left += 1
            if right % 2:
                right -= 1
                result = min(result, self.tree[right])
            left //= 2
            right //= 2
        return result

class SegmentTreeMax:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [float('-inf')] * (2 * self.n)
        self.build_tree(data)
    
    def build_tree(self, data):
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = max(self.tree[i * 2], self.tree[i * 2 + 1])

    def update(self, index, value):
        pos = index + self.n
        self.tree[pos] = value
        while pos > 1:
            pos //= 2
            self.tree[pos] = max(self.tree[2 * pos], self.tree[2 * pos + 1])

    def range_max(self, left, right):
        result = float('-inf')
        left += self.n
        right += self.n + 1
        while left < right:
            if left % 2:
                result = max(result, self.tree[left])
                left += 1
            if right % 2:
                right -= 1
                result = max(result, self.tree[right])
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

    
N, M, K = isi()
data = [ii() for _ in range(N)]
seg_tree = SegmentTree(data)