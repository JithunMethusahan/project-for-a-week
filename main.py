import datetime as dt

def date(d):
 d = dt.date.today()
 print("Date:",d)  

def time(t):
  while True:
   t = dt.datetime.now()
   print("Time:", t.time() ) 

def menu(d, t):
  while True:
    print("*"*50)
    date(d)
    time(t)
    break
     

menu("", "")