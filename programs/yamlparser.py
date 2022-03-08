import logging
import yaml
from threading import Thread
import time
from logger import logger 
from common import *
file = open('Milestone1B.yaml','r')
content= yaml.safe_load(file)
class Parser:
    li = []
    flownames =''
    current_task =''
    execution = ''
    arggg =[]
    def get_all_values(self,nested_dictionary):
        for key, value in nested_dictionary.items():
            if(key=='Inputs'):
                logger.info("Added Debug"+ str(self.execution) + str(self.current_task))
                if(self.execution == 'Concurrent'):
                    logger.info(self.current_task+" Executing TimeFunction "+ '(' + value['FunctionInput']+ ','+value['ExecutionTime']+')')
                    Thread(target=time_function(value['FunctionInput'],value['ExecutionTime'])).start()
                    logger.info(self.current_task+" Exit")
                else:
                    logger.info(self.current_task+" Executing TimeFunction "+ '(' + value['FunctionInput']+ ','+value['ExecutionTime']+')')
                    time_function(value['FunctionInput'],value['ExecutionTime'])
                    logger.info(self.current_task+" Exit")
                print(key, ":", value)
            # if(key=='Activities'):
            #     print("dfjkvnidfbvhdfbvuhvbuvbdfubvdfuybvdfuybdubvdfuvbujh")
            #     print(value)
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

