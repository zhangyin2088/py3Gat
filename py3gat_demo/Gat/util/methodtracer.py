# coding=utf-8
'''
Created on 2013-7-8

@author: tiande.zhang
'''
from Gat.util.logger4py.logger import Logger
from settings import GlobalConfig
import functools
import re

def MethodTracer(msg=None):
    def MethodInvokeTracer(method):
        @functools.wraps(method)
        def tracer(*args):
            #print(method.__name__)
            traceMessage(method, args, msg)
            return method(*args)
        return tracer
    return MethodInvokeTracer


def traceMessage(method,args,msg=None):
    '''信息记录入日志'''
    if GlobalConfig.IsDebug:
        logger=Logger()
        if msg:
            msg = improve_msg(msg,args)
            logger.traceloginfo(msg)
        logger.tracelog(method.__module__ + "." + method.__name__ + " was invoked and parameters are " + str(args))

def traceFrameMessage(msg=None,level="info"):
    '''信息记录入日志'''
    if GlobalConfig.IsDebug:
        logger=Logger()
        logger.tracelog(logger.get_invoker_info())
        if msg != None:
            if level == "info":
                logger.traceloginfo(msg)
            elif level == "debug":
                logger.tracelog(msg)


def improve_msg(msg,args):
    arg_keys_list = re.findall("\\${args\\[(.*?)]\\[(.*?)]}\\$", msg)
    if arg_keys_list:
        for arg_keys in arg_keys_list:
            arg_key0 = int(arg_keys[0])
            # print(arg_key0)
            arg_key1 = str(arg_keys[1])
            # print(arg_key1)
            if arg_key1 == "":
                result = args[arg_key0]
                # print("///" + str(args[arg_key0]))
            else:
                result = args[arg_key0][arg_key1]
                # print("///" + str(args[arg_key0][arg_key1]))
            msg = msg.replace(re.search("\\${(.*?)}\\$", msg).group(), str(result))
    return msg


@MethodTracer("ssssssss")
def exe():
    print("aaaa")
    pass

if __name__ == "__main__":
    print(exe.__module__)
    exe()
    traceMessage(method=exe,args="",msg="不不不不不不木")