from collections import deque


def flights(*args):
    flights_dict = {}
    flights_queue = deque(args)

    while not flights_queue[0] == "Finish":
        destination = flights_queue.popleft()
        passengers = flights_queue.popleft()

        if destination not in flights_dict:
            flights_dict[destination] = 0
        flights_dict[destination] += passengers

    return flights_dict


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
