window.addEventListener('DOMContentLoaded', function() {
	console.log(123456789);

	var button=document.getElementById('button_fixed_toolbar');
	var toolbar=document.getElementById('toolbar_container');	
		button.addEventListener("click",function()
		{
		   toolbar.classList.toggle('toolbar_container_open');
		   button.classList.toggle('button_fixed_toolbar_open');
		});	

});