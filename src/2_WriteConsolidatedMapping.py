import pandas as pd
import re
from att.logger import exception
from att.logger import create_logger
from att.config import getConfig
from att.crossAccountMapping import dictAcNameDict

logger = create_logger()

@exception(logger)
def getNeedManualReview(row):
    return "NeedManualReview"

@exception(logger)
def getCrossAccountName(row):
    acName = "Suspense"
    for key,val in dictAcNameDict.items():
        #key = r".*" + key + ".*"
        match = re.findall(key, row['DescriptionRefNo'].lower())
        if match:
            acName =  val
        
    return acName

@exception(logger)
def getColumnName(key):
    if "_" in key:
        key_r = key.split("_")[1]
    else:
        key_r = key

    return key_r

@exception(logger)
def getCrossAccountName_v2(row):
    acName = "Suspense"
    my_match = []
    my_v2 = []
    my_label = []
                        
    isLog = True
    if "mr atin kumar sbin0010079" in row["DescriptionRefNo"]:
        logger.info (f"isLog = True : {row['DescriptionRefNo']}")
        isLog = True

    if isLog: logger.info (f"{row}")


    for key,val in dictAcNameDict.items():
        match = False

        if isLog: logger.info (f"1:  {(key, val)}")

        for l_item in val:
            if isLog: logger.info (f"2: {l_item}")

            for k1, v1 in l_item.items():
                if isLog: logger.info (f"3:  {(k1, v1)}")
                column_name = getColumnName(k1)
                for v2 in v1:
                    if isLog:
                        logger.info (f"4:  {v2}")
                        logger.info (f"match: {(v2, row[column_name].lower())}")

                    match = re.findall(v2.lower(), row[column_name].lower())
                    if match:
                        my_match.append(";".join(match))
                        my_v2.append(v2)
                        my_label.append(k1)
                        #match,v2,k1 = [], "", ""

                        if isLog: logger.info("4: There is match. breaking")
                        break;

                if not match:
                    if isLog: logger.info("3: There is nott a match. breaking")
                    break

            if match:
                if isLog: logger.info("2: There is match. breaking")
                break

        if match:
            if isLog: logger.info("1: There is match. returning value")
            acName =  key
            break

    return acName, my_match, my_v2, my_label


@exception(logger)
def getIsContra(row):
    dctContraAccount = {
        "All": ["Cash","Fixed Deposit", "PayTM Withdrawal"],
        "ATT LOGICS PVT LTD": [],
        "ATIN KUMAR": [],
        "POOJA GUPTA": [],
        "GIRJESH GUPTA": [],
        "SHARAD GUPTA": [],
    }

    IsContra = False

    try:
        lstContraAccount = dctContraAccount["All"] + dctContraAccount[row['AccountName']]
    except:
        pass

    if row['CrossAccountName'] in lstContraAccount:
        IsContra = True


    return IsContra

@exception(logger)
def getVoucherType(row):
    strVoucherType = ""
    lstAllowedVoucherTypes = ["Receipt","Payment","Contra","Journal","Purchase",
                              "Sales","Debit Note","Credit Note"]
    if row['IsContra']:
        strVoucherType = "Contra"
    elif row['AmountDebit'] > 0:
        strVoucherType = "Payment"
    elif row['AmountCredit'] > 0:
        strVoucherType = "Receipt"

    return strVoucherType

@exception(logger)
def getIsTransferInFamily(row):
    IsTransferInFamily = False
    dctFamily = {
        "ATT LOGICS PVT LTD": [],
        "ATIN KUMAR": [],
        "POOJA GUPTA": [],
        "GIRJESH GUPTA": [],
        "SHARAD GUPTA": [],
    }

    IsTransferInFamily = False

    lstFamily = dctFamily[row['AccountName']]

    if row['CrossAccountName'] in lstFamily:
        IsTransferInFamily = True

    return IsTransferInFamily

@exception(logger)
def getIsSuspense(row):
    return row['CrossAccountName'] == "Suspense"

@exception(logger)
def getIsTaxRebate(row):
    dctTRAccount = {
        "All": ["LIC",],
        "ATT LOGICS PVT LTD": [],
        "ATIN KUMAR": [],
        "POOJA GUPTA": [],
        "GIRJESH GUPTA": [],
        "SHARAD GUPTA": [],
    }

    IsTaxRebate = False

    lstTRAccount = dctTRAccount["All"] + dctTRAccount[row['AccountName']]

    if row['CrossAccountName'] in lstTRAccount:
        IsTaxRebate = True

    return IsTaxRebate

@exception(logger)
def getAccountBankName(row):
    strAccountBankName = ""
    
    if "atin" in row["AccountName"].lower():
        strAccountBankName = "Atin" + row["Bank"]
    if "pooja" in row["AccountName"].lower():
        strAccountBankName = "Pooja" + row["Bank"]
    if "girjesh" in row["AccountName"].lower():
        strAccountBankName = "Girjesh" + row["Bank"]
    if "200008519416" in row["AccountNo"].lower():
        strAccountBankName = "ATTLogics" + row["Bank"]
    if "100004509247" in row["AccountNo"].lower():
        strAccountBankName = "Girjesh" + row["Bank"]
    
    return strAccountBankName


@exception(logger)
def getAccountName(row):
    strAccountName = row['AccountName']
    
    if "100004509247" in row["AccountNo"].lower():
        strAccountName = "GIRJESH GUPTA"
    if "200008519416" in row["AccountNo"].lower():
        strAccountName = "ATT LOGICS PVT LTD"
    
    return strAccountName



@exception(logger)
def writeConsolidatedMapping(strAccountNameToProcess=""):
    dfBS = pd.read_csv(getConfig("bankstatements", "consolidated"))

    # We need to export the specific account only
    if strAccountNameToProcess != "":
        dfBS = dfBS[dfBS["AccountName"] == strAccountNameToProcess]
        dfBS.reset_index(inplace=True)


    dfBS['CrossAccountName'] = ""
    dfBS['IsContra'] = ""
    dfBS['VoucherType'] = ""
    dfBS['IsTransferInFamily'] = ""
    dfBS['IsSuspense'] = ""
    dfBS['IsTaxRebate'] = ""
    dfBS['AccountBankName'] = ""
    dfBS['Match'] = ""
    dfBS['Pattern'] = ""
    dfBS['Label'] = ""
    
    for i in range(0, len(dfBS)):
        refNo = dfBS.loc[i,'RefNo']

        if not refNo:
            refNo = ""
        elif type(refNo) != str:
            refNo = str(refNo)
        
        dfBS.loc[i,'DescriptionRefNo'] = dfBS.loc[i,'Description'] + " # " + refNo
        dfBS.loc[i,'AccountName'] = getAccountName(dfBS.iloc[i])
        dfBS.loc[i,'AccountBankName'] = getAccountBankName(dfBS.iloc[i])
        dfBS.loc[i,'CrossAccountName'],match,pattern,label = getCrossAccountName_v2(dfBS.iloc[i])
        dfBS.loc[i,'IsContra'] = getIsContra(dfBS.iloc[i])
        dfBS.loc[i,'VoucherType'] = getVoucherType(dfBS.iloc[i])
        dfBS.loc[i,'IsTransferInFamily'] = getIsTransferInFamily(dfBS.iloc[i])
        dfBS.loc[i,'IsSuspense'] = getIsSuspense(dfBS.iloc[i])
        dfBS.loc[i,'IsTaxRebate'] = getIsTaxRebate(dfBS.iloc[i])
        dfBS.loc[i,'Match'] = "\r\n".join(match)
        dfBS.loc[i,'Pattern'] = "\r\n".join(pattern)
        dfBS.loc[i,'Label'] = "\r\n".join(label)
        

    del dfBS["Description"]
    del dfBS["RefNo"]

    dfBS_cols = "AccountName,Bank,AccountBankName,TxnDate,DescriptionRefNo,CrossAccountName,Match,Pattern,Label,AmountDebit,AmountCredit,Balance,IsContra,VoucherType,IsTransferInFamily,IsSuspense,IsTaxRebate".split(",")
    #dfBS_cols_2 = "AccountBankName,TxnDate,DescriptionRefNo,CrossAccountName,Match,Pattern,Label,AmountDebit,AmountCredit".split(",")

    dfBS = dfBS[dfBS_cols]

    dfBS.to_csv(getConfig("bankstatements", "consolidatedMapping"), index = False)

if __name__ == "__main__":
    # Specify which account to be processed. Specify nothing to include all
    strAccountName = "ATT LOGICS PVT LTD"
    writeConsolidatedMapping(strAccountName)