document.addEventListener("DOMContentLoaded", function(event) {
	DAN.$('button_gen').onclick = ()=>{
		let form = new FormData()
		DAN.modal.add('Подождите. Идёт обработка и создание датасета')
		DAN.ajax('/metallurgy/dataset_generation', form, function(data){
			document.location.href = '/metallurgy/dataset'
		})
	}
});

