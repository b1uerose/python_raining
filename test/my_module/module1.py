"""
 * 模块1
 * Author: xiaojl
 * Date:2023-10-06 22:31
"""

__all__ = ['test_a']


def test_func(x, y):
    return x + y


def test_a(x, y):
    return x - y


if __name__ == '__main__':
    test_a(1, 2)
    test_func(2, 3)
