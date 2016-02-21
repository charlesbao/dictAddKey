import json
import os
def loadJSON(fileName):
    print 'read %s' % fileName
    fp = open(fileName)
    jsonObj = json.load(fp)
    fp.close()
    return jsonObj

def writeJSON(dict,fileName):
    print 'write'
    print dict['products'][0]['handler_instruction']
    jsonStr = json.dumps(dict, sort_keys=False, indent=2)
    fp = open(fileName,'w')
    fp.write(jsonStr)
    fp.close()

def changeValue(jsonArr,dict):
    i = 0
    for eachArr in jsonArr:
        for each in dict:
            jsonArr[i][each] = dict[each]
        i += 1
    return jsonArr

def getFileList(file):
    if os.path.isdir(file):
        arr = []
        for parent,dirnames,filenames in os.walk(file):
            for each in filenames:
                arr.append(file+'/'+each)
        return arr
    else:
        return file

def init(file,dict,arrKey = None):
    fileList = getFileList(file)
    for each in fileList:
        if each.endswith('.json'):
            jsonObj = loadJSON(each)
            if arrKey == None:
                jsonObj = changeValue(jsonObj,dict)
            else:
                jsonObj[arrKey]= changeValue(jsonObj[arrKey],dict)
            writeJSON(jsonObj,each)
        else:
            print 'pass:%s' % each

fileList = 'moz_designs_addHandler_instruction'
dict = {
    'handler_instruction':'http://mozdesigns.com/spec_library/IMPORTANT_HandlerInstructionsForMozMetals.pdf'
}
init(fileList,dict,'products')
