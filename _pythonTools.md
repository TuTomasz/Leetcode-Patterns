## 1. Lists:

- **Methods:**
  - `append(x)`: Adds an item to the end of the list.
  - `extend(iterable)`: Extends the list by appending elements from the iterable.
  - `insert(i, x)`: Inserts an item at a given position.
  - `remove(x)`: Removes the first occurrence of a value.
  - `pop([i])`: Removes and returns the item at the given position or the last item.
  - `index(x)`: Returns the index of the first occurrence of a value.

## 2. Dictionaries:

- **Methods:**
  - `get(key[, default])`: Returns the value for a key, or a default value if the key is not found.
  - `keys()`: Returns a view of all keys.
  - `values()`: Returns a view of all values.
  - `items()`: Returns a view of all key-value pairs.
  - `update(iterable)`: Updates the dictionary with elements from another iterable.

## 3. Sets:

- **Methods:**
  - `add(elem)`: Adds an element to the set.
  - `remove(elem)`: Removes the specified element.
  - `discard(elem)`: Removes the specified element if present.
  - `union(other_set)`: Returns the union of two sets.
  - `intersection(other_set)`: Returns the intersection of two sets.

## 4. Counter:

- **Methods:**
  - `from_iterable(iterable)`: Creates a Counter from an iterable.
  - `elements()`: Returns an iterator over elements repeating each as many times as its count.
  - `most_common([n])`: Returns a list of the n most common elements and their counts.

## 5. Heap (Heapq module):

- **Methods:**
  - `heapify(iterable)`: Transforms a list into a heap.
  - `heappush(heap, elem)`: Adds an element to the heap.
  - `heappop(heap)`: Removes and returns the smallest element.
  - `heapreplace(heap, elem)`: Pop and return the smallest element, and then push a new element.

## 6. Deque (Collections module):

- **Methods:**
  - `append(x)`: Add x to the right side.
  - `appendleft(x)`: Add x to the left side.
  - `pop()`: Remove and return the rightmost element.
  - `popleft()`: Remove and return the leftmost element.
  - `rotate(n)`: Rotate the deque n steps to the right.

## 7. Defaultdict (Collections module):

- **Methods:**
  - Default methods like `get()`, `keys()`, `values()`, and `items()` are applicable.

## 8. OrderedDict (Collections module):

- **Methods:**
  - Default methods like `get()`, `keys()`, `values()`, and `items()` are applicable.

## 9. defaultdict (Collections module):

- **Methods:**
  - Default methods like `get()`, `keys()`, `values()`, and `items()` are applicable.

## 10. itertools:

- **Functions:**
  - `permutations(iterable, r)`: Returns all possible r-length tuples of elements from the iterable.
  - `combinations(iterable, r)`: Returns all possible r-length combinations of elements from the iterable.
  - `product(*iterables, repeat=1)`: Cartesian product of input iterables.

## USAGE OF THINGS

sortedPairs = sorted(pairs, key=lambda x:x[1], reverse=True)
