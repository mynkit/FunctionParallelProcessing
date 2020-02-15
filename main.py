from parallel_process_func import parallel_process_func


def x():
    print('-- x() START --')
    [i for i in range(10000000)]
    print('-- x() END --')


def y():
    print('-- y() START --')
    [i for i in range(10000000)]
    print('-- y() END --')


if __name__ == '__main__':
    parallel_process_func(x, y)
