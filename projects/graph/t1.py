from pudb import set_trace as st


def f(n, a = None):
    # st()
    if a == None:
        a = []

    if n == 0:
        return 0, [0]

    low_lvl = f(n-1, a)
    a.append(low_lvl[0])

    return n, a


if __name__ == "__main__":
    print(f(10))