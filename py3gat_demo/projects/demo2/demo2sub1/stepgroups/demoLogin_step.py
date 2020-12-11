import json
import requests
from Gat.util.assertHelper import AssertHelper
from projects.demo2.demo2sub1 import constant
from Gat.util.stepvaluepool import StepValuePool
from Gat.util.parameterHelper import ParameterHelper


class DemoLoginStep(object):

    def __init__(self):
        '''
        Constructor
        '''
        self.url = constant.BASEURL + "login"

    def demoLoginSucStep(self,parameterID):
        stepParameters = ParameterHelper.getStepParameters(parameterID)
        parameters = stepParameters["Parameters"]
        #下面的这两句用来从上一个接口获取参数，如果xml里没写这个参数就试着去参数池子里找（池子里的参数是之前的步骤存的）
        parameters["mobile"] = ParameterHelper.get_selected_param(parameters,"mobile")
        parameters["ticket"] = ParameterHelper.get_selected_param(parameters, "ticket")
        print("Params: {}".format(parameters))
        expect_result = stepParameters["Expect"]
        if expect_result == None:
            expect_result = {"code": 0}
        #signed_params = sign_method_name(parameters) #demo不提供签名方法，框架xml里加了join_sign前缀的参数才参与签名
        #res_txt = requests.get(self.url, signed_params)  #http(s)的接口就直接用requests库了
        #res_dict = json.loads(res_txt.text) #拿到实际结果
        res_dict = {"code": 0,"message": "success","result":{"token":"test_token","info":"test"}} #demo不实际发送，直接定义一个返回结果
        valuepool = StepValuePool()
        valuepool.put_value("token", res_dict["result"]["token"]) #把token存起来给别的接口用
        AssertHelper.assert_dict_contain_after_logging(expect_result, res_dict) #框架提供的断言包含方法

    def demoLoginFailedStep(self,parameterID):
        stepParameters = ParameterHelper.getStepParameters(parameterID)
        parameters = stepParameters["Parameters"]
        print("Params: {}".format(parameters))
        expect_result = stepParameters["Expect"]
        if expect_result == None:
            expect_result = {"code": 102}
        # signed_params = sign_method_name(parameters) #demo不提供签名方法，框架xml里加了join_sign前缀的参数才参与签名
        # res_txt = requests.get(self.url, signed_params)  #http(s)的接口就直接用requests库了
        # res_dict = json.loads(res_txt.text) #拿到实际结果
        res_dict = {"code": 102, "message": "illegal params"}  # demo不实际发送，直接定义一个返回结果
        AssertHelper.assert_dict_contain_after_logging(expect_result, res_dict)  # 框架提供的断言包含方法