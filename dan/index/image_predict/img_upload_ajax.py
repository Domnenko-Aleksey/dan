# from system.catalog.classes.Char import Char
import shutil
import sys
import json
# sys.path.append('system/catalog/classes')


def img_upload_ajax(SITE):
    print('PATH -> index/image_predict/img_upload_ajax.py')

    print(SITE.post)
    print('--------------------', SITE.post['image'].name, SITE.post['image'].filename, SITE.post['image'].content_type)  # content_type='image/jpeg',
    tmp_file = SITE.post['image'].file

    # file_matcher = re.compile (r'\.(?:jpe?g|gif|png)$', re.IGNORECASE)
    # ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
    # def allowed_file(filename):
    # this has changed from the original example because the original did not work for me
    # return filename[-3:].lower() in ALLOWED_EXTENSIONS





    field = SITE.post['image']

    with open('777.jpg', 'wb') as f:
        while True:
            chunk = field.read_chunk()  # 8192 bytes by default.
            if not chunk:
                break
            size += len(chunk)
            f.write(chunk)






    img_path = '/media/soyuz.jpg'

    answer = {'answer': 'success', 'img_path': img_path}
    return {'ajax': json.dumps(answer)}
