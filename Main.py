import json_prep
import accGenerate
import email_handle
import pyautogui
'''
1)Запускаем прокси
2)Получаем email от email.py
3)генерируем юзер имя пасс
4)отправляем на регистрацию
5)Ловим ответ с 




'''

username = accGenerate.username()
name = accGenerate.generatingName()
#email = email_handle.getFakeMail()
password = accGenerate.generatePassword()
print(username,password)


#json_prep.CreateAccount(username='kappuchinaxo282',name='Kappa Mappa',email='new_test@910interior.ru',password='2Kappa823!')
#json_prep.SetEmailCode('483992')