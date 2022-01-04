from pywhatkit import sendwhatmsg as DJzk
import datetime

def validateTime():
    x = datetime.datetime.now()
    hour = int(x.strftime("%H"))
    min = int(x.strftime("%M"))
    sec = int(x.strftime("%S"))
    print(hour) 
    print(min)
    print(sec)
    min = min + 1
    if sec >= 30:
        sec = sec - 30
        min = min + 1
    if min >= 60:
        min = min - 60
        hour = hour + 1
    if hour >= 24:
        hour = hour - 24
    return [hour, min, sec]

messages = ["Hey, how are you?", 
            "This is Dannie here", 
            "Wanted to test out this random whatsapp module", 
            "Seems like it works, but will it?", 
            "Lets find out"
            ]

#pywhatkit.sendwhatmsg("+919080936115", "Hey, how are you?", 16, 12)
for i in range(len(messages)):
    list = validateTime()
    h = list[0]
    m = list[1]
    s = list[1]
    print(h)
    print(m)
    print(s)
    DJzk("+919080936115", messages[i], h, m, s, True, 2)
