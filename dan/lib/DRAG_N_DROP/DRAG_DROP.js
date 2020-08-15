// СХЕМА РАБОТЫ:
// Отслеживаем событие mousedown на иконке с классом 'drag_drop_ico'
// У иконки считываем 'data-f', 'data-id', 'data-target-id' - id цели (для body - можно ''), 'data-class' - класс объекта перетаскивания, data-direction - направление перетаскивания (all, x, y)
// Вызываем перетаскивание для цели с id = _id и объекта перетаскивания с указанным классом
// Отслеживаем событие движения мыши 'f_mousemove' - добавляем класс c абсолютным позиционированием к объекту 'drag_drop_move'
// При отпускании мыши 'f_mouseup' - удаляем слушателя события 'f_mousemove', и удаляем объект DRAG_DROP.obj
// Функция возвращает id цели - 'target_id', id объекта 'object_id' и порядок следования 'ordering'
// После окончания перетаскивания пытается запустить функцию data-f - если такая есть
DRAG_DROP = function(){
	f_initialize() // Инициализация
	var drag_drop_ico_arr = document.getElementsByClassName('drag_drop_ico');
	for (var i = 0; i < drag_drop_ico_arr.length; i++){
		drag_drop_ico_arr[i].onmousedown = function(event){
			event.preventDefault()
			if(event.which != 1) return // Если нажата не левая кнопка - выходим

			DRAG_DROP.ico = this
			DRAG_DROP.f = DRAG_DROP.ico.getAttribute('data-f') ? DRAG_DROP.ico.getAttribute('data-f') : false
			DRAG_DROP.data_id = DRAG_DROP.ico.getAttribute('data-id')
			DRAG_DROP.target_id = DRAG_DROP.ico.getAttribute('data-target-id')
			DRAG_DROP.obj_class = DRAG_DROP.ico.getAttribute('data-class')
			DRAG_DROP.direction = DRAG_DROP.ico.getAttribute('data-direction')

			DRAG_DROP.target = DRAG_DROP.target_id ? DAN.$(DRAG_DROP.target_id) : document.body
			DRAG_DROP.obj = f_get_obj(DRAG_DROP.ico, DRAG_DROP.obj_class) // Объект перетаскивания

			DRAG_DROP.obj.mouse_offset = f_get_mouse_offset(event, DRAG_DROP.obj) // Находим смещение мыши относительно объекта

			DRAG_DROP.obj.w = DRAG_DROP.obj.getBoundingClientRect().width
			DRAG_DROP.obj.style.width = DRAG_DROP.obj.w + 'px' // Ширина элемента
			DRAG_DROP.obj.style.transition = 'none'
			DRAG_DROP.obj.dd_actions = 'start'

			document.addEventListener('mousemove', f_mousemove) // Перетаскивание
			document.addEventListener('mouseup', f_mouseup) // Завершение перетаскивания
		}
	}


	// Начало перетаскивания
	function f_mousemove(event){
		var obj_over = document.elementFromPoint(event.clientX, event.clientY) // находим элемент под курсором
		event.preventDefault();

		if(DRAG_DROP.obj && DRAG_DROP.obj.dd_actions != 'stop'){
			// Перемещение
			DRAG_DROP.obj.classList.add('drag_drop_move')
			DRAG_DROP.obj.style.position = 'absolute'
			DRAG_DROP.obj.style.zIndex = 10010
			DRAG_DROP.obj.style.pointerEvents = 'none' // не взаимодействовать с переносимым элементом - для elementFromPoint - нахождения элемента под курсором
			DRAG_DROP.obj.style.cursor = 'move'

			// Иногда при смене позиции на абсолютную - меняется размер перетаскиваемого объекта (например, при flex-grow = 1), тогда тащим за центр плашки.
			/*
			if(DRAG_DROP.obj.dd_actions == 'start' && DRAG_DROP.obj.w != DRAG_DROP.obj.getBoundingClientRect().width)
			{
				DRAG_DROP.obj.dd_actions = 'move';
				DRAG_DROP.obj.mouse_offset.left = DRAG_DROP.obj.getBoundingClientRect().width;
			}
			*/

			// Положение родителя DRAG_DROP.target.offsetTop / DRAG_DROP.target.offsetLeft

			// Вычисляем - положение цели абсолютное или нормальное. Это выражение надо осмыслить, не торопись с выводом.
			// Если положение на экране + прокрутка > чем отступ цели - это абсолютное положение
			if((DRAG_DROP.target.getBoundingClientRect().top + window.pageYOffset) > DRAG_DROP.target.offsetTop){
				// ABSOLUTE
				if(DRAG_DROP.direction != 'x') DRAG_DROP.obj.style.top = event.clientY - DRAG_DROP.target.getBoundingClientRect().top - DRAG_DROP.obj.mouse_offset.top + 'px'
				if(DRAG_DROP.direction != 'y') DRAG_DROP.obj.style.left = event.clientX - DRAG_DROP.target.getBoundingClientRect().left - DRAG_DROP.obj.mouse_offset.left + 'px'
			}
			else {
				// NORMAL
				if(DRAG_DROP.direction != 'x') DRAG_DROP.obj.style.top = event.pageY - DRAG_DROP.target.offsetTop - DRAG_DROP.obj.mouse_offset.top + 'px'
				if(DRAG_DROP.direction != 'y') DRAG_DROP.obj.style.left = event.pageX - DRAG_DROP.target.offsetLeft - DRAG_DROP.obj.mouse_offset.left + 'px'
			}

			var obj_over_type = f_get_obj(obj_over, DRAG_DROP.obj_class) // находим элемент указанного типа
			DRAG_DROP.obj_over_target = f_over_target(obj_over, DRAG_DROP.target)

			if(obj_over_type && DRAG_DROP.obj_over_target){
				DRAG_DROP.obj_over = obj_over_type
				DRAG_DROP.obj_over.coordinates = DRAG_DROP.obj_over.getBoundingClientRect()
			}

			DRAG_DROP.obj.dd_actions = 'move'
		}
	}


	// Завершение перетаскивания
	function f_mouseup(event){
		// Удаляем, что бы куча функций не висела в памяти и мешала друг другу
		document.removeEventListener('mousemove', f_mousemove)
		document.removeEventListener('mouseup', f_mouseup)
		document.removeEventListener('mousemove', f_mousemove)

		if(DRAG_DROP.obj && DRAG_DROP.obj.dd_actions == 'move'){ // mouseup должен отработать событие после mousemove (DRAG_DROP.obj.dd_actions = 'move';) иначе по клику произойдёт перемещение вниз
			DRAG_DROP.obj.classList.remove('drag_drop_move')
			DRAG_DROP.obj.style.position = ''
			DRAG_DROP.obj.style.zIndex = ''
			DRAG_DROP.obj.style.top = ''
			DRAG_DROP.obj.style.left = ''
			DRAG_DROP.obj.style.width = ''
			DRAG_DROP.obj.style.pointerEvents = ''
			DRAG_DROP.obj.style.cursor = ''
			DRAG_DROP.obj.style.transition = ''

			if(DRAG_DROP.obj_over_target){ // Перемещаем только в случае, если перетаскиваемый объект находится над целью
				// Вставляем новый объект DRAG_DROP.obj перед объектом подобного типа DRAG_DROP.obj_over при  условии размещении DRAG_DROP.obj_over в том же целевом окне, где и стоит курсор
				if (DRAG_DROP.obj_over){
					// Определяем, куда втавлять - перед obj_over или после - для этого смотрим, курсор в верхней половине или в нижней.
					// Направление DnD
					if(DRAG_DROP.direction == 'y'){
						var obj_over_coordinates_center_y = DRAG_DROP.obj_over.coordinates.top + DRAG_DROP.obj_over.coordinates.height/2

						if(event.clientY > obj_over_coordinates_center_y) DRAG_DROP.obj_over.insertAdjacentElement('afterend', DRAG_DROP.obj) // Вставляем снизу
						else DRAG_DROP.obj_over.insertAdjacentElement('beforebegin', DRAG_DROP.obj) // Вставляем сверху
					}
					else { // DRAG_DROP.direction == all | x
						var obj_over_coordinates_center_x = DRAG_DROP.obj_over.coordinates.left + DRAG_DROP.obj_over.coordinates.width/2

						if(event.clientX > obj_over_coordinates_center_x)DRAG_DROP.obj_over.insertAdjacentElement('afterend', DRAG_DROP.obj) // Вставляем справа
						else DRAG_DROP.obj_over.insertAdjacentElement('beforebegin', DRAG_DROP.obj) // Вставляем слева
					}
				}
				else DRAG_DROP.obj_over_target.appendChild(DRAG_DROP.obj)	// Вариант, когда в целевом элементе ещё нет объектов подобного типа или DRAG_DROP.obj_over принадлежит другому целевому элементу

				f_return() // Функция возвращает данные для обновления 'ordering'
			}
		}

		DRAG_DROP.obj = false
		DRAG_DROP.obj_over = false
		DRAG_DROP.obj.dd_actions = 'stop'
	}


	// Получаем объект указанного типа, поднимаясь по родительским элементам до тех пор, пока не совпадёт тип
	function f_get_obj(_obj, _class){
		while(_obj){
			if (_obj.classList.contains(_class)) return _obj;
			_obj = _obj.parentElement;
		}
		return false;
	}


	// Проверяет - есть ли у данного объекта цель
	function f_over_target(_obj, _target){
		while(_obj){
			if (_obj = _target) return _obj;
			_obj = _obj.parentElement;
		}
		return false;
	}


	// Отступ мыши от объекта перетаскивания
	function f_get_mouse_offset(event, _obj){
		var offset = {
			// От позиции мыши - отнимаем позицию объекта перетаскивания
			top: event.pageY - _obj.getBoundingClientRect().top - window.pageYOffset, // События на мыши - координаты в окне - отступ окна от страниы (прокрутка)
			left: event.pageX - _obj.getBoundingClientRect().left - window.pageXOffset
			// top: event.pageY - DRAG_DROP.target.offsetTop - _obj.offsetTop,
			// left: event.pageX - _obj.offsetLeft
		}
		return offset
	}


	// Функция возвращает id цели - 'target_id', id объекта 'object_id' и порядок следования 'ordering'
	function f_return(){
		// Получим коллекцию элементов узла цели DRAG_DROP.target:
		var elements = DRAG_DROP.target.getElementsByClassName(DRAG_DROP.obj_class)

		var ordering = 0
		for (i = 0; i < elements.length; i++){
			if (elements[i] == DRAG_DROP.obj) break
			ordering++
		}

		// Помещаем данные
		var r = {
			target_id: DRAG_DROP.target_id,
			object_id: DRAG_DROP.ico.getAttribute('data-id'),
			ordering: ordering
		}

		if(DRAG_DROP.f){
			let f_name = DRAG_DROP.f + '(r)'
			eval (f_name)			
		}

		f_initialize() // Инициализация			
	}


	function f_initialize(){
		DRAG_DROP.data_id = false
		DRAG_DROP.f = false // функция, которая вызывается после drag and drop
		DRAG_DROP.target_id = false
		DRAG_DROP.obj_class = false
		DRAG_DROP.target = false // цель
		DRAG_DROP.obj = false // объект перетаскивания
		DRAG_DROP.obj_over = false; // Объект типа над которым находится или находился перетаскиваемый объект.
		DRAG_DROP.ico = false // Иконка drag_n_drop
		DRAG_DROP.obj.dd_actions = false // Текущее действие false, 'start', 'stop', 'move'
	}
}