from django.http import HttpResponse
from django.views import View
from django_redis import get_redis_connection

from libs.captcha.captcha import captcha

# Create your views here.

'''
前端：
    拼接了一个url 地址 img标签请求该地址
    url: 127.0.0.1:8000/image_codes/<uuid>/


后端：
    接收请求
        uuid

    处理业务逻辑
        生成图片验证码与图片二进制
        redis 进行图片验证码的保存

    返回响应
        返回图片二进制数据

    路由：
        get

    第三方包
        captcha
'''


class ImageCodeView(View):
    # 图片验证码使用get即可
    #   因为图片验证码不需要保密,并且传递比post更快
    def get(self, request, uuid):
        """
        :param request:
        :param uuid:
        :return:

        text: 验证码内容
        image： 图片
        """
        '''
            将第三方包captcha放入libs
            (*)然后安装Pillow的图片库(*)
                pip  install  Pillow  -i https://pypi.tuna.tsinghua.edu.cn/simple
            *********注意********
            如果无法正常显示图片验证码
            报错:
                AttributeError: 'ImageDraw' object has no attribute 'textsize'
            则可能是因为Pillow版本过高,与当前的captcha不兼容
            降低版本即可
                pip install Pillow==9.5.0(如果9.5依旧不行,继续尝试其他版本即可, 例如: 9.4.0等等,以此类推)
            ********************
        '''
        # generate_captcha()方法会自动生成一个图片验证码(二进制格式的一串数字)
        # 然后使用拆包的方式将 "验证码内容" 和 "图片" 分别存入 text,image
        text, image = captcha.captcha.generate_captcha()
        # 将验证码保存到redis
        # 这里的code是settings中设置的redis数据库保存配置（不同的数据保存在不同的库中）
        # 因为图片验证码不需要长期保存,所以不使用Mysql,使用redis临时存储
        redis_cli = get_redis_connection('image_code')
        """
            setex() 设置图片验证码的key Expiration time(过期时间) value
            key:    uuid(uuid永不重复)
            time:   单位:秒
            value:  内容
        """
        redis_cli.setex(uuid, 100, text)
        # 这里返回的是二进制数字,并非字典类型的数据,所以这里不能使用JsonResponse返回数据
        # 使用HttpResponse(返回的内容,返回的内容类型) 此方法可以设置返回内容的类型
        # content_type='image/jpeg':    返回类型: image（图片类型） 文件后缀: jpeg
        return HttpResponse(image, content_type='image/jpeg')
