import xmltodict
import os


class Address_Changer:

    def __init__(self):
        self.input_folder = "D:w\P20220907\\04_evaluation\\17_Veip_16mm_wet_cup\Muhrec_time_series\\"
        self.output_folder = "D:\P20220907\\04_evaluation\\17_Veip_16mm_wet_cup\Kip_time_series\\"

    def change_input_address(self, adress):
        self.input_folder = adress

    def change_output_address(self, adress):
        self.output_folder = adress


class Xml_Changer:

    def __init__(self):
        self.config_xml = {"kiplprocessing":
                         {"inputfolder": "this should be something else",
                          "outputfolder": "this should be something else"
                          }}

    def change_config_xml(self, xml_address_changed):
        self.config_xml["kiplprocessing"]["image"]["srcfilemask"] = xml_address_changed.input_folder
        self.config_xml["kiplprocessing"]["outimage"]["dstpath"] = xml_address_changed.output_folder

    def set_config_file_default(self, xml_default):
        self.config_xml = xml_default

    def set_itteration_config(self,start_int,end_int):
        self.config_xml["kiplprocessing"]["image"]["firstfileindex"] = start_int
        self.config_xml["kiplprocessing"]["image"]["lastfileindex"] = end_int


# class Thread_Controller:
#
#     def __init__(self):
#         self.folder_list = []
#         self.start_index = 0
#         self.end_index = 0
#         self.thread = 1
#
#     def assign_folder_list(self, assigned_list):
#         self.folder_list = assigned_list
#
#     def assign_start_index(self, start_int):
#         self.start_index = start_int
#
#     def assign_end_index(self, end_int):
#         self.end_index = end_int
#
#     def assign_thread_number(self,thread_int):
#         self.thread_int = thread_int
#
#     def initialize_new_run(self):
#         xml_changer[f"{self.thread}"] = Xml_Changer()
#         adress_changer[f"{self.thread}"] = Address_Changer()
#         with open('CurrentKIPToolConfig.xml') as xmlfile:
#             xml_changer[f"{self.thread}"].set_config_file_default(xmltodict.parse(xmlfile.read()))
#
#     def run_list(self):
#         print(xml_changer[f"{self.thread}"].config_xml)
#         print(adress_changer[f"{self.thread}"].output_file,adress_changer[f"{self.thread}"].input_file)

if __name__ == '__main__':

    parent_input = "D:w\P20220907\\04_evaluation\\17_Veip_16mm_wet_cup\Muhrec_time_series\\"
    parent_output = "D:\P20220907\\04_evaluation\\17_Veip_16mm_wet_cup\Kip_time_series\\"
    address_changer1 = Address_Changer()
    xml_changer1 = Xml_Changer()
    with open('CurrentKIPToolConfig.xml') as xmlfile:
            xml_changer1.set_config_file_default(xmltodict.parse(xmlfile.read()))

    for i in os.listdir("./test"):
        address_changer1.change_input_address(parent_input+"\\"+i)
        print(address_changer1.input_folder)
        address_changer1.change_output_address(parent_output +"\\"+ i)
        xml_changer1.change_config_xml(address_changer1)
        xml_changer1.set_itteration_config(0, 500)
        with open(f"./test/{i}/xml{i}.xml", 'w') as f:
            xml = xmltodict.unparse(xml_changer1.config_xml, pretty=True)
            f.write(xml)

        #first call

        print("first call complete? otherwise break!")

        xml_changer1.set_itteration_config(501, 1000)
        with open(f"./test/{i}/xml{i}.xml", 'w') as f:
            xml = xmltodict.unparse(xml_changer1.config_xml, pretty=True)
            f.write(xml)

        #second call

        xml_changer1.set_itteration_config(1001, 1500)
        with open(f"./test/{i}/xml{i}.xml", 'w') as f:
            xml = xmltodict.unparse(xml_changer1.config_xml, pretty=True)
            f.write(xml)

        #third call

        xml_changer1.set_itteration_config(1501, 2000)
        with open(f"./test/{i}/xml{i}.xml", 'w') as f:
            xml = xmltodict.unparse(xml_changer1.config_xml, pretty=True)
            f.write(xml)

        #fourth call
