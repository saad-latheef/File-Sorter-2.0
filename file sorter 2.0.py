import os
import shutil

#####

path=input('enter the path of the folder:-->')
path=path.replace('\\','/')
os.chdir(path)
print(os.getcwd())
content=os.listdir(path)


folder=[]

audio=['3gp','aa','aac','aax','act','aiff','ala','amr','ape','au','awb','dss','dvf','flac','gsm','iklax','ivs','m4a','m4b','m4p','mmf','movpkg','mp3','mpc','msv','nmf','ogg','oga','mogg','opus','ra','rm','raw','rf64','sln','tta','voc','vox','wav','wma','wv','webm','8svx','cda']
video=['yuv','wmv','webm','vob','viv','svi','roq','rmvb','rm','ogv','ogg','nsv','mxf','MTS','M2TS','TS','mpg','mpeg','m2v','mpg','mp2','mpeg','mpe','mpv','mp4','m4p','m4v','mov','qt','mng','mkv','m4v','gifv','gif','flv','f4v','f4p','f4a','f4b','flv','drc','avi','asf','amv','3gp','3g2']
compressed=['7z','arj','deb','pkg','rar','rpm','z','zip']
database=['csv','dat','db','dbf','log','mdb','sav','sql','tar','xml']
text=['doc','docx','odt','pdf','rtf','tex','txt','wpd']
spreadsheets=['ods','xls','xlsm','xlsx']
programm=['apk','c','cgi','pl','class','cpp','cs','h','jar','java','php','py','sh','swift','vb']
presentation=['key','odp','pps','ppt','pptx']
image=['ai','bmp','ico','jpeg','jpg','png','ps','psd','scr','svg','tif','tiff','webp']

files=['Images','Audios','Videos','Compressed Files','Databases','Text Files','Spreadsheets','Presentations','Codes']

img=[]
aud=[]
vid=[]
comp=[]
db=[]
txt=[]
sps=[]
pgm=[]
ppt=[]
       
######
    
for i in content:
    if '.' not in i:
        folder.append(i)
for i in folder:
    if i in content:
        content.remove(i)

l=[]
extension_final=[]
for i in content:
    j=i.rsplit('.',1)
    l.append(j)

for i in l:
    extension= i[-1]
    extension_final.append(extension)

for i in l:
    if i[-1] in audio:
        aud.append(i)
    if i[-1] in video:
        vid.append(i)
    if i[-1] in compressed:
        comp.append(i)
    if i[-1] in database:
        db.append(i)
    if i[-1] in text:
        txt.append(i)
    if i[-1] in spreadsheets:
        sps.append(i)
    if i[-1] in programm:
        pgm.append(i)
    if i[-1] in presentation:
        ppt.append(i)
    if i[-1] in image:
        img.append(i)


        




for i in files:
    for j in l:
        if aud and i=='Audios':
            if not os.path.exists(path+'/File of '+i):
                os.makedirs(path+'/File of '+i)
            if j[-1] in audio:
                j[-1]='.'+j[-1]
                shutil.move(path+'/'+''.join(j),path+'/File of Audios')
                
        if vid and i=='Videos':
            if not os.path.exists(path+'/File of '+i):
                os.makedirs(path+'/File of '+i)
            if j[-1] in video:
                j[-1]='.'+j[-1]
                shutil.move(path+'/'+''.join(j),path+'/File of Videos')
                
        if comp and i=='Compressed Files':
            if not os.path.exists(path+'/File of '+i):
                os.makedirs(path+'/File of '+i)
            if j[-1] in compressed:
                j[-1]='.'+j[-1]
                shutil.move(path+'/'+''.join(j),path+'/File of Compressed Files')
                
        if db and i=='Databases':
            if not os.path.exists(path+'/File of '+i):
                os.makedirs(path+'/File of '+i)
            if j[-1] in database:
                j[-1]='.'+j[-1]
                shutil.move(path+'/'+''.join(j),path+'/File of Databases')
                
        if txt and i=='Text Files':
            if not os.path.exists(path+'/File of '+i):
                os.makedirs(path+'/File of '+i)
            if j[-1] in text:
                j[-1]='.'+j[-1]
                shutil.move(path+'/'+''.join(j),path+'/File of Text Files')
                
        if sps and i=='Spreadsheets':
            if not os.path.exists(path+'/File of '+i):
                os.makedirs(path+'/File of '+i)
            if j[-1] in spreadsheets:
                j[-1]='.'+j[-1]
                shutil.move(path+'/'+''.join(j),path+'/File of Spreadsheets')
                
        if pgm and i=='Codes':
            if not os.path.exists(path+'/File of '+i):
                os.makedirs(path+'/File of '+i)
            if j[-1] in programm:
                j[-1]='.'+j[-1]
                shutil.move(path+'/'+''.join(j),path+'/File of Codes')
                
        if ppt and i=='Presentations':
            if not os.path.exists(path+'/File of '+i):
                os.makedirs(path+'/File of '+i)
            if j[-1] in presentation:
                j[-1]='.'+j[-1]
                shutil.move(path+'/'+''.join(j),path+'/File of Presentations')
                
        if img and i=='Images':
            if not os.path.exists(path+'/File of '+i):
                os.makedirs(path+'/File of '+i)
            if j[-1] in image:
                j[-1]='.'+j[-1]
                shutil.move(path+'/'+''.join(j),path+'/File of Images')


