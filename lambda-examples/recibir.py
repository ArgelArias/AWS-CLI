import boto3

# Create SQS client
sqs = boto3.client('sqs')

def recibir_mensaje(cola):
# Recibir un mensaje de la cola
 response = sqs.receive_message(
    QueueUrl=cola,
    AttributeNames=[
        'SentTimestamp'
    ],
    MaxNumberOfMessages=1,
    MessageAttributeNames=[
        'All'
    ],
    VisibilityTimeout=0,
    WaitTimeSeconds=0
 )

 message = response['Messages'][0]
 receipt_handle = message['ReceiptHandle']

# Borrar el mensaje que hemos recibido
 sqs.delete_message(
    QueueUrl=cola,
    ReceiptHandle=receipt_handle
 )
 print('El mensaje ha sido recibido y borrado: %s' % message)
