# 商城项目

------

##### 状态:未完成

------

#### 所用版本：

**Python(3.8.7)**

**Django(4.2.7)**

**Mysql(8.0)**

**Redis(5.0.14.1)**

**mysqlclient(2.2.0)**

**django-cors-headers(4.3.1)**

------

## Q&A

怎么使用？

##### **前端:**

将TuLing和TuLing前端两个包拉到本地，然后在TuLing前端中打开cmd，输入以下command

```cmd
python -m http.server 端口号(一般使用8080,不要和django的端口号冲突)
```

然后就可以在浏览器中输入本地回环地址（127.0.0.1）加端口号（8080）加网页名（index.html等）进行访问测试了

```html
127.0.0.1:8080/index.html(你想测试的网页名)
```

##### **后端:**

使用Pycharm打开Tuling文件夹，然后配置好环境后，运行即可。