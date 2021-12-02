# this is the solution to part 1
def count_increases(a):
    increases = 0
    for i, elem in enumerate(a[1:], start=1):
        if elem > a[i - 1]:
            increases += 1
    return increases


def example1():
    IN = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    print('in :', IN)
    OUT = count_increases(IN)
    print('out:', OUT)
    assert OUT == 7, 'WRONG!'


def test1():
    IN = [199, 200]
    print('in :', IN)
    OUT = count_increases(IN)
    print('out:', OUT)
    assert OUT == 1, 'WRONG!'


def test2():
    IN = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print('in :', IN)
    OUT = count_increases(IN)
    print('out:', OUT)
    assert OUT == 0, 'WRONG!'


def my_puzzle_1():
    IN = list(map(int, map(str.strip, open('day1_input.txt').readlines())))
    print('in :', IN[:10], '...')
    OUT = count_increases(IN)
    print('out:', OUT)
    return OUT


# this is the solution to part 2
def count_window_increases(a):
    sums = []
    for e1, e2, e3 in zip(a, a[1:], a[2:]):
        sums.append(e1 + e2 + e3)
    return count_increases(sums)


def example2():
    IN = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    print('in :', IN)
    OUT = count_window_increases(IN)
    print('out:', OUT)
    assert OUT == 5, 'WRONG!'



def my_puzzle_2():
    IN = list(map(int, map(str.strip, open('day1_input.txt').readlines())))
    print('in :', IN[:10], '...')
    OUT = count_window_increases(IN)
    print('out:', OUT)
    return OUT


if __name__ == '__main__':
    print('AoC Day 1')
    print('part 1')
    print('count the number of times a depth measurement increases')
    for f in (example1, test1, test2, my_puzzle_1):
        print()
        f()
        print()

    print('part 2')
    print('count the number of times the sum of measurements in sliding window increases')
    for f in (example2, my_puzzle_2):
        print()
        f()
        print()
