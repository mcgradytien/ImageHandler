#!usr/bin/env python
# -*- encoding:utf-8 -*-
# @author :
# @date   :
# @desc   :

import os,time
from PIL import Image
import numpy as np

def write_val_to_csv(data_list):
    # 数据写入到文件
    _time = time.localtime()
    _nowfile = "time_"+str(str(time.mktime(_time)).split('.')[0])+'.csv'
    csvp = r"D:\Python\imagetomatrix"  # csv 文件 路径， -- 修改
    path = os.path.join(csvp,_nowfile)
    try:
        with open(path,'w',newline='') as f:
            for data in data_list:
                str_ = ''
                # str_ = str(data[0]) + "," +str(data[1])
                for i in data:
                    str_ = str_ + str(i) + ","
                str_ = str_.strip(",")
                f.write(str_)
                f.write('\n')
    except Exception as e:
        print('eee')
    pass

def array_justfiy(width,height,list):
    # 降数调整为指定长度的二维列表
    new_list = []
    try:
        xh = len(list)/height
        xw = len(list[0])/width
        xh = int(xh)
        xw = int(xw)
    except ZeroDivisionError as e:
        print("维度错误，核对再输入:%s,%s"%s(str(len(list)), str(len(list[0]))))
        print("分散的数据需要可以同时被整除！")

    # 横向分组
    tempw = []
    for h in range(len(list)):
        for w in range(xw):
            tempw.append(list[h][w*width:(w+1)*width])
    # 纵向分组
    for_list = []
    num_dic = {}
    for _li in range(len(list)):
        unit_list = []
        if _li in num_dic:
            continue
        for d in range(height):
            index  = d*height+_li
            num_dic[index] = ''
            unit_list.append(tempw[index])
        new_list.append(unit_list)
        _li = None
    return new_list

def dimension_reduct(array):
    # 二维转一维
    image_vale = []
    for list in array:
        if len(list) == 0:
            continue
        for d in list:
            image_vale.append(d)
    return image_vale

def image_to_array(imagefilepath):
    # 图片 转 数组
    im = Image.open(imagefilepath)
    # im.show()
    data = im.convert("L") # 转灰度图，彩图需要
    array = np.array(data)
    return array

def image_val_to_file(folds):
    data_list = []
    for parent,folds,files in os.walk(folds):
        if len(files) == 0:
            continue
        for file in files:
            print(file)
            fileP = os.path.join(parent, file)
            array = image_to_array(fileP)
            image_val_list = dimension_reduct(array)
            # image_val_list = [file] + image_val_list
            data_list.append(image_val_list)
    # 矩阵转置
    data_list_re = [[r[col] for r in data_list] for col in range(len(data_list[0]))]
    # write_val_to_csv(data_list_re) # 写入文件
    print(len(data_list_re),len(data_list_re[0]))
    
    # justify_list = array_justfiy(10,10,data_list_re) # 修改 维度，需要是原始的倍数

    imageNum = 0
    for arr in data_list_re:
        imageNum += 1
        saveFile = "D:\Python\imagetomatrix\save"
        svp = os.path.join(saveFile,str(imageNum)+'.png')
        _arr = np.array(arr)
        _arr = np.reshape(_arr,(3,1)) # 自定义
        new_img = Image.fromarray(_arr)
        new_img.save(svp, 'png')
        
    pass


if __name__ == "__main__":
    folds = r"D:\Python\imagetomatrix\test" # 图片的路径--修改
    image_val_to_file(folds)
    pass