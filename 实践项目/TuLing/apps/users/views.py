import re
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse

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
