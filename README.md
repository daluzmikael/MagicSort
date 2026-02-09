# MagicSort (Adaptive Sorting Algorithm Selector)

A Python sorting utility that **dynamically chooses the most appropriate sorting strategy** based on the input list’s structure (already sorted, reverse sorted, nearly sorted, or general case). This is a lightweight “introspective” approach meant to demonstrate practical algorithm selection rather than forcing a single algorithm for all inputs.

---

## What It Does

`magic_sort(L)` sorts a list **in-place** and returns a set indicating which strategy was used.

It performs a quick linear scan to detect easy/fast cases:
- **Already sorted** → do nothing
- **Reverse sorted** → reverse the list in-place
- **Nearly sorted** (≤ 5 out-of-order adjacent inversions) → use insertion sort
- **Otherwise** → use quicksort with:
  - insertion sort for small partitions (≤ 10)
  - a recursion depth limit (introsort-style)
  - fallback to mergesort if recursion gets too deep

---

## Functions (High-Level)

- `magic_sort(L)`: main entry point (sorts in-place, returns set of algorithms used)
- `linear_scan(L)`: detects edge cases (sorted / reverse / nearly sorted)
- `reverse_list(L, left, right)`: in-place reverse helper
- `insertionsort(L, left=0, right=None)`: insertion sort (also used for small partitions)
- `quicksort(L, left, right, rec_max=None)`: quicksort w/ depth limit + small-partition optimization
- `mergesort(L, left=0, right=None)`: fallback stable sort

---

## Requirements

- Python 3.x  
(No external libraries required)

---

## How to Run

This file is designed to be imported and used in another script or a REPL.

Example usage:

```python
from MagicSort import magic_sort

L = [5, 1, 4, 2, 8]
used = magic_sort(L)

print(L)      # [1, 2, 4, 5, 8]
print(used)   # e.g. {'quicksort'} or {'insertion_sort'} depending on input
```
