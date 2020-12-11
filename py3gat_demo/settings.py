# coding=utf-8
'''
Created on 2013-7-1
updated on 2020-06-24 by 张印
注意非必要不要在svn/git提交此文件！！！
@author: tiande.zhang
'''

import sys
import os

class GlobalConfig(object):
    '''
    全局静态变量
    '''
    TestCaseFilePath=None
    UIElementFilePath=None
    StepParameterFilePath=None
    IsDebug=True
    ROOTDIR=None
    AUTOPROJECTFOLDER="projects"
    STEPMETHODGROUPNAME="gateside.autotesting.iat_testgroups."
    STEPMETHODGROUPFOLDER="testgroups"
    
    
    @staticmethod
    def get_rootdir():
        if GlobalConfig.ROOTDIR==None:
            return os.path.dirname(os.path.abspath(".."))
        else:
            return GlobalConfig.ROOTDIR
    
    @staticmethod
    def get_slash():
        if sys.platform=="win32":
            return "\\"
        else:
            return "/" 
    @staticmethod
    def get_autoproject(self):
        return GlobalConfig.AUTOPROJECTFOLDER
    
    @staticmethod
    def get_stepmethod_pagepath(self):
        return GlobalConfig.STEPMETHODGROUPNAME
    
    @staticmethod
    def get_testcase_filepath(projectname,filename):
        slash = GlobalConfig.get_slash()
        result = GlobalConfig.get_rootdir()+slash+"projects"+slash+projectname+slash+"datafiles"+slash+filename
        return result
    @staticmethod
    def get_parameter_filepath(projectname,filename):
        slash = GlobalConfig.get_slash()
        result=GlobalConfig.get_rootdir()+slash+"projects"+slash+projectname+slash+"datafiles"+slash+filename
        return result

    @staticmethod
    def get_logger_configpath():
        return GlobalConfig.get_rootdir() + GlobalConfig.get_slash() + "logger.conf"

    @staticmethod
    def get_logdir():
        return GlobalConfig.get_rootdir() + GlobalConfig.get_slash() + "log"







        

        
    
    
    
    
    
    
    
    