import pandas as pd
from config import getConfig
import re
from crossAccountMapping import dictAcNameDict

def getNeedManualReview(row):
    return "NeedManualReview"

def getCrossAccountName(row):
    acName = "Suspense"
    for key,val in dictAcNameDict.items():
        #key = r".*" + key + ".*"
        match = re.search(key, row['Description'].lower())
        if match:
            acName =  val
        
    return acName

def getColumnName(key):
    if "_" in key:
        key_r = key.split("_")[1]
    else:
        key_r = key

    return key_r

def getCrossAccountName_v2(row):
    acName = "Suspense"

    isLog = False
    if "SBIN220227778045" in row["Description"]:
        isLog = True
    
    if isLog: print (row)

    
    for key,val in dictAcNameDict.items():
        match = False
    
        if isLog: print ("1: ", (key, val))
        
        for l_item in val:
            if isLog: print ("2: ", l_item)
            
            for k1, v1 in l_item.items():
                if isLog: print ("3: ", (k1, v1))
                column_name = getColumnName(k1)
                for v2 in v1:
                    if isLog:
                        print ("4: ", v2)
                        print ("match: ", (v2, row[column_name].lower()))
                    
                    match = re.search(v2.lower(), row[column_name].lower())
                    if match:
                        if isLog: print("4: There is match. breaking") 
                        break;

                if not match:
                    if isLog: print("3: There is nott a match. breaking") 
                    break

            if match:
                if isLog: print("2: There is match. breaking")
                break
                    
        if match:
            if isLog: print("1: There is match. returning value")
            acName =  key
        
    return acName


def getIsContra(row):
    return "IsContra"

def getVoucherType(row):
    return "VoucherType"

def getIsTransferInFamily(row):
    return "IsTransferInFamily"

def getIsSuspense(row):
    return "IsSuspense"

def getIsTaxRebate(row):
    return "IsTaxRebate"

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


def getAccountName(row):
    strAccountName = row['AccountName']
    
    if "100004509247" in row["AccountNo"].lower():
        strAccountName = "Girjesh Gupta"
    if "200008519416" in row["AccountNo"].lower():
        strAccountName = "ATT Logics Pvt Ltd"
    
    return strAccountName



def writeConsolidatedMapping():
    dfBS = pd.read_csv(getConfig("bankstatements", "consolidated"))

    dfBS['CrossAccountName'] = ""
    dfBS['IsContra'] = ""
    dfBS['VoucherType'] = ""
    dfBS['IsTransferInFamily'] = ""
    dfBS['IsSuspense'] = ""
    dfBS['IsTaxRebate'] = ""
    dfBS['AccountBankName'] = ""
    
    for i in range(0, len(dfBS)):
        dfBS.loc[i,'AccountName'] = getAccountName(dfBS.iloc[i])
        dfBS.loc[i,'AccountBankName'] = getAccountBankName(dfBS.iloc[i])
        dfBS.loc[i,'CrossAccountName'] = getCrossAccountName_v2(dfBS.iloc[i])
        dfBS.loc[i,'IsContra'] = getIsContra(dfBS.iloc[i])
        dfBS.loc[i,'VoucherType'] = getVoucherType(dfBS.iloc[i])
        dfBS.loc[i,'IsTransferInFamily'] = getIsTransferInFamily(dfBS.iloc[i])
        dfBS.loc[i,'IsSuspense'] = getIsSuspense(dfBS.iloc[i])
        dfBS.loc[i,'IsTaxRebate'] = getIsTaxRebate(dfBS.iloc[i])

    print(dfBS.head())
    
    dfBS.to_csv(getConfig("bankstatements", "consolidatedMapping"), index = False)

if __name__ == "__main__":
    writeConsolidatedMapping()