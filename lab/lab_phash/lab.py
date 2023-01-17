'''
Author: zyy
Date: 2022-12-16 20:24:06
LastEditTime: 2022-12-16 20:24:07
Description: 
'''

import os
import imagehash
from PIL import Image
import csv
import sys 
import time
sys.path.append('./')
import image_hash

label_path = "./build_data/labels/label.csv"
result_path = "./lab/lab_phash/result"
threshold = 10

def lab_phash():
    accuracy_avg = []
    precision_avg = []
    recall_avg = []
    F1_avg = []
    if not os.path.exists(result_path):  #判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(result_path)
    # 全部结果写入地址，包括每一类的和平均的
    # res_all_path = os.path.join(result_path, "res_all.csv")
    # with open(res_all_path, 'w', encoding='utf8') as fa:
    #     res_write = csv.writer(fa)
    #     res_write.writerow(["Category", "Accuracy", "Recall", "F1-Score", "Precision", "Time"])
    
    time_all = 0
    total = 0
    TP = 1
    FP = 1
    TN = 1
    FN = 1
    res_csv_path = os.path.join(result_path, "res_spec_info.csv")
    f = open(res_csv_path, 'w', encoding='utf8')
    res_info_write = csv.writer(f)

    with open(label_path, 'r', encoding='utf8') as f:
        reader = csv.reader(f)
        for row_data in reader:
        # 对label中的相似对和不相似对文本进行simhash计算
        
            time_start = time.time()
            img_path1 = row_data[0]
            img_path2 = row_data[1]
            sim_sample = int(row_data[2])
            
            hash1 =  image_hash.pHash(img_path1)
            hash2 =  image_hash.pHash(img_path2)
            
            res_dist = image_hash.hamming_distance(hash1, hash2)
            res_sim = image_hash.similarity(hash1, hash2)
            if res_dist > threshold:
                sim_exp = 0
            else:
                sim_exp = 1
            data_row = [img_path1, img_path2, sim_sample, sim_exp]
            res_info_write.writerow(data_row)
            # 结果为相似（正）
            if sim_exp == 1: 
                if sim_sample == 1: 
                    TP += 1    # 样本为正
                else: 
                    FP += 1    # 样本为负
            # 结果为不相似（负）
            else:
                if sim_sample == 0: 
                    TN += 1
                else:
                    FN += 1
            total += 1

    time_end = time.time()
    time_use = time_end - time_start
    time_all += time_use
    accuracy =  (TP + TN )/( TP + FP + TN + FN)
    precision = TP / (TP + FP)
    recall = TP / (TP + FN)
    F1 = 2 * precision * recall / (precision + recall)

    # 写入准确率、精确率、召回率、F1的结果
    res_all_path = os.path.join(result_path, "res_all.csv")
    with open(res_all_path, 'w', encoding='utf8') as fs:
        res_write = csv.writer(fs)
        res_write.writerow(["total", total])
        res_write.writerow(["TP", TP])
        res_write.writerow(["FP", FP])
        res_write.writerow(["TN", TN])
        res_write.writerow(["FN", FN])
        res_write.writerow(["accuracy", accuracy])
        res_write.writerow(["precision", precision])
        res_write.writerow(["recall", recall])
        res_write.writerow(["F1-Score", F1])
        res_write.writerow(["time", time_use])

    

if __name__ == "__main__":
    lab_phash()
