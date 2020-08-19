import collections

# Match And Condition if there is a dictionary
# Match Or Condition if there is a list

dictAcNameDict = collections.OrderedDict()

dictAcNameDict = {
    "Online Shopping": 
        [   # Match Or Condition for all list items
            { # Match And Condition for all list items
                "1_DescriptionRefNo":[r".*amazon.*",r".*shopclues.*",r".*/6244/PAYPAL", r".*ROMSONS.IN.*",r".*2CO.com.*sketchman-stud.*", 
                    r".*apple.com.*", ".*razorpaypg.*",r".*collect-pay.*",r".*PL_SERVICES_1.*",
                    r".*INDLOCAL SOLUTIONS.*",r".*Times of Money Limited.*", r".*Flipkart.*"],
                "2_DescriptionRefNo":[r"^((?!rev).)*$",],
                
            },
        ],
        
        "Kitchen LPG Subsidy": 
        [   # Match Or Condition for all list items
            { # Match And Condition for all list items
                "1_DescriptionRefNo":[r".*ioc.*ref.*no.*"],
                "2_DescriptionRefNo":[r"^((?!rev).)*$",],
                
            },
        ],
        
        "Government Document Exp": 
        [
            {
                "1_DescriptionRefNo":[r".*passport.*",],
                "2_DescriptionRefNo":[r"^((?!rev).)*$",],
                
            },
        ],
        
    
    "Training Delivery Exp": 
        [
            {
                "1_DescriptionRefNo":[r".*udemy.*",
                    r".*linux academy.*",
                    r".*PACKTPUBLISHING.*",
                    r".*LinkedIn.*",
                    r".*BLOCKCHAIN COURSE.*",
                    r".*BLOCKCHAINCOUNCIL.*",
                    r".*Pluralsight.*",
                    r".*manning.*",
                    r".*IIT.*",
                    r".*Flight.*Tickets.*",r".*E2E.*Networks.*",],
                "2_DescriptionRefNo":[r"^((?!rev).)*$",],
                
            },
        ],
    
    "Self Learning Exp": 
        [
            {
                "1_DescriptionRefNo":[
                    r".*google.*",
                    r".*namecheap.*",
                    r".*name-cheap.*",
                    r".*vultr.*",
                    r".*wabox.*",
                    r".*SALESHANDY.*",
                    r".*Agoda.com.*",
                    r".*Water bottl.*",
                    r".*Cab Bangalo.*",
                    r".*Zoho.*",
                    r".*ola.*money.*",
                    r".*uber.*",
                    r".*MAKEMYTRIP.*",
                    r".*Ozonetel.*",
                    r".*hotel.*", r".*HOTAL.*"
                    ],
                "2_DescriptionRefNo":[r"^((?!rev).)*$",],
                
            },
        ],

    "Mobile RECHARGE": 
        [
            {
                "1_DescriptionRefNo":[
                    r".*reliancejio.*",
                    r".*JIO.*RECHARGE.*",
                    r".*Vodafone.*",
                    r".*airtel.*",
                    ],
                "2_DescriptionRefNo":[r"^((?!rev).)*$",],
                
            },
        ],

    "Medical Exp": 
        [
            {
                "1_DescriptionRefNo":[
                    r".*otbliss.*",
                    r".*hospital.*",
                    r".*Medicine.*",
                    r".*STAR.*DENTAL.*",
                    ],
                "2_DescriptionRefNo":[r"^((?!rev).)*$",],
                
            },
        ],

    "Kids Education Exp": 
        [
            {
                "1_DescriptionRefNo":[
                    r".*prodigy.*",
                    r".*mammoth.*",
                    r".*typesy.*",
                    ],
                "2_DescriptionRefNo":[r"^((?!rev).)*$",],
                
            },
        ],

    "Electricity Bill Exp": 
        [
            {
                "DescriptionRefNo":[r".*uppcl.*"],
            },
        ],            
    "PayTM Withdrawal": 
        [
            {
                "DescriptionRefNo":[r".*paytm.*",r".*upi/add-money.*"],
            },
        ],    
    "Legal Exp": 
        [
            {
                "DescriptionRefNo":[r".*UNIFIC TECHONE.*"],
            },
        ],    
    "NPS": 
        [
            {
                "DescriptionRefNo":[r".*nps.*",],
            },
        ],
    "Online Shopping Refund": 
        [
            {
                "1_DescriptionRefNo":[r".*refund.*",r".*OSPUECOM.*", r".*PAYU REV.*"],
                "2_DescriptionRefNo":[r"^((?!NPS).)*$",],
            },
        ],    
    "Bank Charges": 
        [
            {
                "DescriptionRefNo":[r".*amb non maintenance.*", r".*atm.*amc.*", r".*DUPLICATE PASSBOOK.*", r".*Chrg:.*", r".*RETURN CHG-.*", r".*SMS.*CHARGES.*", r".*ACH.*MANDATE.*CHARGES.*",
                               r".*Commission of IMPS.*"],
            },
        ],    
    "Training Delivered": 
        [
            {
                "DescriptionRefNo":[r".*koenig.*"],
            },
        ],    
    "Jay Prakash Sewa Sansthan": 
        [
            {
                "DescriptionRefNo":[r".*jaiprakash.*",r".*jaypee.*school.*",],
            },
        ],    
    "Bank Interest Received": 
        [
            {
                "DescriptionRefNo":[r".*int.pd.*", r".*CREDIT INTEREST.*", r".*Consolidated.*Interest.*Payment.*",],
            },
        ],    
    "Cash Withdrawal": 
        [
            {
                "1_DescriptionRefNo":[r".*atm", r".*atm.*",r".*atw/.*",r".*atl/.*"],
                "2_DescriptionRefNo":[r"^((?!reverse).)*$"],
                "3_DescriptionRefNo":[r"^((?!amc).)*$"],
            },
        ],    
    "Rev Cash Withdrawal": 
        [
            {
                "1_DescriptionRefNo":[r".*REVERSE.*",],
                "2_DescriptionRefNo":[r".*ATM.*",],
            },
        ],
    "LIC Premium": 
        [
            {
                "DescriptionRefNo":[r".*/lic.*", r".*Life Insurance Corpora.*"],
            },
        ],
    "Office Rent":
        [
            {
                "DescriptionRefNo":[r".*rent.*", r".*dr shivani.*",
                r".*26400100004509.*", r".*26400100014027.*", r".*barb.*shivani.*"],
            },
        ],
    "Mutual Fund": 
        [
            {
                "DescriptionRefNo":[r".*bd-.*", r".*ddr.*", r".*DEBIT-ACHDr.*"],
            },
        ],    
    "Share Bonus Received": 
        [
            {
                "DescriptionRefNo":[r".*ecsicr.*"],
            },
        ],    
    "RO Rent AMC Received": 
        [
            {
                "DescriptionRefNo":[r".*drvasundhar.*", r".*vipinjindal.*", r".*UPI/vishunagi8-.*", r".*UPI/kumar.atin9.*",
                               r".*simran.*", r".*V V S N S YUGANDARA.*", r".*Payment fro.*",
                               r".*ro.*amc.*",],
            },
        ],
    "KSPAYOUT Received": 
        [
            {
                "DescriptionRefNo":[r".*KSPAYOUT.*"],
            },
        ],
    "Cash": 
        [
            {
                "DescriptionRefNo":[r".*CASH DEPOSIT.*"],
            },
        ],
    "Atin SBI": 
        [
            {
                "DescriptionRefNo":[r".*ATIN.*",".*9810707414.*",r".*3564.*"],
                "AccountBankName":[r"atinkmbl"],
            },
        ],
    "Sharad SBI": 
        [
            {
                "DescriptionRefNo":[r".*sharad.*",],
                "AccountBankName":[r"atinkmbl",r"atinsbi",r"poojasbi",r"girjeshsbi",r"girjeshindusind",],
            },
        ],
    "Atin KMBL": 
        [
            {
                "DescriptionRefNo":[r".*ATIN.*",".*9810707414.*",r".*0819.*"],
                "AccountBankName":[r"atinsbi"],
            },
        ],
    "Kotak Securities": 
        [
            {
                "DescriptionRefNo":[r".*AR6L0.*"],
                "AccountBankName":[r"atinkmbl"],
            },
        ],
    "ATT Logics Pvt LTD": 
        [
            {
                "DescriptionRefNo":[r".*ATT LOGICS.*",],
                "AccountBankName":[r"atinkmbl",r"atinsbi"],
            },
        ],
    "Director Remuneration Girjesh Gupta":
        [
            {
                "DescriptionRefNo":[r".*Girjesh.*", r".*8982.*", r".*4509247.*"],
                "AccountBankName":[r"ATTLogicsindusind"],
            },
        ],
    "Director Remuneration Pooja Gupta":
        [
            {
                "DescriptionRefNo":[r".*Pooja.*", r".*3826.*"],
                "AccountBankName":[r"ATTLogicsindusind"],
            },
        ],
    "Velocis Systems":
        [
            {
                "DescriptionRefNo":[r".*CHEQUE DEPOSIT.*HDFC.*", r".*velocis.*"],
                "AccountBankName":[r"ATTLogicsindusind"],
            },
        ],
    "Fixed Deposit": 
        [
            {
                "DescriptionRefNo":[r".*FD A/c.*",],
            },
        ],
    "Cash":
        [
            {
                "DescriptionRefNo":[r".*self.*",],
                "AccountBankName":[r"ATTLogicsindusind"],
            },
        ],
    "ATT Traders": 
        [
            {
                "DescriptionRefNo":[r".*att traders.*",r".*9416.*"],
                "AccountBankName":[r"atinkmbl",r"atinsbi"],
            },
        ],
    "Pooja Gupta":
        [
            {
                "DescriptionRefNo":[r".*pooja.*", r".*3826.*"],
                "AccountBankName":[r"atinsbi",r"girjeshsbi","atinkmbl"],
            },
        ],    
    "Atin Gupta":
        [
            {
                "DescriptionRefNo":[r".*atin.*", r".*3564.*",".*9810707414.*", r".*0819.*",],
                "AccountBankName":[r"girjeshsbi",r"girjeshindusind","poojasbi","attlogicsindusind"],
            },
        ],    
    "Girjesh Gupta":
        [
            {
                "DescriptionRefNo":[r".*girjesh.*", r".*8982/.*"],
                "AccountBankName":[r"atinsbi",r"poojasbi",r"atinkmbl"],
            },
        ],    
    "Girjesh Indusind":
        [
            {
                "DescriptionRefNo":[r".*girjesh.*", r".*9247/.*"],
                "AccountBankName":[r"girjeshsbi"],
            },
        ],    
    "Girjesh SBI":
        [
            {
                "DescriptionRefNo":[r".*girjesh.*", r".*8982/.*"],
                "AccountBankName":[r"girjeshindusind"],
            },
        ],    
    "Salary Received":
        [
            {
                "DescriptionRefNo":[r".*ATT LOGICS.*", r".*200008519416.*", r".*DIRECTOR REMUNR.*"],
                "AccountBankName":[r"girjeshsbi",r"girjeshindusind",r"poojasbi"],
            },
        ],    
    "Training Provided":
        [
            {
                "DescriptionRefNo":[r".*BRAIN4CE.*", ".*iiht.*", ".*sfj.*", r".*TAI INFOTECH.*"],
            },
        ],
    "Freelancing Received":
        [
            {
                "DescriptionRefNo":[r".*PAYPAL PAYMENTS.*", ".*Freelancing.*"],
            },
        ],
    "Freelancing Paid":
        [
            {
                "DescriptionRefNo":[r".*Freelancing.*"],
            },
        ],        
    }



def populateDictAcNameDict(dictAcNameDict, dickKey , lstVals):
    dctNew = collections.OrderedDict()

    dctNew = {"DescriptionRefNo": []}
    for val in lstVals:
        dctNew["DescriptionRefNo"].append(r".*" + val + ".*")

    for val in lstVals:
        dctNew["DescriptionRefNo"].append(r".*" + val[-8::] + ".*")

    for val in lstVals:
        dctNew["DescriptionRefNo"].append(r".*" + val[-6::] + ".*")


    dictAcNameDict[dickKey] = [dctNew]
    
    return dictAcNameDict


strVals = "10180118,10184664,10408385,10889039,18833575,20097219,72190201,79438736,83036128," \
          "117882716,172019159,184943560,185174217,1911660819,3203601614,4211692078,6394948043," \
          "7111683696,9350980414,9654577826,9654577827,9665718639,9810707414,9990256123,30254443564," \
          "30793793105,85538430859,100004509247,100008377484,100008430196,110124505306,110164377159," \
          "200008519416,191102000020703,191102000021766,191104000173810,191104000284295,191675100044280," \
          "200107000030117,307502010463469,307503020140245,4213240312191650,4213240602874190," \
          "4213240605342910,4213683075013600,4587771910152500,191PPF00000000000410,191PPF00000000000426," \
          "AHNPK3502D,AR6L0,Arnav,Arshiya,ATI82_7,Atin,E79994,Girjesh,IBKL0000191,INDB0000049,INDB0000162," \
          "KKBK0005030,Pooja,SBIN0008110,SBIN0010079,SBIN0011469,Sharad,TDW3156487"
lstVals = strVals.split(",")
dictAcNameDict = populateDictAcNameDict(dictAcNameDict, "Suspense2", lstVals)