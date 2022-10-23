import sys
import random

def apriori(D, minSup):
    """
    频繁项集用keys表示，
    key表示项集中的某一项，
    cutKeys表示经过剪枝步的某k项集。
    C表示某k项集的每一项在事务数据库D中的支持计数
    :param D:
    :param minSup:
    :return:
    """
    C1 = {}
    for T in D:
        for I in T:
            if I in C1:
                C1[I] += 1
            else:
                C1[I] = 1

    _keys1 = C1.keys()

    keys1 = []
    for i in _keys1:
        keys1.append([i])

    n = len(D)
    cutKeys1 = []
    for k in keys1[:]:
        if C1[k[0]] * 1.0 / n >= minSup:
            cutKeys1.append(k)

    cutKeys1.sort()

    keys = cutKeys1
    all_keys = []
    while keys != []:
        C = getC(D, keys)
        cutKeys = getCutKeys(keys, C, minSup, len(D))
        for key in cutKeys:
            all_keys.append(key)
        keys = aproiri_gen(cutKeys)

    return all_keys


def getC(D, keys):
    """
     对keys中的每一个key进行计数
    :param D:
    :param keys:
    :return:
    """
    C = []
    for key in keys:
        c = 0
        for T in D:
            have = True
            for k in key:
                if k not in T:
                    have = False
            if have:
                c += 1
        C.append(c)
    return C


def getCutKeys(keys, C, minSup, length):
    """
    剪枝步
    :param keys:
    :param C:
    :param minSup:
    :param length:
    :return:
    """
    for i, key in enumerate(keys):
        if float(C[i]) / length < minSup:
            keys.remove(key)
    return keys


def keyInT(key, T):
    """
    判断项key是否在数据库中某一元组T中
    :param key:
    :param T:
    :return:
    """
    for k in key:
        if k not in T:
            return False
    return True


def aproiri_gen(keys1):
    """
    连接步
    :param keys1:
    :return:
    """
    keys2 = []
    for k1 in keys1:
        for k2 in keys1:
            if k1 != k2:
                key = []
                for k in k1:
                    if k not in key:
                        key.append(k)
                for k in k2:
                    if k not in key:
                        key.append(k)
                key.sort()
                if key not in keys2:
                    keys2.append(key)

    return keys2

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
slice = random.sample(list, 5)  #从list中随机获取5个元素，作为一个片断返回
D = [random.sample(list, 5) for i in range(10)]
print(D)
F = apriori(D, 0.5)
print(F)
# [['B'], ['C'], ['E'], ['B', 'E'], ['C', 'E']]