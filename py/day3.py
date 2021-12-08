# solution to part 1
def power_consumption(INPUT):
    # how many of bits in each number
    nbits = len(INPUT[0])
    # all bits for each position
    cols = [''] * nbits
    for bit in INPUT:
        for i, b in enumerate(bit):
            cols[i] += b

    # most common bit per position
    most_common = ''
    for col in cols:
        most_common += str(int(col.count('0') < col.count('1')))

    # convert to decimal
    gamma_rate = int(most_common, 2)
    # xor and convert to decimal
    epsilon_rate = int(bin(gamma_rate ^ (2**(nbits + 1) - 1))[3:], 2)

    return gamma_rate * epsilon_rate


def example1():
    INPUT = """
        00100
        11110
        10110
        10111
        10101
        01111
        00111
        11100
        10000
        11001
        00010
        01010
    """
    INPUT = INPUT.split()
    print('INPUT:', INPUT)
    OUT = power_consumption(INPUT)
    print('OUT:', OUT)
    assert OUT == 198, 'Wrong!'


def my_input1():
    INPUT = open('day3_input.txt').read().split()
    print('INPUT:', INPUT[:4], '...')
    OUT = power_consumption(INPUT)
    print('OUT:', OUT)


# solution to part 2

def most_common_nth_bit(INPUT, n=1, keep_1_if_equal=True):
    col_bits = ''
    for bit in INPUT:
        col_bits += bit[n - 1]
    if keep_1_if_equal:
        most_common = str(int(col_bits.count('0') <= col_bits.count('1')))
    else:
        most_common = str(int(col_bits.count('0') < col_bits.count('1')))
    return most_common


def least_common_nth_bit(INPUT, n=1, keep_1_if_equal=True):
    most_common = most_common_nth_bit(INPUT, n, keep_1_if_equal)
    return str(int(not int(most_common)))


def life_support_rating(INPUT):
    nbits = len(INPUT[0])
    most_common_1 = most_common_nth_bit(INPUT, 1)

    # search for oxygen generator rating
    with_this_bit = [i for i in INPUT if i[0] == most_common_1]
    while len(with_this_bit) > 1:
        for j in range(1, nbits):
            mc = most_common_nth_bit(with_this_bit, j + 1)
            with_this_bit = [i for i in with_this_bit if i[j] == mc]
            if len(with_this_bit) == 1:
                break

    oxygen_generator_rating = int(with_this_bit[0], 2)

    # search for the CO2 scrubber rating
    least_common_1 = str(int(not most_common_1))
    with_this_bit = [i for i in INPUT if i[0] == least_common_1]
    while len(with_this_bit) > 1:
        for j in range(1, nbits):
            lc = least_common_nth_bit(with_this_bit, j + 1)
            with_this_bit = [i for i in with_this_bit if i[j] == lc]
            if len(with_this_bit) == 1:
                break
    CO2_scrubber_rating = int(with_this_bit[0], 2)

    return oxygen_generator_rating * CO2_scrubber_rating


def example2():
    INPUT = """
        00100
        11110
        10110
        10111
        10101
        01111
        00111
        11100
        10000
        11001
        00010
        01010
    """
    INPUT = INPUT.split()
    print('INPUT:', INPUT)
    OUT = life_support_rating(INPUT)
    print('OUT:', OUT)
    assert OUT == 230, 'Wrong!'


def example3():
    INPUT = """
        00100
        11110
        10110
        10011
        10000
        01111
    """
    INPUT = INPUT.split()
    print('INPUT:', INPUT)
    OUT = life_support_rating(INPUT)
    print('OUT:', OUT)


def my_input2():
    INPUT = open('day3_input.txt').read().split()
    print('INPUT:', INPUT[:4], '...')
    OUT = life_support_rating(INPUT)
    print('OUT:', OUT)


if __name__ == '__main__':
    example1()
    my_input1()

    print()
    example2()
    print()
    example3()
    my_input2()