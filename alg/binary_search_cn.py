# Binary Search
# Try to use other language for programming as UTF-8 is now a standard.
from typing import Optional


def 二分法(入数组: list, 查找项: int) -> Optional[int]:
    低值 = 0
    高值 = len(入数组) - 1

    while 低值 <= 高值:
        中值 = (低值 + 高值) // 2
        预测 = 入数组[中值]
        if 预测 == 查找项:
            return 中值
        if 预测 > 查找项:
            高值 = 中值 - 1
        if 预测 < 查找项:
            低值 = 中值 + 1
    return None


入数组 = [1, 3, 5, 7, 9]
assert 二分法(入数组, 5) == 2
assert 二分法(入数组, 10) is None
