#importing libraries
from langdetect import detect
import pandas as pd 

#take input from user
text = input("Enter Text in Any Language: ")

#printing output

language = print(detect(text))

data_set1 ={
'639-1 Code':['af','sq','ar','bn','bg','ca','zh','hr','cs','da','nl','en','et','fi','fr','de','el','gu','he','hi','hu','id','it','ja','kn','ko','lv','lt','mk','ml','mr','ne','no','fa','pl','pt','pa','ro','ru','sk','sl','so','es','sw','sv','tl','ta','te','th','tr','tw','uk','ur','vi','cy'],
'Language':['Afrikaans','Albanian', 'Arabic' ,'Bengali' ,'Bulgarian','Catalan','Chinese','Croatian','Czech','Danish','Dutch','English','Estonian','Finnish','French','German','Greek','Gujarati','Hebrew','Hindi','Hungarian','Indonesian','Italian','Japanese','Kannada','Korean','Latvian','Lithuanian','Macedonian','Malayalam','Marathi','Nepali','Norwegian','Persian','Polish','Portuguese','Punjabi','Romanian','Russian','Slovak','Slovenian','Somali','Spanish','Swahili','Swedish','Tagalog','Tamil','Telugu','Thai','Turkish','Twi','Ukranian','Urdu','Vietnamese','Welsh']} 
    
df1 = pd.DataFrame(data_set1)

print(df1)






