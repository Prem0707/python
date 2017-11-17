from .models import User


#  Django auth 应用内置只支持用户名和密码的认证方式
#  验证用户提供的凭据（这里是邮箱以及密码）是合法的，完全仿照内置的 ModelBackend 代码即可
class EmailBackend(object):
    def authenticate(self, request, **credentials):
        # 要注意登录表单中用户输入的用户名或者邮箱的 field 名均为 username
        email = credentials.get('email', credentials.get('username'))
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            pass
        else:
            if user.check_password(credentials["password"]):
                return user

    def get_user(self, user_id):
        """
        该方法是必须的
        """
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None