'''
Created on 2015-4-7

@author: Devuser
'''
import unittest
from gateside.autotesting.Gat.executor.istepscaseexecutor import IStepsCaseExecutor


class Test(unittest.TestCase):


    def testName(self):
        executor=IStepsCaseExecutor("testcase.xml","xxxid")
        executor.execute()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()