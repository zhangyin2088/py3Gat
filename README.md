# py3Gat
python3 + pytest + allure +xml +自封装的支持多平台、多项目、多(组合)接口、多环境的接口自动化测试框架
---------------------------
**重要文件介绍**

`set_rootdir.py`：自动生成本地`ROOTDIR`，只需第一次执行前运行一次

`caseCreartor.py`：自动生成case文件

`stepvaluepool.py`：存储Step method中间数据

`run.py`： 各项目下有一个，用来批量运行项目case，也可以放在最外层运行全项目case，可以接参数

![项目目录介绍](https://user-gold-cdn.xitu.io/2020/7/27/1738eff1c6689ac0?w=1321&h=675&f=png&s=81871)
----------

**项目操作步骤介绍**
 1. api_pygat目录  pip3 install -i https://pypi.douban.com/simple/ -r requirements.txt 可以批量安装所需依赖包
 2. 运行根目录下的`set_rootdir.py`文件，生成本地`ROOTDIR`(仅首次使用该框架运行一次，这里需要进到该目录下运行，不能在别的目录用相对或绝对路径运行，直接在pycharm运行该文件也可以)
 3. 在`projects`目录下创建项目，目前最多支持二级（这里提供了demo项目作为参考，其中demo1为1层，demo2是两层目录，比如有的项目可能分学生端、教师端等）
 4. 各项目的`datafile`目录中存储用例参数文件(***parameters.xml)和用例描述文件(***testcases.xml），`stepgroups`目录中编写py脚本
 5. 运行根目录CaseCreator 目录下的 `CaseCreator.py`，会自动根据用例描述文件在对应的testcases目录下生成pytest测试用例（这里也需要进到当前目录）
 6. 去项目的testcases目录下找到新生成的test_*.py文件运行单个的测试用例，也可以运行项目目录下的run.py批量跑测试用例（可以接 --casetag P1+BVT,p2 跑指定标记的用例集）

----------

**注意**

1.`.idea`文件和`setting.py`如果只是改了`rootdir`的话不用提交!!!
2. 大部分框架可能只有一个参数文件(parameters文件)加一个测试用例文件（test_*.py），这个框架会多出一个用例描述文件和stepgroups下面的接口step脚本文件，用例描述文件用来可视化的描述用例，单个测试用例可以包含多个接口，都可以在里面配置（这也是实现组合接口的一个方式），且单组参数和单个接口step是可以一一组合的，具体的接口测试也都是在接口step文件里完成的，而测试用例test_*.py是自动生成的，不需要我们编写，会自动根据用例描述文件里挨个去调这个case用到的接口step

