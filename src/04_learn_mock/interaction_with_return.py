def send(message: str):
    ok = receive(message)

    if ok:
        print('success')
    else:
        print('failure')


def receive(message: str) -> bool:
    print('received: {}'.format(message))

    return True
