if (!ADMIN.catalog)
	ADMIN.catalog = {}

window.addEventListener('DOMContentLoaded', function(){
	ADMIN.catalog.item.init()
});


ADMIN.catalog.item = {
	// Начальная инициализация
	init: ()=>{
		ADMIN.catalog.item.image_file()
		DRAG_DROP()
		var contextmenu_images = [["#ADMIN.catalog.item.image_delete", "contextmenu_delete", "Удалить"]];
		CONTEXTMENU.add("drag_drop_ico", contextmenu_images, "left");
	},

	image_file: ()=>{
		DAN.$('image_file').onchange = function(){
			let files = this.files
			let id = this.dataset.id

			if (!files[0].type.match(/image.*/)) {
				alert("Данный формат файла не поддерживается");
				return;
			}

			var reader = new FileReader();
			reader.onload = function(read_src)
			{
				img_src = read_src.target.result;
				img_uri = encodeURIComponent(img_src);


				let req = new XMLHttpRequest()
				let form = new FormData()
				// form.append('id', id)
				// form.append('img_src', img_uri)
				req.open('post', '/admin/com/catalog/item/img_upload_ajax', true)
				req.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
				req.send("act=upload&id=" + id + "&img_src=" + img_uri);
				// req.send(form)
				req.onreadystatechange = ()=>{
					if (req.readyState == 4 && req.status == 200) {
						console.log(req.responseText)
						var data = JSON.parse(req.responseText)
						if (data.answer == 'success') {
							DAN.$('drag_trg').innerHTML += '<img class="drag_drop_ico" src="' + data.img_path + '" data-target-id="drag_trg" data-class="drag_drop_ico" data-f="ADMIN.catalog.item.images_ordering">';
							if (DAN.$('images_order').value == '')
								DAN.$('images_order').value = data.img_name;
							else
								DAN.$('images_order').value += ';' + data.img_name;
							DAN.$('img_status').innerHTML = '';

							ADMIN.catalog.item.init()
							// contextmenu("drag_drop_ico", contextmenu_item_photo);			
						} else {
							DAN.modal.add('Ошибка', 350)
						}
					}
				}
			}

			reader.readAsDataURL(files[0]);
			document.getElementById("img_status").innerHTML = "<div align=\"left\"><img src=\"/administrator/tmp/images/loading.gif\" /></div>";
		}
	},


	image_delete: (obj)=>{
		let file_name = obj.src.split('/').pop()
		id = DAN.$('image_file').dataset.id

		let req = new XMLHttpRequest()
		let form = new FormData()
		form.append('id', id)
		form.append('file_name', file_name)
		req.open('post', '/admin/com/catalog/item/img_delete_ajax', true)
		req.send(form)

		req.onreadystatechange = ()=>{
			if (req.readyState == 4 && req.status == 200) {
				console.log(req.responseText)
				var data = JSON.parse(req.responseText)
				if (data.answer == 'success') {
					obj.remove()
					s = '/' + file_name + '[;]?/'
					DAN.$('images_order').value = DAN.$('images_order').value.replace(s, '')
					ADMIN.catalog.item.init()
				} else {
					DAN.modal.add('Ошибка', 350)
				}
			}
		}
	},


	images_ordering: ()=>{
		let images = DAN.$('drag_trg').getElementsByClassName('drag_drop_ico')
		let new_images = ''
		for (var i = 0; i < images.length; i++) {
			let file_name = images[i].src.split('/').pop()
			new_images += (i < images.length - 1) ? file_name + ';' : file_name
		}

		DAN.$('images_order').value = new_images
	}
}