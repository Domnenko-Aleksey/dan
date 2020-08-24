'''

import os
from imageai.Detection import ObjectDetection


def aiimage_2(SITE):
    print('FUNCTION -> aiimage/aiimage_2')
    detector = ObjectDetection()

    # Эта функция устанавливает тип модели созданного вами экземпляра обнаружения объекта на модель YOLOv3
    detector.setModelTypeAsYOLOv3()

    # Путь к загруженному файлу модели и соответствует типу модели, установленному вами для экземпляра обнаружения объекта.
    # Параметр detection_speed  (optional): (необязательно): этот параметр позволяет сократить время, необходимое для прогнозирования изображения, до 80%, что приводит к небольшому снижению точности. Этот параметр принимает строковые значения. Доступные значения:  “normal”, “fast”, “faster” and “fastest”. The default values is “normal”
    detector.setModelPath('index/aiimage/models/yolo.h5')

    # Загружает модель из пути, указанного в вызове функции выше
    detector.loadModel()

    # Функция, которая выполняет задачу обнаружения объектов после загрузки модели. Его можно вызывать много раз для обнаружения объектов на любом количестве изображений.
    # - параметр input_image (обязательно): это путь к файлу изображения, который вы хотите обнаружить. 
    #   Вы можете установить этот параметр в массив Numpy потока файлов любого изображения, если вы установите для параметра input_type значение «array» или «stream».
    # - параметр output_image_path (требуется, только если input_type = «file»): относится к пути к файлу, в который будет сохранено обнаруженное изображение. 
    #   Требуется, только если input_type = «file»
    # - параметр minimum_percentage_probability (необязательный): этот параметр используется для определения целостности результатов обнаружения. 
    #   При уменьшении значения отображается больше объектов, а при увеличении значения обеспечивается обнаружение объектов с максимальной точностью. 
    #   Значение по умолчанию - 50.
    # - параметр output_type (необязательно): этот параметр используется для установки формата, в котором будет создаваться обнаруженное изображение. 
    #   Доступные значения: «file» и «array». Значение по умолчанию - «file». Если для этого параметра установлено значение «array», 
    #   функция вернет массив Numpy обнаруженного изображения.
    # - параметр display_percentage_probability (необязательный): этот параметр может использоваться, чтобы скрыть процентную вероятность каждого объекта, 
    #   обнаруженного на обнаруженном изображении, если установлено значение False. Значения по умолчанию - True
    # - параметр display_percentage_probability (необязательный): этот параметр может использоваться, чтобы скрыть процентную вероятность каждого объекта, 
    #   обнаруженного на обнаруженном изображении, если установлено значение False. Значения по умолчанию - True
    detections = detector.detectObjectsFromImage(input_image="index/aiimage/images/2.jpg", output_image_path="index/aiimage/images/new.jpg", minimum_percentage_probability=30)

    for obj in detections:
        print(obj['name'] , ' : ', obj['percentage_probability'], ' : ', obj['box_points'] )
        print('--------------------------------')
'''


from imageai.Detection import ObjectDetection
import os


def aiimage_2(SITE):
    print('FUNCTION -> aiimage/aiimage_2')
    root_path = os.getcwd()
    execution_path = str(root_path) + '/index/aiimage/images'

    print("--------------------------------")
    print(os.path.join(execution_path , "1.jpg"))
    print("\n\n")


    detector = ObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath(os.path.join(execution_path , "yolo.h5"))
    detector.loadModel()
    detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "1.jpg"), output_image_path=os.path.join(execution_path , "imagenew.jpg"), minimum_percentage_probability=30)

    for eachObject in detections:
        print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )
        print("--------------------------------")







    SITE.content += '<h1>AI image 2</h1>'
