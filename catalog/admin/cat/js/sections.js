if (!ADMIN.catalog)
	ADMIN.catalog = {}

ADMIN.catalog.section = {
	delete_modal: (obj)=>{
		let id = obj.dataset.id
		let content = 
			'<div style="text-align:center;font-size:20px">Удалить раздел и всё содержимое</div>' +
			'<div style="text-align:center;margin:20px 0px"><input id="admin_modal_checkbox" type="checkbox" name="check"> Подтверждаю удаление</div>' + 
			'<div class="flex_row">' + 
				'<div style="margin-right:5px">' + 
					'<input id="admin_modal_submit" class="button_red" type="submit" name="submit" value="Удалить">' +
				'</div>' + 
				'<div style="margin-left:5px">' + 
					'<input id="admin_modal_cancel" class="button_white" type="submit" name="cancel" value="Отменить">' +
				'</div>' + 
			'</div>'
		DAN.modal.add(content, 350)
		DAN.$('admin_modal_cancel').onclick = DAN.modal.del
		DAN.$('admin_modal_submit').onclick = ()=>{
			let check = DAN.$('admin_modal_checkbox')
			if (!check.checked) {
				alert('Вы не подтвердили удаление каталога - необходимо поставить галочку')
				return
			} 
			else {
				let req = new XMLHttpRequest()
				let form = new FormData()
				form.append('id', id)
				form.append('agree', 'yes')
				req.open('post', '/admin/com/catalog/section/delete', true);
				req.send(form)
				req.onreadystatechange = ()=>{
					if(req.readyState == 4 && req.status == 200){
						var data = JSON.parse(req.responseText)
						if (data.answer == 'success')
							document.location.href = '/admin/com/catalog/cat/' + data.catalog_id
						else {
							console.log(req.responseText)
							DAN.modal.add('Ошибка', 350)
						}
					}
				}
			}
		}
	}
} 