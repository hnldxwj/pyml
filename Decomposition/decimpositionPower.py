# -*- coding:utf-8 -*-
import os
dir = "J:\\Seq\\DrivingInCity_3840x1920_30fps_8bit_420\\"
width=3840
height=1920
number=120#帧数
Ysize=width*height
UVsize=Ysize>>2
partsCount=4
#暂时储存的四个部分的yuv
Ybuffer=[bytearray(Ysize/partsCount) for y in range(partsCount)]
Ubuffer=[bytearray(UVsize/partsCount) for y in range(partsCount)]
Vbuffer=[bytearray(UVsize/partsCount) for y in range(partsCount)]
#对于文件夹下每一个文件
for root, dirs, files in os.walk(dir):
    for filename in files:

        print os.path.join(root,filename)
        if not filename.endswith("erp.yuv"):
            break
        file=open(os.path.join(root,filename),"rb")

        for x in range(120/number):#总共要处理的份数
            d4outputfilepath=os.path.join(root,filename)+"-"+str(x)+"-"+str(number)+"fpowerd4.yuv"
            d4outputfile=open(d4outputfilepath,"wb")
            for y in range(number):#处理该文件的number帧
                #读取一帧的Y部分
                lines=file.read(Ysize)
                pos=0
                line=0
                while pos <Ysize:
                    for w in range(width/2):
                        for partNum in range(2):
                            Ybuffer[partNum][(line/2)*(width/2)+(pos-line*width)/2]=lines[pos]
                            pos=pos+1
                    line=line+1
                    for w in range(width/2):
                        for partNum in range(2,4):
                            Ybuffer[partNum][(line/2)*(width/2)+(pos-line*width)/2]=lines[pos]
                            pos=pos+1
                    line = line + 1
                #读取一帧的U部分
                lines=file.read(UVsize)
                pos=0
                line=1
                while pos <UVsize:
                    for w in range(width/2):
                        for partNum in range(2):
                            Ubuffer[partNum][(line/2)*(width/2)+(pos-line*width)/2]=lines[pos]
                            pos=pos+1
                    line = line + 1
                    for w in range(width/2):
                        for partNum in range(2,4):
                            Ubuffer[partNum][(line/2)*(width/2)+(pos-line*width)/2]=lines[pos]
                            pos=pos+1
                    line=line+1
                #读取一帧的V部分
                lines=file.read(UVsize)
                pos=0
                line=0
                while pos <UVsize:
                    for w in range(width/2):
                        for partNum in range(2):
                            Vbuffer[partNum][(line/2)*(width/2)+(pos-line*width)/2]=lines[pos]
                            pos=pos+1
                    line = line + 1
                    for w in range(width/2):
                        for partNum in range(2,4):
                            Vbuffer[partNum][(line/2)*(width/2)+(pos-line*width)/2]=lines[pos]
                            pos=pos+1
                    line = line + 1
                #把这一帧decomposition出的partsCount帧写入
                for partNum in range(partsCount):
                    d4outputfile.write(Ybuffer[partNum])
                    d4outputfile.write(Ubuffer[partNum])
                    d4outputfile.write(Vbuffer[partNum])
            #处理完number帧
            d4outputfile.close()
        file.close()

