import json
import requests
import jsonpath
import unittest
import pytest

BASE_URI="https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"



class Test(unittest.TestCase):

    def test_total_day(self):
        response = requests.get(BASE_URI, )
        json_response = json.loads(response.text)
        content = jsonpath.jsonpath(json_response, "cnt")
        total_day = content[0] // 24
        assert total_day == 4


    def test_temp_assert(self):
        # For all 4 days, the temp should not be less than temp_min and not more than temp_max
        response = requests.get(BASE_URI, )
        assert response.status_code == 200
        resp = response.json()
        cnt = resp['cnt']
        print(cnt)
        print(type(cnt))
        for i in range(0, cnt - 1):
            temp_max = resp['list'][i]['main']['temp_max']
            temp_min = resp['list'][i]['main']['temp_min']
            act_temp = resp['list'][i]['main']['temp']
            assert act_temp >= temp_min
            assert act_temp <= temp_max


    def test_check_weather(self):
        response = requests.get(BASE_URI, )
        resp = response.json()
        cnt = resp['cnt']
        for i in range(0, cnt - 1):
            id = resp['list'][i]['weather'][0]['id']
            if id == 500:
                assert resp['list'][i]['weather'][0]['description'] == 'light rain'

            elif id == 800:
                assert resp['list'][i]['weather'][0]['description'] == 'clear sky'



    def test_print_all_time(self):
            response = requests.get(BASE_URI, )
            resp = response.json()
            cnt = resp['cnt']
            for i in range(0, cnt - 1):
                dt_time = resp['list'][i]['dt_txt']
                mylst = dt_time.split()
                print((mylst[1].split(":"))[0])

