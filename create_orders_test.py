#Рожкова Анна 23 когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request
import data

def get_track(response):
    return response.json().get("track")

data.params_track["t"] = get_track(sender_stand_request.response)

def test_positive_assert():
    track_response = sender_stand_request.get_order(data.params_track)
    assert track_response.status_code == 200

