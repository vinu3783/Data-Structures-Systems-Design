import heapq


def get_room_name(n):
    name = ""
    n += 1
    while n > 0:
        n, r = divmod(n - 1, 26)
        name = chr(65 + r) + name
    return "Room " + name


def assign_rooms(events):
    order = sorted(range(len(events)), key=lambda i: events[i][0])
    busy = []
    free = []
    total_rooms = 0
    result = [None] * len(events)

    for i in order:
        start, end = events[i]

        while busy and busy[0][0] <= start:
            end_time, room = heapq.heappop(busy)
            heapq.heappush(free, room)

        if free:
            room = heapq.heappop(free)
        else:
            room = total_rooms
            total_rooms += 1

        heapq.heappush(busy, (end, room))
        result[i] = (events[i], get_room_name(room))

    return result


if __name__ == "__main__":
    for event, room in assign_rooms([(9, 12), (9, 10), (10, 11), (11, 13)]):
        print(event, "->", room)
