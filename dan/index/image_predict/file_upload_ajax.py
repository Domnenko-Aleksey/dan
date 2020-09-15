# from system.catalog.classes.Char import Char
import sys
import json
# sys.path.append('system/catalog/classes')


def file_upload_ajax(SITE):
    print('PATH -> index/image_predict/file_upload_ajax.py')

    print('--- --- --- --- ---')
    print(SITE.file)

    '''
    filename = SITE.file['image']

    # You cannot rely on Content-Length if transfer is chunked.
    size = 0
    with open(filename, 'wb') as f:
        while True:
            chunk = filename['field'].read_chunk()  # 8192 bytes by default.
            if not chunk:
                break
            size += len(chunk)
            f.write(chunk)





    field = SITE.post['image']

    with open('777.jpg', 'wb') as f:
        while True:
            chunk = field.read_chunk()  # 8192 bytes by default.
            if not chunk:
                break
            size += len(chunk)
            f.write(chunk)

    '''




    img_path = '/media/soyuz.jpg'

    answer = {'answer': 'success', 'img_path': img_path}
    return {'ajax': json.dumps(answer)}
