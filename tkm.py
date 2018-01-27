import random
bscm = ['tas','kagit','makas']
skr = 3


k = str("k")
m = str("m")
t = str("t")
while skr >= 0:
    bot = random.choice(bscm)
    if(bot == "tas"):
        print("Seciminiz : ")
        kscm = str(input())
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



    if(bot == "kagit"):
        print("Seciminiz : ")
        kscm = str(input())
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



    if(bot == "makas"):
        print("Seciminiz : ")
        kscm = str(input())
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
    print "Botun sectigi " , bot , " idi "

