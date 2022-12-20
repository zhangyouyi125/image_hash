'''
Author: zyy
Date: 2022-12-05 12:19:50
LastEditTime: 2022-12-09 17:21:11
Description: 
'''

import time
import os.path as path
import cv2
import image_hash as ihash
import imagehash


# from core_hash.dedup_core_base import *


def concat_info(type_str, score, time):
    temp = '%s相似度：%.2f %% -----time=%.4f ms' % (type_str, score * 100, time)
    print(temp)
    return temp


def test_diff_hash(img1_path, img2_path, loops=1000):
    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)
    start_time = time.time()

    for _ in range(loops):
        hash1 = ihash.dHash(img1)
        hash2 = ihash.dHash(img2)
        ihash.cmp_hash(hash1, hash2)

    print(">>> 执行%s次耗费的时间为%.4f s." % (loops, time.time() - start_time))


def test_aHash(img1, img2):
    # img1 = cv2.imread(img1)
    # img2 = cv2.imread(img2)

    time1 = time.time()
    hash1 = ihash.aHash(img1)
    hash2 = ihash.aHash(img2)
    # print(hex(int(hash1, 2)))
    # print(hex(int(hash2, 2)))
    n = ihash.hamming_distance(hash1, hash2)
    s = ihash.similarity(hash1, hash2)
    return concat_info("均值哈希算法", s, time.time() - time1) + "\n"


def test_dHash(img1, img2):
    # img1 = cv2.imread(img1)
    # img2 = cv2.imread(img2)

    time1 = time.time()
    hash1 = ihash.dHash(img1)
    hash2 = ihash.dHash(img2)
    # print(hex(int(hash1, 2)))
    # print(hex(int(hash2, 2)))
    n = ihash.hamming_distance(hash1, hash2)
    s = ihash.similarity(hash1, hash2)
    return concat_info("差异哈希算法", s, time.time() - time1) + "\n"


def test_pHash(img1_path, img2_path):

    time1 = time.time()
    hash1 = ihash.pHash(img1_path)
    hash2 = ihash.pHash(img2_path)
    # print(hex(int(hash1, 2)))
    # print(hex(int(hash2, 2)))
    n = ihash.hamming_distance(hash1, hash2)
    s = ihash.similarity(hash1, hash2)
    return concat_info("感知哈希算法", s, time.time() - time1) + "\n"


def deal(img1_path, img2_path):
    info = ''

    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)

    # 计算图像哈希相似度
    info = info + test_aHash(img1, img2)
    info = info + test_dHash(img1, img2)
    info = info + test_pHash(img1_path, img2_path)
    return info


def contact_path(file_name):
    output_path = "./build_data/dataset"
    return path.join(output_path, file_name)


def main():
    # data_img_name = '101_ObjectCategories/airplanes/image_0001.jpg'
    data_img_name = 'test.jpg'

    data_img_name_base = data_img_name.split(".")[0]

    base = contact_path(data_img_name)
    light = contact_path("%s_light.jpg" % data_img_name_base)
    resize = contact_path("%s_resize.jpg" % data_img_name_base)
    contrast = contact_path("%s_contrast.jpg" % data_img_name_base)
    sharp = contact_path("%s_sharp.jpg" % data_img_name_base)
    blur = contact_path("%s_blur.jpg" % data_img_name_base)
    color = contact_path("%s_color.jpg" % data_img_name_base)
    rotate = contact_path("%s_rotate.jpg" % data_img_name_base)
    print(base)

    # 测试算法的效率
    # test_diff_hash(base, base)
    # test_diff_hash(base, light)
    # test_diff_hash(base, resize)
    # test_diff_hash(base, contrast)
    # test_diff_hash(base, sharp)
    # test_diff_hash(base, blur)
    # test_diff_hash(base, color)
    # test_diff_hash(base, rotate)

    # 测试ahash
    print(test_aHash(base, base))
    print(test_aHash(base, light))
    print(test_aHash(base, resize))
    print(test_aHash(base, contrast))
    print(test_aHash(base, sharp))
    print(test_aHash(base, blur))
    print(test_aHash(base, color))
    print(test_aHash(base, rotate))

     # 测试dhash
    print(test_dHash(base, base))
    print(test_dHash(base, light))
    print(test_dHash(base, resize))
    print(test_dHash(base, contrast))
    print(test_dHash(base, sharp))
    print(test_dHash(base, blur))
    print(test_dHash(base, color))
    print(test_dHash(base, rotate))
    
     # 测试phash
    print(test_pHash(base, base))
    print(test_pHash(base, light))
    print(test_pHash(base, resize))
    print(test_pHash(base, contrast))
    print(test_pHash(base, sharp))
    print(test_pHash(base, blur))
    print(test_pHash(base, color))
    print(test_pHash(base, rotate))
    

if __name__ == '__main__':
    main()
