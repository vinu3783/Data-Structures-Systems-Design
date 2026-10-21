import random, threading
from collections import OrderedDict
from lru_cache import LRUCache
from event_scheduler import can_attend_all, min_rooms_required
from room_assignment import assign_rooms, get_room_name
from thread_safe_lru import ThreadSafeLRUCache

# LRU vs reference
for trial in range(300):
    cap = random.randint(1, 6)
    c, ref = LRUCache(cap), OrderedDict()
    for _ in range(200):
        k = random.randint(0, 10)
        if random.random() < 0.5:
            exp = -1
            if k in ref: ref.move_to_end(k); exp = ref[k]
            assert c.get(k) == exp
        else:
            v = random.randint(0, 99)
            if k in ref: ref.move_to_end(k)
            ref[k] = v
            if len(ref) > cap: ref.popitem(last=False)
            c.put(k, v)

def brute_rooms(ev):
    pts = set(t for e in ev for t in e)
    return max([sum(1 for s, e in ev if s <= t < e) for t in pts] or [0])

for trial in range(2000):
    ev = []
    for _ in range(random.randint(0, 8)):
        s = random.randint(0, 20); ev.append((s, s + random.randint(1, 6)))
    r = min_rooms_required(ev)
    assert r == brute_rooms(ev), ev
    assert can_attend_all(ev) == (r <= 1), ev
    a = assign_rooms(ev)
    assert len(set(x[1] for x in a)) == r
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            (s1, e1), r1 = a[i]; (s2, e2), r2 = a[j]
            if r1 == r2: assert e1 <= s2 or e2 <= s1

assert get_room_name(0) == "Room A" and get_room_name(25) == "Room Z" and get_room_name(26) == "Room AA"
assert can_attend_all([]) and min_rooms_required([]) == 0

ts = ThreadSafeLRUCache(50)
def work():
    for i in range(20000):
        ts.put(random.randint(0, 100), i); ts.get(random.randint(0, 100))
th = [threading.Thread(target=work) for _ in range(8)]
[t.start() for t in th]; [t.join() for t in th]
n, node = 0, ts.head.next
while node is not ts.tail: n += 1; node = node.next
assert n == len(ts.map) <= 50
print("ALL TESTS PASSED")
