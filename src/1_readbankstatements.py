from datetime import datetime
import csv
import sys
import pandas as pd
import logging
import logger
from os import listdir
from os.path import isfile, join
import pyexcel as p
from bankStatementConfig import getBankStatementConfig
from config import getConfig
import re

Sno = 0
dataFilesPath = getConfig("bankstatements", "folderpath")
logging.basicConfig(level=logging.DEBUG)

def processAccountName(accountName, accountNo):
    accountName = accountName.lower()

    if "atin" in accountName:
        accountName = "ATIN KUMAR"
    elif "pooja" in accountName:
        accountName = "POOJA GUPTA"
    elif "girjesh" in accountName:
        accountName = "GIRJESH GUPTA"
    elif "att logics" in accountName:
        accountName = "ATT LOGICS PVT LTD"
    elif "att traders" in accountName:
        accountName = "ATT TRADERS"
    elif "sharad" in accountName:
        accountName = "SHARAD KUMAR GUPTA"
    elif "200008519416" in accountNo:
        accountName = "ATT LOGICS PVT LTD"
    elif "100004509247" in accountNo:
        accountName = "GIRJESH GUPTA"


    return accountName

def toDate(datetime_str, strFormat):
    try:
        datetime_object = datetime.strptime(datetime_str, strFormat)
        return datetime_object.strftime("%d-%b-%Y")
    except:
        return ""


def periodToDates(period):
    period = re.sub(r"From ", "", period)

    periods = period.split(" To ")
    return periods;

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

def removeSpace(s):
    s = str(s)
    s = re.sub(r"^\s+|\s+$", "", s)
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"=", "", s)
    s = re.sub(r"\"", "", s)
    return s

#@logger.logentry
def getCSVFiles():
    files = [join(dataFilesPath, f) for f in listdir(dataFilesPath) if isfile(join(dataFilesPath, f)) and f.endswith(".csv")]

    return files

#@logger.logentry
def getExcelFiles():
    files = [join(dataFilesPath, f) for f in listdir(dataFilesPath) if isfile(join(dataFilesPath, f)) and f.endswith(".xls")]

    return files

#@logger.logentry
def readCSVFiles():
    csvfiles = getCSVFiles()
    
    fields = ['File Name', 'Sno', 'SnoCopied', 'Bank', 'AccountName', 'AccountNo', 'StartDate', 'EndDate','TxnDate','ValueDate','Description',
    'RefNo','AmountDebit','AmountCredit','Balance'] 
    rows = []

    with open(getConfig("bankstatements", "consolidated"), 'w', newline='') as csvfile: 
        csvwriter = csv.writer(csvfile) 
        csvwriter.writerow(fields) 

        for csvfile in csvfiles:
            rows_new = readCSVFile(csvfile)
            #logging.info(rows_new)
            
            rows.extend(rows_new)

        csvwriter.writerows(rows)

            #logging.info("df1: ", df1)

def detectBankName(strFilePath):
    strType = "-"
    strFilePath = strFilePath.upper()
    if "SBI" in strFilePath:
        strType = "sbi"
    if "KMBL" in strFilePath:
        strType = "kmbl"
    if "INDUSIND" in strFilePath:
        strType = "indusind"

    return strType


def getValueFromSheet(bankName, sheet, strLabel, row_ref=0):
    if strLabel == "Amount1":
        logging.info("-------------------Starting getValueFromSheet: " + strLabel)

    strValue = ""
    try:
        if strLabel == "Amount1":
            logging.info(bankName + " : " + strLabel + " : " +  str(row_ref))

        ref_Label = getBankStatementConfig(bankName,strLabel)

        if strLabel == "Amount1":
            logging.info("ref_Label : " + str(ref_Label))

        if ref_Label != "Calc" and ref_Label != "-":
            if row_ref == 0:
                strValue = sheet[ref_Label]
            else:
                ref_Label_C = ref_Label + str(row_ref)
                
                if strLabel == "Amount1":
                    logging.info("ref_Label_C : " + ref_Label_C)
                strValue = sheet[ref_Label_C]

        if strLabel == "Amount1":
            logging.info(strLabel + " : " + str(ref_Label) + " : " + str(strValue))
    except IndexError:
        strValue = ""
        #raise
    except:
        
        print("Unexpected error:", sys.exc_info()[0])
        raise
    finally:
        #logging.info(bankName)
        #logging.info(strLabel)
        #logging.info(row_ref)
        #logging.info(ref_Label)
        pass
        
    return removeSpace(strValue)
    

#@logger.logentry
def readCSVFile(strFilePath):
    global Sno

    logging.info("strFilePath: " + strFilePath)
    
    bankName = detectBankName(strFilePath)
    logging.info("bankName: " + bankName)

    sheet = p.get_sheet(file_name=strFilePath)

    accountNo = "'" + getValueFromSheet(bankName, sheet, "AccountNo")
    accountName = getValueFromSheet(bankName, sheet, "AccountName")
    accountName = processAccountName(accountName, accountNo)
    period = getValueFromSheet(bankName, sheet, "Period")
    periods = periodToDates(period)
    startDate = getValueFromSheet(bankName, sheet, "StartDate")
    endDate = getValueFromSheet(bankName, sheet, "EndDate")
    
    if bankName == "sbi":
        accountNo = re.sub(r"_000000", "", accountNo)

    if period  != "":
        startDate, endDate = periods

    dateFormat = getBankStatementConfig(bankName, "dateFormat")

    header_row = getBankStatementConfig(bankName,"header-row")
    header_row = int(str(header_row))

    rows = []

    i = 1
    sbiSno = 0
    while True:
        row_ref = header_row + i
        SnoCopied = getValueFromSheet(bankName, sheet, "Sno", row_ref)
        TxnDate = getValueFromSheet(bankName, sheet, "TxnDate", row_ref)
        ValueDate = getValueFromSheet(bankName, sheet, "ValueDate", row_ref)
        Description = getValueFromSheet(bankName, sheet, "Description", row_ref)
        RefNo = getValueFromSheet(bankName, sheet, "RefNo", row_ref)
        Amount = toNumber(getValueFromSheet(bankName, sheet, "Amount", row_ref))
        Debit_Credit = getValueFromSheet(bankName, sheet, "Debit_Credit", row_ref)
        AmountDebit = toNumber(getValueFromSheet(bankName, sheet, "AmountDebit", row_ref))
        AmountCredit = toNumber(getValueFromSheet(bankName, sheet, "AmountCredit", row_ref))
        Balance = toNumber(getValueFromSheet(bankName, sheet, "Balance", row_ref))

        if bankName == "sbi":
            sbiSno = sbiSno + 1
            sno_target = sbiSno
        else:
            sno_target = SnoCopied
        


        #if (Description == "" and TxnDate == "") or not (SnoCopied.isnumeric() and SnoCopied != "-" and SnoCopied != ""  and SnoCopied != " " ):
        if (AmountDebit == 0 and AmountCredit == 0 and Balance == 0):
            logging.info("Break...................")
            break

        TxnDate = toDate(TxnDate, dateFormat)
        if ValueDate != "":
            ValueDate = toDate(ValueDate, dateFormat)

        if Debit_Credit == "DR":
            AmountDebit = Amount
            Amount = 0
        if Debit_Credit == "CR":
            AmountCredit = Amount
            Amount = 0

        Sno = Sno + 1
        row = [strFilePath, Sno, sno_target,bankName,accountName, accountNo, startDate, endDate,TxnDate,ValueDate,Description,
RefNo,AmountDebit,AmountCredit,Balance]
        rows.append(row)

        i += 1

    return rows


#print(readCSVFiles())
print(readCSVFiles())