import requests


def fetch_address(zipcode: str) -> str:
    # TODO: WebAPIを呼び出す予定

    url = f'https://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}'
    response = requests.get (url)

    response_json = response.json ()
    address1 = response_json['results'][0]['address1']
    address2 = response_json['results'][0]['address2']
    address3 = response_json['results'][0]['address3']

    return f'{address1}{address2}{address3}'



