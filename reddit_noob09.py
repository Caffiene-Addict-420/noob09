#Installing Dependencies

#type 'pip' if its not on your machine, it will most likely tell you how to download it e.g.:
#may have to do '(sudo) apt-get install python-pip' or equivalent

#once you have pip installed:
#pip install praw

#If you have any trouble at any time, just PM me on reddit. This is a demo version, for only r/bitcoin.
#I have obfuscated the code to prevent you from just taking my work without payment

import traceback
try:
    import praw,csv, os
    def get_directory():
        return os.path.dirname(os.path.realpath(__file__))
            
    def write_csv(OOO0OO0OO000O0000):
        with open(os.path.join(get_directory(), 'reddit.csv'),'w')as O0000OOOOOO0O0OOO :
            #O0OO0000O0OOOOOOO=csv.writer(O0000OOOOOO0O0OOO,delimiter =' ',quotechar =',',quoting =csv.QUOTE_MINIMAL )
            for OO00OO00O0OOO00OO in OOO0OO0OO000O0000:
                O0000OOOOOO0O0OOO.write("%s,%s,%s\n" % (OO00OO00O0OOO00OO[0], OO00OO00O0OOO00OO[1], OO00OO00O0OOO00OO[2])) 
    def get_top (O0OOOOO00OO0O0O00,OOO0O0OOOOO00OO0O ):
        O00000O00OO0000O0=[]
        OOOOOO00O00000000="7DnqoEzW8bOXDw"
        OOOOO0000OOO00O00="oZOdibnbBgHDTH-6KFtsBrJZ7f8"
        OO0000O0OOOO0O000=praw.Reddit(client_id =OOOOOO00O00000000,client_secret=OOOOO0000OOO00O00,user_agent ='Python Praw Bot')
        for O00OO0OO00O0000OO in OO0000O0OOOO0O000.subreddit (O0OOOOO00OO0O0O00 ).top(limit=OOO0O0OOOOO00OO0O):
            OOOOO0OOO0OOO0OOO=O00OO0OO00O0000OO.title.replace(",", "").encode('utf-8')
            OO00O0OO00OOOOO0O=O00OO0OO00O0000OO.url.replace(",", "").encode('utf-8')
            O0OO00OO000000O0O=O0OOOOO00OO0O0O00.replace(",", "").encode('utf-8')
            O00000O00OO0000O0.append ([OOOOO0OOO0OOO0OOO,OO00O0OO00OOOOO0O,O0OO00OO000000O0O])
        write_csv(O00000O00OO0000O0)
        print("Written Top %s posts from r/%s to reddit.csv"%(str(OOO0O0OOOOO00OO0O ),O0OOOOO00OO0O0O00 ))
    get_top("bitcoin",20 )
except:
    traceback.print_exc ()
while True:pass
