from hello import app


def test_home():
    tester = app.test_client()
    response = tester.get('/', content_type='html/text')
    assert response.status_code == 200
    assert b'Hello World!' in response.data


def test_other():
    tester = app.test_client()
    response = tester.get('a', content_type='html/text')
    assert response.status_code == 404
    assert b'does not exist' in response.data