# coding=utf-8
'''
Created on 2013-7-6

@author: tiande.zhang
'''

import inspect

class ObjectInfo(object):
    '''
    classdocs
    '''


    def __init__(self,frame):
        '''
        Constructor
        '''
        self.frame=frame
    
    def getCurrentFrame(self):
        '''获取当前frame'''
        return inspect.currentframe()
    
    def getModule(self):
        '''获取调用者模块名称'''
        self.callFrame=inspect.getouterframes(self.frame, 3)
        #print("***20200807***")
        #print(self.callFrame)
        return self.callFrame[3][1]
    
    def getMethod(self):
        '''获取调用者方法名称'''
        self.callFrame=inspect.getouterframes(self.frame, 2)
        return self.callFrame[3][3]

    def getLineNumber(self):
        '''获取调用者方法名称'''
        self.callFrame=inspect.getouterframes(self.frame, 2)
        return self.callFrame[3][2]
         
        
        