#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random, time, Queue
from multiprocessing import Queue, Process
from multiprocessing.managers import BaseManager
class NodeManager(object):
    def start_Manager(self,url_q,result_q):
        #把创建的两个队列注册在网络上，利用register方法，callable参数关联了Queue对象，
        # 将Queue对象在网络中暴露
        BaseManager.register('get_task_queue',callable=lambda:task_queue)
        BaseManager.register('get_result_queue',callable=lambda:result_queue)
        #绑定端口8001，设置验证口令‘baike’。这个相当于对象的初始化
        manager=BaseManager(address=('127.0.0.1', 5000), authkey=b'abc')
        #返回manager对象
        return manager
def test(task,result):
    print "start"
    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task %d...' % n)
        task.put(n)
    # 从result队列读取结果:
    print('Try get results...')
    for i in range(10):
        r = result.get(timeout=10)
        print('Result: %s' % r)
if __name__ == '__main__':
    # 发送任务的队列:
    task_queue = Queue()
    # 接收结果的队列:
    result_queue =Queue()
    node = NodeManager()
    manager = node.start_Manager(task_queue, result_queue)
    p = Process(target=test, args=(task_queue,result_queue))
    p.start()
    manager.get_server().serve_forever()