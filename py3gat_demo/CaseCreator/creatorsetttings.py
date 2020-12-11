# coding=utf-8
'''
Created on 2015-4-7
updated on 2020-06-24 by 张印
@author: 张天得
'''
import sys, os

print(sys.path)
sys.path.append(os.getcwd())
# import os

from settings import GlobalConfig


class CreatorSettings(object):
    ROOTDIR = GlobalConfig.ROOTDIR

    @staticmethod
    def get_rootdir():
        if CreatorSettings.ROOTDIR == None:
            return os.path.abspath("..")
        else:
            return CreatorSettings.ROOTDIR

    @staticmethod
    def get_testproject_rootdir():
        if CreatorSettings.ROOTDIR == None:
            return (os.path.abspath("..") + GlobalConfig.get_slash() + GlobalConfig.AUTOPROJECTFOLDER)
        else:
            return (CreatorSettings.ROOTDIR + GlobalConfig.get_slash() + GlobalConfig.AUTOPROJECTFOLDER)

    @staticmethod
    def get_stepgroups_rootdir():
        if CreatorSettings.ROOTDIR == None:
            return (os.path.abspath("..") + GlobalConfig.STEPMETHODGROUPFOLDER)
        else:
            return (CreatorSettings.ROOTDIR + GlobalConfig.STEPMETHODGROUPFOLDER)

    @staticmethod
    def get_template_folder():
        if CreatorSettings.ROOTDIR == None:
            return CreatorSettings.get_rootdir() + GlobalConfig.get_slash() + "CaseCreator" + GlobalConfig.get_slash() + "templates"
        else:
            return CreatorSettings.ROOTDIR + GlobalConfig.get_slash() + "CaseCreator" + GlobalConfig.get_slash() + "templates"

    @staticmethod
    def get_datafiles_folder(projectname):
        return CreatorSettings.get_testproject_rootdir() + GlobalConfig.get_slash() + projectname + GlobalConfig.get_slash() + "datafiles"

    @staticmethod
    def get_method_tempatepath():
        return CreatorSettings.get_template_folder() + GlobalConfig.get_slash() + "test_method.txt"

    @staticmethod
    def get_testclass_tempatepath():
        return CreatorSettings.get_template_folder() + GlobalConfig.get_slash() + "Test_class.txt"

    @staticmethod
    def get_loggerconf_tempatepath():
        return CreatorSettings.get_template_folder() + GlobalConfig.get_slash() + "logger.conf"

    @staticmethod
    def get_project_runpy():
        return CreatorSettings.get_template_folder() + GlobalConfig.get_slash() + "run.py"

