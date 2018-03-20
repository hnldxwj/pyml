import os
dir = "e:\\"
width=3840
height=1920
number=10#帧数
Ysize=width*height
UVsize=Ysize>>2
partsCount=4
#暂时储存的四个部分的yuv
Ybuffer=[[0 for x in range(Ysize/partsCount)] for y in range(partsCount)]
Ubuffer=[[0 for x in range(UVsize/partsCount)] for y in range(partsCount)]
Vbuffer=[[0 for x in range(UVsize/partsCount)] for y in range(partsCount)]
#对于文件夹下每一个文件
for root, dirs, files in os.walk(dir):
    for file in files:
        print os.path.join(root,file)
        #full生成1s的、2s、4s的切片
        fulloutputfilepath=os.path.join(root,file)+".full.yuv"
        fulloutputfile=open(fulloutputfilepath,"w")
        for x in range(12):#总共要处理的份数
            for y in range(number):#处理该文件的number帧
                lines=file.read(Ysize+UVsize+UVsize)
                fulloutputfile.write(lines)

            





