#Рожкова Анна 23 когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request

def test_positive_assert():
    response_create_order = sender_stand_request.post_new_order()
    track = response_create_order.json()["track"]
    response_get_order = sender_stand_request.get_order(track)
    assert response_get_order.status_code == 200


