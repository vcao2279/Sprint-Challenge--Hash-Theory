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
    short_set = [
        (None, 'PDX'),
        ('PDX', 'DCA'),
        ('DCA', None)
    ]
    print(reconstruct_trip(short_set))  # ['PDX', 'DCA']

    long_set = [
        ('PIT', 'ORD'),
        ('XNA', 'CID'),
        ('SFO', 'BHM'),
        ('FLG', 'XNA'),
        (None, 'LAX'),
        ('LAX', 'SFO'),
        ('CID', 'SLC'),
        ('ORD', None),
        ('SLC', 'PIT'),
        ('BHM', 'FLG'),
    ]
    print(reconstruct_trip(long_set))
    # ['LAX', 'SFO', 'BHM', 'FLG', 'XNA', 'CID', 'SLC', 'PIT', 'ORD']

    incorrect_set = [
        ('LHD', 'DAB'),
        (None, 'HVN'),
        ('MSO', 'SFO'),
        ('RDU', 'ABQ'),
        ('ACY', None),
    ]
    print(reconstruct_trip(incorrect_set))  # []
