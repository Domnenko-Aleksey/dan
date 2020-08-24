import os
from imageai.Prediction import ImagePrediction
# from imageai.Detection import VideoObjectDetection

# detector = VideoObjectDetection()

# Класс VideoObjectDetection предоставляет вам функцию для обнаружения объектов в видео и прямой трансляции с камер устройства и 
# IP-камер с использованием предварительно обученных моделей, которые были обучены на наборе данных COCO. 
# Поддерживаемые модели: RetinaNet, YOLOv3 и TinyYOLOv3.



def aiimage_1(SITE):
    print('FUNCTION -> aiimage/aiimage_1')
    prediction = ImagePrediction()

    # Устанавливает тип модели созданного вами экземпляра распознавания изображений для модели SqueezeNet
    prediction.setModelTypeAsSqueezeNet()

    # Путь к файлу модели, который вы загрузили, и должна соответствовать типу модели, который вы установили для своего экземпляра. 
    # prediction.setModelPath('index/aiimage/models/squeezenet_weights_tf_dim_ordering_tf_kernels.h5')
    prediction.setModelPath('index/aiimage/models/squeezenet_weights_tf_dim_ordering_tf_kernels.h5')

    # Загружает модель из пути, указанного в вызове функции выше, в экземпляр прогнозирования изображения.
    # parameter prediction_speed (optional): (необязательно): этот параметр позволяет сократить время, необходимое для прогнозирования изображения, до 80%, что приводит к небольшому снижению точности. Этот параметр принимает строковые значения. Доступные значения:  “normal”, “fast”, “faster” and “fastest”. The default values is “normal”
    prediction.loadModel()

    # Предсказание изображения. Его можно вызывать много раз для многих изображений после загрузки модели в экземпляр прогноза.
    # Параметр result_count (необязательно): это число возможных прогнозов, которые должны быть возвращены. По умолчанию для параметра установлено значение 5.
    # Возвращает prediction_results (список Python): первое значение, возвращаемое функцией predictionImage, представляет собой список, 
    # содержащий все возможные результаты предсказания. Результаты расположены в порядке убывания процентной вероятности.
    # Возвращает prediction_probabilities (список Python): второе значение, возвращаемое функцией predictionImage, представляет собой список, 
    # который содержит соответствующую процентную вероятность всех возможных прогнозов в prediction_results .
    prediction_results, prediction_probabilities = prediction.predictImage("index/aiimage/images/2.jpg", result_count=10)

    print('---prediction_results---', prediction_results)
    print('---prediction_probabilities---', prediction_probabilities)

    SITE.content += '<h1>AI image 1</h1>'
