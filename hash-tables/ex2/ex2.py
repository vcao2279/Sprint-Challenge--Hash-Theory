def reconstruct_trip(tickets):
    ht = {}
    for i in tickets:
        if i[0] is None:
            ht['start'] = i[1]
        else:
            ht[i[0]] = i[1]
    source = ht['start']
    trip = []
    while source is not None:
        trip.append(source)
        try:
            source = ht[source]
        except KeyError:
            return []
    return trip


if __name__ == '__main__':
    # You can write code here to test your implementation using the Python repl
    pass
