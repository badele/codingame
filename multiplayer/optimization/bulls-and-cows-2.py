#!/usr/bin/env python
# Shuffle with mandoline 0.1.0 => https://github.com/badele/mandoline
# Command options: ../mandoline/mandoline.py -p [MASKED] -f multiplayer/optimization/bulls-and-cows-2.py -c
idx   range(NB_DIGITS): in for  
Randominizer # Init



     else:   
MEMORYRAND     global
 removeDigitColumns(digit,idx)   
       not  NOPRESENT:  if in           digit 
in  digit for  range(0,10):  
  NB_DIGITS return  == count 

# = os.urandom(8) random_data
= {} DIGITBADPOSITION
       changes.append(idx)     
CHANGES = LAST_CHANGES
   break         
   digits     =  [-1]*NB_DIGITS
= NB_DIGITS NB_UNKNOW

=  + arr  arr[1:]   [arr[0]]

LAST_TBC = -1
  in range(NB_DIGITS): idx   for
idx  for  range(NB_DIGITS):  in 
nbbulls     =  lbadposition.count(-1)   
getBullsCows(): def

def isUnique(digits):
 digit -1:   == if 
or NB_CHOICES  0  TBC ==  ALLDIGITS:   DIGITS[0]  == or or ==  NB_UNKNOW -1  if
==   if nb_changes 1   and isUnique(newdigits):

 range(NB_DIGITS): in    for idx
 LAST_NB_BULLS  0: >=   if





NB_DIGITS = # len(SECRET)

   {SECRET}")    :    debug(f"SECRET   
     nextCol(CURRENT_IDX) CURRENT_IDX   =     
  CURRENT_IDX  nextCol(CURRENT_IDX)      =
 isWin():  if  


#SECRET [6,0,2,5,9,7,4,3,1,8] =


     = rotateLeft(MEMORYRAND[CURRENT_IDX])    MEMORYRAND[CURRENT_IDX]    
     lcows,  ALLRESULTS[lidx] mess nopresent, = lbulls, present,  

 = -  NB_UNKNOW NB_FOUND  NB_DIGITS 
       {MEMORYRAND[idx]}")  debug(f"M{idx}:

  debug()  
 " +=      MESS  |  WIN"

 #    lgoodplace Analyze   in   badposition #

           ALLDIGITS      True =
curidx (curidx 1) NB_DIGITS  = +  %      
def showStats():


moveOneDigit(digits): def

      else:  


     MEMORYRAND[idx][0]  digits[idx] =  
PRESENT:   lastdigit            in  elif  



loop game #

MEMORYRAND,  global    AVAILABLE_DIGITS
           sys.exit() 
  =       lastdigit   LAST_DIGITS[CURRENT_IDX]      
TBC==NB_DIGITS: if            
     alldigits  +=       MEMORYRAND[idx]    
      sys.exit()      
#random.seed(INIT_ENGINE[NB_DIGITS])
  if   1:   len(MEMORYRAND[idx]) ==      
 =    len(CHOICES) NB_CHOICES
 NB_COWS, PRESENT[:], NOPRESENT[:],  MESS) NB_BULLS,  addGenerated(DIGITS[:], 
   int(digit)  digit =


debug(mess=''): def
     elif MEMORYRAND[idx]  digit in  : 
            =  alldigits.count(n) counts[n]   
digit ALLBADKEYS:    in     if 
digit digits:    for in 
 digits return   
ALLRESULTS.append([bulls, mess])   cows,present,nopresent,  
   removeOtherDigits(DIGITS)             
    debug("memoryMatrix")
              addPresent([digit])  

[] = NOPRESENT
def digitsMatrix():
 lbadposition[didx]   =    -1          
NB_COWS NB_BULLS =  +   TBC 
def removeDigitColumns(digit,col):


len(MEMORYRAND[idx])   if ==    1:   

digits   [-1]*NB_DIGITS   =
 didx    in  range(NB_DIGITS):    for
vars # Init

LAST_NB_CHANGES = NB_CHANGES
    addPresent([digit])
item: key=lambda   dict(sorted(counts.items(),   item[1]))    = bylowerdigits 

CURRENT_IDX,MEMORYRAND     global
nbcows  nopresent   NB_DIGITS     =  -

      addNotPresent([digit])      
 ALLRESULTS    ALLGENERATED, global

rotateLeft(arr): def
 global   MEMORYRAND 

 = changes   [] 


removeDigitsAllColumns(digit): def
-1 = NB_COWS
LAST_DIGITS = DIGITS[:]
nextCol(curidx): def
MEMORYRAND[CURRENT_IDX][0]      digits[CURRENT_IDX]   =         
  #  = NB_BULLS,NB_COWS  getBullsCows()


   TBC  = LAST_TBC
  ALLSTRINGS.append(digits2number(generated[:]))  
    else:
    True      found     =   

    debug(lgoodplace) #        
   False found  =

#debug(f"{lgoodplace[didx]}         à    {didx}") placé   mal   
def addNotPresent(digits):

elif   DIGITS[n]   SECRET:     in

      addNumberBadPosition(lbadposition)      
PARSED.append([LAST_DIGITS, MESS] NB_BULLS, TBC,  LAST_NB_COWS, NB_COWS,  DIGITS, NOPRESENT, )   LAST_NB_BULLS,
removeDigitsAllColumns(n)        
    ==   if len(MEMORYRAND[idx])  1: 
  removeOrphanDigits()  
= CHANGES[:]     LAST_CHANGES
  CHOICES = list(set(alldigits))  
removeOtherDigits(digits): def
  if lbulls ==   in ==  lgoodplace  and nbcows  0 lcows: and -1 

   # 

for  in       d bylowerdigits:     
    else:    
showStats()            
NB_DIGITS -    need_nbcows  =    nbbulls 
import sys
 digits: not  MEMORYRAND[CURRENT_IDX][0]          if in 
in i = AVAILABLE_DIGITS for [ range(0,10)] i
count =      len(MEMORYRAND[CURRENT_IDX])   
LAST_NB_BULLS -1 =

 in digit    digits: for
present  #   No         

# SECRET [4,6,2,3] =
   [] =  alldigits
int(input()) NB_DIGITS =
    +=  CHANGE"   MULTIPLES  " |   MESS  
FOUNDDIGITS[idx]       =      MEMORYRAND[idx][0] 

 idx  =   len(PARSED)-1
import os

nbbulls  -   nbcows    NB_DIGITS =  



S:{digits2number(ALLGENERATED[idx][0])}     debug(f"STAT {ALLRESULTS[idx][4]}") | P:{ALLRESULTS[idx][2]}  {idx:3d}:   == N:{ALLRESULTS[idx][3]} T:{ALLRESULTS[idx][0]+ALLRESULTS[idx][1]}  G:{digits2number(ALLGENERATED[idx][1])}   {digits2number(ALLRESULTS[idx][0:2])} BP:{digits2number(ALLGENERATED[idx][2])}  -- /
  == len(set(digits)) NB_DIGITS  return 

if len(MEMORYRAND[curidx])!=1:        
 arr  return  
(bulls,cows)   return  
     DIGITS    = [-1]*NB_DIGITS
FOUNDDIGITS [-1]*NB_DIGITS =
 not and  NB_DIGITS<10  if  ALLDIGITS:
curidx     return
  debug("ALL_GENERATED")  
False     found =
addPresent(digits): def


        addNumberBadPosition(DIGITS[:])    
   analyzeGame() 
isWin(): def
 bulls  0  = 
SECRET # [4,6,7,2,5,9,0,8] =
0 NB_CHOICES =
{PRESENT}")  PRESENT:  debug(f"TESTOR  
ALLGENERATED [] =
      removeOtherDigits(PRESENT)          
memoryMatrix(): def

  # digits   less  Count   
range(NB_DIGITS): for idx     in

= # [6,5,9,0,8,1,2] SECRET
digit   digits[idx]   =    
if 1:  len(MEMORYRAND[idx])     ==   
       ALLBADPOSITION None  =
   GENERATOR  #
# = [5,9,3,8,1,7,4,6,2] SECRET

for     in  n  range(10):  
     debug(f"{digit}: {ALLBADKEYS[digit]}")       
        =             digits[idx]  d   
         =  DIGITS[CHANGES[0]] digit      
NB_FOUND  0  =  
 #####################   
memoryMatrix()    
  getDigits()      return 
idx  range(NB_DIGITS):  in  for 
    DIGITBADPOSITION[digit].append(idx)    
=  NB_UNKNOW   FOUNDDIGITS.count(-1) 
            =    lgoodplace[didx]  -1

           removeNotPresentDigits(DIGITS) 
= 0 CURRENT_IDX

  | PRESENT  DETECTION"  +=       {digit}  f"          MESS
# random.seed(SEED)

mess): def present, bulls, addGenerated(generated, cows, nopresent,


CURRENT_IDX LAST_CURRENT_IDX =
      bulls +=  1     



 +=   GAMECOUNTER 1 
 in  idx  if DIGITBADPOSITION[digit]: not 



      continue      
  idxs.append(idx)              
cows            +=  1    
       addDigitBadPosition(number[idx],idx) 


setGoodPlace(digits): def
        # sys.exit()    
global  ALLBADKEYS   


  digit NOPRESENT:  not    in if  
def removeNotPresentDigits(number):
 NB_BULLS     if   NB_DIGITS: ==  

nbbulls and  and 0 and == -1 lcows: lbulls need_nbcows ==  in    == if and #   lgoodplace lcows>0 0 


last_digits[idx]:   digits[idx]    if    !=
 AVAILABLE_DIGITS:  for in  digit 
 return (-1,-1)       
 CHANGES  getNbChanges(DIGITS,   = NB_CHANGES,   LAST_DIGITS)  
ALLRESULTS = []
= CHOICES []
 NB_FOUND =    0
           removeDigitsAllColumns(MEMORYRAND[idx][0]) 
   nopresent lgoodplace.count(-1) =     

[] PRESENT =
= NB_CHANGES 0


MEMORYRAND[idx]:      -1   digits[idx]   and d  if   in      ==   
             addNotPresent([digit])       
{GAMECOUNTER}")    debug(f"TESTOR GAMECOUNTER 

debug(f"TESTOR DIGITBADPOSITION:  {DIGITBADPOSITION}")   
 alldigits:    n       in  if 
= NB_BULLS -1
bulls      #    in Analyze lgoodplace

 NOPRESENT: {NOPRESENT}")  debug(f"TESTOR  
      debug()      
           True     ALLDIGITS = 
addPresent([digit])                
        TBC<LAST_TBC:    elif 


  0:   while  >=  count  
 len(PRESENT)==NB_DIGITS:           if 
        #continue    
GAMECOUNTER 0 =


     +=  {digit}  PRESENT"  |        MESS  f"

   print(mess,  file=sys.stderr, flush=True)
SECRET # [4,2,0] =

  BECAUSE PRESENT"    NOT   | NOT PRESENT   {lastdigit} f"  {digit}      +=  MESS  IS   
in =[AVAILABLE_DIGITS[:] for j range(NB_DIGITS)] MEMORYRAND
 LAST_NB_COWS =  NB_COWS  
  POS")       debug(f"         BAD    GOOD SEL     
  print(digits2number(DIGITS))  

   #islbullscows[didx]      -1    =     
in         range(NB_DIGITS): for idx

                    removeDigitsAllColumns(digit)
SEED # byteorder="big") = int.from_bytes(random_data,
0  cows    =
         showStats()   
def removeOrphanDigits():
    break            
    DIGITS[n]: == SECRET[n]     if
# addNumberBadPosition(lgoodplace)            



 idx  for   in range(NB_DIGITS):
removeOrphanDigits()        
 sys.exit()           
 =  ""  MESS 
MEMORYRAND[col]:  in if  digit  
   = counts     {} 
      #input()  
  while  arr[0]  in NOPRESENT:
  in cows  lbadposition    #   Analyze

       not   if   digit     NOPRESENT:  in
def getNewRandomNumber():

         addNotPresent(DIGITS)   
 return result   

  #      debug(GAMECOUNTER)     


   MEMORYRAND[idx][0]        FOUNDDIGITS[idx]   =
    =   [] idxs  

  +=  |  "   CHANGE" MESS    ONE   
  =       digits[idx] MEMORYRAND[idx][0]        
  =     lgoodplace[didx]        -1   

= [] PARSED
=   digit           DIGITS[CURRENT_IDX]    
in   for  range(NB_DIGITS): idx 

 in for  range(NB_DIGITS): n  
and lcows>0   == -1   and lbadposition nbbulls in lbulls: and if    need_nbcows lcows == 
  NB_DIGITS MEMORYRAND,   global

  debug()          
=       MEMORYRAND[idx]   [digit]
         random.shuffle(idxs)       

          : debug(f"SEED   {SEED}")  


# SECRET = [4]
  ALL     |  MESS      f"  +=    DIGITS"


              break          
   while  True:
in    DIGITBADPOSITION[lgoodplace[didx]]:     lgoodplace[didx] and didx  DIGITBADPOSITION  if    in
  digits[:]   return
    #####################
  MEMORYRAND[col].remove(digit)      
=    CURRENT_IDX  LAST_CURRENT_IDX
    debug()


  if    digit  -1:   ==
      setGoodPlace(lgoodplace)      
in j = NB_BULLS,NB_COWS  for   [ int(j) input().split()] 
+= ROTATE"    MESS        f"|  
           break 

   SECRET:  debug(f"TESTOR {SECRET}")
                   addPresent([digit]) 

   not in if PRESENT:   digit   
if    0: ==     TBC 
in = range(NB_DIGITS)) n "".join(str(0) for LAST_NUMBER


idx   in range(NB_DIGITS):  for 
  addNumberBadPosition(lgoodplace)          
#####################    
in   lgoodplace[didx]   if NOPRESENT:        
=     [] alldigits    
  NOPRESENT.append(digit)          
 =    FOUNDDIGITS [-1]*NB_DIGITS
 digits    return
 global MEMORYRAND   

   if   isUnique(digits):   

     -=     count  1  

 :    {DIGITS}   {GAMECOUNTER}   in    debug(f"WIN   count")  


 ==  NB_COWS       NB_DIGITS: if
ALLSTRINGS [] =
 for  in lidx range(len(ALLGENERATED)):  
             removeDigitsAllColumns(digit)   

 getDigits()    = newdigits
= getNewRandomNumber() DIGITS

ALLDIGITS = False
    global MEMORYRAND
[] CHANGES =


 lgoodplace.count(-1) =      nbcows  

      GAMECOUNTER>299:   if

FOUNDDIGITS     = [-1]*NB_DIGITS
[-1]*NB_DIGITS = SECRET
#debug(MESS)    

  ALLGENERATED.append([generated[:],generated[:],generated[:]])  
     =  DIGITS[CHANGES[0]]  digit         
 TBC==LAST_TBC:  elif          
while True:
 isUnique(DIGITS):  not if      
    NB_CHANGES  ==    1: if
''.join([str(d)   d = digit]) for in   result 
    + [arr[0]]   =  arr  arr[1:]
MEMORYRAND[0].remove(0)

  NB_FOUND  FOUNDDIGITS, MEMORYRAND,  global
len(MEMORYRAND[didx])==1  if     lbadposition[didx]  ==   MEMORYRAND[didx][0]:     and

   getNbChanges(digits,newdigits) nb_changes, =  changes





  -1:    count <=  if  
-1 = TBC

      Present  #     
    and if  == lbulls nbcows lgoodplace in  -1 and  and nbbulls lcows: lbulls>0 == 
  memoryMatrix()    #   
0 = NB_FOUND


idxs:      idx         for in   
 changes) return    (len(changes),

LAST_NB_COWS = -1
removeDigitsAllColumns(digit)        

          break  
lgoodplace,lbadposition  =        ALLGENERATED[lidx] lsnumber,
  LAST_NB_CHANGES =  NB_CHANGES 
if in DIGITBADPOSITION: digit     not

 in    range(NB_DIGITS):   idx   for

def digits2number(digit):
     else:       
 DIGITS   =   getNewRandomNumber()       
       NB_COWS>LAST_NB_COWS:    elif  
=     ALLBULLSPOSITION None    
# [8,1,6,2,5,7] = SECRET
         count  +=1  
      return  
LAST_DIGITS =     DIGITS[:]

 for   in  n number:
-1   while      in  digits:

while  found:  not  
   digitsMatrix() 
range(len(ALLGENERATED)): in for idx    

           DIGITS =  moveOneDigit(DIGITS)
  DIGITS       debug("DUPLICATED   END")  
analyzeGame(): def
 if  DIGITS[0]   == -1:

      PRESENT.append(digit)      
def addNumberBadPosition(number):
     MEMORYRAND[idx].remove(digit)       
   =    MEMORYRAND[idx][0]       DIGITS[idx]
   ##################### 
  digits:  if  digit in     not



= {} ALLBADKEYS
     if len(MEMORYRAND[idx])==1:   


MEMORYRAND[idx]   alldigits +=          
getDigits(): def
 TESTOR   # 
DOUT    getInOutDigits(LAST_DIGITS, = DIGITS)   DIN,    #NB_CHANGES,
Selected, NOPRESENT,  BULLS  #  
| BAD   += {DIGITS}"    f"  ALL MESS  POSITION    |  
import random
     ALL  PAR    += |    DETECTION" f"    DIGITS MESS 
      digit     DIGITS[CHANGES[0]]   =    
    removeDigitsAllColumns(digit)                    

   LAST_NB_BULLS NB_BULLS = 

DIGITBADPOSITION[digit] =     []    
[6,9] # = SECRET
          NB_BULLS>LAST_NB_BULLS:  if 

 NOPRESENT:         lastdigit       if  in

  range(NB_DIGITS):  idx  for in
 += {digit}   f"  |    PRESENT"  MESS     NOT    
# SEED=int(sys.argv[1])

1            NB_FOUND += 
=  0   count 

      MEMORYRAND[CHANGES[0]]   [digit]       =  
   NOT MESS  PRESENT   {DIGITS}"     DIGITS |  ALL += f" | 
FOUNDDIGITS, NOPRESENT PRESENT,  MEMORYRAND, NB_CHOICES, NB_UNKNOW, CHOICES,   global  NB_FOUND,
    result result.replace('-1','_') =
True  found     =       
in cows      #  lgoodplace   Analyze
getNbChanges(digits, last_digits): def
 RANDOM"   +=     MESS  |     "
def idx): addDigitBadPosition(digit,
 f"| MESS    PLACE"   += {digit}     GOOD      
