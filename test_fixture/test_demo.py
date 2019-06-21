import pytest

class Test_fixture:
    @pytest.fixture
    def log(self):
        print('wellcome')
    @pytest.mark.xfail
    def test_open(self):
        print('open the URl')
        assert 15 < 20

    @pytest.mark.skip
    def test_task(self):
        print('click on enter button')
        assert 5*5 == 25

    def test_assign(self):
        print('assigh the tas ')

    def test_check(self):
        print('everythig is fine')
        assert 'abc' == 'abc'

    def test_login(self):
        print('loging suucess')
        assert 4 == 4