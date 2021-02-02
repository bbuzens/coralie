import lib.data_input as data_input
import lib.data_conf as data_conf
import inspect
import pandas


def test_data_input_init():
    path = "input"
    file = "exemple_v2.0.xlsx"

    data = data_input.Data(path, file)
    # print ("\nDATA :")
    # print(data.get_data())
    assert data.data.empty is False

def test_data_input_get_data():
    path = "input"
    file = "exemple_v2.0.xlsx"

    data = data_input.Data(path, file)
    dataFrame=data.get_data()
    # print ("\nDATA :")
    # print(data.get_data())
    assert dataFrame.empty is False

def test_data_input_affect_groups():
    path = "input"
    file = "exemple_v2.0.xlsx"
    conf = data_conf.DataConf("conf")
    data = data_input.Data(path, file)
    output = data.affect_groups(conf)
    assert output.empty is False
    print(output)
