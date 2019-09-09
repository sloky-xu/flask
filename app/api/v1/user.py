from app.libs.redprint import Redprint


# 实例化一个红图对象
api = Redprint('user')


@api.route('/get', methods=['GET'])
def get_user():
    return 'hello'
