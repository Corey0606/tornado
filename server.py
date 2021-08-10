#!/usr/bin/env python
# _*_coding:utf-8_*_
import tornado.web
''' 
tornado的基础web框架模块

'''
import tornado.ioloop
'''
tornado的核心IO循环模块，封装了Linux的epoll和BSD的kqueue,是tornado高效的基础
'''
import tornado.httpserver

# 类比django的视图
# 一个业务处理类
class IndexHandle(tornado.web.RequestHandler):
    # 处理get请求，不能处理post请求
    def get(self, *args, **kwargs):
        # 对应http请求的方法
        # 给浏览器响应信息
        self.write('Hello tornado11')


if __name__ == '__main__':
    # 实例化一个app对象
    # Application: 是tornado web框架的核心应用类，是与服务器对应的接口
    # 里面保存了路由映射表，有一个listen方法用来创建一个http服务器的实例，并绑定了端口
    app = tornado.web.Application([
        (r'/', IndexHandle)
    ])
    # 绑定监听端口
    # 注意： 此时服务器并没有开启监听
    app.listen(8000)
    '''
    httpServer = tornado.httpserver.HTTPServer(app)
    httpServer.listen(8000)
    
    //启动多个进程 不用监听先绑定 
    httpServer.bind(port)
    httpServer.start(num) num不写默认为1，启动几个就写几个， 写0或者负数默认用cpu核数来启动
    （1）listen()只能在单进程中使用
    （2）虽然tornado给我们提供了上述得启用多进程得方式，但是因为一些问题，上述方法不建议使用。而是手动启动多个进程，并且我们还可以绑定多个端口（运行多次py文件）
    '''


    '''
    IOLoop.current():返回当前线程的IOLoop实例
    IOLoop.start():启动IOLoop实例的I/O循环，同时开启监听
    '''
    tornado.ioloop.IOLoop.current().start()