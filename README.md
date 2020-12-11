# py3Gat
python3 + pytest + allure +xml +自封装的支持多平台、多项目、多接口、多环境的接口自动化测试框架
---------------------------
**重要文件介绍**

`set_rootdir.py`：自动生成本地`ROOTDIR`，只需第一次执行前运行一次

`caseCreartor.py`：自动生成case文件

`stepvaluepool.py`：存储Step method中间数据

`getsign.py`：参数sign计算方法

![项目目录介绍](https://user-gold-cdn.xitu.io/2020/7/27/1738eff1c6689ac0?w=1321&h=675&f=png&s=81871)
----------

**项目操作步骤介绍**
 
 1. 运行根目录下的`set_rootdir.py`文件，生成本地`ROOTDIR`(仅首次使用该框架运行)
 2. 在`projects`目录下创建项目，目前最多支持二级
 3. `datafile`目录中存储用例参数文件(***parameters.xml)和用例描述文件(***testcases.xml），`stepgroups`目录中编写py脚本
 4. 运行`CaseCreator.py`根据用例描述文件在对应的testcases目录下生成pytest测试用例
 5. 可以直接找到文件运行单个的测试用例，也可以运行项目根目录下的run.py批量跑测试用例（可以接 --casetag P1+BVT,p2 跑指定标记的用例集）

----------

**注意**

1.`.idea`文件和`setting.py`如果只是改了`rootdir`的话不用提交!!!
2. api_pygat目录  pip3 install -i https://pypi.douban.com/simple/ -r requirements.txt 可以批量安装所需依赖包
3.安装Crypto模块后，仍提示 ImportError: No module named Crypto的解决办法：
  进入python的安装路径如：C:\Users\Administrator\AppData\Local\Programs\Python\Python37\Lib\site-packages，将包crypto的文件名称改成Crypto
