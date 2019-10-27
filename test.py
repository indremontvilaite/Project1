from googletrans import Translator
translator = Translator()
print(translator.translate('prego', dest='lt', src='it'))
