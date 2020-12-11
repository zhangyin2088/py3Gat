# coding=utf-8
'''
Created on 2013-7-8

@author: tiande.zhang
'''
from Gat.util.logger4py.logger import Logger
from settings import GlobalConfig

def ClassTracer(klass):
    class Tracer(klass):
        tracemessage(klass)
    return Tracer

def ClassMsgTracer(msg=None):
    def ClassTracer(klass):
        class Tracer(klass):
            tracemessage(klass,msg)
        return Tracer
    return ClassTracer

def tracemessage(klass,msg=None):
    '''信息记录入日志'''
    if GlobalConfig.IsDebug:
        logger=Logger()
        if msg:
            logger.traceloginfo(msg)
        logger.tracelog("class: " + klass.__dict__['__module__'])
    