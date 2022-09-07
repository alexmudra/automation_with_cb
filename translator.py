#https://dev-gang.ru/article/perevod-teksta-s-pomosczu-google-translate-api-v-python-ahgm88wx1k/
from googletrans import Translator

translator = Translator()
translation_rslt = translator.translate("Der Himmel ist blau und ich mag Bananen", dest='en')
print(f"Ориг. текст буде:  {translation_rslt.origin}")
print(f"Текст після перекладу в нашому випадку буде: {translation_rslt.text}")
print(f"Мова на яку потрібно перекластиє: {translation_rslt.dest}")
print(f"Вимова буде така: {translation_rslt.pronunciation}")

##############################
transl_phrase ="Привіт світ"
translation_rslt_to_ukr = translator.translate(transl_phrase, src='uk',dest='en')
print(f"фраза/слово uk: {transl_phrase} -> переклад на en: {translation_rslt_to_ukr.text}") #фраза/слово uk: Привіт світ -> переклад на en: Hi world
##############################
#переклад сліів/фраз із списку
uk_phrases = ['закупівлі', 'допорогова закупівля', 'учасник', 'номер тендера']
tran_ukr_phrs_rslt_to_en = translator.translate(uk_phrases, src='uk', dest='en')
for trnsl in tran_ukr_phrs_rslt_to_en:
    print(trnsl.text)










# quotes_file = open(r"C:\Users\alex\PycharmProjects\automation_with_cb\quotes.txt")
# print(quotes_file)
# type(quotes_file)