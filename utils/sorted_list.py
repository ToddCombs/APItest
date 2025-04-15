# 常用排序函数sorted
from icecream import ic
number = [882, 27, 1, 8, 5, 220, 28, 109, 223, 21, 10, 4]

s_number = sorted(number)

ic(number, s_number)

# 冒泡排序算法
def bub_sort(arr):
    '''
    冒泡排序算法，比大小如果当前元素大于下一个就交换两个元素的位置
    :param arr:
    :return:
    '''
    n = len(arr)
    # 遍历列表内所有元素
    for i in range(n):
        # 最后的i元素已经排好无需再比较
        for j in range(0, n-i-1):
            # 如果当前元素>下一个元素则交换
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

ic(bub_sort(number))