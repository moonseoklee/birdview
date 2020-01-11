import json


f = open("ingredient-data.json", 'r',encoding='utf-8')
data = f.read()
data = json.loads(data)
f.close()
f = open("item-data.json", 'r',encoding='utf-8')
data2 = f.read()
data2 = json.loads(data2)
f.close()



dict = {}
for i in data:
    dict[i['name']] = i

for i in data2:
    temp = i['ingredients'].split(',')
    i['price'] =int(i['price'])
    oilyscore,dryscore,sensitivescore = 0,0,0

    for j in temp:
        if dict[j]['oily']=='O':
            oilyscore+=1
        elif dict[j]['oily']=='X':
            oilyscore-=1
        if dict[j]['dry']=='O':
            dryscore+=1
        elif dict[j]['dry']=='X':
            dryscore-=1
        if dict[j]['sensitive']=='O':
            sensitivescore+=1
        elif dict[j]['sensitive']=='X':
            sensitivescore-=1

    i['forOily'] = oilyscore
    i['forDry'] = dryscore
    i['forSensitive'] = sensitivescore
    

f=open("item-data-final.json","w",encoding='utf-8')
temp = ''
for i in data2:
    tt = ''
    i = str(i)
    for j in i:
        if j=="'":
            j = "\""
        tt+=j
    
    temp += "{\"model\": \"item.item\",\"fields\": " + tt +" },"

f.write(temp)