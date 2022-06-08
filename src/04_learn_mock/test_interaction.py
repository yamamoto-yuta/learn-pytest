import interaction
from interaction import send


def test_send(mocker):
    # mockを使う場合（この場合、返される関数receive()は本物と完全に異なる実装）a
    receive = mocker.patch('interaction.receive')
    # spyを利用した場合（この場合、返される関数は本物のreceive()）
    # receive = mocker.spy(interaction, 'receive')

    send('Hello World!')

    # テスト
    receive.assert_called_once_with('Hello World!')

    # これでもテストできる
    # assert receive.call_args_list == [
    #     mocker.call('Hello World!'),
    # ]
