import PyPDF2 as pyp
import pikepdf as pike
from pikepdf import  *
import pyttsx3 as pyt 
import os
from os import *
from os.path import isfile, join 
mypath = "./"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
pdf_files = [file for file in onlyfiles if ".pdf" == file[(len(file)-4):(len(file))]]
no_files = len(pdf_files)
print(f"PDF Files detected : {no_files}  ")
print(f"Files: {pdf_files}")

def readAloud(file_name,text,voice):
    engine = pyt.init()
    rate = engine.getProperty('rate')
    volume = engine.getProperty('volume')
    engine.setProperty('volume',0.8)
    engine.setProperty('rate',125)
    voices = engine.getProperty('voices')
    if voice == '-f':
        engine.setProperty('voice',voices[1].id)
    elif voice == "-m":
        engine.setProperty('voice',voices[0].id)
    if ".pdf" in file_name:    
        file_name = file_name.replace('.pdf',"").strip()
    print("Generating Audiobook.....")
    engine.save_to_file(text,file_name+".mp3")
    engine.runAndWait()

def extract_text(file_name,pdf_begin,pdf_end,voice):
    if no_files > 0:
            print("Initializing....... ")

            if file_name in pdf_files:
                if '.pdf' in file_name:
                    print("Opening file ..... ")
                    doc = pike.open(file_name)
                else:
                    pass
                if doc:
                    print("Decrypting.... ")
                    doc.save("convertable.pdf")
                    pread = pyp.PdfFileReader("convertable.pdf")
                    if pread:
                        if pdf_end == "end" or pdf_end == "END":
                            pdf_end = pread.getNumPages()
                        else:
                            pdf_end = int(pdf_end)
                        if pdf_begin == "start" or pdf_begin == "START":
                            pdf_begin = 1
                        else:
                            pdf_begin = int(pdf_begin)
                        for y in range(pdf_begin,pdf_end):
                            page = pread.getPage(y)
                            text = page.extractText()
                            return text
                            
                        if pdf_begin == pdf_end:
                            page = pread.getPage(pdf_begin)
                            text = page.extractText()
                            return text           

                    else:
                        print("[Error: Could not read text]")
                else:
                    print("[Error: Could not decrypt file]")       
            else:
                print(f"[Error: File not found '{file_name}']")    
    else:
        print("No pdf files detected")    
        
#  Contribute to the below function
def extractAll(pdf_files,voice):
    if no_files>0:
        for file in pdf_files:
            print(f"opening {file} .....")
            doc = pike.open(file)
            if doc:
                print(f"Decrypting {file} .....") 
                doc.save(file+"_convertable.pdf")
                docread = pyp.PdfFileReader(file+"_convertable.pdf")
                if docread:
                    #  Get number of pages
                    no_pages = docread.getNumPages()    
                     
                    for i in range(no_pages):
                        page = docread.getPage(i)
                        text = page.extractText()
                        return text
                readAloud(file,text,voice)            
cmd_temp = "aud .conv -f main.pdf 4:6"

while True:
    try:
        cmd = input("~$ ")
        if "aud .conv" in cmd:
            for f in pdf_files:
                if f in cmd:
                    if "-f" in cmd:
                        voice = "-f"
                        pos_f = cmd.index("-f")
                    elif "-m" in cmd :
                        voice = "-m"
                        pos_f = cmd.index("-m")
                    else:
                        print("Voice option invalid")
                    if ".pdf" in cmd and ':' in cmd:
                        pos = cmd.index(".pdf")
                        col = cmd.index(":")
                        wordInts = ["end","END","start","START"]
                       
                        pdf_begin = cmd[(pos+4):(col)].strip()
                        pdf_end = cmd[col+1:]
                        file_name = (cmd[(pos_f+2):(pos+4)].strip())
                        readAloud(file_name,extract_text(file_name,pdf_begin,pdf_end,voice),voice)
        else:
            print("Invalid syntax , Type aud -help")                 
        if cmd == "aud -help":
            help = """
                Convert pdf file to an audiobook : [aud .conv -voiceOption filename.pdf startPage:EndPage ]
                For instance : aud .conv -f filename.pdf 35:38
                Voices: (male and female)
                How to use male voice: [aud .conv -m mydocument.pdf startPage:EndPage ]
                How to use female voice: [aud .conv -f filename.pdf startPage:EndPage ]
                
            """
            print(help.strip())

    except:
        print("Oops, An unexpected Error occured")
    finally:
        print("Exiting....")
        conv = [a for a in onlyfiles if 'convertable' in a]
        for p in conv:
            os.remove(p)
        print("Done .")
