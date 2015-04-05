from ML import FileImport
if __name__=='__main__':
    print "Hellow You guys!!"

    t1=FileImport.FileImport.file2matrix('testcase.txt')
    print t1
    t2=FileImport.FileImport.normalization(t1)
    print t1
    print t2
