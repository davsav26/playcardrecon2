import glob
import os
import cv2  
import numpy as np
from PIL import Image
from PIL import ImageEnhance
from PIL import ImageOps
import tensorflow as tf
import scipy.misc as sm
from scipy import ndimage
#img= cv2.imread('serpent.jpg') 
#npimg = np.array(Image.open('serpent.jpg'))

#im = Image.open('serpent.jpg')

path = os.path.dirname(os.path.abspath(__file__))
count = 0
opimgnum = 1
#imgpath = "Traindata2.0"
imgpath = "modtrainset1"
if not os.path.exists(imgpath):
    os.makedirs(imgpath)
#oldpath = "data_train"
oldpath = "trainset1"
nw = '/card%d'% (count)

#oldpath = "C:/spring2020/compvis/Final/data_train"
for jpgfile in glob.iglob(os.path.join(oldpath, "*.jpg")):
    npimg = np.array(Image.open(jpgfile))
    im = Image.open(jpgfile)
    enhancer = ImageEnhance.Brightness(im)
    enhanced_im = enhancer.enhance(1.8)
    enhanced_im2 = enhancer.enhance(0.5)
    enhanced_im3 = enhancer.enhance(0.75)
    enhanced_im4 = enhancer.enhance(1.0)
    enhanced_im5 = enhancer.enhance(1.5)
    enhanced_im6 = enhancer.enhance(1.25)
    
    enhancer2 = ImageEnhance.Contrast(im)
    enhanced_c = enhancer2.enhance(1.8)
    enhanced_c2 = enhancer2.enhance(0.5)
    enhanced_c3 = enhancer2.enhance(1.0)
    enhanced_c4 = enhancer2.enhance(0.75)
    enhanced_c5 = enhancer2.enhance(1.5)
    enhanced_c6 = enhancer2.enhance(1.25)
    
    enhancer3 = ImageEnhance.Sharpness(im)
    enhanced_s = enhancer3.enhance(1.8)
    enhanced_s2 = enhancer3.enhance(1.0)
    enhanced_s3 = enhancer3.enhance(0.5)
    enhanced_s4 = enhancer3.enhance(0.75)
    enhanced_s5 = enhancer3.enhance(1.5)
    enhanced_s6 = enhancer3.enhance(1.25)
    
    enhancer4 = ImageEnhance.Color(im)
    enhanced_l = enhancer3.enhance(1.8)
    enhanced_l2 = enhancer3.enhance(1.0)
    enhanced_l3 = enhancer3.enhance(0.5)
    enhanced_l4 = enhancer3.enhance(0.75)
    enhanced_l5 = enhancer3.enhance(1.5)
    enhanced_l6 = enhancer3.enhance(1.25)
    
    im_32 = npimg // 32 * 32
    im_128 = npimg // 128 * 128
    im_dec = npimg
    im_i = 255 - npimg
    
    flip_1 = np.fliplr(npimg)
    flip_2 = np.flipud(npimg)
    rot = np.rot90(npimg)
    im_trim1 = npimg[128:384, 128:384]
    im_bin_64 = (npimg > 64) * 255
    im_bin_192 = (npimg > 192) * 255
    
    Image.fromarray(npimg).save(imgpath + '/card%d.jpg' %(count))
    count+=1
    Image.fromarray(im_dec).save(imgpath + '/card%d.jpg' %(count))
    count +=1
    Image.fromarray(im_32).save(imgpath + '/card%d.jpg' %(count))
    count+=1
    Image.fromarray(im_128).save(imgpath + '/card%d.jpg' %(count))
    count+=1
    Image.fromarray(im_i).save(imgpath + '/card%d.jpg' %(count))
    count+=1
    Image.fromarray(flip_1).save(imgpath + '/card%d.jpg' %(count))
    count+=1
    Image.fromarray(flip_2).save(imgpath + '/card%d.jpg' %(count))
    count+=1
    Image.fromarray(rot).save(imgpath + '/card%d.jpg' %(count))
    count+=1
    #Image.fromarray(enhanced_im).save('Traindata2/card%d.jpg' %(count))
    enhanced_im.save(imgpath + '/card%d.jpg' %(count))
    count+=1
    enhanced_im2.save(imgpath + '/card%d.jpg' %(count))
    count+=1
    enhanced_im3.save(imgpath + '/card%d.jpg' %(count))
    count+=1
    enhanced_im4.save(imgpath + '/card%d.jpg' %(count))
    count+=1
    enhanced_im5.save(imgpath + '/card%d.jpg' %(count))
    count+=1
    enhanced_im6.save(imgpath + '/card%d.jpg' %(count))
    count+=1
    enhanced_c.save(imgpath + '/card%d.jpg' %(count))
    count+=1
    enhanced_c2.save(imgpath + '/card%d.jpg' %(count))
    count+=1
    enhanced_c3.save(imgpath + '/card%d.jpg' %(count))
    count+=1
    enhanced_c4.save(imgpath + '/card%d.jpg' %(count))
    count+=1
    enhanced_c5.save(imgpath + '/card%d.jpg' %(count))
    count+=1
    enhanced_c6.save(imgpath + '/card%d.jpg' %(count))
    count+=1
    enhanced_s.save(imgpath + '/card%d.jpg' %(count))
    count+=1
    enhanced_s2.save(imgpath + '/card%d.jpg' %(count))
    count+=1
    enhanced_s3.save(imgpath + '/card%d.jpg' %(count))
    count+=1
    enhanced_s4.save(imgpath + '/card%d.jpg' %(count))
    count+=1
    enhanced_s5.save(imgpath + '/card%d.jpg' %(count))
    count+=1
    enhanced_s6.save(imgpath + '/card%d.jpg' %(count))
    count+=1
    enhanced_l.save(imgpath + '/card%d.jpg' %(count))
    count+=1  
    enhanced_l2.save(imgpath + '/card%d.jpg' %(count))
    count+=1  
    enhanced_l3.save(imgpath + '/card%d.jpg' %(count))
    count+=1  
    enhanced_l4.save(imgpath + '/card%d.jpg' %(count))
    count+=1
    enhanced_l5.save(imgpath + '/card%d.jpg' %(count))
    count+=1  
    enhanced_l6.save(imgpath + '/card%d.jpg' %(count))
    count+=1  
print('done')

    