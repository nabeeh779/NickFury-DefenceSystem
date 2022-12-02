from random import randint
import json
import TheAvengers 

HR = {}
def get_input():
    #This Function Get input by user 
    return input("Enter Any Thing:")

def input_file_data(file):
    #This Function Help us import  file data splitted by ',' 
    temp = []
    with open(file,'r') as file:
        for line in file:
            grade_data = line.strip().split(',')
            temp.append(grade_data)
            #print(grade_data)
    return temp
########################################################
#                                                      #          
#      This functions Help The avengers commucation    #
#                                                      #
########################################################
def extract_info_from_NickMSG_json(str1):
    #This function extracat data from json form
    msg =  json.loads(str1)
    print(type(msg))
    print(msg)
    code = msg["Code"]
    threat = msg["Threat"]
    crew = msg["Crew"]
    hr = msg["HR"]
    sender = msg["Sender"]
    return [code,threat,hr,crew,sender]

def extract_info_from_json(str1):
    #This function extracat data from json form

    print("extract_info_from_json function:\n")
    print(str1)
    msg =  json.loads(str1)
    print(type(msg))
    print(msg)
    code = msg["Code"]
    threat = msg["Reciver"]
    crew = msg["msg"]
    return [code,threat,crew]

def return_obj(avengers,name):
    #This function search for the wanted instance
    for i in avengers:
        if name in str(i):
            return i
    print('error')
    return 0 


def check_msg_code(code,name):
    #This function check what is the code in the recived message
    #And Detremine what to respond
    #code number 1: instance is HR
    #code number 2: Return Location
    #code number 3:
    if code== '1':
        response = response = {
        "Code": "2",
        "Sender":'HR',
        "Threat": "Send Location To HR Please",
        "Sender":name.get_name(),
        "crew":None,
        "HR":None
        }
        return response
    if code == '2':
        return name.get_location()
    if code == '3':
        print(str(name.get_name())+' Is HR')