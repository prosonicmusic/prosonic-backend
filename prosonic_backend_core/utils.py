from random import randint
from rest_framework.response import Response
from rest_framework import status


def CustomResponse(status_code, errors, message, data, status):
    return Response(
        {
            "status_code": str(status_code),
            "error": errors,
            "data": data,
            "message": message,
        },
        status,
    )


def GenerateResetCode(num):
    start_with = 10 ** (num - 1)
    end_with = (10**num) - 1
    return randint(start_with, end_with)
