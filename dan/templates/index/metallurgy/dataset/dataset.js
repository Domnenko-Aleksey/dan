document.addEventListener("DOMContentLoaded", function(event) {
	DAN.$('button_gen').onclick = ()=>{
		let form = new FormData()
		let r = DAN.$('rand').value
		form.append('r', r)
		DAN.ajax('/metallurgy/dataset_generation', form, function(data){
			DAN.$('dataset_out').innerHTML = data.content
			console.log('-----------------')
		})
	}
});

