print ("Καλησπέρα" +\
"!! Χρησιμοποιείται η έκδοση 3.6 της python !!")

print ("ΆΣΚΗΣΗ 7:Γράψτε ένα πρόγραμμα το οποίο παίρνει ως είσοδο τα ονόματα δύο χρηστών του\n"
"twitter και εμφανίζει ποιος από τους δύο, έχει στα τελευταία 10 του tweets έχει περισσότερες λέξεις.")

import tweepy
from tweepy import OAuthHandler

consumer_key = 'WjX7fp1d8D7NcVAYnJZMOF9NA'
consumer_secret = 'R2pCP9mEWXZEcmxs5ZMbvJ7zxOmrOXKPOFARlQ5ORCS231sOQB'
access_token = '1236403638-lPVuaMJFVoTTxOsuY0YtPvlCDBKAmOaIEDvel70'
access_secret = 'OXNYCYs8v0entx0k3jzc5GDvG9nkBGyrp6aL2gOydGnHT'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

userid1=(input("Username 1ου χρήστη: "))
userid2=(input("Username 2ου χρήστη: "))

#ελέγχει τα username να έχουν μπει σωστά
while (userid1==userid2):
    if (userid1==userid2==" "):
        break
    print("Δώστε ξεχωριστά username!")
    userid1=(input("Username 1ου χρήστη: "))
    userid2=(input("Username 2ου χρήστη: "))

while (userid1 == " " or userid2 == " "):
    if (userid1== " "):
        userid1= (input ("Ξαναδώστε το username του 1ου χρήστη ώστε να μην είναι το κενό :\n"))
    else:
        userid2= (input ("Ξαναδώστε το username του 2ου χρήστη ώστε να μην είναι το κενό :\n"))

ver1=api.verify_credentials(id=userid1)
ver2=api.verify_credentials(id=userid2)

if (ver1==False):
    while (ver1==False):
        print ("Το username δεν υπάρχει!")
        userid1=(input("Ξαναδώστε το username του 1ου χρήστη:"))

elif (ver2==False):
    while (ver2==False):
        print ("Το username δεν υπάρχει!")
        userid2=(input("Ξαναδώστε το username του 2ου χρήστη:"))

#εμφάνιση των tweet
i=1
sum1=0
sum2=0


stuff1 = api.user_timeline(screen_name = userid1, count = 10, include_rts = True)

for status in stuff1:
     print (status)
     sum1= sum1 +len(status)

stuff2 = api.user_timeline(screen_name = userid2, count = 10, include_rts = True)

for status in stuff2:
    print (status)
    sum2 = sum2 + len(status)


#σύγκριση των tweet

if (sum1 > sum2):
    print ("Ο χρήστης ",userid1 ," έχει τα περισσότερα tweets.")

elif (sum1==sum2):
    print ("Ο χρήστης",userid1 , "και ο χρήστης ", userid2 , " έχουν ίδιο αριθμό tweet.")

else:
    print ("Ο χρήστης ", userid2 , " έχει τα περισσότερα tweets.")

print ("!!!!!!! ΤΕΛΟΣ ΑΣΚΗΣΗΣ 7 !!!!!!!")
