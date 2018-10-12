def get_indices_of_item_weights(weights, limit):
    # ht ={weights[i]:i for i in range(len(weights))}
    ht = {}
    for i in range(len(weights)):
        if weights[i] not in ht:
            ht[weights[i]] = [i]
        else:
            ht[weights[i]].append(i)

    for k, v in ht.items():
        if (limit-k) == k:
            return (ht[k][1], ht[k][0])
        if (limit-k) in ht:
            return (v[0], ht[limit-k][0]) if v[0] > ht[limit-k][0] else (ht[limit-k][0], v[0])
    return ()


if __name__ == '__main__':
    # You can write code here to test your implementation using the Python repl
    print(get_indices_of_item_weights([9], 9))  # ()
    print(get_indices_of_item_weights([4, 4], 8))  # (1, 0)
    print(get_indices_of_item_weights([4, 6, 10, 15, 16], 21))  # (3, 1)
    print(get_indices_of_item_weights(
        [12, 6, 7, 14, 19, 3, 0, 25, 40], 7))  # (6, 2)
