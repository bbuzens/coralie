import os
import pandas
import logging


class DataConf:
    def __init__(self, configuration_directory_path):
        self.configuration_directory_path = configuration_directory_path
        self.load()

    def __iter__(self):
        return self.dataframes.__iter__()

    def __getitem__(self, item):
        return self.dataframes[item]

    def load(self):
        self.dataframes = {}
        for filename in os.listdir(self.configuration_directory_path):
            if (filename.endswith(".xlsx") or filename.endswith(".xls")) and not filename.startswith("~$"):
                configuration_file_path = "{configuration_directory_path}/{filename}".format(
                    configuration_directory_path=self.configuration_directory_path, filename=filename)
                self.dataframes[filename.split(".xls")[0]] = pandas.read_excel(configuration_file_path)
            else:
                print("fichier {filename} non chargé".format(filename=filename))
        return self

    def approx_age(self, age, dataframe_name):
        ages_list = self[dataframe_name].loc[:, ["AGE"]]
        logging.debug("AGES_LIST :\n{}".format(ages_list))
        age_approx = age
        age_max = ages_list.values[-1][0]
        tmp_dist = age_max
        for value in ages_list.values:
            iter_age = value[0]
            dist = abs(iter_age - age)
            logging.debug("DIST : {}".format(dist))
            logging.debug("AGE APPROX : {}".format(age_approx))
            if iter_age != iter_age :
                print("Error NaN")
                print("AGES_LIST :\n{}".format(ages_list))
                raise ValueError
            if dist == 0.0:
                age_approx = iter_age
                break
            elif dist < tmp_dist:
                tmp_dist = dist
                age_approx = iter_age
            else:
                pass
        return age_approx

    def get_group(self, age, dataframe_name, value):
        dataframe = self.dataframes[dataframe_name].query("AGE=={}".format(age))
        if dataframe.empty:
            print("AGE : {}".format(age))
            print("DATA : {}".format(dataframe_name))
            print("ERR_AGE_VALUE")
            raise ValueError
            return "ERR_AGE_VALUE"

        dataframe_titles = []
        for dataframe_title in dataframe:
            dataframe_titles.append(dataframe_title)
            logging.debug(dataframe_title)
        dataframe_titles.remove("AGE")
        logging.debug(dataframe_titles)
        dataframe_without_age = dataframe.loc[:, dataframe_titles]
        logging.debug(dataframe_without_age)
        tmp_val = 0
        indx = 0
        for indx, val in enumerate(dataframe_without_age.values[0]):
            logging.debug(val)
            if val < value:
                tmp_val = val
                logging.debug(tmp_val)
                if indx == len(dataframe_without_age.values[0]) - 1:
                    indx += 1
            else:
                break
        logging.debug(tmp_val)
        logging.debug(indx)
        intervals_limits = list(dataframe_without_age.columns)
        intervals_limits.insert(0, "INF")
        intervals_limits.append("SUP")
        logging.debug(intervals_limits)
        interval = "{inf}-{sup}".format(inf=intervals_limits[indx], sup=intervals_limits[indx + 1])
        return interval
