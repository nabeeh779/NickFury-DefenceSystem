import pika


def RMQ_SERVER_CLIENT():
   
    connection = pika.BlockingConnection( pika.ConnectionParameters(host='localhost'))

    channel = connection.channel()
    
    channel.queue_declare(queue='HR')    
    #channel.queue_declare(queue='IronMan')
    channel.queue_declare(queue='CaptainAmerica')
    channel.queue_declare(queue='Thor')
    channel.queue_declare(queue='BlackWindow')
    channel.queue_declare(queue='Hulk')
    channel.queue_declare(queue='Hawkeye')
    

    def hr_request_handle(ch, method, props, body):
        msg = body
        response = 'Its from HR'#####
        print(str(body))
        ch.basic_publish(exchange='',
                        routing_key='CaptainAmerica',
                        properties=pika.BasicProperties(correlation_id = \
                                                            props.correlation_id),
                        body=str(response))
        ch.basic_ack(delivery_tag=method.delivery_tag)
    def CaptainAmerica_request_handle(ch, method, props, body):
        msg = body
        response = 'Its from CaptainAmerica'#####
        print(str(body))
        ch.basic_publish(exchange='',
                        routing_key='HR',
                        properties=pika.BasicProperties(correlation_id = \
                                                            props.correlation_id),
                        body=str(response))
        ch.basic_ack(delivery_tag=method.delivery_tag)
        
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='HR', on_message_callback=hr_request_handle)
    channel.basic_consume(queue='CaptainAmerica', on_message_callback=CaptainAmerica_request_handle)
    
    '''channel.basic_consume(queue='CaptainAmerica', on_message_callback=on_request)
    channel.basic_consume(queue='Thor', on_message_callback=on_request)
    channel.basic_consume(queue='BlackWindow', on_message_callback=on_request)
    channel.basic_consume(queue='Hulk', on_message_callback=on_request)
    channel.basic_consume(queue='Hawkeye', on_message_callback=on_request)'''
    
    #print(" [x] Awaiting RPC requests")
    channel.start_consuming()
    
    
RMQ_SERVER_CLIENT()