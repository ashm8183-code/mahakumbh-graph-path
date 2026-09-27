from collections import deque

n = int(input())

graph = {}

for _ in range(n):
    parts = input().split()
    station = parts[0]

    if station not in graph:
        graph[station] = set()

    for x in parts[1:]:
        graph[station].add(x)

        if x not in graph:
            graph[x] = set()

        graph[x].add(station)

q = int(input())

queries = []

for _ in range(q):
    queries.append(input().split())

r = int(input())

restricted = {}

for _ in range(r):
    parts = input().split()
    restricted[parts[0]] = set(parts[1:])


for query in queries:

    if len(query) == 2:
        start = query[0]
        end = query[1]

        blocked = restricted.get(start, set())

        queue = deque([start])
        visited = {start}

        possible = False

        while queue:
            current = queue.popleft()

            if current == end:
                possible = True
                break

            for next_station in graph.get(current, set()):

                if next_station in visited:
                    continue

                if next_station in blocked:
                    continue

                visited.add(next_station)
                queue.append(next_station)

        if possible:
            print("yes")
        else:
            print("no")

    elif len(query) == 3:

        station1 = query[0]
        action = query[1]
        station2 = query[2]

        if station1 not in graph:
            graph[station1] = set()

        if station2 not in graph:
            graph[station2] = set()

        if action == "connects":
            graph[station1].add(station2)
            graph[station2].add(station1)

        elif action == "disconnects":
            graph[station1].discard(station2)
            graph[station2].discard(station1)
