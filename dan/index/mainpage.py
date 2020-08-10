import sys


def mainpage(SITE):
    print('FUNCTION -> system_> mainpage')

    SITE.content += f'''<div class="mainpage_container">
            <div class="w1200 wrap flex_between mainpage_wrap ">
                <div class="mainpage_block">
                    <div>
                        <div class="mainpage_title">Разработка чат-бота</div>
                        <div>
                            <br><i class="mainpage_text" style="font-size: 24px;">Разработка функционала чат-ботов, который помогает пользователям с повседневными задачами</i></div>
                        <!--<table style="margin-top:30px;">
                            <tbody>
                                <tr>
                                    <td style="height:50px; width:50px">
                                        <svg class="mainpage_icon">
                                            <use xlink:href="/lib/svg/sprite.svg#pipline_1"></use>
                                        </svg>
                                    </td>
                                    <td><span style="font-size:18px"><span style="color:#ffffff">Информация о трассах</span></span>
                                    </td>
                                </tr>
                                <tr>
                                    <td style="height:50px">
                                        <svg class="mainpage_icon">
                                            <use xlink:href="/lib/svg/sprite.svg#pipline_2"></use>
                                        </svg>
                                    </td>
                                    <td><span style="font-size:18px"><span style="color:#ffffff">Объекты, сведения</span></span>
                                    </td>
                                </tr>
                                <tr>
                                    <td style="height:50px">
                                        <svg class="mainpage_icon">
                                            <use xlink:href="/lib/svg/sprite.svg#monitoring"></use>
                                        </svg>
                                    </td>
                                    <td><span style="font-size:18px"><span style="color:#ffffff">Получение данных с датчиков на основе Iot (интернет вещей)</span></span>
                                    </td>
                                </tr>
                                <tr>
                                    <td style="height:50px">
                                        <svg class="mainpage_icon">
                                            <use xlink:href="/lib/svg/sprite.svg#alarm"></use>
                                        </svg>
                                    </td>
                                    <td><span style="font-size:18px"><span style="color:#ffffff">Контроль несанкционированного доступа (Iot)</span></span>
                                    </td>
                                </tr>
                                <tr>
                                    <td style="height:50px">
                                        <svg class="mainpage_icon">
                                            <use xlink:href="/lib/svg/sprite.svg#map"></use>
                                        </svg>
                                    </td>
                                    <td><span style="font-size:18px"><span style="color:#ffffff">Карта с отображением трасс, узлов, объектов</span></span>
                                    </td>
                                </tr>
                            </tbody>
                        </table>-->
                        <table style="margin-top: 30px;">
                            <tbody>
                                <tr>
                                    <td><a class="button_custom" href="/help" style="text-align:center;">Помощь</a></td>
                                    <td style="width:10px">&nbsp;</td>
                                    <td><a class="button_light" href="/map">Карта</a></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
				<div class="mainpage_img"><img alt="Django" src="/media/mainpage_img.jpg"></div>				
            </div>
			<div class="wave-gray"></div>
	   </div>
	   <div class="gray_container">
		   <div class="w1300 flex_row p_40_20">
				<div class="white_element">
					<img class="white_element_img" alt="" src="/media/white_element_img.png">
					<h2 style="font-size: 24px">Заголовок 2</h2>
					<p style="text-align: center;">Разнообразный и богатый опыт реализация намеченных плановых заданий требуют от нас анализа позиций.</p>
				</div>
				<div class="white_element"><img class="white_element_img alt="" src="/media/white_element_img.png">
				<h2 style="font-size: 24px">Заголовок 2</h2>
				<p style="text-align: center;">Разнообразный и богатый опыт реализация намеченных плановых заданий требуют от нас анализа позиций.</p>
				</div>
				<div class="white_element"><img class="white_element_img alt="" src="/media/white_element_img.png">
				<h2 style="font-size: 24px">Заголовок 2</h2>
				<p style="text-align: center;">Разнообразный и богатый опыт реализация намеченных плановых заданий требуют от нас анализа позиций.</p>
				</div>
				<div class="white_element"><img class="white_element_img alt="" src="/media/white_element_img.png">
				<h2 style="font-size: 24px">Заголовок 2</h2>
				<p style="text-align: center;">Разнообразный и богатый опыт реализация намеченных плановых заданий требуют от нас анализа позиций.</p>
				</div>
			</div>
		</div>
		<div class="wave-gray-bottom"></div>
		<div class="white_container">
			<div class="w1300 flex_row p_40_20">
				<div class="gray_element">
					<img class="white_element_img alt="" src="/media/white_element_img.png">
					<div style="padding: 15px;"
					<strong><h2 style="font-size: 24px">Заголовок 2 уровня</h2></strong>
					<hr />
					<p>Разнообразный и богатый опыт реализация намеченных плановых заданий требуют от нас анализа позиций, занимаемых участниками в отношении поставленных задач. С другой стороны начало повседневной работы по формированию позиции представляет собой интересный эксперимент проверки форм развития. Разнообразный и богатый опыт реализация намеченных плановых заданий влечет за собой процесс внедрения и модернизации новых предложений. Значимость этих проблем настолько очевидна, что реализация намеченных плановых заданий представляет собой интересный эксперимент проверки дальнейших направлений развития.</p>
					</div>
				</div>
				<div class="gray_element_2">
					<div style="flex-basis: 220px;"><img style="width: 100%;height: auto;" alt="" src="/media/white_element_img.png"></div>
					<div style="padding: 20px;"><strong><h2 style="font-size: 24px">Заголовок 2 уровня</h2></strong>
                        <ul>
                            <li>Текст 1</li>
                            <li>Текст 2</li>
                            <li>Текст 3</li>
                            <li>Текст 4</li>
                        <ul>
                    </div>
				</div>
			</div>
		</div>
    '''
