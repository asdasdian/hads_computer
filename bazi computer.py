import os
def sercher(firest,last,ch):
#    ch=''
 #   firest=0
  #  last=100
    mid=int((firest +last)/2)
    if ch=='y':
        print("yes i find it\a")
        return 'y'
    if ch=='k':
        firest=mid+1
        last=last
        mid=int((firest +last)/2)
        return firest,last
    if ch=='b' :
        firest=firest
        last=mid -1 
        mid=int((firest +last)/2)
        return firest,last
         

print(" ye adad ro dar nazar b gir bein 0 ta 100")
print(" hala behem komak kon ta manam peidash konam ")
print(" baraye komak kardan az b bozorgtar k hochiktar y osavi  estefade kon")
a=input("y ro baraye shoro bezan ")
if a=='y' or a=='Y' :
    os.system('cls')
#if a=='n' or a=='N' :
    
tt='pls write  b or k or y'
firest=0
last=100
mid=int((firest +last)/2)
hads=mid
print("hads ---> ",hads)
hu=input(": ")
#print(sercher(firest,last,hu))
##print("\n##############\n")
os.system('cls')

while sercher(firest,last,hu) !='y'or firest==mid-1 or last==mid+1 :
    firest,last=sercher(firest,last,hu)
    mid=int((firest +last)/2)
    hads=mid
    print("hads ---> ",hads)
    hu=input("vaziat ? :")
#    print("\n##############\n")
    os.system('cls')

#    print("firest ",firest ,"\n last ",last, "\n vaziiat ",hu)
    
    
          
os.system('cls')        
print("hoooraa eyval adad ro peyda kardam \a")
print("adadet ",hads,"hast \a")

