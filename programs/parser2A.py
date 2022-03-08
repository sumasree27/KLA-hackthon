import logging
from multiprocessing import Condition
import yaml
from threading import Thread
import time
from logger import logger 
from common import *
file = open('Milestone2A.yaml','r')
content= yaml.safe_load(file)
class Parser:
    li = []
    flownames =''
    current_task =''
    execution = ''
    function_type = ''
    number_of_defects = None
    arggg =[]
    def get_all_values(self,nested_dictionary):
        for key, value in nested_dictionary.items():
            if('task' in key.lower()):
                # print("Valuee-->",value)
                condition_success= True
                if(value['Function']=='DataLoad'):
                    if 'Condition' in value:
                        condition = value['Condition']
                        if '>' in value['Condition']:
                            if(self.number_of_defects >int(condition.split('>')[-1])):
                                condition_success = True
                            else:
                                condition_success = False
                                logger.info(self.current_task+" Skipped")
                        if '<' in value['Condition']:
                            if(self.number_of_defects <int(condition.split('>')[-1])):
                                condition_success = True
                            else:
                                condition_success = False
                                logger.info(self.current_task+" Skipped")
                    if condition_success:
                        logger.info(self.current_task+" Executing TimeFunction "+ '(' + value['Inputs']['Filename']+')')
                        data_table, self.number_of_defects = Load_data(value['Inputs']['Filename'])
                        logger.info(self.current_task+" Exit")
                elif(self.execution == 'Concurrent'):
                    logger.info(self.current_task+" Executing TimeFunction "+ '(' + value['Inputs']['FunctionInput']+ ','+value['Inputs']['ExecutionTime']+')')
                    Thread(target=time_function(value['Inputs']['FunctionInput'],value['Inputs']['ExecutionTime'])).start()
                    logger.info(self.current_task+" Exit")
                else:
                    logger.info(self.current_task+" Executing TimeFunction "+ '(' + value['Inputs']['FunctionInput']+ ','+value['Inputs']['ExecutionTime']+')')
                    time_function(value['Inputs']['FunctionInput'],value['Inputs']['ExecutionTime'])
                    logger.info(self.current_task+" Exit")
                print(key, ":", value)
            elif type(value) is dict:
                print("puree vallll-->",key)
                self.arggg.append(key)
                if 'flow' in key.lower():
                    self.execution = value['Execution']
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
p=Parser()
p.get_all_values(content)
p.li.append(p.flownames)
p.li = p.li[1:]
print("jnviuniuw-->",p.li)
print("Final arggg--->",p.arggg)
while(p.li):
    logger.info(p.li.pop()[1:]+" Exit")
print(p.flownames)

