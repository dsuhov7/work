import requests
import re
import collections

#import BeautifulSoup
x = requests.get('https://www.cs.cmu.edu/~rgs/alice-I.html')
#soup = BeautifulSoup(x.text, 'html.parser')
#soup.find_all('p')

s = x.text
sp = re.findall(r'\w+',s)
print(sp)
#sn = re.sub{'',s}

#print(x.text)

