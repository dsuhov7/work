import datetime
import sys

if len(sys.argv) < 2:
    print('Fault')
sys.exit(2)
ps = sys.argv[1]
with open("new.py") as f:
   while True:
       ps = f.readline()
       if ps == "":
           break
   psn = re.sub('^\s,{2,5}',' '*4,s)
   psn = re.sub("\t"," "*4,s)
   sl += psn
   if __name__ =="__main__":
       d = datetime.datetime.now()
       sd = "Test complete{}.{} in {}:{}".format(d.day,d.month,d.hour,d.minutes)
       print(sd)

