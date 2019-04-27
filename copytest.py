import os
import time   

sourceDir = r"F:\kankan"
targetDir = r"D:\mmtimages"  
copyFileCounts = 0

def copyFiles(sourceDir, targetDir):   
    global copyFileCounts
    print sourceDir
    print u"%s Current processing drictory%shave process%s files" %(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())), sourceDir,copyFileCounts)   
    for f in os.listdir(sourceDir):
        sourceF = os.path.join(sourceDir, f)
        targetF = os.path.join(targetDir, f)

        if os.path.isfile(sourceF):   
            #create drictory   
            if not os.path.exists(targetDir):
                os.makedirs(targetDir)
            copyFileCounts += 1               
    
            if not os.path.exists(targetF) or (os.path.exists(targetF) and (os.path.getsize(targetF) != os.path.getsize(sourceF))):
  
                open(targetF, "wb").write(open(sourceF, "rb").read())
                print u"%s %s copy finish." %(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())), targetF)   
            else:
                print u"%s %s file is exist,can' copy agian." %(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())), targetF)
           
        if os.path.isdir(sourceF):   
            copyFiles(sourceF, targetF)   

if __name__ == "__main__":
    try:   
        import psyco
        psyco.profile()   
    except ImportError:
        pass
    copyFiles(sourceDir,targetDir)
