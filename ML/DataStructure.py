class Node:
    def __init__(self,val,label):
        self.val=val
        self.label=label


class BinarySearchArray:
    def __init__(self,size):
        self.maxsize=size
        self.size=0
        self.list=[]
        self.type=0

    def insert(self,Node):
        if self.size==0:
            self.list.append(Node)
            self.size+=1
            return True
        if self.size==1:
            if (self.type==0 and Node.val>self.list[0].val) or (self.type==1 and Node.val<self.list[0].val):
                self.list.insert(0,Node)
            else:
                self.list.insert(1,Node)
            #deal with the size
            if self.size==self.maxsize:
                self.list.pop()
            else:
                self.size+=1
            return True



        start=0
        end=self.size-1
        while True:
            if start+1==end:
                #desc
                if self.type==0:
                    if Node.val>self.list[start].val:
                        self.list.insert(start,Node)
                    elif Node.val>self.list[end].val:
                        self.list.insert(end,Node)
                    else:
                        self.insert(end+1,Node)
                #asc
                elif self.type==1:
                    if Node.val<self.list[start].val:
                        self.list.insert(start,Node)
                    elif Node.val<self.list[end].val:
                        self.list.insert(end,Node)
                    else:
                        self.insert(end+1,Node)
                #deal with the size
                if self.size==self.maxsize:
                    self.list.pop()
                else:
                    self.size+=1
                return True
            #find scope
            middle=(start+end)/2
            if self.type==0:
                if Node.val>self.list[middle]:
                    end=middle
                else:
                    start=middle
            if self.type==1:
                if Node.val<self.list[middle]:
                    end=middle
                else:
                    start=middle




    #asc 1 / desc 0
    def setType(self,choose):
        self.type=choose

    def findMost(self):
        dict={}
        most=0
        for x in self.list:
            if dict.get(x.label)==None:
                dict[x.label]=1
            else:
                dict[x.label]+=1
        for label,frequency in dict.items():
            if frequency>most:
                mostlabel=label
        return mostlabel