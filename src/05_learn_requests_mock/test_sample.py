from sample import sample


def test_sample(mocker):
    # 嘘のレスポンスを作成
    responseMock = mocker.Mock()
    responseMock.status_code = 404
    responseMock.text = '127.0.0.1'

    # requests.get の戻り値を patch する
    mocker.patch('requests.get').return_value = responseMock

    actual = sample()
    assert actual['statusCode'] == 404
    assert actual['ip'] == '127.0.0.1'
