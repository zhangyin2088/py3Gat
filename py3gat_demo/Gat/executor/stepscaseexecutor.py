#coding=utf-8
'''
Created on 2015-4-2
updated on 2020-06-24 by 张印
@author: 张天得
'''
from settings import GlobalConfig
from Gat.util.classtracer import ClassTracer
from Gat.util.methodtracer import MethodTracer
from Gat.util.methodinvoker import MethodInvoker
from Gat.util.stepvaluepool import StepValuePool
from Gat.util.XMLparsehelp import get_testcaselist4xml,get_templateSteplistByTab


@ClassTracer
class StepsCaseExecutor(object):
    '''
    classdocs
    '''

    @MethodTracer("==============================New Testcase: ${args[-1][]}$==============================")
    def __init__(self,project_name,casefilename,caseid):
        '''
        Constructor
        '''
        GlobalConfig.TestCaseFilePath=GlobalConfig.get_testcase_filepath(project_name,casefilename)
        self.project_name=project_name
        self.testcaseid=caseid

    @MethodTracer()
    def execute(self):
        '''执行测试用例'''
        try:
            self.setup()
            self.execute_setp()
            self.teardown()
        finally:
            self.teardownfinal()
        
        
    @MethodTracer()
    def setup(self):
        stepvaluepool=StepValuePool()
        setupSteps = get_templateSteplistByTab(GlobalConfig.TestCaseFilePath,SetUp="True")

        if setupSteps:
            self.excute_step_with_StepsTemplate(setupSteps)
    
    @MethodTracer()
    def teardown(self):
        teardownSteps = get_templateSteplistByTab(GlobalConfig.TestCaseFilePath, TearDown="True")
        if teardownSteps:
            self.excute_step_with_StepsTemplate(teardownSteps)
        stepvaluepool=StepValuePool()
        stepvaluepool.clear_all()

    @MethodTracer()
    def teardownfinal(self):
        stepvaluepool = StepValuePool()
        stepvaluepool.clear_all()

        
    
    @MethodTracer()
    def execute_setp(self):
        '''执行测试步骤'''
        testcase = self.get_testcase()
        teststeps = self.get_teststeps(testcase)
        self.excute_step_with_StepsTemplate(teststeps)

    def excute_step_with_StepsTemplate(self,teststeps):
        for teststep in teststeps:
            if "@StepsTemplateID" in teststep:
                templateSteps = get_templateSteplistByTab(GlobalConfig.TestCaseFilePath, ID=teststep["@StepsTemplateID"])
                self.excute_step_with_StepsTemplate(templateSteps)
            else:
                self.call_step_method(teststep)

    @MethodTracer()
    def get_testcase(self):
        testcaselist = get_testcaselist4xml(GlobalConfig.TestCaseFilePath)
        for testcase in testcaselist:
            if testcase["@ID"] == self.testcaseid:
                return testcase
        raise Exception("can't find testcaseID in testcasefile!!!")
        return None

    @MethodTracer()
    def get_teststeps(self,testcase):
        teststeps = testcase["TestSteps"]["Step"]
        if not isinstance(teststeps,list):
            teststeps = [teststeps]
            #print("******now teststeps list: ******")
            #print teststeps
        for teststep in teststeps:
            for key in ["@StepParametersFileName", "@StepPackage", "@StepModule", "@StepGroup"]:
                if key not in teststep:
                    try:
                        teststep[key] = testcase[key]
                    except KeyError:
                        raise Exception("%s is not exist" % key)
        return teststeps

    def get_step_project_and_file_name(self,teststep):
        step_peoject_name = ""
        step_file_name = ""
        StepParamsFileName = teststep["@StepParametersFileName"]
        if "/" not in StepParamsFileName:
            step_peoject_name = self.project_name
            step_file_name = StepParamsFileName
        else:
            project_and_file_list = StepParamsFileName.split("/")
            step_file_name = project_and_file_list[-1]
            project_floors = len(project_and_file_list) - 1
            for i in range(project_floors):
                step_peoject_name += project_and_file_list[i]
                if i != project_floors - 1:
                    step_peoject_name += GlobalConfig.get_slash()
        return step_peoject_name,step_file_name

    @MethodTracer("++++++++++++++++++++New Step: ${args[-1][@StepParameterID]}$ ++++++++++++++++++++")
    def call_step_method(self,teststep):
        step_project_name,step_file_name = self.get_step_project_and_file_name(teststep)
        GlobalConfig.StepParameterFilePath = GlobalConfig.get_parameter_filepath(step_project_name,step_file_name)
        #instance = MethodInvoker.get_instance(teststep["@StepPackage"], teststep["@StepGroup"], teststep["@StepPackage"].split('.'))
        module_name = teststep["@StepPackage"] + "." + teststep["@StepModule"]
        instance = MethodInvoker.get_instance(module_name, teststep["@StepGroup"], module_name.split('.'))
        method=MethodInvoker.get_method(instance,teststep["@StepName"])
        #print(method)
        #arglist=list()
        method(teststep["@StepParameterID"])
        
        
        