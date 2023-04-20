import pytest

@pytest.fixture
def some_data():
    data = {
        'name': 'pytest',
        'version': '5.0.1',
    }
    print('Setting up some_data')
    yield data # 返回 data 字典
    print('Tearing down some_data')


def test_fixture(some_data):
    print(f'Testing with {some_data}')
    assert some_data['name'] == 'pytest'
    assert some_data['version'] == '5.0.1'
