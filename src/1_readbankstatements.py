import csv
import sys
import logging
from att.logger import create_logger
from att.logger import exception
from att.utils import toNumber, toDate, removeSpace, isFileExists

from os import listdir
from os.path import isfile, join
import pyexcel as p
from att.bankStatementConfig import getBankStatementConfig
from att.config import getConfig
import re

Sno = 0
dataFilesPath = getConfig("bankstatements", "folderpath")

logger = create_logger()

@exception(logger)
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


@exception(logger)
def periodToDates(period):
    period = re.sub(r"From ", "", period)

    periods = period.split(" To ")
    return periods;



@exception(logger)
def getCSVFiles():
    files = [join(dataFilesPath, f) for f in listdir(dataFilesPath) if isfile(join(dataFilesPath, f)) and f.endswith(".csv")]

    return files

@exception(logger)
def getExcelFiles():
    files = [join(dataFilesPath, f) for f in listdir(dataFilesPath) if isfile(join(dataFilesPath, f)) and f.endswith(".xls")]

    return files

@exception(logger)
def readCSVFiles():
    strFileToWrite = getConfig("bankstatements", "consolidated")
    if isFileExists(strFileToWrite):
        print(f"File {strFileToWrite} already exists.")
        return

    csvfiles = getCSVFiles()
    
    fields = ['File Name', 'Sno', 'SnoCopied', 'Bank', 'AccountName', 'AccountNo', 'StartDate', 'EndDate','TxnDate','ValueDate','Description',
    'RefNo','AmountDebit','AmountCredit','Dr/Cr','Balance']
    rows = []

    with open(strFileToWrite, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile) 
        csvwriter.writerow(fields) 

        for csvfile in csvfiles:
            rows_new = readCSVFile(csvfile)
            #logger.info(rows_new)
            
            rows.extend(rows_new)

        csvwriter.writerows(rows)

            #logger.info("df1: ", df1)

@exception(logger)
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


@exception(logger)
def getValueFromSheet(bankName, sheet, strLabel, row_ref=0):
    if strLabel == "Amount1":
        logger.info("-------------------Starting getValueFromSheet: " + strLabel)

    strValue = ""
    try:
        if strLabel == "Amount1":
            logger.info(bankName + " : " + strLabel + " : " +  str(row_ref))

        ref_Label = getBankStatementConfig(bankName,strLabel)

        if strLabel == "Amount1":
            logger.info("ref_Label : " + str(ref_Label))

        if ref_Label != "Calc" and ref_Label != "-":
            if row_ref == 0:
                strValue = sheet[ref_Label]
            else:
                ref_Label_C = ref_Label + str(row_ref)
                
                if strLabel == "Amount1":
                    logger.info("ref_Label_C : " + ref_Label_C)
                strValue = sheet[ref_Label_C]

        if strLabel == "Amount1":
            logger.info(strLabel + " : " + str(ref_Label) + " : " + str(strValue))
    except IndexError:
        strValue = ""
        #raise
    except:
        
        print("Unexpected error:", sys.exc_info()[0])
        raise
    finally:
        #logger.info(bankName)
        #logger.info(strLabel)
        #logger.info(row_ref)
        #logger.info(ref_Label)
        pass
        
    return removeSpace(strValue)
    

@exception(logger)
def readCSVFile(strFilePath):
    global Sno

    logger.info("strFilePath: " + strFilePath)
    
    bankName = detectBankName(strFilePath)
    logger.info("bankName: " + bankName)

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
        Amount_Orig = toNumber(getValueFromSheet(bankName, sheet, "Amount", row_ref))
        Debit_Credit = getValueFromSheet(bankName, sheet, "Debit_Credit", row_ref)
        AmountDebit = toNumber(getValueFromSheet(bankName, sheet, "AmountDebit", row_ref))
        AmountCredit = toNumber(getValueFromSheet(bankName, sheet, "AmountCredit", row_ref))
        Balance = toNumber(getValueFromSheet(bankName, sheet, "Balance", row_ref))
        Amount = Amount_Orig


        if bankName == "sbi":
            sbiSno = sbiSno + 1
            sno_target = sbiSno
        else:
            sno_target = SnoCopied
        


        #if (Description == "" and TxnDate == "") or not (SnoCopied.isnumeric() and SnoCopied != "-" and SnoCopied != ""  and SnoCopied != " " ):
        if (AmountDebit == 0 and AmountCredit == 0 and Balance == 0):
            logger.info("Break...................")
            break

        TxnDate = toDate(TxnDate, dateFormat)
        if ValueDate != "":
            ValueDate = toDate(ValueDate, dateFormat)

        if Debit_Credit == "DR":
            AmountDebit = Amount
            AmountCredit = 0
        if Debit_Credit == "CR":
            AmountCredit = Amount
            AmountDebit = 0

        if Debit_Credit == "":
            if AmountDebit > 0:
                Debit_Credit = "DR"
            else:
                Debit_Credit = "CR"

        if AmountDebit == 0 and AmountCredit == 0:
            print (Amount)

        Sno = Sno + 1
        row = [strFilePath, Sno, sno_target,bankName,accountName, accountNo, startDate, endDate,TxnDate,ValueDate,Description,
RefNo,AmountDebit,AmountCredit,Debit_Credit,Balance]
        rows.append(row)

        i += 1

    return rows


#print(readCSVFiles())
print(readCSVFiles())