window.addEventListener('DOMContentLoaded', function(){
	ADMIN.catalog.settings()
});

ADMIN.catalog = {
	settings: ()=>{
		let shop_on = DAN.$('catalog_shop_on')
		shop_on.onclick = ()=>{
			let tab = DAN.$('catalog_shop_settings')
			tab.style.display = shop_on.checked ? '' : 'none';
		}
	}
}