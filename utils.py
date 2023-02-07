import requests


class Map:

    def __init__(self, center_pos, z):  # spn - масштаб
        self._centre_pos = center_pos
        self._z = z

    def get_image(self):
        url = 'https://static-maps.yandex.ru/1.x/'
        params = {'ll': ",".join(map(str, self._centre_pos)),  # широтаб долгота
                  'z': str(self._z),
                  'l': 'map',
                  'size': '650,450'
                  }
        response = requests.get(url, params=params)

        return response.content
