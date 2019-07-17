import pysndfile
import glob
import wave
import numpy as np

wavFiles = glob.glob('./soundFiles/wav/*.wav') #sprema nazive svih wav datoteka u VEPRAD bazi podataka


labFolder = './soundFiles/lab/'
txtFolder = './soundFiles/txt/'
wordsFolder = './words/'

filesConverted = 0
filesToConvert = len(wavFiles)

for wavFilePath in wavFiles:
    
    print(wavFilePath)
    wavObject = pysndfile.PySndfile(wavFilePath) #stvara pysndfile objekt
    sampleRate = wavObject.samplerate() #sprema sample rate objekta
    
    labFilePath = labFolder + wavFilePath.split('/')[-1].split('.')[0] + '.lab' #reze path wav datoteke kako bi dosao do naziva datoteke, te joj mijenja ekstenziju u lab
    txtFilePath = txtFolder + wavFilePath.split('/')[-1].split('.')[0] + '.txt' #reze path wav datoteke kako bi dosao do naziva datoteke, te joj mijenja ekstenziju u txt
    
    textFile = open(txtFilePath, 'r') #otvara txt datoteku
    labFile = open(labFilePath, 'r') #otvara lab datoteku
    text = textFile.readlines() #cita sadrzaj txt datoteke
    lab = labFile.readlines() #cita sadrzaj lab datoteke
    
    letterCounter = 0 #prati na kojem je slovu
    wordCounter = 0 #broji koliko je rijeci obradeno
    
    #razdvaja sadrzaj kod svakog razmaka i sprema u "words"
    for line in text: 
        words = line.split() 
        
    for word in words:
        wordLength = len(word)
        #posebni slucajevi gdje se dva slova iz txt tretiraju kao jedno u lab
        if 'nj' in word:
            wordLength-=1
        if 'lj' in word:
            wordLength-=1
        if 'ds' in word:
            wordLength-=1
        if 'ts' in word:
            wordLength-=1
        if 'jedanaest' in word:
            wordLength-=1
        if 'dvanaest' in word:
            wordLength-=1
        if 'trinaest' in word:
            wordLength-=1
        if '~etrnaest' in word:
            wordLength-=1
        if 'petnaest' in word:
            wordLength-=1
        if '{esnaest' in word:
            wordLength-=1
        if 'sedamnaest' in word:
            wordLength-=1
        if 'osamnaest' in word:
            wordLength-=1
        if 'devetnaest' in word:
            wordLength-=1
        if 'ije' in word:
            wordLength-=1
        if '~etiri' in word:
            wordLength-=1
        if 'lij' in word:
            wordLength-=1
           
       
            
        destinationFile = wordsFolder + word #daje ime datoteci koju će stvoriti
        
        #mijenja simbole u hrvatske znakove
        destinationFile = destinationFile.replace('`','ž') 
        destinationFile = destinationFile.replace('{','š')
        destinationFile = destinationFile.replace('~','č')
        destinationFile = destinationFile.replace('^','ć')
        destinationFile = destinationFile.replace('#','dž') 
        destinationFile = destinationFile.replace('}','đ')
        
        
        letter = lab[letterCounter].split()[2] #sprema trenutno slovo
        #ako je trenutno slovo "sil", "greska", "buka" ili "uzdah" preskace liniju
        if letter == 'sil' or letter == 'greska' or letter == 'uzdah' or letter == 'buka':
            #uzima pocetak i kraj trenutnog slova
            start = int(lab[letterCounter].split()[0])
            start = ((start/10000)*sampleRate)/1000
            end = int(lab[letterCounter].split()[1])
            end = ((end/10000)*sampleRate)/1000
            framesNum = end - start #racuna koliko frame-ova treba preskociti
            currentWord = wavObject.read_frames(framesNum,np.float64) #preskace to slovo
            letterCounter+=1
        # "nj" se u labu oznacava sa "N", prema tome smanjuje se broj preskocenih slova
        #if letter == 'N':
            #letterCounter-=1
        #if letter == 'L':
            #letterCounter-=1
        #ako je u txt neka greska, buka ili uzdah, preskace se rijec
        if word[0] == '<' and word[-1] == '>':
            continue
        #uzima pocetak prvog slova
        start = int(lab[letterCounter].split()[0])
        start = ((start/10000)*sampleRate)/1000
        #preskace do zadnjeg slova u rijeci
         #broji slova u rijeci
        letterCounter = letterCounter + wordLength - 1
        #uzima kraj zadnjeg slova
        end = int(lab[letterCounter].split()[1])
        end = ((end/10000)*sampleRate)/1000
        framesNum = end - start #racuna koliko frame-ova treba procitati
        currentWord = wavObject.read_frames(framesNum,np.float64) #cita trenutnu rijec
        pysndfile.sndio.write(destinationFile,currentWord,sampleRate,'wav') #zapisuje rijec u novu datoteku
        letterCounter+=1
        
    #zatvara koristene datoteke
    textFile.close()
    labFile.close() 
    
    filesConverted+=1
print(str(filesConverted) + " out of " + str(filesToConvert) + " files converted succesfully")
    
   