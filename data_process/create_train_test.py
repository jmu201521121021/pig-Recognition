import numpy as np
import os
import  cPickle as pickle
import sys
import cv2
import shutil
#srcDataDir = '/media/jinshan/0EA21AAE0EA21AAE/pigData/'
srcDataDir = './yoloTest/train/'
pigClass = 30
pigTrainNumber = 200
pigtestNumber = 50
pigTestStrat = 200
trainTxt = './train_val.txt'

def mkDir(file_path):
    if not os.path.isdir(file_path):
        print file_path + 'not exit that can create'
        os.makedirs(file_path)
        print 'create'+file_path+'success'
        return True
    else:
        print 'warning'+file_path+'is exit'
        return False

def rmFild(file_path):
    if os.path.isdir(file_path):
        shutil.rmtree(file_path)
        print file_path+'remove successfully'
    else:
        print 'warning'+file_path+'is not exit'
# def train(classNumber,trainNumber):
#     for i in range(classNumber):
#         if(mkDir('./train/'+str(i))):
#             for j in range(trainNumber):
#                 img = cv2.imread(srcDataDir+str(i+1)+'/'+str(j)+'.jpg')
#                 cv2.imwrite('./train/'+str(i)+'/'+str(i)+'_'+str(j)+'.jpg', img)
#                 print 'id:' + str((i*classNumber+trainNumber)) + ' save ' + str(j) + '.jpg' + '\n'
#
# def test(classNumber,TestNumber,startNumber):
#     count = 0
#     for i in range(classNumber):
#         for j in range(TestNumber):
#             img = cv2.imread(srcDataDir+str(i+1)+'/'+str(j+startNumber)+'.jpg')
#             cv2.imwrite('./test/'+str(i)+'_'+str(count)+'.jpg', img)
#             print 'id:' + str(count) + 'save ' + str(count) + '.jpg' + '\n'
#           count = count + 1

def createImg(classNumber,jNumber,mode,imgPath,srcDataDir):
    for i in range(classNumber):
        if mode == 'train':
            mkDir('./' + mode + '/' + str(i))
        for j in range(jNumber):
            img = cv2.imread(srcDataDir+str(i)+'/'+ imgPath[i][j])
            print srcDataDir+str(i)+'/'+ imgPath[i][j]
            if mode == 'train':
                cv2.imwrite('./'+mode+'/'+str(i)+'/'+str(i)+'_'+str(j)+'.jpg', img)
            else:
                cv2.imwrite('./' + mode + '/' + str(i) + '_' + str(i*jNumber+j) + '.jpg', img)
            print mode, ' id:' + str((i*classNumber+jNumber)) + ' save ' + str(j) + '.jpg' + '\n'
def saveTrainTxt(classNumber,trainNumber):
    file = open('./train_val.txt', 'w')
    txt = []
    for i in range(classNumber):
        for j in range(trainNumber):
            path = '/train/'+str(i)+'/'+str(i)+'_'+str(j)+'.jpg'
            txt.append(path+' '+str(i)+'\n')
    file.writelines(txt)
    file.close()

def saveTextTxt(classNumber, TestNumber):
    file = open('./val.txt', 'w')
    count = 0
    txt = []
    for i in range(classNumber):
        for j in range(TestNumber):
            path = '/val/'+str(i)+'_'+str(count)+'.jpg'
            txt.append(path + ' ' + str(i) + '\n')
            count = count + 1
    file.writelines(txt)
    file.close()
def readAllImg():
    global  srcDataDir
    trainPath = []
    testPath = []
    valPath = []
    for i in range(30):
        path1 = srcDataDir+str(i)+'/'
        readPath = os.listdir(path1)
        trainPath.append(readPath[0:600])
        testPath.append(readPath[600:700])
        valPath.append(readPath[700:800])
    return trainPath, testPath, valPath
#if mkDir('./train'):
#train(pigClass,pigTrainNumber)
#if mkDir('./test'):
#    test(pigClass, pigtestNumber, pigTestStrat)

#saveTrainTxt(pigClass, pigTrainNumber)
#saveTextTxt(pigClass, pigtestNumber)

#second method 2017-11-30
# trainPath, testPath, valPath = readAllImg()
#
# print len(trainPath[0])
# print len(testPath[29])
# print len(valPath[0])
#
# if mkDir('./train'):
#     createImg(pigClass, 600, 'train', trainPath)
# if mkDir('./test'):
#     createImg(pigClass, 100, 'test', testPath)
# if mkDir('./val'):
#     createImg(pigClass, 100, 'val', valPath)

saveTrainTxt(pigClass, 3000)
#saveTextTxt(pigClass, 800)