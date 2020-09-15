# import os
# import matplotlib.pyplot as plt

def form(SITE):
    print('PATH -> index/image_predict/form.py')

    SITE.addHeadFile('/lib/DAN/DAN.css')
    SITE.addHeadFile('/lib/DAN/DAN.js')    
    SITE.addHeadFile('/templates/index/image_predict/form.css')
    SITE.addHeadFile('/templates/index/image_predict/form.js')

    SITE.content += '<h1>Предсказание объектов на изображении</h1>'
    SITE.content += '<input id="image_predict_form_file" type="file" multiple="">'
    SITE.content += '<div id="image_predict_img_target"></div>'  