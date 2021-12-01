import json


def SetEmailCode(code):


    with open('Email.json', 'r', encoding='utf-8') as fh:  # открываем файл на чтение
        data = json.load(fh)

        for each in data["Commands"]:
            if each['Command'] == 'type' and each['Target'] == 'name=email_confirmation_code':
                each['Value'] = code
    with open('Email_Ready.json', 'w', encoding='utf-8') as bye:  # открываем файл на запись
        bye.write(json.dumps(data, ensure_ascii=False))



def CreateAccount(username,name,email,password):
    with open('test.json', 'r', encoding='utf-8') as fh:  # открываем файл на чтение
        data = json.load(fh)  # загружаем из файла данные в словарь data

    for each in data["Commands"]:
        if each["Target"] == 'name=emailOrPhone':

            each["Value"] = email
            print(each['Value'])
            each
        elif each["Target"] == "name=fullName":

            each['Value'] = name
            print(each['Value'])
        elif each["Target"] == "name=username":
            each['Value'] = username
        elif each["Target"] == "name=password":
            each['Value'] = password
        elif each['Value'] == 'label=июнь':
            each['Value'] = 'label=август' #сделать генерацию
        elif each['Value'] == "label=15":
            each['Value'] = 'label=23' #сделать генерацию
        elif each['Value'] == 'label=1995':
            each['Value'] = 'label=1991' #сделать генерацию


    with open('NewData2.json', 'w', encoding='utf-8') as bye:  # открываем файл на запись
        bye.write(json.dumps(data, ensure_ascii=False))






CreateAccount("kappa232314231","Kappa Daopa","testasdad23@mail.com","Kappa1337")