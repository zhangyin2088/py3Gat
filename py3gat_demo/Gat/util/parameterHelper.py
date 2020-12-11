from lib2to3.pytree import convert

from Gat.util.XMLparsehelp import get_stepParameters4xml
from Gat.util.stepvaluepool import StepValuePool
from settings import GlobalConfig
from Gat.util.dichelper import DictHelper
from Gat.util.methodtracer import traceFrameMessage

class ParameterHelper(object):

    @staticmethod
    def getStepParameters(parameterID):
        allstr_stepParameters = get_stepParameters4xml(GlobalConfig.StepParameterFilePath, parameterID)
        single_layer_stepParameters = DictHelper.dicVstr2num(allstr_stepParameters)
        stepParameters = DictHelper.paramstr2dic(single_layer_stepParameters)
        stepParameters = DictHelper.convert_byte2str(stepParameters)
        traceFrameMessage("stepParameters: %s" % str(stepParameters), level="debug")
        return stepParameters

    @staticmethod
    def get_selected_param(params, key):

        if key in params:
            return params[key]
        if "join_sign" in params:
            if key in params["join_sign"]:
                return params["join_sign"][key]

        valuepool = StepValuePool()
        return valuepool.get_value(key)


    @staticmethod
    def set_params(params,key,value):
        if params == None:
            params = {}
        params[key] = value

    @staticmethod
    def set_join_sign_params(params,key,value):
        if params == None:
            params = {}
        if "join_sign" not in params:
            params.setdefault("join_sign")
            params["join_sign"] = {}
        params["join_sign"][key] = value


if __name__ == '__main__':
    params = {'join_sign': {'status': 1, 'uid': '154353'}, 'start_ts': 1560000000}
    key = 'order_id'
    valuepool = StepValuePool()
    valuepool.put_value("order_id", "1222")
    valuepool.put_value("product_id", "1212121")
    print(valuepool.get_value("order_id"))
    params["join_sign"]["order_id"] = ParameterHelper.get_selected_param(params,key)
    print(params)






