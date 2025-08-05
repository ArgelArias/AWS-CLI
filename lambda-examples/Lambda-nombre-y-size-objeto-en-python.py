import json
import urllib.parse
import boto3

print('Loading function')

s3 = boto3.client('s3')


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))

    # Recuperar el objeto y ver su content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    try:
        respuesta = s3.get_object(Bucket=bucket, Key=key)
        print("Nombre del objeto:"+key)
        print("Tamaño: " + str(respuesta['ContentLength']))
        return "El objeto "+key+ "tiene un tamaño de -->"+str(respuesta['ContentLength'])+" Bytes"
    except Exception as e:
        print(e)
        print('Error al recuperar el objeto  {} del bucket {}. Comprueba que existe y que se encuentra en la misma region.'.format(key, bucket))
        raise e