import allure


def test_a():
    print('aaa')
    assert 1

@allure.step(title='测试登录的流程')
def test_login():
    allure.attach('登录','输入用户名')
    print('aaaaaaaaa')

    allure.attach('登录', '输入密码')
    print('bbbbbbbbbb')

    allure.attach('登录', '点击登录')
    print('vvvvvvvv')


    assert 0