import speech_recognition as sr
import pyttsx3
from nltk.chat.util import Chat
import webbrowser as web


qa_pairs = [    [ 'what is your owner name' ,                               ['Ishu'] ]  ,
                [ '(.*)name' ,                                              [ 'Ishu kumar' ] ]  ,           
                [ 'what is your favourate colour' ,                         ['Black'] ]  ,
                [ 'what is your age'              ,                         [ '18' ] ]                     ,
                [ 'what is your favourate book'    ,                        ['Gita'] ]        ,
                [ 'what is your favourate food' ,                           [ 'Chiken' ] ]      ,                                      
                [ 'what is your creater' ,                                  [ 'Ishu kumar' ] ]       ,       
                [ 'what is the favourate colour of your owner' ,            ['black'] ]    ,            
                [ '(hi|HI|Hi|hey|HEY|Hey|HELLO|Hello|hello)',               [' \t Hello  \n  How can i help u'  ,  ''] ] ,            
                [ '(.*)(location|city|address|place|Place) ?',              ['JAIPUR ']   ]   ,
                [ '(.*)contact(.*)' ,                                       ['call - xxxx for more information ℹ '] ]   ,
                [  '(.*)weather(.*)' ,                                      ['it cool  ']    ] ,
                [ '(.*)',                                                   ['Sorry pleas say again']  ]
                
            ]
cb = Chat(qa_pairs)

tts=pyttsx3.init()

rec=sr.Recognizer()
flag=False
while True:
    with sr.Microphone() as mic:
        audio=rec.listen(mic,phrase_time_limit=3,timeout=5)
        print('speak')
        try:
            text=rec.recognize_google(audio).lower()

            if flag==True:
                if 'search' in text:
                    item=text.split('search')[-1].strip()
                    flipkart='https://flipkart.com/search?q='
                    YouTube='https:youtube.com/'
                    web.open_new(flipkart+item)
                    web.open_new(YouTube+item)
                flag=False
            else:
                response= cb.respond(text)
                tts.say(response)
                tts.runAndWait()


            
            if 'ok google' in text:
                flag=True
            elif 'quit' in text:
                break
        except Exception as err:
            print(err)
