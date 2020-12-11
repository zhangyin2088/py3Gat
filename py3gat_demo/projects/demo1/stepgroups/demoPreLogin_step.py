import json
import requests
from Gat.util.assertHelper import AssertHelper
from projects.demo1 import constant
from Gat.util.stepvaluepool import StepValuePool
from Gat.util.parameterHelper import ParameterHelper
from Gat.util.randomdataHelper import random_phone

class DemoPreLoginStep(object):

    def __init__(self):
        '''
        Constructor
        '''
        self.url = constant.URL + "prelogin"

    def demoPreLoginSucStep(self,parameterID):
        '''
        :desc：这个方法一般用来跑我们期望成功的case，参数里不写手机号时支持随机生成，整个接口成功后把ticket存起来给后其他接口用
        :param parameterID: 就是每一组testcase里的每个step里的parameterID，代表一组参数
        '''

        stepParameters = ParameterHelper.getStepParameters(parameterID) #框架封装好的根据paramterID解析出该组参数的方法
        parameters = stepParameters["Parameters"] #取出要发送的参数部分
        if "mobile" not in  parameters:           #如果参数里没有手机号，则用框架提供的方法随机生成一个，动态覆盖更多情况
            parameters["mobile"] = int(random_phone())
        print("Params: {}".format(parameters))
        expect_result = stepParameters["Expect"]  #取出期望结果部分
        if expect_result == None:              #有的参数可以同时用于成功或失败的方法，没有写期望结果，我们就赋一个默认值
            expect_result = {"code": 0}
        #signed_params = sign_method_name(parameters) #对参数进行签名加密等，demo不提供签名算法
        #res_txt = requests.get(self.url, signed_params)  #http(s)的接口就直接用requests库了
        #res_dict = json.loads(res_txt.text) #拿到实际结果
        res_dict = {"code": 0,"message": "success","result":{"ticket": "i'm a ticket", "info": "test"}} #demo不实际发送，直接定义一个返回结果
        valuepool = StepValuePool() #框架提供的单例模式的进程池
        valuepool.put_value("mobile", parameters["mobile"]) #把手机号存起来给后面的接口用
        valuepool.put_value("ticket", res_dict["result"]["ticket"]) #这里把ticket存起来
        AssertHelper.assert_dict_contain_after_logging(expect_result, res_dict) #框架提供的断言包含方法

    def demoPreLoginFailStep(self,parameterID):
        '''
        :desc：这个方法一般用来跑我们期望失败的case，参数里些什么就是什么（可以测参数错误和缺失），也不会存值向后传递
        :param parameterID: 就是每一组testcase里的每个step里的parameterID，代表一组参数
        '''
        stepParameters = ParameterHelper.getStepParameters(parameterID)
        parameters = stepParameters["Parameters"]
        print("Params: {}".format(parameters))
        expect_result = stepParameters["Expect"]
        if expect_result == None:
            expect_result = {"code": 102}      #有的参数可以同时用于成功或失败的方法，没有写期望结果，我们就赋一个默认值
        # signed_params = sign_method_name(parameters) #对参数进行签名加密等，demo不提供签名算法
        # res_txt = requests.get(self.url, signed_params)  #http(s)的接口就直接用requests库了
        # res_dict = json.loads(res_txt.text) #拿到实际结果
        res_dict = {"code": 102, "message": "illegal params"}  # demo不实际发送，直接定义一个返回结果
        AssertHelper.assert_dict_contain_after_logging(expect_result, res_dict)  # 框架提供的断言包含方法