import pandas as pd
import numpy as np
import math
from datetime import timedelta, date, datetime
from jinja2 import Template
import json



# ГЕНЕРИРУЕТ ДАТАСЕТ ИЗ CSV ФАЙЛОВ
def dataset_generation(SITE):
    print('PATH -> index/metallurgy/dataset_generation.py')


    # Получаем датафрейм отчёта за указанный интервал дат
    def get_otchet(start_date, end_date):
        if len(str(start_date)) != 10 or len(str(end_date)) != 10:
            return pd.DataFrame()
        # print("DATE", start_date, end_date)
        
        format = "%d.%m.%Y"
        s_date = datetime.strptime(start_date, format)
        e_date = datetime.strptime(end_date, format)
        delta = int(str(e_date - s_date).split(' ')[0])
        if delta < 1:
            return pd.DataFrame()
        df_sum = pd.DataFrame()
        for i in range(delta + 1):
            day = str(s_date + i*timedelta(days=1)).split(' ')[0]
            day_list = day.split('-')
            day_new = str(day_list[2]) + '.' + str(day_list[1]) + '.' + str(day_list[0])
            
            df_new = o_data[(o_data['Дата'] == day_new)].head()
            df_sum = df_sum.append(df_new, ignore_index = True)

        # print("DF_SUM.SHAPE", df_sum.shape, "\n")
        df_select = pd.DataFrame()
        # df_select['Вес разлитой стали'] = df_sum['Вес разлитой стали, т']
        df_select['Температура стали'] = df_sum['Темп. стали в с/к, °C']
        df_select['Частота качания'] = df_sum['Частота качания, кол-во/мин']
        df_select['Ход кристализатора'] = df_sum['Ход кр-ра, мм']    
        df_select['Скорость разливки'] = df_sum['Скорость разливки, м/мин']   
        df_select['Расход воды'] = df_sum['Расход воды на кр-р, л/мин']
        df_select['Дельта температуры воды'] = df_sum['Дельта температуры воды, °C']    
        df_select['Расход воды 1'] = df_sum['Расход воды ЗВО №1, л/мин']
        df_select['Расход воды 2'] = df_sum['Расход воды ЗВО №2, л/мин'] 
        df_select['Расход воды 3'] = df_sum['Расход воды ЗВО №3, л/мин']
        # df_select['C, %'] = df_sum['C, %']
        # df_select['Si, %'] = df_sum['Si, %']
        # df_select['Mn, %'] = df_sum['Mn, %']
        # df_select['S, %'] = df_sum['S, %']
        # df_select['P, %'] = df_sum['P, %']
        # df_select['Cr, %'] = df_sum['Cr, %']
        # df_select['Ni, %'] = df_sum['Ni, %']
        # df_select['Cu, %'] = df_sum['Cu, %']
        # df_select['As, %'] = df_sum['As, %']
        # df_select['Mo, %'] = df_sum['Mo, %']
        # df_select['Nb, %'] = df_sum['Nb, %']



        # Удаляем пустые (nan) ячейки
        df_select = df_select.dropna()
        print("DF_SELECT 2\n", df_select)
        # Получаем среднее
        df_mean = df_select.mean()


        print("DF_MEAN\n", df_mean)


        return df_mean

    p_data = pd.read_csv('index/metallurgy/p_data.csv')  # Таблица паспортов
    g_data = pd.read_csv('index/metallurgy/geometry.csv')  # Таблица геометрий
    o_data = pd.read_csv('index/metallurgy/otchet.csv')  # Таблица отчёта
    # print("ПАСПОРТА\n", p_data.head(3), "\n")
    # print("ГЕОМЕТРИЯ\n", g_data.head(3), "\n")
    # print("ОТЧЁТ\n", o_data.head(3), "\n")

    # Создаём новый датафрейм
    df = pd.DataFrame()

    # Перебираем строки датафрейма p_data для создания нового датафрейма df
    for i in range(p_data.shape[0]):
        # Убираем из датасета строки, по которым нет данных по количеству плавок до 
        if p_data.iloc[i, 86] == 1:
            continue
        # print('ГИЛЬЗА №', p_data.iloc[i, 0])
        
        st = 0
        # Находим максимальное значение стойкости
        # Простите, нет времени писать рекурсию и чистить код.
        if not math.isnan(p_data.iloc[i, 55]):
            st = p_data.iloc[i, 55]
            # Получаем датафрейм из отчёта
            df_otchet = get_otchet(p_data.iloc[i, 52], p_data.iloc[i, 53])
            if df_otchet.empty:
                # Проблема с затой
                continue
        else:
            if not math.isnan(p_data.iloc[i, 43]):
                st = p_data.iloc[i, 43]
                df_otchet = get_otchet(p_data.iloc[i, 40], p_data.iloc[i, 41])
                if df_otchet.empty:
                    continue
            else:
                if not math.isnan(p_data.iloc[i, 31]):
                    st = p_data.iloc[i, 31]
                    df_otchet = get_otchet(p_data.iloc[i, 28], p_data.iloc[i, 29])
                    if df_otchet.empty:
                        continue
                else:
                    if not math.isnan(p_data.iloc[i, 19]):
                        st = p_data.iloc[i, 19]
                        df_otchet = get_otchet(p_data.iloc[i, 16], p_data.iloc[i, 17])
                        if df_otchet.empty:
                            continue
                    else:
                        if not math.isnan(p_data.iloc[i, 7]):
                            st = p_data.iloc[i, 7]
                            df_otchet = get_otchet(p_data.iloc[i, 4], p_data.iloc[i, 5])
                            if df_otchet.empty:
                                continue
                        else:
                            continue
                
                
                
        # print('ST', st)    

        t_st = 1565 if df_otchet['Температура стали'] > 1700 or df_otchet['Температура стали'] < 1500 else df_otchet['Температура стали']
        ch_k = 200 if df_otchet['Частота качания'] > 300 or df_otchet['Частота качания'] < 30 else df_otchet['Частота качания']
    


        df_row = pd.DataFrame({
            "№ гильзы": [p_data.iloc[i, 0]],
            # 'Вес разлитой стали': df_otchet['Вес разлитой стали'],
            'Температура стали': t_st,
            'Частота качания': ch_k,
            'Ход кристализатора': df_otchet['Ход кристализатора'], 
            'Скорость разливки': df_otchet['Скорость разливки'], 
            'Расход воды': df_otchet['Расход воды'],
            'Дельта температуры воды': df_otchet['Дельта температуры воды'], 
            'Расход воды 1': df_otchet['Расход воды 1'],
            'Расход воды 2': df_otchet['Расход воды 2'],
            'Расход воды 3': df_otchet['Расход воды 3'], 
            # 'C, %': df_otchet['C, %'],
            # 'Si, %': df_otchet['Si, %'],
            # 'Mn, %': df_otchet['Mn, %'],
            # 'S, %': df_otchet['S, %'],
            # 'P, %': df_otchet['P, %'],
            # 'Cr, %': df_otchet['Cr, %'],
            # 'Ni, %': df_otchet['Ni, %'],
            # 'Cu, %': df_otchet['Cu, %'],
            # 'As, %': df_otchet['As, %'],
            # 'Mo, %': df_otchet['Mo, %'],
            # 'Nb, %': df_otchet['Nb, %'],
            "Стойкость": [st]
        })

        df = df.append(df_row, ignore_index = True)


    # Удаляем пустые (nan) ячейки
    df = df.dropna()
    print(df.head(20))

    df.to_csv('index/metallurgy/dataset.csv')

    answer = {'answer': 'success'}
    return {'ajax': json.dumps(answer)}