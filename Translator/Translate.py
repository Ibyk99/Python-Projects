# import required materials
import boto3
from Language_list import language_list 
from tabulate import tabulate

client = boto3.client('translate')

# introductory message
print(" ")
print("Hello! Welcome to my simple translator app, this has been made using Amazon Translate!")
print(" ")
print("Below are listed the supported languages and their associated codes: ")
print(tabulate(language_list, headers=["Language", "Language Code"], tablefmt="fancy_grid"))


# inputs - what we want to translate, the source language, the target language
user_input = input("Please type the text that you would like to be translated:  ")
print(" ")
sourcelang = input("Please type the language code of the source language (leave blank for auto-language detection): ") or "auto"
print(" ")
targetlang = input("Please type the language code of the target language: ")



# translation function - takes our inputs and uses AWS translate to return our translated text
def translation_function (user_input, sourcelang, targetlang):
    translation = client.translate_text( Text = user_input, SourceLanguageCode = sourcelang, TargetLanguageCode = targetlang)
    return translation['TranslatedText']

#print the output
print(" ")
print("Your translated text is" + ": " + translation_function(user_input, sourcelang, targetlang))
print(" ")
