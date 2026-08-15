from process_data import read_csv_data_file, process_csv_file
from exception_handling_utility import try_except_decorator
import json
from loguru import logger
import boto3
import io

@try_except_decorator
def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    logger.info(f"Bucket: {bucket}")
    logger.info(f"Key: {key}")
    logger.info(event)
    logger.info(context)

    s3 = boto3.client("s3")
    response = s3.get_object(Bucket=bucket, Key=key)
    logger.info(f"get_object response is {response}")

    with io.TextIOWrapper(response['Body'], encoding='utf-8') as file:
        df = read_csv_data_file(file)
        result = process_csv_file(df)

    logger.info(f"Result is: {result}")

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "Data processed successfully",
                "bucket": bucket,
                "file": key
            }
        )
    }