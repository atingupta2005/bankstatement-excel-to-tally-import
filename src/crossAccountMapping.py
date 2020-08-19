# Match And Condition if there is a dictionary
# Match Or Condition if there is a list

dictAcNameDict = {
    "Online Shopping": 
        [   # Match Or Condition for all list items
            { # Match And Condition for all list items
                "1_Description":[r".*amazon.*",r".*google.*",r".*namecheap.*",r".*name-cheap.*",r".*prodigy.*",r".*otbliss.*",r".*vultr.*",r".*udemy.*",r".*mammoth.*",r".*typesy.*",r".*hospital.*",r".*wabox.*",r".*shopclues.*",r".*linux academy.*",r".*PACKTPUBLISHING.*",r".*SALESHANDY.*",r".*/6244/PAYPAL", r".*ROMSONS.IN.*",r".*2CO.com.*sketchman-stud.*", r".*apple.com.*", r".*/collect-pay.*",r".*LinkedIn.*", r".*Agoda.com.*",
                               r".*Medicine.*",r".*Water bottl.*",r".*Cab Bangalo.*",r".*BLOCKCHAIN COURSE.*", r".*Pluralsight.*", r".*/Zoho.*",r".*reliancejio.*", r".*manning.*", r".*PACKTPUBLISHING.*", ".*razorpaypg.*",r".*BLOCKCHAINCOUNCIL.*",
                               r".*payu.*",r".*PL_SERVICES_1.*",r".*ola.*money.*",r".*JIO.*RECHARGE.*",r".*Vodafone.*",r".*airtel.*",
                               r".*INDLOCAL SOLUTIONS.*",r".*uber.*",r".*Times of Money Limited.*",r".*MAKEMYTRIP.*",r".*IIT.*",r".*STAR.*DENTAL.*",
                               r".*Ozonetel.*",],
                "2_Description":[r"^((?!rev).)*$",],
                
            },
        ],
    "PayTM Withdrawal": 
        [
            {
                "Description":[r".*paytm.*",r".*upi/add-money.*"],
            },
        ],    
    "Legal Exp": 
        [
            {
                "Description":[r".*UNIFIC TECHONE.*"],
            },
        ],    
    "NPS": 
        [
            {
                "Description":[r".*nps.*",],
            },
        ],
    "Online Shopping Refund": 
        [
            {
                "1_Description":[r".*refund.*",r".*OSPUECOM.*", r".*PAYU REV.*"],
                "2_Description":[r"^((?!NPS).)*$",],
            },
        ],    
    "Bank Charges": 
        [
            {
                "Description":[r".*amb non maintenance.*", r".*atm.*amc.*", r".*DUPLICATE PASSBOOK.*", r".*Chrg:.*", r".*RETURN CHG-.*", r".*SMS.*CHARGES.*", r".*ACH.*MANDATE.*CHARGES.*",
                               r".*Commission of IMPS.*"],
            },
        ],    
    "Training Delivered": 
        [
            {
                "Description":[r".*koenig.*"],
            },
        ],    
    "Jay Prakash Sewa Sansthan": 
        [
            {
                "Description":[r".*jaiprakash.*",r".*jaypee.*school.*",],
            },
        ],    
    "Bank Interest Received": 
        [
            {
                "Description":[r".*int.pd.*", r".*CREDIT INTEREST.*", r".*Consolidated.*Interest.*Payment.*",],
            },
        ],    
    "Cash Withdrawal": 
        [
            {
                "1_Description":[r".*atm", r".*atm.*",r".*atw/.*",r".*atl/.*"],
                "2_Description":[r"^((?!reverse).)*$"],
                "3_Description":[r"^((?!amc).)*$"],
            },
        ],    
    "Rev Cash Withdrawal": 
        [
            {
                "1_Description":[r".*REVERSE.*",],
                "2_Description":[r".*ATM.*",],
            },
        ],
    "LIC Premium": 
        [
            {
                "Description":[r".*/lic.*", r".*Life Insurance Corpora.*"],
            },
        ],    
    "Rent Paid": 
        [
            {
                "Description":[r".*rent.*", r".*dr shivani.*"],
            },
        ],    
    "Mutual Fund": 
        [
            {
                "Description":[r".*bd-.*", r".*ddr.*", r".*DEBIT-ACHDr.*"],
            },
        ],    
    "Share Bonus Received": 
        [
            {
                "Description":[r".*ecsicr.*"],
            },
        ],    
    "RO Rent AMC Received": 
        [
            {
                "Description":[r".*drvasundhar.*", r".*vipinjindal.*", r".*UPI/vishunagi8-.*", r".*UPI/kumar.atin9.*",
                               r".*simran.*", r".*V V S N S YUGANDARA.*"],
            },
        ],
    "KSPAYOUT Received": 
        [
            {
                "Description":[r".*KSPAYOUT.*"],
            },
        ],
    "Cash": 
        [
            {
                "Description":[r".*CASH DEPOSIT.*"],
            },
        ],
    "Atin SBI": 
        [
            {
                "Description":[r".*ATIN.*",".*9810707414.*",r".*3564.*"],
                "AccountBankName":[r"atinkmbl"],
            },
        ],
    "Sharad SBI": 
        [
            {
                "Description":[r".*sharad.*",],
                "AccountBankName":[r"atinkmbl",r"atinsbi",r"poojasbi",r"girjeshsbi",r"girjeshindusind",],
            },
        ],
    "Atin KMBL": 
        [
            {
                "Description":[r".*ATIN.*",".*9810707414.*",r".*0819.*"],
                "AccountBankName":[r"atinsbi"],
            },
        ],
    "Kotak Securities": 
        [
            {
                "Description":[r".*AR6L0.*"],
                "AccountBankName":[r"atinkmbl"],
            },
        ],
    "ATT Logics Pvt LTD": 
        [
            {
                "Description":[r".*ATT LOGICS.*",],
                "AccountBankName":[r"atinkmbl"],
            },
        ],
    "Director Renumeration": 
        [
            {
                "Description":[r".*Pooja.*",r".*Girjesh.*",],
                "AccountBankName":[r"ATTLogicsindusind"],
            },
        ],
    "Velocis Systems": 
        [
            {
                "Description":[r".*CHEQUE DEPOSIT.*HDFC.*",],
                "AccountBankName":[r"ATTLogicsindusind"],
            },
        ],
    "Cash": 
        [
            {
                "Description":[r".*self.*",],
                "AccountBankName":[r"ATTLogicsindusind"],
            },
        ],
    "ATT Traders": 
        [
            {
                "Description":[r".*att traders.*",r".*9416.*"],
                "AccountBankName":[r"atinkmbl",r"atinsbi"],
            },
        ],
    "Pooja Gupta":
        [
            {
                "Description":[r".*pooja.*", r".*3826.*"],
                "AccountBankName":[r"atinsbi",r"girjeshsbi","atinkmbl"],
            },
        ],    
    "Atin Kumar":
        [
            {
                "Description":[r".*atin.*", r".*3564.*",".*9810707414.*"],
                "AccountBankName":[r"girjeshsbi","poojasbi","attlogicsindusind"],
            },
        ],    
    "Girjesh Gupta":
        [
            {
                "Description":[r".*girjesh.*", r".*8982/.*"],
                "AccountBankName":[r"atinsbi",r"poojasbi",r"atinkmbl"],
            },
        ],    
    "Girjesh Indusind":
        [
            {
                "Description":[r".*girjesh.*", r".*9247/.*"],
                "AccountBankName":[r"girjeshsbi"],
            },
        ],    
    "Girjesh SBI":
        [
            {
                "Description":[r".*girjesh.*", r".*8982/.*"],
                "AccountBankName":[r"girjeshindusind"],
            },
        ],    
    "Salary Received":
        [
            {
                "Description":[r".*ATT LOGICS.*"],
                "AccountBankName":[r"girjeshsbi",r"poojasbi"],
            },
        ],    
    "Training Provided":
        [
            {
                "Description":[r".*BRAIN4CE.*", ".*iiht.*", ".*sfj.*"],
            },
        ],
    "Freelancing Received":
        [
            {
                "Description":[r".*PAYPAL PAYMENTS.*", ".*Freelancing.*"],
            },
        ],
    "Freelancing Paid":
        [
            {
                "Description":[r".*Freelancing.*"],
            },
        ],
    }