#NEXTE 我永远喜欢雪之下雪乃
#step.one 模板准备
import cv2
import numpy as np
def roi_area(image_path):
    img = cv2.imread(image_path)
    roi_coordinates=[100,100,200,200]#需要进行调参，只是进行一个示范
    x,y,w,h=roi_coordinates
    roi=img[y:y+h,x:x+w]
    return roi

def load(image_path):
    img = cv2.imread(image_path)
    return img
#step.two 滑动窗口
def template_matching(target_image_path,template_image_path):
    target_img = load(target_image_path)
    template_img = load(template_image_path)
    w,h=template_img.shape[:2]
    result=cv2.matchTemplate(target_img,template_img,cv2.TM_CCOEFF_NORMED)#这个地方会返回一个矩阵，与目标图像大小相同
    min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(result)
    top_left=max_loc
    bottom_right=(top_left[0]+w,top_left[1]+h)
    cv2.rectangle(target_img,(top_left[0],top_left[1]),bottom_right,255,2)
