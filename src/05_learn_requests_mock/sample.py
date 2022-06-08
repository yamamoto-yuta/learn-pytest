import requests


def sample():
    try:
        # ここを Mock したい
        res = requests.get("http://checkip.amazonaws.com/")

    except requests.RequestException as e:
        print(e)
        raise e

    return {
        "statusCode": res.status_code,
        "ip": res.text,
    }
