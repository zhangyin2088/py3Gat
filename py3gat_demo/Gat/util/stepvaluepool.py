#coding=utf-8
'''
Created on 2015-4-7

@author: 张天得
'''
from Gat.util.methodtracer import MethodTracer

def singleton(cls,*args,**kw):
    instances={}
    def _singleton():
        if cls not in instances:
            instances[cls]=cls(*args,**kw)
        return instances[cls]
    return _singleton




@singleton
class StepValuePool(object):
    '''
    存数Step method中间数据
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.valuepool=dict()

    @MethodTracer("Put Value:  ${args[1][]}$:${args[2][]}$")
    def put_value(self,key,value):
        self.valuepool[key]=value

    @MethodTracer("Get Value:  ${args[1][]}$")
    def get_value(self,key):
        result=None
        try:
            result=self.valuepool[key]
        except Exception as ex:
            pass
        return result
    
    def clear_all(self):
        self.valuepool.clear()
    
    
        