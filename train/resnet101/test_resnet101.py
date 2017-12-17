import sys
sys.path.append('.')
sys.path.append('/home/jinshan/caffe')
sys.path.append('/home/jinshan/caffe/python')
sys.path.append('/home/jinshan/caffe/python/caffe')
import numpy as np
import cv2
import random
import cPickle as pickle
import caffe
import csv
import  os
import time
# caffemodel
MODEL_FILE = './resnet101-1209B_iter_60000.caffemodel'
# deploy
mean_file = './resnet50_mean.npy'
DEPLOY_FILE = './deploy.prototxt'
testDataDir = '/home/jinshan/Workpace/DataBase/test_B/'
timeNow = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
result_path = './csv/test/pigScore-resnet101B' + timeNow + '.csv'
class_n = './csv/test/class-resnet101B72000' + timeNow + '.csv'
false_n = './csv/test/false-resnet101B72000' + timeNow + '.csv'
fileClass = open(class_n, 'w')
file = open(result_path, 'w')
false_file = open(false_n, 'w')
write = csv.writer(file)
write1 = csv.writer(fileClass)
writeFalse = csv.writer(false_file)
writeFalse.writerow(['id', 'score'])

caffe.set_mode_gpu()
net = caffe.Net(DEPLOY_FILE, MODEL_FILE, caffe.TEST)
pigNumber = 0
computerClass = np.zeros(30)
transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
#transformer.set_mean('data',mean_file)
transformer.set_transpose('data', (2, 0, 1))
transformer.set_raw_scale('data', 255)
transformer.set_channel_swap('data', (2, 1, 0))
transformer.set_mean('data', np.load(mean_file).mean(1).mean(1))
net.blobs['data'].reshape(1, 3, 224, 224)

pigNumber = 0
for fileName in os.listdir(testDataDir):
    #print  fileName
    #img = cv2.imread(testDataDir+fileName)
    #img = cv2.resize(img, (224, 224))
    #img = np.swapaxes(img, 0, 2)
    #net.blobs['data'].data[...] = img
    #cv2.imshow('s',img)
    #cv2.waitKey(10)
    img = caffe.io.load_image((testDataDir + fileName))
    imgSrc = cv2.imread(testDataDir + fileName)
    net.blobs['data'].data[...] = transformer.preprocess('data', img)
    [id,s] = fileName.split('.')
    out = net.forward()

    pridects = out['prob'][0]
    index =pridects.argmax()
    if pridects[index] <=0.6:
        writeFalse.writerow([id, index])
        cv2.imwrite('./low/'+fileName, imgSrc)

    computerClass[index] = computerClass[index] + 1
    count = 1
    for score in pridects:
        result = [int(id), count, round(score, 9)]
        write.writerow(result)
        count = count + 1
    pigNumber = pigNumber + 1
    #if pigNumber>10:
    #    break
    print 'pridects: ' + str(id) +' '+ 'count: ' + str(pigNumber) + ' result: ' + str(pridects.argmax())
file.close()
false_file.close()
count1 = 0
for i in computerClass:
    count1 = count1 + 1
    write1.writerow([count1, i])
    print count1, ': ',i
fileClass.close()

