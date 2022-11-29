from ast import If
import pika
import uuid
import os,sys
from HelpFunctions import get_input 
from HelpFunctions import input_file_data 

QUEUE_NAME_1 ='THREAT'
THREATS_FILE_PATH = 'Threats.txt'
class Threat:
    
    def __init__(self,description, location, damage, time):
        self.description = description
        self.location = location
        self.damage = float(damage)
        self.time = float(time)
    def __str__(self):
        return 'Threat:\nDescription:{}\nLocation:{}\nDamage:{}\nTime:{}'.format(self.description,self.location,self.damage,self.time)
    
def consturct_threat(msg):
    #This Function recive Threat Details in list and convert it to Threat instance
    threat1 = Threat(msg[0],msg[1],msg[2],msg[3])
    return threat1    

def on_reply_message_received(ch, method, properties, body):
    print(f"reply recieved: {body}")
    
def start_RMQ_client(queueName,var):
    #Establish connection
    connection_parameters = pika.ConnectionParameters('localhost')
    connection = pika.BlockingConnection(connection_parameters)
    channel = connection.channel()
    
    reply_queue = channel.queue_declare(queue='', exclusive=True)
    channel.basic_consume(queue=reply_queue.method.queue, auto_ack=True,on_message_callback=on_reply_message_received)   
    #channel.queue_declare(queue=QUEUE_NAME_1)
    
    cor_id = str(uuid.uuid4())#generate a unique id
    
    print("Starting Client\n")
    print(f"Sending Threat Details:\n{var}")
    
    channel.basic_publish('', routing_key=queueName, properties=pika.BasicProperties(
        reply_to=reply_queue.method.queue,
        correlation_id=cor_id
    ), body=str(var))

    channel.start_consuming()
    
def main():
    
    threats = input_file_data("Threats.txt")
    msg = threats[0]
    start_RMQ_client(QUEUE_NAME_1,msg)
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)