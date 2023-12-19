import json
import re

from django.contrib.auth import login
from django.views import View
from django.http import JsonResponse
from users.models import User

# restful api 设计规则
'''
前端：
    用户输入用户名之后，鼠标时区焦点即发送一个(axios)ajax请求

后端：接收请求做响应

参数：
    用户名

业务逻辑：
    根据用户名查询数据库，如果查询的数量等于0，说明当前用户名没有被注册
    如果count等于1，说明当前用户名已被注册

响应数据：
    json数据
        {code: 0, count: 0/1, errmsg: ok}
        code是返回状态码
        count是查询数据库返回username的同名数量
                因为username是unique（唯一不可重复）的,所以只可能是0或1
        errmsg:错误信息

设计路由：
    /usernames/<username>/count/
'''


# 用户名查重视图
class UsernameCountView(View):
    def get(self, request, username):
        # 1. 接受用户名,并检验用户名合法性 #
        #     限制要求,使用字母和数字 长度在 5 ~ 20 之间
        # if not re.match('[a-zA-Z0-9_-]{5,20}', username):
        #     return JsonResponse({'code': 1, 'errmsg': '用户名不满足要求'})
        # 为了方便多个页面实现该限制功能,不重复书写,
        # 所以此类功能应该在工具包util中写为自定义转换器,后续使用只需要直接调用即可
        # 类似重复使用的功能都应该在工具包中书写,方便调用

        # 2. 根据用户名进行数据库查询 #
        """
            filter: 查询多个
            get:    只能查询一个
            这里使用filter,虽然username是unique（唯一不可重复）的,
            但为了保险起见,依旧使用filter进行查询
        """
        # 查询username字段 = 传入的username的值的数量
        # count() 统计数量
        count = User.objects.filter(username=username).count()

        # 3. 将查询结果以Json数据的格式返回给前端 #
        """
        调用API时使用的对应参数
            code: 状态码
            count: 返回在数据库中查找的同名数量
            errmsg: 错误码
        """
        return JsonResponse({'code': 0, 'count': count, 'errmsg': 'ok'})


# 手机号查重视图
class MobileCountView(View):
    def get(self, request, mobile):
        # 查找重复的手机号,作用同上
        count = User.objects.filter(mobile=mobile).count()
        return JsonResponse({'code': 0, 'count': count, 'errmsg': 'ok'})


'''
注册功能
    前端
        用户输入用户名 密码 确认密码 手机号 是否同意协议
        如果当前的值都没有问题，并且用户点击了注册按钮
        前端就会发送一个请求

    后端
        请求：接收请求，获取数据
        业务逻辑：验证数据，数据入库
        响应：{'code': 0, 'errmsg': 'ok'}

    路由：
        POST register/

    步骤：
        1. 接收请求
        2. 获取数据
        3. 验证数据
            1. 用户名 密码 确认密码 手机号 协议 等参数
            2. 用户名必须满足要求， 并不能重复
            3. 密码满足规则
            4. 确认密码必须与之前填写的密码一致
            5. 手机号满足规则 不能重复
            6. 必须同意协议
        4. 数据入库
        5. 返回响应
'''


# 用户注册视图
class RegisterView(View):
    # 获取前端传来的表单数据
    """
        使用post提交方式:
            可以复习一下提交方式的知识

            一点简单的因素:
                post比get更加安全
    """

    def post(self, request):
        # 1. 接受请求
        """
            使用body,是因为传回的数据是Json格式
            而Json数据实在body中
        """
        body_bytes = request.body
        # 将json数据载入然后转为字典类型
        body_dict = json.loads(body_bytes)

        # 2.获取数据
        username = body_dict.get('username')
        password = body_dict.get('password')
        password2 = body_dict.get('password2')
        mobile = body_dict.get('mobile')
        # sms_code 是短信验证码
        # sms_code = body_dict.get('sms_code')
        allow = body_dict.get('allow')

        # 3.数据验证
        #   因为前端的验证可以绕过,所以某种意义上相当于没有,所以需要在后端再次验证
        #       1. 用户名 密码 确认密码 手机号 协议等参数必备
        if not all([username, password, password2, mobile, allow]):
            #   all()是一个方法,验证数组的值是否为空,只要有一个为空就返回False
            return JsonResponse({'code': 400, 'errmsg': '缺少必要参数'})

        #       2. 用户名满足规则(使用正则完成)
        if not re.match(r'^[a-zA-Z0-9_]{5,20}$', username):
            return JsonResponse({'code': 400, 'errmsg': 'username格式有误'})
        #       3. 密码满足规则
        if not re.match(r'^[0-9A-Za-z]{8,20}', password):
            return JsonResponse({'code': 400, 'errmsg': 'pwassword格式有误'})
        #       4. 确定两次密码是否相同
        if password != password2:
            return JsonResponse({'code': 400, 'errmsg': '请确认两次输入的密码是否相同'})
        #       5. 手机号满足规则,并不能重复
        if not re.match(r'^1[3-9]\d{9}$', mobile):
            return JsonResponse({'code': 400, 'errmsg': 'mobile格式有误'})
        #       6. 必须同意使用协议
        if allow != True:
            return JsonResponse({'code': 400, 'errmsg': 'allow格式有误'})

        # 4.数据入库（将通过验证的用户注册信息存入数据库）
        #   通过user模型进行保存,没有密码加密
        # User.objects.create(username=username, password=password, mobile=mobile)
        # 但是在存入数据的过程中,存在因为一些故障因素而使数据并未存入,所以使用try except,当没有存入时则打印错误,并且返回'注册失败'
        try:
            # 使用create_user存储数据时会将password自动加密
            user = User.objects.create_user(
                username=username,
                password=password,
                mobile=mobile
            )
        except Exception as e:
            print(e)
            return JsonResponse({'code': 400, 'errmsg': '注册失败'})

        # 5.返回响应
        '''
            两种响应
                1. 当你注册完账号之后进行自动登录 (需要状态保持)
                    用户体验较好(安全性不好)
                2. 用户注册完账号之后跳转到登录页,然后用户手动登录
                    用户体验不好(安全性较好)
        '''
        # 设置以user_id为名的 session信息（值为user.id的值,即数据库中user表单的id)
        # request.session['user_id'] = user.id

        """
            1. 状态保持：
                - 将通过认证的用户的唯一标识信息（比如：用户ID）写入到当前session会话中

            2. login()方法：
                - Django用户认证系统提供了 `login()` 方法
                - 封装了写入session的操作，帮助我们快速实现状态保持
                
        """
        login(request, user)
        # 最终返回注册结果
        return JsonResponse({'code': 0, 'errmsg': 'ok'})
