def nums(lst):
    target = 9
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == target:
                return [i, j]

print(nums([2, 7, 11, 15]))


def strs(lst):
    count = {}
    for s in (lst):
        count[s] = count.get(s, 0) + 1

    for i in range (len(lst)):
        if count[lst[i]] == 1:
            return i
    return -1

print(strs("loveleetcode"))


def isomorf(s, t):
    mapst = {}
    mapts = {}

    for i in range (len(s)):
        a = s[i]
        b = t[i]

        if a in mapst and mapst[a] != b:
            return False
        if b in mapts and mapts[b] != a:
            return False
        mapst[a] = b
        mapts[b] = a
    return True
print(isomorf("egg", "add"))


def isHappy(n):
    seen = set()
    while n != 1:
        if n in seen:
            return False
        seen.add(n)

        total = 0
        while n > 0:
            digit = n % 10
            total += digit * digit
            n //= 10
        n = total
    return True
print(isHappy(19))


from collections import deque
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
def lvlorder(lst):
    if not lst:
        return []
    queue = deque([lst])
    result = []
    while queue:
        level = []
        size = len(queue)
        for i in range(size):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result

lst = Node(3)
lst.left = Node(9)
lst.right = Node(20)
lst.right.left = Node(15)
lst.right.right = Node(7)
print(lvlorder(lst))

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
def maxdepth(lst):
    if not lst:
        return 0
    left = maxdepth(lst.left)
    right = maxdepth(lst.right)
    return 1 + max(left, right)
lst = Node(3)
lst.left = Node(9)
lst.right = Node(20)
lst.right.left = Node(15)
lst.right.right = Node(7)
print(maxdepth(lst))


def symmetric(lst):
    def mirror(a, b):
        if not a and not b:
            return True
        if not a or not b:
            return False
        if a.val != b.val:
            return False

        return mirror(a.left, b.right) and mirror(a.right, b.left)
    return mirror(lst.left, lst.right)
lst = Node(1)
lst.left = Node(2)
lst.right = Node(2)
lst.left.left = Node(3)
lst.left.right = Node(4)
lst.right.left = Node(4)
lst.right.right = Node(3)
print(symmetric(lst))

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
def longestConsecutive(root):
    if not root:
        return 0
    best = 0
    def dfs(node, parent, length):
        nonlocal best
        if not node:
            return
        if parent and node.val == parent.val + 1:
            length += 1
        else:
            length = 1
        best = max(best, length)
        dfs(node.left, node, length)
        dfs(node.right, node, length)
    dfs(root, None, 0)
    return best
root = Node(1)
root.right = Node(3)
root.right.left = Node(2)
root.right.right = Node(4)
root.right.right.right = Node(5)

print(longestConsecutive(root))


def sortColors(nums):
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

    return nums
print(sortColors([2,0,2,1,1,0]))


def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quickSort(left) + mid + quickSort(right)
print(quickSort([3,6,8,10,1,2,1]))


def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]

    return result
print(mergeSort([5,2,3,1]))


def heapify(arr, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
def heapSort(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr
print(heapSort([4,10,3,5,1]))