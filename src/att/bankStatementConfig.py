import yaml

file = open('resources/bankstatements-format.yaml', 'r')
cfg = yaml.load(file, Loader=yaml.FullLoader)

def getBankStatementDict(strKey):
    return cfg.get(strKey, "")


def getBankStatementConfig(strLabel, *labels):
    strVal = cfg.get(strLabel,"")
    i = 0
    while type(strVal) is dict:
        strVal = strVal.get(labels[i],"")
        i += 1

    return strVal

if __name__=="__main__":
    print(getBankStatementConfig("sbi", "RefNo"))