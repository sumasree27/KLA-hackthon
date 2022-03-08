import logging
import yaml
import time
from logger import logger 
from common import *
file = open('Milestone1A.yaml','r')
content= yaml.safe_load(file)
class Parser:
    li = []
    flownames =''
    current_task =''
    def get_all_values(self,nested_dictionary):
        for key, value in nested_dictionary.items():
            if(key=='Inputs'):
                logger.info(self.current_task+" Executing TimeFunction "+ '(' + value['FunctionInput']+ ','+value['ExecutionTime']+')')
                time_function(value['FunctionInput'],value['ExecutionTime'])
                logger.info(self.current_task+" Exit")
                print(key, ":", value)
            elif type(value) is dict:
                if 'flow' in key.lower():
                    self.li.append(self.flownames)
                    self.flownames+='.'+key
                    logger.info(self.flownames[1:]+" Entry")
                if 'task' in key.lower():
                    logger.info(self.flownames[1:]+'.'+key+" Entry")
                    self.current_task = self.flownames[1:]+'.'+key
                # self.str1=self.key
                self.get_all_values(value)
            else:
                print(key, ":", value)

# nested_dictionary = {"dict1": {"a": 1},"dict2": {"b": 2}}
p=Parser()
p.get_all_values(content)
p.li.append(p.flownames)
p.li = p.li[1:]
print("jnviuniuw-->",p.li)
while(p.li):
    logger.info(p.li.pop()[1:]+" Exit")
print(p.flownames)

