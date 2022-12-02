
import TheAvengers
import pika
import numbers
QUEUE_NAME_1 = 'THREAT'
import NickFury_Defense_Functions
import json

hr = ' '
def RMQ_HR_RESPONE(ch, method, properties, body):
    print(str(body))
    print("HR on it ")


def RMQ_on_request_THREAT_message_received(ch, method, properties, body):
    #Handle Threat
    global hr
    print(f'Recived msg is:{body.decode("utf-8")}')
    #Build the msg that nick sends
    msg = {
        'Code': '1',
        'Threat': body.decode("utf-8"),
        'HR':hr[0],
        'Crew': NickFury_Defense_Functions.select_crew(),
        'Sender':'NickFury'
    }
    # convert into JSON:
    js = json.dumps(msg)
    print(js)
    msg = js
    
    try:
        print(f'Sending Threat Details to HR:{msg}')
        #ch.basic_publish('', routing_key=properties.reply_to, body=f'The Answer is : {msg}')
        ch.basic_publish('', routing_key=str(hr[0]), body=f'{msg}')
    except ValueError:
        print("Sending Input type incorect")
        ch.basic_publish('', routing_key=properties.reply_to, body=f'The Answer is : Sending Input type incorect')    
         
def start_RMQ_server():
    #This Function starts a RMQ Server
    global hr
    hr = str(NickFury_Defense_Functions.selectHR())
    print("Starting NickFury Defense Engine")
    connection_parameters = pika.ConnectionParameters('localhost')
    connection = pika.BlockingConnection(connection_parameters)
    channel = connection.channel()
    
    channel.queue_declare(queue=QUEUE_NAME_1, durable=True)    
    channel.queue_declare(queue=hr, durable=False)       

    channel.basic_consume(queue=QUEUE_NAME_1, auto_ack=True,
        on_message_callback=RMQ_on_request_THREAT_message_received)
    
    channel.basic_consume(queue=hr, auto_ack=False,
        on_message_callback=RMQ_HR_RESPONE)
    
    channel.start_consuming()
    
def main():
    print('hererere')
    start_RMQ_server()

if __name__ == '__main__':
    main()

