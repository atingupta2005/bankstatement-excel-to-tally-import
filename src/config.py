import yaml
import json

file = open('./config.yaml', 'r')
cfg = yaml.load(file, Loader=yaml.FullLoader)

def getConfig(strLabel, *labels):
    strVal = cfg.get(strLabel,"")
    i = 0
    while type(strVal) is dict:
        print (strVal)
        strVal = strVal.get(labels[i],"")
        i += 1

    return strVal

if __name__=="__main__":
    print(getConfig("bankstatements", "folderpath"))