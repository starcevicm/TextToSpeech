import pysndfile
import numpy as np

inputText = input("Enter an input sentence: ")
inputWords = inputText.split() #razdvaja riječi i sprema u words
outputFile = './sentences/' + inputText #ime izlazne datoteke
sentenceObject = pysndfile.PySndfile(outputFile,'rw',pysndfile.construct_format('wav', 'float64'),1,16000) #kreira novu datoteku u koju će zapisivati(format se mora proslijediti u obliku integera koji kreira funkcija construct_format iz stringova koji joj se zadaju)

#za svaku riječ iz ulazne rečenice
for word in inputWords:
    wordFilePath = './words/' + word #pronađe riječ u bazi
    wordObject = pysndfile.PySndfile(wordFilePath) #stvara objekt iz trenutne riječi
    wordData = wordObject.read_frames() #čita i privremeno pohranjuje data iz objekta
    sentenceObject.write_frames(wordData) #zapisuje gore pohranjene podatke na kraj izlazne datoteke
    

