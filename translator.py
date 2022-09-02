#https://dev-gang.ru/article/perevod-teksta-s-pomosczu-google-translate-api-v-python-ahgm88wx1k/

from googletrans import Translator

translator = Translator()
translation_rslt = translator.translate("Der Himmel ist blau und ich mag Bananen", dest='en')
print(f"Ориг. текст буде:  {translation_rslt.origin}")
print(f"Текст після перекладу в нашому випадку буде: {translation_rslt.text}")
print(f"Мова на яку потрібно перекластиє: {translation_rslt.dest}")
print(f"Вимова буде така: {translation_rslt.pronunciation}")


# quotes_file = open(r"C:\Users\alex\PycharmProjects\automation_with_cb\quotes.txt")
# print(quotes_file)
# type(quotes_file)