#coding=utf-8
'''
Created on 2015-4-3

@author: 张天得
'''

from Gat.util.methodtracer import traceFrameMessage

class MethodInvoker(object):
    '''
    动态调用方法
    '''

    @staticmethod
    def get_instance(moudelname,classname,packagelist):
        moudel= __import__(moudelname,fromlist=packagelist)
        #print("*****moudel*****")
        #print(moudel)
        klass=getattr(moudel,classname)
        #print("******class*****")
        #print(klass)
        instance=klass()
        traceFrameMessage()
        return instance
    
    @staticmethod
    def get_moudel(moudelname,packagelist):
        return __import__(moudelname,fromlist=packagelist)
    
    @staticmethod
    def get_method(instance,methodname):
        method=getattr(instance,methodname)
        #print(method)
        traceFrameMessage(method)
        return method
    
    @staticmethod
    def invoke_method(method,args):
        method(*args)
    
        