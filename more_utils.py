import re, datetime

def ProcessFileName(Filename):
    #Split retrieved filename
    Dur = ""
    Start = ""
    Exp = ""
    SFileName = re.sub(r'\..+', "", Filename) 
    SFileName = SFileName.split("_")
    #Search through split filename for parameters dur, start, exp 
    for each in SFileName:
        if ("dur" in each):
            Dur = each.replace("dur", "")
            if Dur.isdigit() != True:
                Dur = ""
            #print Dur  
        if("start" in each):
            Start = each.replace("start", "")
            if validate(Start) == -1:
                Start = ""
            #print Start
        if("exp" in each):
            Exp = each.replace("exp", "")
            if validate(Exp) == -1:
                Exp = ""
            #print Exp  
    return [Dur, Start, Exp]

def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%m-%d-%Y')
        return 1
    except ValueError:
        return -1

