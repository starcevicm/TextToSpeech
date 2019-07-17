# TextToSpeech

cutWords.py is used to cut all wav files from the "wav" folder in "soundFiles" into words and save them separately in the "words" folder.
makeSentence.py asks user for an input sentence. If all the words in that sentence are available in the "words" folder, a new sound file corresponding to the input sentence will appear in the "sentences" folder.
Input files are stored in the "soundFiles" folder, divided into three folders: "wav", "txt" and "lab". Each wav file has a corresponding txt and lab file with the same name. 
Txt file contains the spoken text. 
Lab file is structured into three columns and it contains information about start and end times of each character spoken.
Application was tested on VEPRAD database. One wav, txt and lab are included for example.
