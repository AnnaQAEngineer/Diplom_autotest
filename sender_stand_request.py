import configuration
import requests
import data

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json = body,
                         headers = data.headers)
response = post_new_order(data.order_body)

def get_order(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER,
                        params = track_number)