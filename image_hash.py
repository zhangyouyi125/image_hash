'''
Author: zyy
Date: 2022-12-04 22:48:01
LastEditTime: 2022-12-09 17:20:33
Description: 
'''
import cv2
import numpy as np
import imagehash
from PIL import Image

# def aHash(img, width=8, high=8):
#     """
#     均值哈希算法
#     :param img: 图像数据
#     :param width: 图像缩放的宽度
#     :param high: 图像缩放的高度
#     :return:感知哈希序列
#     """
#     # 缩放为8*8
#     img = cv2.resize(img, (width, high), interpolation=cv2.INTER_CUBIC)
#     # 转换为灰度图
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     # s为像素和初值为0，hash_str为hash值初值为''
#     s = 0
#     hash_str = ''
#     # 遍历累加求像素和
#     for i in range(8):
#         for j in range(8):
#             s = s + gray[i, j]

#     # 求平均灰度
#     avg = s / 64
#     # 灰度大于平均值为1相反为0生成图片的hash值
#     for i in range(8):
#         for j in range(8):
#             if gray[i, j] > avg:
#                 hash_str = hash_str + '1'
#             else:
#                 hash_str = hash_str + '0'
#     return hash_str


# def dHash(img, width=9, high=8):
#     """
#     差值感知算法
#     :param img:图像数据
#     :param width:图像缩放后的宽度
#     :param high: 图像缩放后的高度
#     :return:感知哈希序列
#     """
#     # 缩放8*8
#     img = cv2.resize(img, (width, high), interpolation=cv2.INTER_CUBIC)
#     # 转换灰度图
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     hash_str = ''
#     # 每行前一个像素大于后一个像素为1，反之置为0，生成感知哈希序列（string）
#     for i in range(high):
#         for j in range(high):
#             if gray[i, j] > gray[i, j + 1]:
#                 hash_str = hash_str + '1'
#             else:
#                 hash_str = hash_str + '0'
#     return hash_str

# def pHash(img_file, width=64, high=64):
#     """
#     感知哈希算法
#     :param img_file: 图像数据
#     :param width: 图像缩放后的宽度
#     :param high:图像缩放后的高度
#     :return:图像感知哈希序列
#     """
#     # 加载并调整图片为32x32灰度图片
#     img = cv2.imread(img_file, 0)
#     img = cv2.resize(img, (width, high), interpolation=cv2.INTER_CUBIC)

#     # 创建二维列表
#     h, w = img.shape[:2]
#     vis0 = np.zeros((h, w), np.float32)
#     vis0[:h, :w] = img  # 填充数据

#     # 二维Dct变换
#     vis1 = cv2.dct(cv2.dct(vis0))
#     vis1.resize(32, 32)

#     # 把二维list变成一维list
#     img_list = vis1.flatten()

#     # 计算均值
#     avg = sum(img_list) * 1. / len(img_list)
#     avg_list = ['0' if i > avg else '1' for i in img_list]

#     # 得到哈希值 
#     return ''.join(['%x' % int(''.join(avg_list[x:x + 4]), 2) for x in range(0, 32 * 32, 4)])

def aHash(img_path, width=8, high=8):
    """
    均值哈希算法
    :param img_path: 图像数据
    :param width: 图像缩放的宽度
    :param high: 图像缩放的高度
    :return:感知哈希序列
    """
    image = Image.open(img_path)
    hash = imagehash.average_hash(image)
    hash = int(str(hash), 16)
    return hash

def dHash(img_path, width=8, high=8):
    """
    感知哈希算法
    :param img_file: 图像数据
    :param width: 图像缩放后的宽度
    :param high:图像缩放后的高度
    :return:图像感知哈希序列
    """
    image = Image.open(img_path)
    hash = imagehash.phash(image)
    hash = int(str(hash), 16)
    return hash

def pHash(img_path, width=8, high=8):
    """
    感知哈希算法
    :param img_file: 图像数据
    :param width: 图像缩放后的宽度
    :param high:图像缩放后的高度
    :return:图像感知哈希序列
    """
    image = Image.open(img_path)
    hash = imagehash.phash(image)
    hash = int(str(hash), 16)
    return hash
def wHash(img_path, width=8, high=8):
    """
    差值感知算法
    :param img:图像数据
    :param width:图像缩放后的宽度
    :param high: 图像缩放后的高度
    :return:感知哈希序列
    """
    image = Image.open(img_path)
    hash = imagehash.whash(image)
    hash = int(str(hash), 16)
    return hash

def cmp_hash(hash1, hash2):
    """
    Hash值对比
    :param hash1: 感知哈希序列1
    :param hash2: 感知哈希序列2
    :return: 返回相似度
    """
    n = 0
    # hash长度不同则返回-1代表传参出错
    if len(hash1) != len(hash2):
        return -1
    # 遍历判断
    for i in range(len(hash1)):
        # 不相等则n计数+1，n最终为相似度
        if hash1[i] != hash2[i]:
            n = n + 1

    return 1 - n / len(hash2)



def hamming_dist(s1, s2):
    # return s1 - s2
    return 1 - sum([ch1 != ch2 for ch1, ch2 in zip(s1, s2)]) * 1. / (32 * 32 / 4)

def hamming_distance(hash_a, hash_b, hashsize = 64):
    x = (hash_a ^ hash_b) 
    distance = 0
    while x:
        distance += 1
        x &= x-1
    return distance

def similarity(a, b):
    HashSize = 64
    return float(HashSize-hamming_distance(a, b)) / float(HashSize)
