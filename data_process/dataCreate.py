import cv2
import numpy as np
import os
import random
import sys
import create_train_test as cf
dataDir = '/media/jinshan/0EA21AAE0EA21AAE/pig-recognition/data/enlarge_train'
srcDataPath = '/home/jinshan/Workpace/pigRecogtion/train'
randomNum = 500
saveDir = '/media/jinshan/0EA21AAE0EA21AAE/pig-recognition/data'
mini_cropPath = '/media/jinshan/0EA21AAE0EA21AAE/pig-recognition/data/mini-crop-150'
def createImg4(classNumber,jNumber,mode,imgPath):
    for i in range(classNumber):
        if mode == 'train':
            cf.mkDir(saveDir +'/' +  mode + '/' + str(i))
        for j in range(jNumber):
            img = cv2.imread(imgPath[i][j])
            print imgPath[i][j]
            if mode == 'train':
                cv2.imwrite(saveDir + '/'+mode+'/'+str(i)+'/'+str(i)+'_'+str(j)+'.jpg', img)
            else:
                cv2.imwrite(saveDir + '/' + mode + '/' + str(i) + '_' + str(i*jNumber+j) + '.jpg', img)
            print mode, ' id:' + str((i*classNumber+jNumber)) + ' save ' + str(j) + '.jpg' + '\n'
def joinPath(pathDir, fileNames): #getwd()
    names = []
    for fileName in fileNames:
        names.append(os.path.join(pathDir, fileName))
    return names

def  readData(pathSdataDir):
   trainPath = []
   valPath = []
   testPath = []
   for i in range(30):
       pathS = dataDir+'/'+str(i)
       color = joinPath(pathS + '/color', random.sample(os.listdir(pathS+'/color/'), 1400))
       crop = joinPath(pathS + '/crop', random.sample(os.listdir(pathS+'/crop/'), 1400))
       mini_crop = joinPath(mini_cropPath + '/' + str(i) + '/mini-crop', random.sample(os.listdir(mini_cropPath + '/' + str(i) + '/mini-crop'), 600))
       mirror =joinPath(pathS +'/mirror',random.sample(os.listdir(pathS+'/mirror/'), 400))
       guass = joinPath(pathS + '/randomGaussian', random.sample(os.listdir(pathS+'/randomGaussian/'), 400))
       src = joinPath(srcDataPath+ '/' + str(i), random.sample(os.listdir(srcDataPath+'/'+str(i)+'/'), 400))
       dirPathTrain = color[0:840] + crop[0:840] + mirror[0:240] + guass[0:240] + src[0:240] + mini_crop
       dirPathVal = color[840:1120] + crop[840:1120] + mirror[240:320] + guass[240:320] + src[240:320]
       dirPathTest = color[1120:1400] + crop[1120:1400] + mirror[320:400] + guass[320:400] +  src[320:400]
       random.shuffle(dirPathTrain)  #shuffle
       random.shuffle(dirPathVal)
       random.shuffle(dirPathTest)
       trainPath.append(dirPathTrain)
       valPath.append(dirPathVal)
       testPath.append(dirPathTest)
   return trainPath,valPath,testPath

trainPath, testPath, valPath = readData(dataDir)
print len(trainPath), len(valPath),len(testPath)

if cf.mkDir(saveDir+'/train'):
    createImg4(30, 3000, 'train', trainPath)

# if cf.mkDir(saveDir + '/test'):
#     createImg4(30, 800, 'test', testPath)
# if cf.mkDir(saveDir + '/val'):
#      createImg4(30, 800, 'val', valPath)






