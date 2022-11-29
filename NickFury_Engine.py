
import TheAvengers
import pika
import numbers
QUEUE_NAME_1 = 'THREAT'
import NickFury_Defense_Functions

def RMQ_HR_RESPONE(ch, method, properties, body):
    print("HR on it ")


def RMQ_on_request_THREAT_message_received(ch, method, properties, body):
    #Handle Threat
    hr = NickFury_Defense_Functions.selectHR()
    msg = [body.decode("utf-8"),]
    print(f'Recived msg is:{body.decode("utf-8")}')
    try:
        answer ='hi'
        #answer = #______#(int(body.decode("utf-8")))
        print(f"Sending Threat Details to HR:{answer}")
        #ch.basic_publish('', routing_key=properties.reply_to, body=f'The Answer is : {answer}')
        ch.basic_publish('', routing_key='HR', body=f'The Threat is : {answer}')
    except ValueError:
        print("Sending Input type incorect")
        ch.basic_publish('', routing_key=properties.reply_to, body=f'The Answer is : Sending Input type incorect')    
         
def start_RMQ_server():
    #This Function starts a RMQ Server
    
    print("Starting NickFury Defense Engine")
    connection_parameters = pika.ConnectionParameters('localhost')
    connection = pika.BlockingConnection(connection_parameters)
    channel = connection.channel()
    
    channel.queue_declare(queue=QUEUE_NAME_1, durable=True)    
    channel.queue_declare(queue='HR', durable=False)       

    channel.basic_consume(queue=QUEUE_NAME_1, auto_ack=True,
        on_message_callback=RMQ_on_request_THREAT_message_received)
    
    channel.basic_consume(queue='HR', auto_ack=True,
        on_message_callback=RMQ_HR_RESPONE)
    
    channel.start_consuming()
    
def main():
    print('hererere')
    start_RMQ_server()

if __name__ == '__main__':
    main()

