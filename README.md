# Data Structures & Systems Design

Python solutions for two problems: an **LRU Cache** and an **Event Scheduler**.

## Files

| File | What it has |
|------|-------------|
| `lru_cache.py` | LRU Cache with O(1) `get` and `put` |
| `event_scheduler.py` | `can_attend_all` and `min_rooms_required` |
| `room_assignment.py` | Gives each event a room name (Room A, Room B, ...) |
| `thread_safe_lru.py` | Thread-safe version of the LRU Cache using a lock |
| `test_all.py` | Tests for all the above |

## Problem 1: LRU Cache

- `get(key)` returns the value if the key exists, otherwise `-1`. It also marks the key as recently used.
- `put(key, value)` adds or updates a key. If the cache is full, it removes the least recently used item first.

**Approach:** I used a dictionary and a doubly linked list together.
The dictionary gives the node for a key in O(1).
The linked list keeps the order of use. The most recently used item is at the front and the least recently used is at the back.
Moving or removing a node only needs a few pointer changes, so both `get` and `put` are O(1).

```python
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
cache.get(1)     # 1
cache.put(3, 3)  # removes key 2
cache.get(2)     # -1
```

## Problem 2: Event Scheduler

Events are given as `(start, end)` tuples, for example `[(9, 10), (10, 11), (11, 12)]`.
Back-to-back events like `(9, 10)` and `(10, 11)` are not counted as overlapping.

- `can_attend_all(events)`: sort by start time and check if any event starts before the previous one ends.
- `min_rooms_required(events)`: sort by start time and use a min heap of end times. If the earliest ending meeting is over, reuse that room. Otherwise add a new room. The final heap size is the answer.

```python
can_attend_all([(9, 10), (10, 11), (11, 12)])               # True
min_rooms_required([(9, 12), (9, 10), (10, 11), (11, 13)])  # 2
```

## Room Assignment

`assign_rooms(events)` uses two heaps: one for busy rooms (by end time) and one for free rooms.
The smallest free room is reused first, so the number of rooms used is the same as `min_rooms_required`.

```
(9, 12)  -> Room A
(9, 10)  -> Room B
(10, 11) -> Room B
(11, 13) -> Room B
```

## Thread Safety

`get` also changes the linked list, so both `get` and `put` take a lock before making changes.

## Complexity

| Function | Time | Space |
|----------|------|-------|
| `LRUCache.get` | O(1) | O(1) |
| `LRUCache.put` | O(1) | O(1) |
| Whole cache | - | O(capacity) |
| `can_attend_all` | O(n log n) | O(n) |
| `min_rooms_required` | O(n log n) | O(n) |
| `assign_rooms` | O(n log n) | O(n) |

## How to Run

Needs Python 3. No extra libraries are required.

```bash
python3 lru_cache.py
python3 event_scheduler.py
python3 room_assignment.py
python3 test_all.py
```

## Author

Vinayaka G C
