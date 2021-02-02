import lib.data_input as data_input
import lib.data_conf as data_conf

path = "input"
file = "exemple_v2.0.xlsx"
conf = data_conf.DataConf("conf")



if __name__=="__main__":
    data = data_input.Data(path, file)
    data_with_groups = data.affect_groups(conf)
    data_with_groups.to_excel("output_{}".format(file), index=False)
