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
        for x in range(12):#总共要处理的份数
            d4outputfilepath=os.path.join(root,file)+"-"+str(x)+"powerd4.yuv"
            d4outputfile=open(outputfilepath,"w")
            for y in range(number):#处理该文件的number帧
                #读取一帧的Y部分
                lines=file.read(Ysize)
                pos=0
                while pos <Ysize:
                    for w in range(width):
                        for partNum in range(2):
                            Ybuffer[partNum][pos/2]=lines[pos]
                            pos=pos+1
                    for w in range(width):
                        for partNum in range(2,4):
                            Ybuffer[partNum][pos/2+2]=lines[pos]
                            pos=pos+1

                #读取一帧的U部分
                lines=file.read(UVsize)
                pos=0
                while pos <UVsize:
                    for w in range(width/2):
                        for partNum in range(2):
                            Ubuffer[partNum][pos/2]=lines[pos]
                            pos=pos+1
                    for w in range(width/2):
                        for partNum in range(2,4):
                            Ubuffer[partNum][pos/2+2]=lines[pos]
                            pos=pos+1
                
                #读取一帧的V部分
                lines=file.read(UVsize)
                pos=0
                while pos <UVsize:
                    for w in range(width/2):
                        for partNum in range(2):
                            Vbuffer[partNum][pos/2]=lines[pos]
                            pos=pos+1
                    for w in range(width/2):
                        for partNum in range(2,4):
                            Vbuffer[partNum][pos/2+2]=lines[pos]
                            pos=pos+1
                #把这一帧decomposition出的partsCount帧写入
                for partNum in range(partsCount):
                    d4outputfile.write(Ybuffer[partNum])
                    d4outputfile.write(Ubuffer[partNum])
                    d4outputfile.write(Vbuffer[partNum])
            #处理完number帧
            d4outputfile.close()




