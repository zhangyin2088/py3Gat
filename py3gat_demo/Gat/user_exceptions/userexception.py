#coding=utf-8
'''
Created on 2015-4-1

@author: 张天得
'''

class XMLElementNoneException(Exception):
    '''
    找不到xmlelement异常
    '''


    def __init__(self,errorMessage):
        '''
        找不到xmlelement元素
        '''
        self.errorMessage=errorMessage
    def __str__(self):
        print("Can not found xml element for: "+self.errorMessage)
        
class UIElementAttributeIsNonException(Exception):
    ''' 页面元素定位属性找不到'''
    def __init__(self,errorMessage):
        self.errorMessage=errorMessage
    
    def __str__(self):
        print("value for attribute: "+self.errorMessage+" is None")
        