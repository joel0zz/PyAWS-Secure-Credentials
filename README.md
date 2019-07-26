# PyAWS Secure Credentials

This script will handle retrieving an encrypted(KMS) object from S3 & de-crypting it. This should be used as a secure way to handle
credentials/api keys that need to be used inside scripts.

Please make sure to upload the encrypted txt file containing the credentials or api key to S3 in the following format.

Credentials:
{'user': user, 'pwd': pwd}

API Key:
{'apikey': apikey}

# Installation

pip install git+ssh://git@github.com/joel0zz/aws-cred-handler.git

# Usage

import cred_handler

Retrieve API Key:
cred_handler.get_api_key(bukcet_name, object_name, region)

Retrieve User/Pwd:
cred_handler.get_credentials(bucket_name, object_name, region)


