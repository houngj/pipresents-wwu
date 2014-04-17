import re

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
            #print Dur
        if("start" in each):
            Start = each.replace("start", "")
            #print Start
        if("exp" in each):
            Exp = each.replace("exp", "")
            #print Exp

    return [Dur, Start, Exp]
