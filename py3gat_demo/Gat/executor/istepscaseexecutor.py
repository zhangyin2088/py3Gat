#coding=utf-8
'''
Created on 2015-4-7

@author: 张天得
'''
from Gat.executor.stepscaseexecutor import StepsCaseExecutor
import logging

class  IStepsCaseExecutor(StepsCaseExecutor):
    '''
    classdocs
    '''

    def __init__(self,projectname,casefilename,caseid):
        '''
        Constructor
        '''
        logging.info(" " * 100)
        StepsCaseExecutor.__init__(self,projectname,casefilename,caseid)
        