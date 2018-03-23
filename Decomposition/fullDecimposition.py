# -*- coding:utf-8 -*-
import os
dir = "J:\\Seq\\DrivingInCity_3840x1920_30fps_8bit_420\\"
width=3840
height=1920
number=120#帧数
count=1#份数
Ysize=width*height
UVsize=Ysize>>2
#对于文件夹下每一个文件
for root, dirs, files in os.walk(dir):
    for filename in files:
        print os.path.join(root,filename)
        #full生成1s的、2s、4s的切片
        file=open(os.path.join(root,filename),"rb")
        for x in range(count):#总共要处理的份数
            fulloutputfilepath = os.path.join(root, filename) +"-"+str(x)+ "-4sfull.yuv"
            fulloutputfile = open(fulloutputfilepath, "wb")
            for y in range(number):#处理该文件的number帧
                lines=file.read(Ysize+UVsize+UVsize)
                fulloutputfile.write(lines)
            fulloutputfile.close()

        file.close()
        exit()





