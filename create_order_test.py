# Надежда Куколева, 9-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request


def test_create_order():
    track = sender_stand_request.create_new_order()
    order = sender_stand_request.get_order_by_track(track)
    assert order.status_code == 200
