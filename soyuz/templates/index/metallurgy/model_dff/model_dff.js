document.addEventListener("DOMContentLoaded", function(event) {
	DAN.$('gen_button').onclick = ()=>{
		let form = new FormData()
		let epochs = DAN.$('gen_epochs').value
        form.append('epochs', epochs)
        DAN.modal.add('Подождите. Идёт обучение модели на протяжении <b>' + epochs + '</b> эпох.', 400)
		DAN.ajax('/metallurgy/model_dff_train', form, function(data){
			document.location.href = '/metallurgy/model_dff'
		})
	}
});