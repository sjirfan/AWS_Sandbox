#code to download data from s3 to local machine.
#note the list ie newdata can be uploaded with file names as a result of scanning sqs queues
newdata = ['cv001_19502.txt']

import boto3
import urllib
import requests
s3 = boto3.client('s3', region_name='eu-central-1')

def download_data_object(newdata):
        for i in newdata:
                url = "https://simplibucketimp.s3.eu-central-1.amazonaws.com/" + i
                urllib.request.urlretrieve(url,i)

download_data_object(newdata)