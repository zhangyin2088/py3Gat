'''
该脚本用来批量运行该项目下符号条件的case
命令行调用，可以跟持续集成结合，生成的xml报告再跟allure（jenkins有插件）结合展示可视化报告
如命令行运行 python3 run.py 后面不接任何参数，则会运行该项目下testcases目录里的所有case
也支持在后面增加 --casetag param，用来运行指定标签的case
    举例：python3 run.py --casetag BVT+P0,P1  表示运行该项目下有bvt加P0双标签的case或者有P1标签的case
'''
import sys
import argparse
sys.path.append(r'{ROOTDIR}')
import pytest
def main():
    pytest_args=['-s', '-q', '--alluredir', r'{XMLREPORTDIR}']
    parser = argparse.ArgumentParser(description='manual to this script')
    parser.add_argument('--casetag', type=str, default=None)  #添加--casetag 这个命令行参数，用来运行指定标记的case
    args = parser.parse_args()
    if args.casetag:
        pytest_args.append('-m')
        if "+" in args.casetag:
            args.casetag = args.casetag.replace("+", " and ") #--casetag 后面的参数里用+号代表组合标记，即同时拥有两个及以上标记的case
        if "," in args.casetag:
            args.casetag = args.casetag.replace(",", " or ")  #--casetag后面的参数里用,号代表多选标签，或者的意思
        pytest_args.append(args.casetag)
    pytest.main(pytest_args)

if __name__ == "__main__":
    main()