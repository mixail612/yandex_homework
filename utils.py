import requests


class Map:

    def __init__(self, center_pos, z):  # spn - масштаб
        self._centre_pos = center_pos
        self._z = z

    def scale_up(self):
        self._z += 1
        if self._z > 14:
            self._z = 14

    def scale_down(self):
        self._z -= 1
        if self._z < 0:
            self._z = 0

    def move_center(self, dir):  # 0 - up, 1 - right, 2 - down, 3 - left
        if dir == 0:
            delta = 90 / 2 ** self._z
            self._centre_pos = self._centre_pos[0] + delta, self._centre_pos[1]

        elif dir == 1:
            delta = 180 / 2 ** self._z
            self._centre_pos = self._centre_pos[0], self._centre_pos[1] + delta

        elif dir == 2:
            delta = 90 / 2 ** self._z
            self._centre_pos = self._centre_pos[0] - delta, self._centre_pos[1]

        elif dir == 3:
            delta = 180 / 2 ** self._z
            self._centre_pos = self._centre_pos[0], self._centre_pos[1] - delta

    def get_image(self):
        url = 'https://static-maps.yandex.ru/1.x/'
        params = {'ll': ",".join(map(str, self._centre_pos)),  # широтаб долгота
                  'z': str(self._z),
                  'l': 'map',
                  'size': '650,450'
                  }
        response = requests.get(url, params=params)

        return response.content
