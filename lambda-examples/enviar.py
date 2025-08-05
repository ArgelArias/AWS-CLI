import boto3

# Crear un cliente SQS
sqs = boto3.client('sqs')


# Enviar una mensaje a una cola SQS 
def mandar_mensaje(cola,cuerpo,nombre,apellidos):
 response = sqs.send_message(
     QueueUrl=cola,
     DelaySeconds=10,
     MessageAttributes={
        'nombre': {
            'DataType': 'String',
            'StringValue': nombre 
        },
        'apellidos': {
            'DataType': 'String',
            'StringValue': apellidos 
        }
     },
     MessageBody=cuerpo
 ) 

 print(response['MessageId'])
