from datetime import datetime
from att.logger import create_logger
from att.logger import exception
from att.config import getConfig
from functools import lru_cache
import re

logger = create_logger()


def toDate(datetime_str, strFormat):
    try:
        datetime_object = datetime.strptime(datetime_str, strFormat)
        return datetime_object.strftime(getConfig("bankstatements","targetDateFormat"))
    except:
        return ""

def toNumber(strNum):
    strNum = removeSpace(strNum)
    strNum = re.sub(r",", "", strNum)
    val = 0
    try:
        val = float(strNum)
    except:
        val=0
        #raise

    return val

def toLowerStr(valCmp):
    if type(valCmp) is str:
        valCmp = valCmp.lower()

    return str(valCmp)

def removeSpace(s):
    s = str(s)
    s = re.sub(r"^\s+|\s+$", "", s)
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"=", "", s)
    s = re.sub(r"\"", "", s)
    return s


def isAmountSame(amount, amount_2):
    if amount<amount_2:
        less_amount = amount
        big_amount = amount_2
    else:
        less_amount = amount_2
        big_amount = amount

    if big_amount < less_amount+5 and big_amount > less_amount - 5:
        return True
    else:
        return False

def isFileExists(strFilePath):
    import os.path
    from os import path

    return path.exists(strFilePath)