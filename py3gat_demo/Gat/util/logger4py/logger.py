# coding=utf-8
'''
Created on 2013-7-2
updated on 2020-08-14 by 张印
@author: tiande.zhang
'''
import logging.config
import os
import inspect
from Gat.util.logger4py.loggerenum import LoggerEnum
from settings import GlobalConfig
from Gat.util.objectinfo import ObjectInfo


class Logger(object):
    '''
    所有logger的基类
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.create_log_dir()
        #print("="*50),GlobalConfig.get_logger_configpath()
        logging.config.fileConfig(GlobalConfig.get_logger_configpath())

    def info(self,msg):
        '''将信息记录为到Trace.log文件中'''
        logger=logging.getLogger(LoggerEnum.FileInfoLogger)
        logger.info(self.get_invoker_info()+msg)
    
    def error(self,msg):
        '''将信息记录为到Error.log文件中'''
        logger=logging.getLogger(LoggerEnum.FileErrorLogger)
        logger.error(self.get_invoker_info()+msg)
    
    def critical(self,msg):
        '''将信息记录为到Critical.log文件中'''
        logger=logging.getLogger(LoggerEnum.FileCriticalLogger)
        logger.critical(self.get_invoker_info()+msg)
    
    def log_to_console(self,msg):
        '''将信息记录为到Critical.log文件中'''
        logger=logging.getLogger(LoggerEnum.StreamLogger)
        logger.debug(msg)
    
    def tracelog(self,msg):
        '''将信息记录为到trace.log文件中'''
        logger=logging.getLogger(LoggerEnum.FileTraceLogger)
        #logger.debug(self.get_invoker_info()+msg)
        logger.debug(msg)

    def traceloginfo(self,msg):
        '''将信息记录为到trace.log文件中'''
        logger=logging.getLogger(LoggerEnum.FileTraceLogger)
        #logger.debug(self.get_invoker_info()+msg)
        logger.info(msg)
    
    def create_log_dir(self):
        if not os.path.exists(GlobalConfig.get_logdir()):
            os.mkdir(GlobalConfig.get_logdir())
    
    def get_current_frame(self):
        return inspect.currentframe()
    
    def get_invoker_info(self):
        currentFrame=ObjectInfo(self.get_current_frame())
        return currentFrame.getModule()+"    "+currentFrame.getMethod()+"    "+str(currentFrame.getLineNumber())+"    "


if __name__ == "__main__":
    logger_t = Logger()
    print(logger_t.get_invoker_info())
        

        
    

    
        
        