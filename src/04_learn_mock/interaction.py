def send(message: str):
    # 正常動作
    receive(message)

    # こうするとテストが通らなくなる
    # receive('[1]: {}'.format(message))
    # receive('[2]: {}'.format(message))


def receive(message: str):
    print('received: {}'.format(message))
