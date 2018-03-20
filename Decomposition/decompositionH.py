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
        #full另写一个py处理吧 需要比较1s的、2s、4s的切片
        #fulloutputfilepath=os.path.join(root,file)+".full.yuv"
        #fulloutputfile=open(fulloutputfilepath,"w")
        for x in range(12):#总共要处理的份数
            d4outputfilepath=os.path.join(root,file)+"-"+str(x)+"d4.yuv"
            d4outputfile=open(outputfilepath,"w")
            orig4outputfilepath=os.path.join(root,file)+"-"+str(x)+".orig4.yuv"
            orig4outputfile=open(orig4outputfilepath,"w")
            for y in range(number):#处理该文件的number帧
                #读取一帧的Y部分
                lines=file.read(Ysize)
                pos=0
                while pos <Ysize:
                    for partNum in range(partsCount):
                        Ybuffer[partNum][pos/partsCount]=lines[pos]
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




