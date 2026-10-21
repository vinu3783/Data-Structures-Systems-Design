import heapq


def can_attend_all(events):
    events = sorted(events)
    for i in range(1, len(events)):
        if events[i][0] < events[i - 1][1]:
            return False
    return True


def min_rooms_required(events):
    if not events:
        return 0

    events = sorted(events)
    rooms = []

    for start, end in events:
        if rooms and rooms[0] <= start:
            heapq.heappop(rooms)
        heapq.heappush(rooms, end)

    return len(rooms)


if __name__ == "__main__":
    print(can_attend_all([(9, 10), (10, 11), (11, 12)]))
    print(can_attend_all([(9, 11), (10, 12)]))
    print(min_rooms_required([(9, 10), (10, 11), (11, 12)]))
    print(min_rooms_required([(9, 12), (9, 10), (10, 11), (11, 13)]))
    print(min_rooms_required([(1, 5), (2, 6), (3, 7), (8, 9)]))
