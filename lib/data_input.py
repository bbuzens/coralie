import pandas
import logging


class Data:
    def __init__(self, data_directory_path, filename):
        self.data_directory_path = data_directory_path
        self.filename = filename
        self.load()

    def load(self):
        if self.filename.endswith(".xlsx") or self.filename.endswith(".xls"):
            data_file_path = "{data_directory_path}/{filename}".format(
                data_directory_path=self.data_directory_path, filename=self.filename)
            self.data = pandas.read_excel(data_file_path)
        else:
            print("fichier {filename} non chargé".format(filename=self.filename))
        return self

    def get_data(self):
        return self.data

    def affect_groups(self, dataConf):
        logging.debug(self.data.columns)
        data_types = self.data.columns
        data_types = data_types.drop(["Ref_Mesure", "Age", "Sexe"])
        data_groups = []
        for data_type in data_types:
            data_groups.append("{}_GROUP".format(data_type))
        logging.debug(data_groups)
        dataFrame = pandas.DataFrame(self.data)
        dataFrame[data_groups] = ""

        for index, row in self.data.iterrows():
            logging.debug(row.loc['Sexe'])
            if row.loc['Sexe'] == "F":
                conf_sexe = "filles"
            elif row.loc['Sexe'] == "M":
                conf_sexe = "garçons"
            else:
                raise ERR_SEXE_INPUT_VALUE("ERR_SEXE_INPUT_VALUE")
                continue
            for data_type in data_types:
                conf_type = "{data_type}_{sexe}".format(data_type=data_type.lower(), sexe=conf_sexe)
                logging.debug("con_type : {}".format(conf_type))
                logging.debug(row.loc['Age'])
                approx_age = dataConf.approx_age(row.loc['Age'], conf_type)
                logging.debug(approx_age)
                dataFrame.loc[index, "{}_GROUP".format(data_type)] = dataConf.get_group(approx_age, conf_type, row.loc[data_type])
            logging.debug(dataFrame.loc[index, :])
        logging.debug(dataFrame)
        return dataFrame
