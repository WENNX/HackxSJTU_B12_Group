from watson_developer_cloud import VisualRecognitionV3
import os
from PIL import Image

imgpath = "D:\Study\Hackx\OriginalData"
savepath1 = "D:\Study\Hackx\Pretreatment"
savepath2 = "D:\Study\Hackx\\"
odirname = []
sdirname = []

for file in os.listdir(imgpath):
    file_path = os.path.join(imgpath, file)
    odirname.append(file_path)
for file in os.listdir(imgpath):
    file_path = os.path.join(savepath1, file)
    sdirname.append(file_path)
for i in range(len(odirname)):
    for file in os.listdir(odirname[i]):
        img = os.path.join(odirname[i], file)
        visual_recognition = VisualRecognitionV3('2018-03-19',
        iam_api_key='e09bM9K5ucmFVcDIFwhtWlb1GN8WICV3Sl9rzpamKpzq')
        with open(img, 'rb') as images_file:
            faces = visual_recognition.detect_faces(images_file)
        width =  faces['images'][0]['faces'][0]['face_location']['width']
        top = faces['images'][0]['faces'][0]['face_location']['top']
        left = faces['images'][0]['faces'][0]['face_location']['left']
        height = faces['images'][0]['faces'][0]['face_location']['height']
        im = Image.open(img)
        im = im.crop((left,top,left + width,top + height))
        im.save(os.path.join(sdirname[i], file))
def cutimg(filename):
    visual_recognition = VisualRecognitionV3('2018-03-19',
                                             iam_api_key='e09bM9K5ucmFVcDIFwhtWlb1GN8WICV3Sl9rzpamKpzq')
    with open(filename, 'rb') as images_file:
        faces = visual_recognition.detect_faces(images_file)
    width = faces['images'][0]['faces'][0]['face_location']['width']
    top = faces['images'][0]['faces'][0]['face_location']['top']
    left = faces['images'][0]['faces'][0]['face_location']['left']
    height = faces['images'][0]['faces'][0]['face_location']['height']
    im = Image.open(filename)
    im = im.crop((left, top, left + width, top + height))
    im.save(savepath2 + filename.split('/')[-1])
    return width, top, left, height
