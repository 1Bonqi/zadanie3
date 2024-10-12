import numpy as np
import requests
import pandas as pd


class Numpy:
    a = np.array([1, 4, 5, 7, 9])
    b = np.sort(a)
    c = np.sum(a)
    print(b)
    print(c)
    print(a[a <= 5])


class Request:
    url = 'https://api.open-meteo.com/v1/forecast'
    params = {'latitude': 64.5401, 'longitude': 40.5433,
              'daily': "temperature_2m_min,temperature_2m_max,precipitation_sum",
              'timezone': 'Europe/Moscow'
              }
    res = requests.get(url, params=params)
    if res.status_code == 200:
        data = res.json()
        temp_min_13 = data['daily']['temperature_2m_min'][2]
        temp_max_13 = data['daily']['temperature_2m_max'][2]
        prec_13 = data['daily']['precipitation_sum'][2]
        print(f"Прогноз погоды в Архангельске на послезавтра:")
        print(f"Минимальная температура: {temp_min_13}°C")
        print(f"Максимальная температура: {temp_max_13}°C")
        print(f"Ожидаемое количество осадков: {prec_13} мм")
    else:
        print(f"Ошибка {res.status_code}: {res.text}")


class Pandas:
    ex = pd.Series([1, 9, 6, 4, 7])
    world_rank = {'Футбольный клуб': ['Реал мадри', 'Бавария', 'Атлетико М', 'Барcелона'],
                  'Страна': ['Испания', 'Германия', 'Испания', 'Испания'],
                  'Мировой рейтинг': [381.0, 276.0, 267.0, 251.0]
                  }
    a = pd.DataFrame(world_rank)
    new_club = {'Футбольный клуб': 'Ювентус','Страна': 'Италия', 'Мировой рейтинг':245}
    a1 = pd.DataFrame([new_club])
    new = pd.concat([a, a1])
    print(ex)
    print(a)
    print(new)
