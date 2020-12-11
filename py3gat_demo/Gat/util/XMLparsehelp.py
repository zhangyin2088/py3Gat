#coding=utf-8
'''
Created on 2020-06-24

@author: 张印
'''
import json
import xmltodict
# from Gat.util.dichelper import DictHelper


# open the input xml file and read
# data in form of python dictionary
# using xmltodict module
def xmlfile2dict(xmlfile):
    with open(xmlfile,encoding="utf-8") as xml_file:
        data_raw = xmltodict.parse(xml_file.read())
        xml_file.close()
    json_str = json.dumps(data_raw)
    data_dict = json.loads(json_str)
    return data_dict

def get_testcaselist4xml(xmlFilepath):
    root_dict = xmlfile2dict(xmlFilepath)
    #print(root_dict)
    testcaselist = root_dict["TestCaseList"]["TestCase"]
    if not isinstance(testcaselist,list):
        testcaselist = [testcaselist]
    for testcase in testcaselist:
        for key in ["@StepParametersFileName", "@StepPackage", "@StepModule", "@StepGroup"]:
            if key not in testcase:
                try:
                    testcase[key] = root_dict["TestCaseList"][key.split("@")[1]]
                except KeyError:
                    raise  Exception("%s in not exist" %key)
    return testcaselist

def get_stepParameters4xml(xmlFilepath, parameterID):
    root_dict = xmlfile2dict(xmlFilepath)
    stepParameter_list = root_dict["StepParametersList"]["StepParameter"]
    if not isinstance(stepParameter_list, list):
        stepParameter_list = [stepParameter_list]
    for stepParameters in stepParameter_list:
        if stepParameters["@ID"] == parameterID:
            #stepParameters = DictHelper.dicVstr2int(stepParameters)
            for key in ["Req_type","Rsp_type"]:
                if key not in stepParameters:
                    try:
                        stepParameters[key] = root_dict["StepParametersList"][key]
                    except KeyError:
                        pass
            initializeStepParametersByTab(stepParameters,"Parameters")
            if "Expect" not in stepParameters:
                stepParameters.setdefault("Expect")
            return stepParameters

def  initializeStepParametersByTab(stepParameters,tab):
    if tab not in stepParameters:
        stepParameters.setdefault(tab)
    if stepParameters[tab] == None:
        stepParameters[tab] = {}

def get_templateSteplistByTab(xmlfile, ID=None, SetUp=None, TearDown=None):
    root_dict = xmlfile2dict(xmlfile)
    if "StepsTemplate" not in root_dict["TestCaseList"]:
        return None
    stepsTemplate_list = root_dict["TestCaseList"]["StepsTemplate"]
    if not isinstance(stepsTemplate_list, list):
        stepsTemplate_list = [stepsTemplate_list]
    templateStep_list = None
    for stepsTemplate in stepsTemplate_list:
        try:
            if ID:
                if stepsTemplate["@ID"] == ID:
                    templateStep_list = stepsTemplate["Step"]
            if SetUp:
                if stepsTemplate["@SetUp"] == SetUp:
                    templateStep_list = stepsTemplate["Step"]
            if TearDown:
                if stepsTemplate["@TearDown"] == TearDown:
                    templateStep_list = stepsTemplate["Step"]
        except KeyError:
            pass
            #print("=" * 50)
        if templateStep_list != None:
            if not isinstance(templateStep_list,list):
                templateStep_list=[templateStep_list]
            for templateStep in templateStep_list:
                for key in ["@StepParametersFileName", "@StepPackage", "@StepModule", "@StepGroup"]:
                    if key not in templateStep:
                        try:
                            templateStep[key] = root_dict["TestCaseList"][key.split("@")[1]]
                        except KeyError:
                            raise Exception("%s in not exist" % key)
        #print(templateStep_list)
            return templateStep_list

# def convert_byte2str(data):
#     if isinstance(data, bytes):
#         return data.decode('ascii')
#     if isinstance(data, dict):
#         return dict(map(convert_byte2str, data.items()))
#     if isinstance(data, tuple):
#         return map(convert_byte2str, data)
#     return data

if __name__ == "__main__":
    #get_testcaselist4xml("test_getAgentInfocases.xml")
    get_templateSteplistByTab("test_getAgentInfocases.xml", "login-out")