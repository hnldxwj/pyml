# -*- coding:utf-8 -*-
import os
dir = "J:\\Seq\\DrivingInCity_3840x1920_30fps_8bit_420\\"
width=3840
height=1920
number=10#帧数
Ysize=width*height
UVsize=Ysize>>2
partsCount=8
#暂时储存的四个部分的yuv
Ybuffer=[bytearray(Ysize/partsCount) for y in range(partsCount)]
Ubuffer=[bytearray(UVsize/partsCount) for y in range(partsCount)]
Vbuffer=[bytearray(UVsize/partsCount) for y in range(partsCount)]

#对于文件夹下每一个文件
for root, dirs, files in os.walk(dir):
    for filename in files:
        print os.path.join(root,filename)
        file=open(os.path.join(root,filename),"rb")
        #full另写一个py处理吧 需要比较1s的、2s、4s的切片
        #fulloutputfilepath=os.path.join(root,file)+".full.yuv"
        #fulloutputfile=open(fulloutputfilepath,"w")
        for x in range(12):#总共要处理的份数
            d4outputfilepath=os.path.join(root,filename)+"-"+str(x)+"-"+str(number)+"fd"+str(partsCount)+".yuv"
            d4outputfile=open(d4outputfilepath,"wb")
            orig4outputfilepath=os.path.join(root,filename)+"-"+str(x)+"-"+str(number)+"forig4.yuv"
            orig4outputfile=open(orig4outputfilepath,"wb")
            for y in range(number):#处理该文件的number帧
                #读取一帧的Y部分
                lines=file.read(Ysize)
                pos=0
                while pos <Ysize:
                    for partNum in range(partsCount):
                        try:
                            Ybuffer[partNum][pos/partsCount]=lines[pos]
                        except IndexError, e:
                            print str(partNum)+"  "+str(pos)
                        pos=pos+1
                orig4outputfile.write(lines)
                #读取一帧的U部分
                lines=file.read(UVsize)
                pos=0
                while pos <UVsize:
                    for partNum in range(partsCount):
                        Ubuffer[partNum][pos/partsCount]=lines[pos]
                        pos=pos+1
                orig4outputfile.write(lines)
                #读取一帧的V部分
                lines=file.read(UVsize)
                pos=0
                while pos <UVsize:
                    for partNum in range(partsCount):
                        Vbuffer[partNum][pos/partsCount]=lines[pos]
                        pos=pos+1
                orig4outputfile.write(lines)
                #把这一帧decomposition出的partsCount帧写入
                for partNum in range(partsCount):
                    d4outputfile.write(Ybuffer[partNum])
                    d4outputfile.write(Ubuffer[partNum])
                    d4outputfile.write(Vbuffer[partNum])
            #处理完number帧
            d4outputfile.close()
            orig4outputfile.close()
        file.close()
        exit()



