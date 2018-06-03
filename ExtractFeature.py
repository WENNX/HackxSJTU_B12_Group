# -*- coding: utf-8 -*-
import dlib
from skimage import io

face_detector = dlib.get_frontal_face_detector()
landmark_predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

def geteye_rect(imgpath):
    data = []
    im = io.imread(imgpath)
    facesrect = face_detector(im, 1)
    if len(facesrect) <= 0:
        return False
    for k, d in enumerate(facesrect):
        shape = landmark_predictor(im, d)
        for i in range(68):
            pt = shape.part(i)
            data.append(pt.x)
            data.append(pt.y)
    return data
def main():
    imgpath = r"D:\Study\Hackx\Ginni_Rometty.jpg"
    geteye_rect(imgpath)

if __name__ == '__main__':
    main()