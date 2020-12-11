# coding=utf-8
'''
Created on 2015-4-7
updated on 2020-06-24 by 张印
@author: Devuser
'''
import sys, os

sys.path.append(os.getcwd() + '/../')
print("*" * 50)
print(sys.path)
print("*" * 50)
from CaseCreator.creatorsetttings import CreatorSettings
from settings import GlobalConfig
from Gat.util.XMLparsehelp import get_testcaselist4xml

import os
import shutil


def get_projectname_list():
    projectspath = CreatorSettings.get_testproject_rootdir()
    projectname_list = []
    for projectdir in os.listdir(projectspath):
        projectpath = projectspath + GlobalConfig.get_slash() + projectdir
        if os.path.isdir(projectpath):
            # python2
            #project_package_init_file = file(projectpath + GlobalConfig.get_slash() + "__init__.py", "w")
            # python3
            project_package_init_file = open(projectpath + GlobalConfig.get_slash() + "__init__.py", "w")

            project_package_init_file.close()
            if os.path.exists(projectpath + GlobalConfig.get_slash() + "datafiles"):
                projectname_list.append(projectdir)
            else:
                for subdir in os.listdir(projectpath):
                    subprojectpath = projectpath + GlobalConfig.get_slash() + subdir
                    if os.path.isdir(subprojectpath):
                        if os.path.exists(subprojectpath + GlobalConfig.get_slash() + "datafiles"):
                            projectname = projectdir + GlobalConfig.get_slash() + subdir
                            subproject_package_init_file = open(
                                subprojectpath + GlobalConfig.get_slash() + "__init__.py",
                                "w")
                            subproject_package_init_file.close()
                            projectname_list.append(projectname)
    return projectname_list


def create_testproject():
    projectname_list = get_projectname_list()
    for projectname in projectname_list:
        currentproject_path = CreatorSettings.get_testproject_rootdir() + GlobalConfig.get_slash() + projectname
        testcases_path = currentproject_path + GlobalConfig.get_slash() + "testcases"
        logtmp_folder = currentproject_path+GlobalConfig.get_slash() + "logtmp"
        project_log_path = currentproject_path + GlobalConfig.get_slash() + "log"
        testcases_log_path = testcases_path + GlobalConfig.get_slash() + "log"
        if os.path.exists(testcases_path):
            if os.path.exists(testcases_log_path):
                shutil.copytree(testcases_log_path,logtmp_folder)
            if sys.platform == "win32":
                #print("win system,force remove")
                os.system("rmdir /s /q %s" % testcases_path)
            else:
                shutil.rmtree(testcases_path)
        os.makedirs(testcases_path)
        if os.path.exists(logtmp_folder):
            shutil.copytree(logtmp_folder,testcases_log_path)
            shutil.rmtree(logtmp_folder)
        else:
            os.makedirs(testcases_log_path)
        if not os.path.exists(project_log_path):
            os.makedirs(project_log_path)
        testcases_package_init_file = open(testcases_path + GlobalConfig.get_slash() + "__init__.py", "w")
        testcases_package_init_file.close()



def genreate_testcase():
    rootdir = GlobalConfig.get_rootdir()
    projectname_list = get_projectname_list()
    for projectname in projectname_list:
        currentproject_path = CreatorSettings.get_testproject_rootdir() + GlobalConfig.get_slash() + projectname
        testcases_path = currentproject_path + GlobalConfig.get_slash() + "testcases"
        datafiles_path = currentproject_path + GlobalConfig.get_slash() + "datafiles"
        xml_report_path = currentproject_path + GlobalConfig.get_slash() + "report" + GlobalConfig.get_slash() + "xml"
        for xmlfile in os.listdir(datafiles_path):
            if xmlfile.endswith("cases.xml"):
                print("Get cases.xml file: {}".format(xmlfile))
                testcaselist = get_testcaselist4xml(datafiles_path + GlobalConfig.get_slash() + xmlfile)
                print(testcaselist)
                # testcaselist=get_testcaselist(RunnerSettings.get_xml_folder()+GlobalConfig.get_slash()+xmlfile)
                testmethodcontent = ""
                for testcase in testcaselist:
                    #print(create_testmethod_content(testcase, xmlfile))
                    testmethodcontent = testmethodcontent + create_testmethod_content(testcase, xmlfile) + "\n"
                #print(testmethodcontent)
                if "testcases.xml" not in xmlfile:
                    classname_content = xmlfile.split("cases.xml")[0].replace("test_", "Test")
                    py_filename = xmlfile.split(".")[0] + ".py"
                else:
                    classname_content = "Test" + xmlfile.split("testcases.xml")[0]
                    py_filename = "test_" + xmlfile.split("testcases.xml")[0] + ".py"
                testclass_content = create_testclass_content(rootdir, classname_content, projectname,
                                                             testmethodcontent, py_filename)
                testcasefile = open(testcases_path + GlobalConfig.get_slash() + py_filename, mode="w",encoding="utf-8")
                testcasefile.write(testclass_content)
                testcasefile.close()
        runpy_content = create_runpy_content(rootdir,xml_report_path)
        runpyfile = open(currentproject_path + GlobalConfig.get_slash() + "run.py",mode="w",encoding="utf-8")
        runpyfile.write(runpy_content)
        runpyfile.close()


def create_testmethod_content(testcase, xmlfile):
    testmethod_template = open(CreatorSettings.get_method_tempatepath(), mode='r',encoding="utf-8")
    testmethod_content = testmethod_template.read()
    pytest_mark_content = ""
    if "@CaseTag" in testcase:
        taglist = testcase["@CaseTag"].split("+")
        for tag in taglist:
            pytest_mark_content += "    @pytest.mark." + tag + "\n"
    testmethod_content = pytest_mark_content + testmethod_content
    testmethod_content = testmethod_content.replace('{TESTMETHOD}', testcase["@Name"])
    testmethod_content = testmethod_content.replace('{CASEFILENAME}', xmlfile)
    testmethod_content = testmethod_content.replace('{CASEID}', testcase["@ID"])
    testmethod_template.close()
    return testmethod_content


def create_testclass_content(rootdir, classname, projectname, classcontent, py_filename):
    testclass_template = open(CreatorSettings.get_testclass_tempatepath(), mode='r',encoding="utf-8")
    testclass_content = testclass_template.read()
    testclass_content = testclass_content.replace('{ROOTDIR}', rootdir)
    testclass_content = testclass_content.replace('{CLASSNAME}', classname)
    testclass_content = testclass_content.replace('{PROJECTNAME}', projectname)
    testclass_content = testclass_content.replace('{TESTMETHODS}', classcontent)
    testclass_content = testclass_content.replace('{PYFILENAME}', py_filename)
    testclass_template.close()
    return testclass_content

def create_runpy_content(rootdir, xml_report_dir):
    runpy_template = open(CreatorSettings.get_project_runpy(),mode='r',encoding="utf-8")
    runpy_content = runpy_template.read()
    runpy_content = runpy_content.replace('{ROOTDIR}', rootdir)
    runpy_content = runpy_content.replace('{XMLREPORTDIR}', xml_report_dir)
    runpy_template.close()
    return runpy_content

def create_loggerconf():
    loggerconf_template = open(CreatorSettings.get_loggerconf_tempatepath(), mode='r',encoding="utf-8")
    loggerconf_content = loggerconf_template.read()
    loggerconf_content = loggerconf_content.replace('{log_folder}', GlobalConfig.get_logdir())
    loggerconf_template.close()
    loogerconf_file = open(GlobalConfig.get_rootdir() + GlobalConfig.get_slash() + "logger.conf", mode='w',encoding="utf-8")
    loogerconf_file.write(loggerconf_content)
    loogerconf_file.close()


if __name__ == '__main__':
    create_loggerconf()
    create_testproject()
    print("*" * 50)
    genreate_testcase()

