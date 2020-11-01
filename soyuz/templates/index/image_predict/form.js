window.addEventListener('DOMContentLoaded', function(){
	IMAGE_PREDICT.init()
});

IMAGE_PREDICT = {
    img_out_num: 1,
    image_files: false,

	// Начальная инициализация
	init(){
        DAN.$('image_predict_form_file').onchange = this.images
    },
    
    // Загрузка изображений
	images(){
        let files = this.files

        if (!files) {
            alert('Не выбрано ни одного изображения')
            return;
        }

        for (var i = 0; i < files.length; i++) {
            if (!files[i].type.match(/image.*/)) {
                alert('Данный формат файла не поддерживается: ' + files[i].name)
                return;
            }
            if (files[i].size > 4096000) {
                alert('Размер изображения ' + files[i].name + ' ' + files[i].size + ' более 4 Мб.');
                return false;
            }
        }

        IMAGE_PREDICT.image_files = files

        let content = 	'<div class="modal_progress_container">'
        content +=			'<h2>Загрука изображений</h2>'
        content +=  		'<div class="modal_img_name_container">'
        content +=      		'<div id="modal_img_name" class="modal_img_name"></div>'
        content +=     			'<div>'
        content +=       			'<span id="modal_num"></span>'
        content +=        			'<span> из </span>'
        content +=        			'<span id="modal_sum">' + files.length + '</span>'
        content +=      		'</div>' 
        content +=  		'</div>'  
        content +=  		'<progress id="modal_progress" class="modal_progress" max="' + files.length + '" value=""></progress>'
        content +=  		'<div id="modal_result"></div>'
        content +=		'</div>'
        
        DAN.modal.add(content, 400)

        // Начинаем загрузку с 0 индекса
        IMAGE_PREDICT.image_load(0)
    },

    // Загрузка изображения на сервер
	image_load(num){
		let req = new XMLHttpRequest()
        let form = new FormData()
		form.append('image', this.image_files[num])
		req.open('post', '/image_predict/file_upload_ajax', true)
		req.send(form)

		DAN.$('modal_num').innerHTML = num + 1
		DAN.$('modal_progress').value = num + 1
		DAN.$('modal_img_name').innerHTML = this.image_files[num].name

		req.onreadystatechange = ()=>{
			if (req.readyState == 4 && req.status == 200) {
				console.log(req.responseText)
				let data = JSON.parse(req.responseText)
				if (data.answer == 'success') {
                    let rnd = Math.floor(Math.random() * 1000000);
                    let out =   '<div class="image_predict_container">'
                    out +=          '<div class="image_predict_title">Обрабатываемое изображение: ' + data.input_img + '</div>'
                    out +=          '<div id="img_predict_wrap_' + IMAGE_PREDICT.img_out_num + '"></div>'
                    out +=      '</div>'
                    DAN.$('image_predict_img_target').innerHTML += out

                    let img = document.createElement('img')
                    img.className = 'image_predict_img'
                    img.src = data.img_path + '?' + rnd

                    DAN.$('img_predict_wrap_' + IMAGE_PREDICT.img_out_num).appendChild(img)

                    num++
                    IMAGE_PREDICT.img_out_num++
					if (num < this.image_files.length) {
                        img.onload = ()=>{
                            IMAGE_PREDICT.image_load(num)
                        }
					} else {
						DAN.$('modal_result').innerHTML = 'Загрузка завершена'
						DAN.modal.del()
					}
				} else {
					DAN.modal.add('Ошибка', 350)
				}
			}
		}
	},
}