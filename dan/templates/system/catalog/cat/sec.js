SYSTEM.section = {
    delete_modal: (obj)=> {
        let id = obj.dataset.id
		let content = 
			'<div style="text-align:center;font-size:20px">Удалить раздел и всё вложенные разделы с элементами?</div>' +
			'<div style="text-align:center;margin:20px 0px"><input id="admin_modal_checkbox" type="checkbox" name="check"> Подтверждаю удаление</div>' + 
			'<div class="flex_row">' + 
				'<div style="margin-right:5px">' + 
					'<input id="modal_submit" class="button_red" type="submit" name="submit" value="Удалить">' +
				'</div>' + 
				'<div style="margin-left:5px">' + 
					'<input id="modal_cancel" class="button_white" type="submit" name="cancel" value="Отменить">' +
				'</div>' + 
			'</div>'
		DAN.modal.add(content, 350)
		DAN.$('modal_cancel').onclick = DAN.modal.del
		DAN.$('modal_submit').onclick = ()=>{
			let check = DAN.$('admin_modal_checkbox')
			if(!check.checked){
				alert('Вы не подтвердили удаление каталога - необходимо поставить галочку')
				return
			}
			else{
				let form = new FormData()
				form.append('id', id)
				form.append('agree', 'yes')				
				DAN.ajax('/system/catalog/section/delete', form, function(data){
					if (data.answer == 'success'){
						console.log('Раздел удалён', data)
						document.location.href = '/system/catalog/cat/' + data.cat_id
					}
				})				
			}
		}
    }
}