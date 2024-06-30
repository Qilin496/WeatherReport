import requests
from datetime import datetime

import boto3

END_POINT = "https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={API_key}"
# END_POINT = "https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}"
TABLE_NAME = "Weather_Info"

def registDynamoDB(itemDict):
    dynamodb = boto3.client("dynamodb")
    dynamodb.put_item(TableName=TABLE_NAME, Item=itemDict)


def getWetherInfo(cityName):
    url = END_POINT.format(city_name = cityName, API_key = "1a2c980345fe720e6420db88ac985abd")

    response = requests.get(url).json()
    dateTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

    return response, dateTime


def main():
    try:
        cityName = "Tokyo"

        wetherData, getTime = getWetherInfo(cityName)
        itemDict = {
            "City": {"S": cityName},
            "Timestamp": {"S": getTime},
            "Tempture": {"S": str(wetherData["main"]["temp"])},
            "Humid": {"S": str(wetherData["main"]["humidity"])}
        }
        registDynamoDB(itemDict)
    except:
        raise

def lambda_handler(event, context):
    # ログを出力する
    print("event:",event)
    print("context:",context)
    main()