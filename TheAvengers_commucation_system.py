import pika
import ast
import json
import HelpFunctions
import TheAvengers

def RMQ_SERVER_CLIENT():
    Avengers = TheAvengers.create_Avengers()
    
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

    channel = connection.channel()
    channel.queue_declare(queue='HR')    
    channel.queue_declare(queue='IronMan')
    channel.queue_declare(queue='CaptainAmerica')
    channel.queue_declare(queue='Thor')
    channel.queue_declare(queue='BlackWindow')
    channel.queue_declare(queue='Hulk')
    channel.queue_declare(queue='Hawkeye')
    

    def hr_request_handle(ch, method, props, body):
        #Here we recive the msg from NickFury
        #msg contains the threat info and the crew info
        print("hr_request_handle FUNCTION\n")
        print(body.decode("utf-8"))    
        lst = HelpFunctions.extract_info_from_NickMSG_json(str(body.decode("utf-8")))
        code = lst[0]
        threat = lst[1]
        hr = lst[2]
        crew = lst[3]
        key = ''

        print("Threat is: "+str(threat))
        print("Crew is:\n"+str(crew))
        ch.close()
        
    def CaptainAmerica_request_handle(ch, method, props, body):
        channel._cleanup()
        print("YOU ARE IN CA")
        msg = body.decode("utf-8")
        print(msg)
        instance1 = HelpFunctions.return_obj(Avengers,'CaptainAmerica')
        info = HelpFunctions.extract_info_from_NickMSG_json(msg)
        code = info[0]
        reciver = info[4]
        response= HelpFunctions.check_msg_code(code,instance1)
        print(response)
        if code == '1':
            crew = info[3]
            for i in crew:
                ch.basic_publish(exchange='',
                            routing_key=i,
                            properties=pika.BasicProperties(correlation_id = \
                                                                props.correlation_id),
                            body=str(response))
                ch.basic_ack(delivery_tag=method.delivery_tag)
        else:
            ch.basic_publish(exchange='',
                        routing_key=reciver,
                        properties=pika.BasicProperties(correlation_id = \
                                                            props.correlation_id),
                        body=str(response))
        ch.basic_ack(delivery_tag=method.delivery_tag)
            
    def Thor_request_handle(ch, method, props, body):
        print("YOU ARE IN Thor")
        msg = body.decode("utf-8")
        print(msg)
        instance1 = HelpFunctions.return_obj(Avengers,'Thor')
        info = HelpFunctions.extract_info_from_NickMSG_json(msg)
        code = info[0]
        reciver = info[4]
        response= HelpFunctions.check_msg_code(code,instance1)
        print(response)
        if code == '1':
            crew = info[3]
            for i in crew:
                ch.basic_publish(exchange='',
                            routing_key=i,
                            properties=pika.BasicProperties(correlation_id = \
                                                                props.correlation_id),
                            body=str(response))
                ch.basic_ack(delivery_tag=method.delivery_tag)
        else:
            ch.basic_publish(exchange='',
                        routing_key=reciver,
                        properties=pika.BasicProperties(correlation_id = \
                                                            props.correlation_id),
                        body=str(response))
        ch.basic_ack(delivery_tag=method.delivery_tag)
        
    def BlackWindow_request_handle(ch, method, props, body):
        print("YOU ARE IN BlackWindow")
        msg = body.decode("utf-8")
        print(msg)
        instance1 = HelpFunctions.return_obj(Avengers,'BlackWindow')
        info = HelpFunctions.extract_info_from_NickMSG_json(msg)
        code = info[0]
        reciver = info[4]
        response= HelpFunctions.check_msg_code(code,instance1)
        print(response)
        if code == '1':
            crew = info[3]
            for i in crew:
                ch.basic_publish(exchange='',
                            routing_key=i,
                            properties=pika.BasicProperties(correlation_id = \
                                                                props.correlation_id),
                            body=str(response))
                ch.basic_ack(delivery_tag=method.delivery_tag)
        else:
            ch.basic_publish(exchange='',
                        routing_key=reciver,
                        properties=pika.BasicProperties(correlation_id = \
                                                            props.correlation_id),
                        body=str(response))
        ch.basic_ack(delivery_tag=method.delivery_tag)
        
    def Hulk_request_handle(ch, method, props, body):
        print("YOU ARE IN Hulk")
        msg = body.decode("utf-8")
        print(msg)
        instance1 = HelpFunctions.return_obj(Avengers,'Hulk')
        info = HelpFunctions.extract_info_from_NickMSG_json(msg)
        code = info[0]
        reciver = info[4]
        response= HelpFunctions.check_msg_code(code,instance1)
        print(response)
        if code == '1':
            crew = info[3]
            for i in crew:
                ch.basic_publish(exchange='',
                            routing_key=i,
                            properties=pika.BasicProperties(correlation_id = \
                                                                props.correlation_id),
                            body=str(response))
                ch.basic_ack(delivery_tag=method.delivery_tag)
        else:
            ch.basic_publish(exchange='',
                        routing_key=reciver,
                        properties=pika.BasicProperties(correlation_id = \
                                                            props.correlation_id),
                        body=str(response))
        ch.basic_ack(delivery_tag=method.delivery_tag)
        
    def Hawkeye_request_handle(ch, method, props, body):
        print("YOU ARE IN Hawkeye")
        msg = body.decode("utf-8")
        print(msg)
        instance1 = HelpFunctions.return_obj(Avengers,'Hawkeye')
        info = HelpFunctions.extract_info_from_NickMSG_json(msg)
        code = info[0]
        reciver = info[4]
        response= HelpFunctions.check_msg_code(code,instance1)
        print(response)
        if code == '1':
            crew = info[3]
            for i in crew:
                ch.basic_publish(exchange='',
                            routing_key=i,
                            properties=pika.BasicProperties(correlation_id = \
                                                                props.correlation_id),
                            body=str(response))
                ch.basic_ack(delivery_tag=method.delivery_tag)
        else:
            ch.basic_publish(exchange='',
                        routing_key=reciver,
                        properties=pika.BasicProperties(correlation_id = \
                                                            props.correlation_id),
                        body=str(response))
        ch.basic_ack(delivery_tag=method.delivery_tag)
        
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='HR', on_message_callback=hr_request_handle)
    channel.basic_consume(queue='CaptainAmerica', on_message_callback=CaptainAmerica_request_handle)
    channel.basic_consume(queue='Thor', on_message_callback=Thor_request_handle)
    channel.basic_consume(queue='BlackWindow', on_message_callback=BlackWindow_request_handle)
    channel.basic_consume(queue='Hulk', on_message_callback=Hulk_request_handle)
    channel.basic_consume(queue='Hawkeye', on_message_callback=Hawkeye_request_handle)

    #print(" [x] Awaiting RPC requests")
    channel.start_consuming()
    
    
def main():
    print('Avengers_Commucation_system')
    RMQ_SERVER_CLIENT()

if __name__ == '__main__':
    main()