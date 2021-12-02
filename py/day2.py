# solution to part 1
def submarine_position(steps):
    depth, horizontal = 0, 0
    for step in steps:
        direction, n = step.split()
        n = int(n)
        if direction == 'forward':
            horizontal += n
        elif direction == 'down':
            depth += n
        elif direction == 'up':
            depth -= n
    return depth * horizontal


def example1():
    steps = """forward 5
        down 5
        forward 8
        up 3
        down 8
        forward 2"""
    steps = list(map(str.strip, steps.split('\n')))
    print('in: ', steps)
    OUT = submarine_position(steps)
    print('out:', OUT)
    assert OUT == 150, 'WRONG!'


def my_input1():
    steps = [line.strip() for line in open('day2_input.txt').readlines()]
    print('in :', steps[:5], '...')
    OUT = submarine_position(steps)
    print('out:', OUT)
    return OUT


# solution to part 2
def submarine_position_aim(steps):
    depth, horizontal, aim = 0, 0, 0
    for step in steps:
        direction, n = step.split()
        n = int(n)
        if direction == 'forward':
            horizontal += n
            depth += aim * n
        elif direction == 'down':
            aim += n
        elif direction == 'up':
            aim -= n
    return depth * horizontal


def example2():
    steps = """forward 5
        down 5
        forward 8
        up 3
        down 8
        forward 2"""
    steps = list(map(str.strip, steps.split('\n')))
    print('in: ', steps)
    OUT = submarine_position_aim(steps)
    print('out:', OUT)
    assert OUT == 900, 'WRONG!'


def my_input2():
    steps = [line.strip() for line in open('day2_input.txt').readlines()]
    print('in :', steps[:5], '...')
    OUT = submarine_position_aim(steps)
    print('out:', OUT)
    return OUT


if __name__ == '__main__':
    # part 1
    example1()
    my_input1()

    # part 2
    example2()
    my_input2()
