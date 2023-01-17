'''
Author: zyy
Date: 2022-12-04 22:42:15
LastEditTime: 2023-01-03 17:39:55
Description: 
'''
import imagehash
from PIL import Image
import image_hash as ihash


def hamming_distance(hash_a, hash_b, hashsize = 64):
    x = (hash_a ^ hash_b) 
    distance = 0
    while x:
        distance += 1
        x &= x-1
    print(distance)
    return distance
highfreq_factor = 4
hash_size = 8
img_size = hash_size * highfreq_factor

# hash1 = imagehash.phash(Image.open('build_data/dataset/image_test.png'),hash_size=hash_size,highfreq_factor=highfreq_factor)
hash1 = imagehash.average_hash(Image.open('build_data/dataset/101_ObjectCategories/gerenuk/image_0003.jpg'))
print(hash1)
# > 354adab5054af0b7
hash2 = imagehash.average_hash(Image.open('build_data/dataset/101_ObjectCategories/gerenuk/image_0004.jpg'))
# hash2 = imagehash.phash(Image.open('build_data/dataset/image_test_rotate.jpg'),hash_size=hash_size,highfreq_factor=highfreq_factor)
print(hash2)
print(str(hash2))
# > 5b7724c8bb364551
print(hash1 - hash2)
hash1 = int(str(hash1),16)
hash2 = int(str(hash2),16)
dis = hamming_distance(hash1, hash2)
print(dis)
print(ihash.similarity(hash1,hash2))# 相似性

print("res")
hash1 = 0x11da2147580056b068095bf0b0a41c52
hash2 = 0x3a215792ec2da88a200baab9c6f895cb
hash1 = int(str(hash1),16)
hash2 = int(str(hash2),16)
print(hash1)
dis = hamming_distance(hash1, hash2)
print(dis)
print(ihash.similarity(hash2,hash1))# 相似性