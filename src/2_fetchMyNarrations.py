import pandas as pd
import re
from att.logger import exception
from att.logger import create_logger
from att.config import getConfig
from att.logger import create_logger
from att.logger import exception
from att.utils import toDate, isFileExists
from att.utils import toNumber
from att.utils import isAmountSame
from att.bankStatementConfig import getBankStatementConfig

logger = create_logger()


myNarrationsFile = getConfig("myDetails", "myNarrationsFile")
consolidatedFile = getConfig("bankstatements", "consolidated")



@exception(logger)
def fetchNarrations():
    dfMyNarrationsFile = pd.read_csv(myNarrationsFile)
    dfConsolidatedFile = pd.read_csv(consolidatedFile)

    dateFormat1 = getConfig("bankstatements", "targetDateFormat")
    dateFormat2 = getConfig("bankstatements", "targetDateFormat")
    dfConsolidatedFile['Dr/ CR'] = ""

    for i in range(0, len(dfConsolidatedFile)):
        txn_Date = dfConsolidatedFile.loc[i, 'TxnDate']
        dfConsolidatedFile.loc[i, 'TxnDate'] = toDate(txn_Date, dateFormat1).lower()

        amountDebit = toNumber(dfConsolidatedFile.loc[i, 'AmountDebit'])
        amountCredit = toNumber(dfConsolidatedFile.loc[i, 'AmountCredit'])
        dfConsolidatedFile.loc[i, 'Amount'] = amountDebit + amountCredit

        if amountDebit > 0:
            dfConsolidatedFile.loc[i, 'Dr/ CR'] = "DR"
        else:
            dfConsolidatedFile.loc[i, 'Dr/ CR'] = "CR"


    for j in range(0, len(dfMyNarrationsFile)):
        txn_Date_2 = dfMyNarrationsFile.loc[j, 'Txn Date']
        dfMyNarrationsFile.loc[j, 'Txn Date'] = toDate(txn_Date_2, dateFormat2).lower()

        amount_2 = toNumber(dfMyNarrationsFile.loc[j, 'Amount'])
        dfMyNarrationsFile.loc[j, 'Amount'] = amount_2

        strAccountBankName_2 = f"{dfMyNarrationsFile.loc[j, 'Initiate Account Bank Name']}"
        dfMyNarrationsFile.loc[j, 'Initiate Account Bank Name'] = strAccountBankName_2.lower()

    dfConsolidatedFile["My_Narration"] = ""
    dfConsolidatedFile["My_Cross Account"] = ""
    dfConsolidatedFile["My_Is Contra?"] = ""
    dfConsolidatedFile["My_Voucher Type"] = ""
    dfConsolidatedFile["My_Suspense?"] = ""
    dfConsolidatedFile["My_Tax Rebate?"] = ""
    dfConsolidatedFile['My Is Matched?'] = ""
    dfConsolidatedFile['CrossMatchesReferences?'] = ""
    dfMyNarrationsFile['My Is Matched?'] = ""
    dfMyNarrationsFile['CrossMatchesReferences?'] = ""

    logger.info(f"Processing {len(dfConsolidatedFile)} Records")
    intMatchCount = 0
    for i in range(0, len(dfConsolidatedFile)):
        if i%100 == 0:
            logger.info(f"Processed {i} Records")

        dfConsolidatedFile.loc[i, 'My Is Matched?'] = False

        txn_Date = dfConsolidatedFile.loc[i,'TxnDate']


        strBank = dfConsolidatedFile.loc[i,'Bank']
        strAccountName = dfConsolidatedFile.loc[i,'AccountName']
        amount = toNumber(dfConsolidatedFile.loc[i,'Amount'])
        StrDrCr = f"{dfConsolidatedFile.loc[i,'Dr/ CR']}".lower()
        strAccountBankName = strAccountName + " " + strBank
        strAccountBankName = strAccountBankName.lower()

        #if amount == 740:
        #    print (dfConsolidatedFile.loc[i,'Description'])


        for j in range(0, len(dfMyNarrationsFile)):
            match = True

            StrDrCr_2 = f"{dfMyNarrationsFile.loc[j, 'Dr/ CR']}".lower()
            txn_Date_2 = f"{dfMyNarrationsFile.loc[j, 'Txn Date']}"

            strAccountBankName_2 = f"{dfMyNarrationsFile.loc[j, 'Initiate Account Bank Name']}"
            amount_2 = dfMyNarrationsFile.loc[j, 'Amount']

            #if amount_2 == 740:
            #    print (dfMyNarrationsFile.loc[j, 'Narration'])

            if txn_Date != txn_Date_2:
                match = False

            if strAccountBankName != strAccountBankName_2:
                match = False

            if not isAmountSame(amount, amount_2):
                match = False

            if match and StrDrCr != StrDrCr:
                print (StrDrCr, StrDrCr)

            if StrDrCr != StrDrCr_2:
               match = False

            if match:
                intMatchCount += 1
                dfConsolidatedFile.loc[i, 'My_Narration'] = dfMyNarrationsFile.loc[j, 'Narration']
                dfConsolidatedFile.loc[i, 'My_Cross Account'] = dfMyNarrationsFile.loc[j, 'Cross Account']
                dfConsolidatedFile.loc[i, 'My_Is Contra?'] = dfMyNarrationsFile.loc[j, 'Is Contra?']
                dfConsolidatedFile.loc[i, 'My_Voucher Type'] = dfMyNarrationsFile.loc[j, 'Voucher Type']
                dfConsolidatedFile.loc[i, 'My_Suspense?'] = dfMyNarrationsFile.loc[j, 'Suspense?']
                dfConsolidatedFile.loc[i, 'My_Tax Rebate?'] = dfMyNarrationsFile.loc[j, 'Tax Rebate?']
                dfConsolidatedFile.loc[i, 'My Is Matched?'] = match

                if dfConsolidatedFile.loc[i, 'CrossMatchesReferences?'] == "":
                    dfConsolidatedFile.loc[i, 'CrossMatchesReferences?'] = str(dfMyNarrationsFile.loc[j, 'Sno'])
                else:
                    dfConsolidatedFile.loc[i, 'CrossMatchesReferences?'] = dfConsolidatedFile.loc[i, 'CrossMatchesReferences?'] + ", " + str(dfMyNarrationsFile.loc[j, 'Sno'])

                if dfMyNarrationsFile.loc[j, 'CrossMatchesReferences?'] == "":
                    dfMyNarrationsFile.loc[j, 'CrossMatchesReferences?'] = str(dfConsolidatedFile.loc[i, 'Sno'])
                else:
                    dfMyNarrationsFile.loc[j, 'CrossMatchesReferences?'] = dfMyNarrationsFile.loc[j, 'CrossMatchesReferences?'] + ", " + str(dfConsolidatedFile.loc[i, 'Sno'])


                #break

    logger.info(f"Total Matched:  {intMatchCount}")

    strFileToWrite = getConfig("bankstatements", "consolidated_myNarration")
    if isFileExists(strFileToWrite):
        print(f"File {strFileToWrite} already exists.")
        return

    dfConsolidatedFile.to_csv(strFileToWrite, index=False)
    dfMyNarrationsFile.to_csv(getConfig("myDetails", "myNarrationsFile_updated_matched"), index=False)

if __name__ == "__main__":
    fetchNarrations()