import pandas as pd
import numpy as np
from att.logger import exception
from att.logger import create_logger
from att.utils import isFileExists
import re
from att.config import getConfig
from att.crossAccountMapping import dictAcNameDict
from att.bankStatementConfig import getBankStatementConfig
from att.bankStatementConfig import getBankStatementDict

logger = create_logger()

@exception(logger)
def getBankLedgerName(row):
    if "indusind" in row['Bank'].lower():
        return "Indusind Bank A/c"
    if "sbi" in row['Bank'].lower():
        return "State Bank of India"
    if "kmbl" in row['Bank'].lower():
        return "Kotak Mahindra Bank Limited"
    if "indian" in row['Bank'].lower():
        return "Indian Bank"

@exception(logger)
def getXLToolColumnNames():
    columns = getBankStatementDict("xltool")

    return list(columns.keys())

@exception(logger)
def writeXLToolFile(accountName):
    dfConsolidatedMapping = pd.read_csv(getConfig("bankstatements", "consolidatedMapping"))
    logger.info(f"{dfConsolidatedMapping.columns}")

    dfConsolidatedMapping = dfConsolidatedMapping[dfConsolidatedMapping['AccountName'] == accountName]
    dfConsolidatedMapping.reset_index(inplace=True)

    columns = getXLToolColumnNames()

    dfXLtoolimport = dfConsolidatedMapping

    dfXLtoolimport['DATE'] = dfXLtoolimport['TxnDate']
    dfXLtoolimport = dfXLtoolimport.replace(np.nan, '', regex=True)
    dfXLtoolimport['STANDARD NARRATION'] = dfXLtoolimport['My_Narration'] + " --- " + dfXLtoolimport['DescriptionRefNo']
    dfXLtoolimport['VOUCHER TYPE'] = dfXLtoolimport['VoucherType']
    dfXLtoolimport['AMOUNT'] = dfXLtoolimport['AmountDebit'] + dfXLtoolimport['AmountCredit']
    dfXLtoolimport['LEDGER - BY / DR'] = ""
    dfXLtoolimport['LEDGER - TO / CR'] = ""
    dfXLtoolimport['BILL / INVOICE DATE'] = ""
    dfXLtoolimport['BILL / INVOICE NO'] = ""
    dfXLtoolimport['VOUCHER NO'] = ""
    dfXLtoolimport['CUSTOMISE VOUCHER TYPE'] = ""

    for i in range(0, len(dfXLtoolimport)):
        try:
            strCrossAccountName = dfXLtoolimport.loc[i, 'CrossAccountName']
            amountDebit = dfXLtoolimport.loc[i, 'AmountDebit']
            amountCredit = dfXLtoolimport.loc[i, 'AmountCredit']
        except:
            print ("Errr")
        strBank = dfXLtoolimport.loc[i, 'Bank']
        strBank = getBankLedgerName(dfXLtoolimport.loc[i])

        if amountDebit <= 0:
            dfXLtoolimport.loc[i,'LEDGER - BY / DR'] = strBank
            dfXLtoolimport.loc[i,'LEDGER - TO / CR'] = strCrossAccountName
        else:
            dfXLtoolimport.loc[i,'LEDGER - TO / CR'] = strBank
            dfXLtoolimport.loc[i,'LEDGER - BY / DR'] = strCrossAccountName

    dfXLtoolimport = dfXLtoolimport[columns]

    strFileToWrite = getConfig("bankstatements", "xltoolimportfile")
    if isFileExists(strFileToWrite):
        print(f"File {strFileToWrite} already exists.")
        return

    dfXLtoolimport.to_csv(strFileToWrite, index=False)

if __name__ == "__main__":
    accountName = "POOJA GUPTA"
    writeXLToolFile(accountName)

