import pandas as pd
from config import getConfig
import re
from crossAccountMapping import dictAcNameDict
from bankStatementConfig import getBankStatementConfig
from bankStatementConfig import getBankStatementDict

def getBankLedgerName(row):
    if "indusind" in row['Bank'].lower():
        return "Indusind Bank A/c"

def getXLToolColumnNames():
    columns = getBankStatementDict("xltool")

    return list(columns.keys())

def writeXLToolFile(accountName):
    dfConsolidatedMapping = pd.read_csv(getConfig("bankstatements", "consolidatedMapping"))
    print(dfConsolidatedMapping.columns)

    dfConsolidatedMapping = dfConsolidatedMapping[dfConsolidatedMapping['AccountName'] == accountName]

    columns = getXLToolColumnNames()

    dfXLtoolimport = dfConsolidatedMapping

    dfXLtoolimport['DATE'] = dfXLtoolimport['TxnDate']
    dfXLtoolimport['STANDARD NARRATION'] = dfXLtoolimport['DescriptionRefNo']
    dfXLtoolimport['VOUCHER TYPE'] = dfXLtoolimport['VoucherType']
    dfXLtoolimport['AMOUNT'] = dfXLtoolimport['AmountDebit'] + dfXLtoolimport['AmountCredit']
    dfXLtoolimport['LEDGER - BY / DR'] = ""
    dfXLtoolimport['LEDGER - TO / CR'] = ""
    dfXLtoolimport['BILL / INVOICE DATE'] = ""
    dfXLtoolimport['BILL / INVOICE NO'] = ""
    dfXLtoolimport['VOUCHER NO'] = ""
    dfXLtoolimport['CUSTOMISE VOUCHER TYPE'] = ""

    for i in range(0, len(dfXLtoolimport)):
        strCrossAccountName = dfXLtoolimport.loc[i,'CrossAccountName']
        amountDebit = dfXLtoolimport.loc[i, 'AmountDebit']
        amountCredit = dfXLtoolimport.loc[i, 'AmountCredit']
        strBank = dfXLtoolimport.loc[i, 'Bank']
        strBank = getBankLedgerName(dfXLtoolimport.loc[i])

        if amountDebit < 0:
            dfXLtoolimport.loc[i,'LEDGER - BY / DR'] = strBank
            dfXLtoolimport.loc[i,'LEDGER - TO / CR'] = strCrossAccountName
        else:
            dfXLtoolimport.loc[i,'LEDGER - TO / CR'] = strBank
            dfXLtoolimport.loc[i,'LEDGER - BY / DR'] = strCrossAccountName

    dfXLtoolimport = dfXLtoolimport[columns]
    dfXLtoolimport.to_csv(getConfig("bankstatements", "xltoolimportfile"), index=False)

if __name__ == "__main__":
    accountName = "ATT LOGICS PVT LTD"
    writeXLToolFile(accountName)

