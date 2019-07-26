import boto3
import json
import base64


def get_auth(bucket_name, object_name):
    encrypted_obj = get_obj_from_s3(bucket_name, object_name)
    secret = decrypt_object(encrypted_obj)
    auth_token = secret['apikey']
    return auth_token


def get_obj_from_s3(bucket, file):
    client = boto3.client('s3')
    obj = client.get_object(Bucket=bucket, Key=file)
    response = obj['Body'].read()
    return response


def decrypt_object(obj):
    client = boto3.client('kms', region_name='ap-southeast-2')
    binary_data = base64.b64decode(obj)
    meta = client.decrypt(CiphertextBlob=binary_data)
    plaintext = meta[u'Plaintext']
    secret_dict = json.loads(plaintext.decode())
    return secret_dict


