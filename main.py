print('Hello Loksewa Aspirants\nWelcome to MCQ checker platform !!!')
print('\n')
print('Practice and Check your MCQ keys of Professional Practice from Civil Engineering(D-prasad)\n')
def make_dic(fopen):
  #fopen=open(f)
  di=dict()
  for line in fopen:
    lis=line.split()
  for i in range(len(lis)):
    k=i+1
    v=lis[i]
    di.update({k:v})
  return di
def chap_name():
  try:
    file1=input('Enter a Chapter name(or press Enter to continue):')
    if len(file1)<1:
      file1='Professional Practice.txt'
    else:
      file1=file1.rstrip()+'.txt'
    return open(file1)
  except:
    print('\nFILE NAME NOT VALID!!!\n')
    chap_name()
  
def check(d,n):
  temp=None
  for k,v in d.items():
    if k==n:
      temp=v
  return temp
def do():
  while True:
    try:
      q=input('\nQuestion Number:')
      if q=='done':
        print('\nTHANK YOU for using and GOOD LUCK for your preparations')
        break
      qn=int(q)
    except:
      print('\nPLEASE ENTER AN INTEGER NUMBER')
      do()
    op=input('Your Option:')
    ak=check(dic,qn)
    if op==ak:
      print('\nCORRECT ANSWER !!')
    elif ak==None:
      print('\nQUESTION NUMBER IS OUT OF RANGE')
    else:
      print('\nYour answer is INCORRECT')
      print('Correct option for the QN',qn,'is option',ak.upper())
cnm=chap_name()
dic=make_dic(cnm)
do()

  
