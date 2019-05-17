def test_hello(client_app):
    uri = '/v0/hello'

    req = client_app.get(uri)

    assert 200 == req.status_code
    assert b'Hello World !' == req.data
