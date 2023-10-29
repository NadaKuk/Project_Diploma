import configuration
import requests
import data


def get_order_by_track(track):
    url = configuration.URL_SERVICE + configuration.GET_ORDER_PATH
    order = requests.get(url=url,
                         params={"t": track})
    return order


def create_new_order():
    url = configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH
    body = data.order_body.copy()
    order = requests.post(url=url,
                          json=body,
                          headers=data.headers)
    return order.json()["track"]
