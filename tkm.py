#python2.x sürümü kulllan
import random
import time
import os
os.system('clear')
print("t = tas -- k = kagit -- m = makas i kullanin \n \n")
bscm = ['tas','kagit','makas']
skr = 0
k = str("k")
m = str("m")
t = str("t")
E = str("E")
e = str("e")
h = str("h")
H = str("H")
M = str("M")
L = str("L")
print ("Zorluk seviyesi --> ' H= Hard - M= Medium - L= Low ' :")
zrlk = str(input())
if(zrlk == "H"):
    skr += 2
if(zrlk == "M"):
    skr += 5
if(zrlk == "L"):
    skr += 10
if(skr <0):
    print("KAYBETTINIZ")
    print("Tekrar oynamak istermisiniz ? [E/H]")
    tkr = str(input())
    if((tkr=="E") or (tkr=="e")):
        skr = 3
        os.system
        ('clear')
    if((tkr == "h") or (tkr == "H")):
        os.system('exit')
        os.system('exit')
while skr >= 0:
    print("\n \n \n")
    bot = random.choice(bscm)
    if(bot == "tas"):
        print("Seciminiz : ")
        kscm = str(input())
        print("tas...")
        time.sleep(0.4)
        print("kagit...")
        time.sleep(0.4)
        print("makas...")
        time.sleep(0.4)
        if(kscm == t):
            print("!BERABERE!")
            print "Skorunuz : ", skr
        if(kscm == k):
            print("!KAZANDINIZ!")
            skr +=1
            print "Skorunuz : ", skr
        if(kscm == m):
            print("!KAYBETTINIZ!")
            skr -=1
            print "Skorunuz : ", skr

    elif(bot == "kagit"):
        print("Seciminiz : ")
        kscm = str(input())
        print("tas...")
        time.sleep(0.4)
        print("kagit...")
        time.sleep(0.4)
        print("makas...")
        time.sleep(0.4)
        if(kscm == k):
            print("!BERABERE!")
            print "Skorunuz : ", skr
        if(kscm == m):
            print("!KAZANDINIZ!")
            skr +=1
            print "Skorunuz : ", skr
        if(kscm == t):
            print("!KAYBETTINIZ!")
            skr -=1
            print "Skorunuz : ", skr

    elif(bot == "makas"):
        print("Seciminiz : ")
        kscm = str(input())
        print("tas...")
        time.sleep(0.4)
        print("kagit...")
        time.sleep(0.4)
        print("makas...")
        time.sleep(0.4)
        if(kscm == m):
            print("!BERABERE!")
            print "Skorunuz : ", skr
        if(kscm == t):
            print("!KAZANDINIZ!")
            skr +=1
            print "Skorunuz : ", skr
        if(kscm == k):
            print("!KAYBETTINIZ!")
            skr -=1
            print "Skorunuz : ", skr
    else:
        print("Seciminiz : ")
        kscm = str(input())
    print "Botun sectigi ->" , bot , "<- idi "
