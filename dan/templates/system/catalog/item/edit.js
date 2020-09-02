if (!SYSTEM.catalog)
	SYSTEM.catalog = {}

window.addEventListener('DOMContentLoaded', function(){
	SYSTEM.catalog.item.init()
});


SYSTEM.catalog.item = {
	// Начальная инициализация
	init: ()=>{
		// SYSTEM.catalog.item.image_file()
		DRAG_DROP()
		// let contextmenu_images = [["#SYSTEM.catalog.item.image_delete", "contextmenu_delete", "Удалить"]];
		// CONTEXTMENU.add("catalog_item_image", contextmenu_images, "left");
		DAN.$('char_value_add').onclick = SYSTEM.catalog.item.char_list
		let del_arr = document.getElementsByClassName("catalog_char_delete")
		for (let i = 0; i < del_arr.length; i++) {
			del_arr[i].onclick = SYSTEM.catalog.item.char_delete
		}
	},


	image_file: ()=>{
        return
		DAN.$('image_file').onchange = function(){
			let files = this.files
			let id = this.dataset.id

			if (!files[0].type.match(/image.*/)) {
				alert("Данный формат файла не поддерживается");
				return;
			}

			let reader = new FileReader();
			reader.onload = function(read_src)
			{
				img_src = read_src.target.result;
				img_uri = encodeURIComponent(img_src);


				let req = new XMLHttpRequest()
				let form = new FormData()
				// form.append('id', id)
				// form.append('img_src', img_uri)
				req.open('post', '/SYSTEM/com/catalog/item/img_upload_ajax', true)
				req.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
				req.send("act=upload&id=" + id + "&img_src=" + img_uri);
				// req.send(form)
				req.onreadystatechange = ()=>{
					if (req.readyState == 4 && req.status == 200) {
						console.log(req.responseText)
						var data = JSON.parse(req.responseText)
						if (data.answer == 'success') {
							DAN.$('drag_trg').innerHTML += '<img class="drag_drop_ico catalog_item_image" src="' + data.img_path + '" data-target-id="drag_trg" data-class="drag_drop_ico" data-f="SYSTEM.catalog.item.images_ordering">';
							if (DAN.$('images_order').value == '')
								DAN.$('images_order').value = data.img_name;
							else
								DAN.$('images_order').value += ';' + data.img_name;
							DAN.$('img_status').innerHTML = '';

							SYSTEM.catalog.item.init()
							// contextmenu("drag_drop_ico", contextmenu_item_photo);			
						} else {
							DAN.modal.add('Ошибка', 350)
						}
					}
				}
			}

			reader.readAsDataURL(files[0]);
			document.getElementById("img_status").innerHTML = "<div align=\"left\"><img src=\"/SYSTEMistrator/tmp/images/loading.gif\" /></div>";
		}
	},

	image_delete: (obj)=>{
		let file_name = obj.src.split('/').pop()
		id = DAN.$('image_file').dataset.id

		let form = new FormData()
		form.append('id', id)
		form.append('file_name', file_name)
		DAN.ajax('/SYSTEM/com/catalog/item/img_delete_ajax', form, function(data){
			obj.remove()
			s = '/' + file_name + '[;]?/'
			DAN.$('images_order').value = DAN.$('images_order').value.replace(s, '')
			SYSTEM.catalog.item.init()
		})
	},

	images_ordering: ()=>{
		let images = DAN.$('drag_trg').getElementsByClassName('drag_drop_ico')
		let new_images = ''
		for (var i = 0; i < images.length; i++) {
			let file_name = images[i].src.split('/').pop()
			new_images += (i < images.length - 1) ? file_name + ';' : file_name
		}

		DAN.$('images_order').value = new_images
	},

	char_list: ()=>{
		let form = new FormData()
		let catalog_id = DAN.$('char_value_add').dataset.catalog_id
		form.append('catalog_id', catalog_id)

		DAN.ajax('/system/catalog/item/char_list_add_ajax', form, function(data){
			let content = '<h1>Добавить характеристику</h1>'
			content += data.content
			DAN.modal.add(content, 450)
		})
	},
	
	char_delete: ()=>{
		let use = document.elementFromPoint(event.clientX, event.clientY)
		let svg = SYSTEM.catalog.item.get_obj(use, 'catalog_char_delete')
		let id = svg.dataset.id;

		if (id == 0)
			return

		let form = new FormData()
		form.append('id', id)
		DAN.ajax('/system/catalog/item/char_delete_ajax', form, function(data) {

			obj_del = SYSTEM.catalog.item.get_obj(svg, 'char_tab')
			obj_del.remove()
			SYSTEM.catalog.item.init()
		})
	},

	char_insert: ()=>{
		console.log('CHAR INSERT')
		let char_list = document.getElementById('char_list')
		let sel = document.getElementById('char_name_select')
		let si = sel.selectedIndex; // selectedIndex в select
		let type = sel.options[si].getAttribute("data-type")
		let unit = sel.options[si].getAttribute("data-unit")
		let name_id = sel.value
		let name = sel.options[si].innerHTML

		DAN.modal.del();

		let tab_inner = '<tr>'
		tab_inner += '<td class="char_tab_ico_dnd">'
		tab_inner += 	'<div class="flex_row contextmenu_wrap">'
		tab_inner += 		'<svg class="drag_drop_ico" title="Перетащить" data-id="' + name_id + '" data-target-id="char_list" data-class="char_tab" data-direction="y" data-f="SYSTEM.catalog.item.ordering">'
		tab_inner += 		'<use xlink:href="/templates/system/svg/sprite.svg#cursor24"></use></svg>'
		tab_inner += 	'</div>'
		tab_inner += '</td>'	
		tab_inner += '<td class="char_tab_name">' + name + ' (' + unit + ')<input type="hidden" name="char_id[]" value=""><input type="hidden" name="char_name_id[]" value="' + name_id + '"></td>'
		
		if (type == 'number') {
			tab_inner += '<td class="char_tab_type">число</td>';
			tab_inner += '<td class="char_tab_value"><input draggable="false" class="input char_input_number" type="text" name="char_value[]" value=""></td>'
		}

		if (type == 'string') {
			tab_inner += '<td class="char_tab_type">строка</td>';	
			tab_inner += '<td class="char_tab_value"><input draggable="false" class="input char_input_string" type="text" name="char_value[]" value=""></td>'
		}

		tab_inner += '<td class="char_tab_delete">'
		tab_inner += 	'<svg class="catalog_char_delete" data-id="0"><use xlink:href=""/templates/system/svg/sprite.svg#delete"></use></svg>'
		tab_inner += '</td>'
		tab_inner += '</tr>'

		let tab = document.createElement('table')
		tab.className = 'char_tab'
		tab.setAttribute('draggable', 'true')
		tab.setAttribute('data-id', '')
		tab.innerHTML = tab_inner

		//char_list.insertBefore(tab, document.getElementById("drag_drop_end"));
		document.getElementById('char_list').appendChild(tab)
		
		// инициализируем заново функцию drag_drop - т.к. появился новый узел на котором следует отслеживать событие
		SYSTEM.catalog.item.init()
	},

	char_ordering: ()=>{
		console.log('ORDERING')
	},
	
	// Получаем объект, поднимаясь по родительским элементам до тех пор, пока не совпадёт класс объекта
	get_obj: (obj, target_class)=>{
		while (obj) {
			if (obj.classList.contains(target_class)) 
				return obj;
			obj = obj.parentElement;
		}
		return false;
	}
}