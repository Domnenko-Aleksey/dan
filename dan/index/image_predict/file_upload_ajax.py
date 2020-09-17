# from system.catalog.classes.Char import Char
import sys
import json
import uuid
# --- DETECT ---
sys.path.append('yolov5_master')
from dan_detect import dan_detect_init


def file_upload_ajax(SITE):
    print('PATH -> index/image_predict/file_upload_ajax.py')

    # Загрузка файла
    # unique_filename = str(uuid.uuid4())
    filename = SITE.post['image'].filename
    content = SITE.post['image'].file.read()

    # img_input_path = 'media/yolov5/images/' + unique_filename + '.jpg'
    img_input_path = 'media/yolov5/images/image.jpg'
    with open(img_input_path, 'wb') as f:
        f.write(content)

    # Обраюотка файла YOLOv3
    dan_detect_init()

    img_output_path = 'media/yolov5/output/image.jpg'
    answer = {'answer': 'success', 'img_path': img_output_path, 'input_img': filename}
    return {'ajax': json.dumps(answer)}


