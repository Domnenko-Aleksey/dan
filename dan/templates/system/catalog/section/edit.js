if (!SYSTEM.catalog)
	SYSTEM.catalog = {}

window.addEventListener('DOMContentLoaded', function(){
	SYSTEM.catalog.section.init()
});


SYSTEM.catalog.section = {
	// Начальная инициализация
	init(){
		DRAG_DROP()
		DAN.$('section_filter_add').onclick = SYSTEM.catalog.section.filter_list
		let del_arr = document.getElementsByClassName("section_filter_delete")
		for (let i = 0; i < del_arr.length; i++) {
			del_arr[i].onclick = SYSTEM.catalog.section.filter_delete
		}
	},

	filter_list(){
		let form = new FormData()
		let catalog_id = DAN.$('section_filter_add').dataset.catalog_id
		form.append('catalog_id', catalog_id)

		DAN.ajax('/system/catalog/section/filter_add_ajax', form, function(data){
			let content = '<h1>Добавить фильтр по характеристике</h1>'
			content += data.content
			DAN.modal.add(content, 450)
		})
	},

	char_insert(){
		let char_list = document.getElementById('section_filter_list')
		let sel = document.getElementById('char_name_select')
		let si = sel.selectedIndex; // selectedIndex в select
		let type = sel.options[si].getAttribute("data-type")
		let unit = sel.options[si].getAttribute("data-unit")
		let name_id = sel.value
		let name = sel.options[si].innerHTML

		let section_filter_tab_arr = document.getElementsByClassName('section_filter_tab')
		for (i=0; i<section_filter_tab_arr.length; i++) {
			if (section_filter_tab_arr[i].dataset.char_name_id == name_id) {
				alert('Характеристика уже добавлена ранее')
				return
			}
		}

		DAN.modal.del();

		let tab_inner = '<tr>'
		tab_inner += '<td class="section_filter_tab_ico_dnd">'
		tab_inner += 	'<div class="flex_row contextmenu_wrap">'
		tab_inner += 		'<svg class="drag_drop_ico" title="Перетащить" data-id="' + name_id + '" data-target-id="section_filter_list" data-class="section_filter_tab" data-direction="y" data-f="SYSTEM.catalog.section.filter_ordering">'
		tab_inner += 		'<use xlink:href="/templates/system/svg/sprite.svg#cursor24"></use></svg>'
		tab_inner += 	'</div>'
		tab_inner += '</td>'	
		tab_inner += '<td class="section_filter_tab_name">' + name + ' (' + unit + ')<input type="hidden" name="filter_id[]" value=""><input type="hidden" name="filter_char_id[]" value="' + name_id + '"></td>'
		
		if (type == 'number') {
			tab_inner += '<td class="section_filter_tab_type">число</td>'
			tab_inner += '<td class="section_filter_tab_value">'
			tab_inner += 	'<input draggable="false" class="input section_filter_input_number" type="text" name="filter_value_1[]" value="">'
			tab_inner += 	'<input draggable="false" class="input section_filter_input_number" type="text" name="filter_value_2[]" value="">'
			tab_inner += '</td>'
		}

		if (type == 'string') {
			tab_inner += '<td class="section_filter_tab_type">строка</td>';	
			tab_inner += '<td class="section_filter_tab_value">'
			tab_inner += 	'<input draggable="false" class="input section_filter_input_string" type="text" name="filter_value_1[]" value="">'
			tab_inner += 	'<input class="input section_filter_input_string" type="hidden" name="filter_value_2[]" value="">'
			tab_inner += '</td>'
		}

		tab_inner += '<td class="section_filter_tab_delete">'
		tab_inner += 	'<svg class="section_filter_delete" data-id="0"><use xlink:href="/templates/system/svg/sprite.svg#delete"></use></svg>'
		tab_inner += '</td>'
		tab_inner += '</tr>'

		let tab = document.createElement('table')
		tab.className = 'section_filter_tab'
		tab.setAttribute('draggable', 'true')
		tab.setAttribute('data-id', '')
		tab.setAttribute('data-char_name_id', name_id)
		tab.innerHTML = tab_inner

		document.getElementById('section_filter_list').appendChild(tab)
		
		// инициализируем заново функцию drag_drop - т.к. появился новый узел на котором следует отслеживать событие
		SYSTEM.catalog.section.init()
	},

	filter_delete(){
		let use = document.elementFromPoint(event.clientX, event.clientY)
		let svg = SYSTEM.catalog.section.get_obj(use, 'section_filter_delete')
		let id = svg.dataset.id;

		obj_del = SYSTEM.catalog.section.get_obj(svg, 'section_filter_tab')
		if (id == 0) {
			obj_del.remove()
			return
		}

		let form = new FormData()
		form.append('id', id)
		DAN.ajax('/system/catalog/section/filter_delete_ajax', form, function(data) {
			obj_del.remove()
			SYSTEM.catalog.section.init()
		})
	},

	filter_ordering(){
		console.log('ORDERING')
	},
	
	// Получаем объект, поднимаясь по родительским элементам до тех пор, пока не совпадёт класс объекта
	get_obj(obj, target_class){
		while (obj) {
			if (obj.classList.contains(target_class)) 
				return obj;
			obj = obj.parentElement;
		}
		return false;
	}
}