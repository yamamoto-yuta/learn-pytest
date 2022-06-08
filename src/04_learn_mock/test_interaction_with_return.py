from interaction_with_return import send


def test_send(mocker, capsys):
    receive = mocker.patch('interaction_with_return.receive', return_value=False)

    send('Hello World!')

    receive.assert_called_once_with('Hello World!')

    out, _ = capsys.readouterr()

    assert out == 'failure\n'
