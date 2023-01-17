'''
Author: zyy
Date: 2022-12-13 22:51:04
LastEditTime: 2022-12-17 19:54:22
Description: 
'''

import image_op as image
import os 
import cv2 as cv
import numpy as np
from PIL import Image
from PIL import ImageEnhance
import csv

dirs_path = "build_data/dataset/101_ObjectCategories"
output_path = "./build_data/dataset-sim"
label_path = "./build_data/labels"
blur = "blur"
sharp = "sharp"
resize = "resize"
light = "light"
contrast = "contrast"

set_nums_img = 10

def generate_img():
    dirs = os.listdir(dirs_path)
    for dir in dirs:
        target_dir = os.path.join(output_path, dir)
        if not os.path.exists(target_dir):  #判断是否存在文件夹如果不存在则创建为文件夹
            os.makedirs(target_dir)
        print(target_dir)
        print(dir)
        sourcedir = os.path.join(dirs_path, dir)
        files = os.listdir(sourcedir)
        files.sort()
        for i in range(set_nums_img):
            img_name = files[i]
            img_src_path = os.path.join(sourcedir, img_name)
            print(img_src_path)
            img = cv.imread(img_src_path)
            
            img_tar_path = []
            # 模糊操作
            img_blur = image.blur(img)
            image.save_img(img_blur, "%s_blur.jpg" % img_name.split(".")[0], target_dir)
            img_tar_path.append(os.path.join(target_dir, "%s_blur.jpg" % img_name.split(".")[0]))

            # 修改图片的亮度
            img_light = image.light(img)
            image.save_img(img_light, "%s_light.jpg" % img_name.split(".")[0], target_dir)
            img_tar_path.append(os.path.join(target_dir, "%s_light.jpg" % img_name.split(".")[0]))

            # 修改图片的大小
            img_resize = image.resize(img)
            image.save_img(img_resize, "%s_resize.jpg" % img_name.split(".")[0], target_dir)
            img_tar_path.append(os.path.join(target_dir, "%s_resize.jpg" % img_name.split(".")[0]))

            # # 修改图片的对比度
            # img_contrast = image.contrast(img)
            # image.save_img(img_contrast, "%s_contrast.jpg" % img_name.split(".")[0], target_dir)
            # img_tar_path.append(os.path.join(target_dir, "%s_contrast.jpg" % img_name.split(".")[0]))

             # 裁剪
            img_contrast = image.crop(img)
            image.save_img(img_contrast, "%s_crop.jpg" % img_name.split(".")[0], target_dir)
            img_tar_path.append(os.path.join(target_dir, "%s_crop.jpg" % img_name.split(".")[0]))
            
            # 锐化
            img_sharp = image.sharp(img)
            image.save_img(img_sharp, "%s_sharp.jpg" % img_name.split(".")[0], target_dir)
            img_tar_path.append(os.path.join(target_dir, "%s_sharp.jpg" % img_name.split(".")[0]))
    
            # 色度变暗
            img_dark = image.dark(img)
            image.save_img(img_dark, "%s_dark.jpg" % img_name.split(".")[0], target_dir)
            img_tar_path.append(os.path.join(target_dir, "%s_dark.jpg" % img_name.split(".")[0]))

            # 随机噪声
            img_noise = image.random_noise(img)
            image.save_img(img_noise, "%s_noise.jpg" % img_name.split(".")[0], target_dir)
            img_tar_path.append(os.path.join(target_dir, "%s_noise.jpg" % img_name.split(".")[0]))
           
            # 旋转
            # img_rotate = image.rotate(img)
            img_rotate1 = Image.open(img_src_path).rotate(45)
            img_rotate1.save(os.path.join(target_dir, "%s_rotate.jpg" % img_name.split(".")[0]))
            img_tar_path.append(os.path.join(target_dir, "%s_rotate.jpg" % img_name.split(".")[0]))

            # 存储到csv中
            # 将图片对的路径和label记录在对应csv文件中
            file_csv = os.path.join(label_path,  "label.csv")
            print(file_csv)
            with open(file_csv, mode='a+', encoding='utf8') as f:
                for target_path in img_tar_path:
                    csv_write = csv.writer(f)
                    #data_row = [file, filename_copy, 1]
                    data_row = [img_src_path, target_path, 1]
                    csv_write.writerow(data_row)
            
    # 两张图片横向合并（便于对比显示）
    # tmp = np.hstack((img, img_rotate))

        
       

if __name__ == "__main__":
    generate_img()