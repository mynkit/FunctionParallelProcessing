# -*- coding: utf-8 -*-

'''引数なし関数を並列処理する

Examples:
    >>> from parallel_process_func import parallel_process_func
    >>> def x():
    ...     print('-- x() START --')
    ...     [i for i in range(10000000)]
    ...     print('-- x() END --')
    ...
    >>> def y():
    ...     print('-- y() START --')
    ...     [i for i in range(10000000)]
    ...     print('-- y() END --')
    ...
    >>> parallel_process_func(x, y)
    -- x() START --
    -- y() START --
    -- x() END --
    -- y() END -- 

'''

from joblib import Parallel, delayed


def run_func(*funcs):
    [f() for f in funcs]


def parallel_process_func(*target_funcs):
    Parallel(n_jobs=-1)([delayed(run_func)(func) for func in target_funcs])
