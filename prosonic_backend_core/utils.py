from random import randint
from rest_framework.response import Response
from rest_framework import status


def GenerateResetCode(num):
    start_with = 10 ** (num - 1)
    end_with = (10**num) - 1
    return randint(start_with, end_with)


def customResponse(status, message, data, success):
    return Response(
        {
            "success": success,
            "message": message,
            "status": status,
            "data": data,
        }
    )
