window.addEventListener('DOMContentLoaded', function(){
	DRAG_DROP()
	ADMIN.chars.delete_modal()
});


ADMIN.chars = {
	delete_modal: ()=>{
		let dels = DAN.$('drag_target').getElementsByClassName('catalog_char_delete')
		for (var i = 0; i < dels.length; i++) {
			dels[i].onclick = function() {
				let id = this.dataset.id
			let content = 
				'<div style="text-align:center;font-size:20px;margin-bottom:40px;">Удалить характеристику и все значения</div>' +
				'<div class="flex_row">' + 
					'<div style="margin-right:5px">' + 
						'<a href="/admin/com/catalog/char/delete/' + id + '" class="button_red">Удалить</a>' +
					'</div>' + 
					'<div style="margin-left:5px">' + 
						'<input id="admin_modal_cancel" class="button_white" type="submit" name="cancel" value="Отменить">' +
					'</div>' + 
				'</div>'
				DAN.modal.add(content)
				DAN.$('admin_modal_cancel').onclick = DAN.modal.del
			}
		}		
	},

	drag_drop: ()=>{
		let tabs = DAN.$('drag_target').getElementsByClassName('drag_drop')
		let catalog_id = DAN.$('drag_target').dataset.catalog_id
		let arr = []
		for (var i = 0; i < tabs.length; i++) {
			arr.push(tabs[i].dataset.id)
		}
		console.log(arr)

		let form = new FormData()
		form.append('catalog_id', catalog_id)
		form.append('char_id_list', arr)
		DAN.ajax('/admin/com/catalog/char/ordering', form, function(data){
			if (data.answer == 'success')
				console.log('Порядок сохранён.')
		})
	}
}