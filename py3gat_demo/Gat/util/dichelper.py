# coding:utf-8

from collections.abc import MutableMapping
# from collections import MutableMapping   python2

class DictHelper(object):

    # @staticmethod
    # def isnumstr(str):
    #     strnum = "-0123456789"
    #     for s in str:
    #         if s not in strnum:
    #             return False
    #     return True

    @staticmethod
    def str2num(s):
        #print(s)
        try:
            num = int(s)
            return num
        except (TypeError, ValueError):
            pass

        try:
            num = float(s)
            return num
        except ValueError:
            pass

        return s


    @staticmethod
    def dicVstr2num(dic):
        for k, v in dic.items():
            if v != None:
                if isinstance(v, dict):
                    v = DictHelper.dicVstr2num(v)
                else:
                    v = v.encode("UTF-8")
                    # print(type(v), v)
                    if "\"".encode() not in v:
                        v = DictHelper.str2num(v)

                    else:
                        v = v.replace("\"".encode(), "".encode())
                dic[k] = v
                # print type(v), v
        return dic

    @staticmethod
    def str2dic(key,value):
        '''
        :description:将 “A.B.C": dic_value 的格式转换成"A":{"B":{"C":dic_value}}}的格式
        :param key: "A.B.C"
        :param value: dic_value
        :return: {"A":{"B":{"C":dic_value}}}
        '''
        # print("***key:%s" % key )
        keys = key.split(".")
        if isinstance(value,dict):
            d2={}
            for k,v in value.items():
                d1= DictHelper.str2dic(k, v)
                d2=DictHelper.rec_merge(d1,d2)
            value = d2
        if len(keys) == 1:
            return {key: value}
        else:
            return {keys[0]: DictHelper.str2dic(".".join(keys[1:]), value)}

    @staticmethod
    def rec_merge(d1, d2):
        '''
        :description:合并2个字典
        :param d1:
        :param d2:
        :return: 合并后的字典
        '''
        for k, v in d1.items():
            if k in d2:
                if all(isinstance(e, list) for e in (v, d2[k])):
                    print("===========list appear")
                    for element in v:
                        d2[k].append(element)

                    continue
                # this next check is the only difference!
                if all(isinstance(e, MutableMapping) for e in (v, d2[k])):
                    d2[k] = DictHelper.rec_merge(v, d2[k])
                # we could further check types and merge as appropriate here.
        d3 = d1.copy()
        d3.update(d2)
        return d3

    @staticmethod
    def dict_insert_list(dic):
        '''
        :description:将字典中带[]的字段转化为list
        :param dic:原本的带key中带[]标记的无list字典
        :return:转化后的带list的字典
        '''
        for k in list(dic):
            # print("="*10),k,("="*10)

            if isinstance(dic[k], dict):
                dic[k] = DictHelper.dict_insert_list(dic[k])
            if "[" in k:
                list_key = k.split("[")[0]

                if list_key in dic:
                    dic[list_key].append(dic.pop(k))
                    # print("%s existed in dic" % list_key)
                    # print("now dic[%s]: " % list_key),dic[list_key]
                else:
                    dic[list_key] = [dic.pop(k)]
                    # print("%s is new in dic" % list_key)
                    # print("now dic[%s]: " % list_key),dic[list_key]
        return dic

    @staticmethod
    def paramstr2dic(case_data):
        dic = {}
        for key, value in case_data.items():
            d1 = DictHelper.str2dic(key, value)
            dic = DictHelper.rec_merge(d1, dic)
        dic = DictHelper.dict_insert_list(dic)
        return dic

    @staticmethod
    def params_pop_prefix(params, prefix):
        sign = None
        if prefix in params:
            sign = params.get(prefix)
            params.pop(prefix)
        if isinstance(sign, dict):
            params.update(sign)

        return params

    @staticmethod
    def convert_byte2str(data):
        if isinstance(data, bytes):
            return data.decode('ascii')
        if isinstance(data, dict):
            return dict(map(DictHelper.convert_byte2str, data.items()))
        if isinstance(data, tuple):
            return map(DictHelper.convert_byte2str, data)
        return data

if __name__ == "__main__":

    dic1 = {
        "@StepName": "InlandHotelListHotelFilterCheck",
        "ConnectionString": None,
        "@ID": "InlandHotelListHotelFilterCheck",
        "CommandText": None,
        "Parameters": {
            "equipmentFilter": "ttttt",
            "brandFilter": "iiiiii",
            "priceFilter": "88888.88888",
            "starFilter": "444444",
            "sortOrder": "55555"
        },

        "Expect": {
            "result.code": "66666",
            "result.message": "77777",
        }
    }

    print(DictHelper.dicVstr2num(dic1))
    # print("*"*50)
    # print(DictHelper.paramstr2dic(dic1))
    #print(float(8888))
