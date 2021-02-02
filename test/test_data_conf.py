import lib.data_conf as data_conf
import pandas


def test_DataConf_init():
    dataConf_instance = data_conf.DataConf("conf")
    assert isinstance(dataConf_instance, data_conf.DataConf)


def test_DataConf_getitem():
    dataConf_instance = data_conf.DataConf("conf")
    setName = "imc_filles"
    dataSet = dataConf_instance[setName]
    assert any(dataSet)
    assert type(dataSet) is pandas.core.frame.DataFrame


def test_DataConf_iter():
    # print("\n\n##############")
    # print("TEST : {}".format(inspect.currentframe().f_code.co_name))
    # print("-------------")
    dataConf_instance = data_conf.DataConf("conf")
    for dataframe_name in dataConf_instance:
        # print(dataframe_name)
        assert any(dataframe_name)
        assert dataConf_instance[dataframe_name].empty is False
    # print("##############")


def test_DataConf_load():
    dataConf = data_conf.DataConf("conf").load()
    setName = "imc_filles"
    dataSet = dataConf[setName]
    # print(type(dataSet))
    #
    # print("\n\n##############")
    # print("TEST : {}".format(inspect.currentframe().f_code.co_name))
    # print("-------------")
    # print("DATACONF :")
    # print(dataConf)
    # print("DATASET : {}".format(setName))
    # print(dataSet)
    # print("##############")
    assert any(dataSet)
    assert type(dataSet) is pandas.core.frame.DataFrame
    assert dataSet.empty is False


def test_DataConf_approx_age():
    dataConf = data_conf.DataConf("conf").load()
    setName = "imc_filles"

    age_approx = dataConf.approx_age(18, setName)
    assert age_approx == 12

    age_approx = dataConf.approx_age(12, setName)
    assert age_approx == 12

    age_approx = dataConf.approx_age(19, setName)
    assert age_approx == 24


def test_DataConf_get_group():
    dataConf = data_conf.DataConf("conf")
    dataframe = "imc_filles"
    dataConf.get_group(12, dataframe, 15.1)
    assert dataConf.get_group(12, dataframe, 10) == "INF-IOTF17"
    assert dataConf.get_group(24, dataframe, 15) == "IOTF17-IOTF25"
    assert dataConf.get_group(72, dataframe, 18) == "IOTF25-IOTF30"
    assert dataConf.get_group(48, dataframe, 25) == "IOTF30-SUP"
    assert dataConf.get_group(49, dataframe, 25) == "ERR_AGE_VALUE"
