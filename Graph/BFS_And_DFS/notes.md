# LeetCode 100 – Same Tree

## 🔹 Problem Summary

You are given two binary trees `p` and `q`. The task is to determine whether they are **structurally identical** and have the **same node values**.

Two trees are considered the same if:

* They have the same structure
* Corresponding nodes have the same values

---

## 🔹 Core Insight

At every node position:

* Both nodes must exist or both must be `None`
* Their values must be equal
* Their left and right subtrees must also be identical

This comparison can be done using **DFS (recursive or iterative)** or **BFS**.

---

## 🔹 Solution 1: Recursive DFS (Best & Most Common)

### 💡 Intuition

Recursively compare nodes from both trees:

* If both nodes are `None`, return `True`
* If only one is `None`, return `False`
* If values differ, return `False`
* Otherwise, compare left and right subtrees

### 🔹 Code

```python
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```

### ⏱ Complexity

* Time: `O(n)`
* Space: `O(h)` (recursive stack, `h` = height of tree)

---

## 🔹 Solution 2: Iterative DFS (Using Stack)

### 💡 Intuition

Simulate recursion using an explicit stack that stores node pairs.

### 🔹 Code

```python
class Solution:
    def isSameTree(self, p, q):
        stack = [(p, q)]

        while stack:
            n1, n2 = stack.pop()

            if not n1 and not n2:
                continue

            if not n1 or not n2:
                return False

            if n1.val != n2.val:
                return False

            stack.append((n1.left, n2.left))
            stack.append((n1.right, n2.right))

        return True
```

### ⏱ Complexity

* Time: `O(n)`
* Space: `O(n)` (explicit stack)

---

## 🔹 Solution 3: BFS / Level Order Traversal

### 💡 Intuition

Traverse both trees level by level using a queue and compare corresponding nodes.

### 🔹 Code

```python
from collections import deque

class Solution:
    def isSameTree(self, p, q):
        queue = deque([(p, q)])

        while queue:
            n1, n2 = queue.popleft()

            if not n1 and not n2:
                continue

            if not n1 or not n2:
                return False

            if n1.val != n2.val:
                return False

            queue.append((n1.left, n2.left))
            queue.append((n1.right, n2.right))

        return True
```

### ⏱ Complexity

* Time: `O(n)`
* Space: `O(n)` (queue)

---

## ❌ Solution 4: Tree Serialization (Not Recommended)

### 💡 Idea

Serialize both trees into strings and compare them.

```python
def serialize(root):
    if not root:
        return "N"
    return f"{root.val},{serialize(root.left)},{serialize(root.right)}"
```

### ⚠️ Why Avoid

* Extra memory usage
* Less readable
* Overkill for interviews

---

## 🔁 Comparison of Approaches

| Approach      | Data Structure | Time | Space | Interview Value |
| ------------- | -------------- | ---- | ----- | --------------- |
| Recursive DFS | Call Stack     | O(n) | O(h)  | ⭐⭐⭐⭐⭐ Best      |
| Iterative DFS | Stack          | O(n) | O(n)  | ⭐⭐⭐⭐            |
| BFS           | Queue          | O(n) | O(n)  | ⭐⭐⭐             |
| Serialization | String         | O(n) | O(n)  | ⭐               |

---

## 🔹 Key Takeaways / Pattern

* Always compare **structure + values together**
* Tree comparison problems usually use **DFS**
* Recursive DFS is the cleanest solution

---

## 🔹 Common Mistakes

❌ Checking values before handling `None`
❌ Ignoring tree structure
❌ Forgetting base cases

---

## 🔹 Similar Problems

* LeetCode 101 – Symmetric Tree
* LeetCode 572 – Subtree of Another Tree
* LeetCode 226 – Invert Binary Tree

---

## ✅ One-Line Recall

> Compare nodes pairwise: if both null → same, if one null or values differ → false, else recurse left & right.
