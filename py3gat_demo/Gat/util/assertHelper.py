from Gat.util.methodtracer import traceFrameMessage
import json

class AssertHelper(object):

    @staticmethod
    def assert_dict_equal(src_data,dst_data):
        assert type(src_data) == type(dst_data),"type: '{}' != '{}'".format(type(src_data), type(dst_data))
        if isinstance(src_data,dict):
            assert len(src_data) == len(dst_data),"dict len: '{}' != '{}'".format(len(src_data), len(dst_data))
            for key in src_data:
                assert dst_data.has_key(key)
                AssertHelper.assert_dict_equal(src_data[key],dst_data[key])
        elif isinstance(src_data,list):
            assert len(src_data) == len(dst_data),"list len: '{}' != '{}'".format(len(src_data), len(dst_data))
            for src_list, dst_list in zip(sorted(src_data), sorted(dst_data)):
                AssertHelper.assert_dict_equal(src_list, dst_list)
        else:
            assert src_data == dst_data,"value '{}' != '{}'".format(src_data, dst_data)

    @staticmethod
    def assert_dict_contain_after_logging(src_data, dst_data):
        traceFrameMessage("Expected Result: {}" .format(src_data))
        traceFrameMessage("Actual Result: {}".format(json.dumps(dst_data).encode("gbk").decode("utf-8")))
        return AssertHelper.assert_dict_contain(src_data, dst_data)

    @staticmethod
    def assert_dict_contain(src_data, dst_data):

        #assert type(src_data) == type(dst_data), "type: '{}' != '{}'".format(type(src_data), type(dst_data))
        if isinstance(src_data, dict):
            for key in src_data:
                if isinstance(dst_data, dict):
                    # assert dst_data.has_key(key)
                    assert dst_data.__contains__(key)
                    AssertHelper.assert_dict_contain(src_data[key], dst_data[key])
                elif isinstance(dst_data, list):
                    dst_list = []
                    for i in dst_data:
                        if isinstance(i,dict):
                            # if i.has_key(key):
                            if i.__contains__(key):
                                dst_list.append(i[key])
                    if len(dst_list) == 0:
                        raise Exception("%s not in dst_dic or dst_dic[%s] type wrong" %(key,key))
                    elif len(dst_list) == 1:
                        AssertHelper.assert_dict_contain(src_data[key], dst_list[0])
                    else:
                        AssertHelper.assert_dict_contain(src_data[key], dst_list)

        elif isinstance(src_data, list):
           # for src_list, dst_list in zip(sorted(src_data), sorted(dst_data)):
                #assert_dict_contain(src_list, dst_list)
            if isinstance(dst_data, list):
                for element in src_data:
                    print("***element:")
                    print(element)
                    print("***dst_data:")
                    print(dst_data)
                    AssertHelper.assert_dict_contain(element, dst_data)
            else:
                raise Exception("src_data is list but dst_data is not")
        else:
            if isinstance(dst_data,list):
                assert src_data in dst_data, "value '{}' not in '{}'".format(src_data, dst_data)
            else:
                assert src_data == dst_data, "value '{}' != '{}'".format(src_data, dst_data)

if __name__ == "__main__":
    xx = {"222":{"44":{"66":[{"333": 555},{"555": 666}]}}}
    yy = {"111": None,"222":{"33": 44,"44":[{"55": 66},{"66": [{"333": 444},{"333": 555},{"555": 666}]}]}}
    AssertHelper.assert_dict_contain_after_logging(xx, yy)

    xx1 = {"111": None, "23456": {"22222": 9999, "33333": "0000", "list": ["3333", "4444"]}}
    yy1 = {"111": None, "23456": {"22222": 9999, "33333": "0000", "list": ["111", "3333", "4444"]}}
    #assert_dict_contain(xx1, yy1)
    list1 = [{"333": 444},{"444": 555},{"s":"7日vip"}]

    print(list1)