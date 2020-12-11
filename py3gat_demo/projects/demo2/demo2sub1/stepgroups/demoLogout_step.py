import json
import requests
from Gat.util.assertHelper import AssertHelper
from projects.demo2.demo2sub1 import constant
from Gat.util.stepvaluepool import StepValuePool
from Gat.util.parameterHelper import ParameterHelper

class DemoLogoutStep(object):

    def __init__(self):
        '''
        Constructor
        '''
        self.url = constant.BASEURL + "logout"

    def demoLogoutSucStep(self,parameterID):
        stepParameters = ParameterHelper.getStepParameters(parameterID)
        parameters = stepParameters["Parameters"]
        ParameterHelper.set_params(parameters,"mobile",ParameterHelper.get_selected_param(parameters, "mobile"))
        ParameterHelper.set_join_sign_params(parameters,"token",ParameterHelper.get_selected_param(parameters,"token"))
        print("Params: {}".format(parameters))
        expect_result = stepParameters["Expect"]
        #signed_params = sign_method_name(parameters) #demo不提供签名方法，框架xml里加了join_sign前缀的参数才参与签名
        #res_txt = requests.get(self.url, signed_params)  #http(s)的接口就直接用requests库了
        #res_dict = json.loads(res_txt.text) #拿到实际结果
        res_dict = {"code": 0,"message": "success","result":{"messge": "Logout！"}} #demo不实际发送，直接定义一个返回结果

        AssertHelper.assert_dict_contain_after_logging(expect_result, res_dict) #框架提供的断言包含方法

    def demoLogoutFailedStep(self,parameterID):
        pass