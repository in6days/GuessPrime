
#القليل من المُتعة مع الأعداد الأولية
#لعبة بسيطة مُقتبسةٌ من كتاب
#Automate the Boring Stuff with Python By Al Sweigart
#مع القليل من التحديثات
#من إنجاز حوري مديحة
#في كل مرة، سيختار البرنامج عددا أوليا ما بين 1 و100 بشكل عشوائي
#وعلى اللاعب العثور على ذلك العدد في ظرف 5 محاولات فقط
#الهدف هو التسلية وحفظ الأعداد الأولية الأقل من 100 بطريقة مُمتعة

import random
p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
print('القليل من المُتعة مع الأعداد الأولية')
print('⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐')
print('مرحبا بيكم معانا في لُعبة اِقترح العدد الأولي الصحيح واربح 🍉 من عندنا')
print('⭐⭐⭐⭐⭐')
print('''تذكير: العدد الأولي هو عدد طبيعي أكبر قطعاً من 1، لا يقبل القسمة إلا على نفسه وعلى واحد فقط ''')
print('⭐⭐⭐⭐⭐')
print('راني حاط في بالي عدد أوَّلي ما بين 1 و 100 وعندك خمس (5) مُحاولات برك باش تلڨاه')
print('تذكير: قائمة الأعداد الأولية من 1 إلى 100 كالآتي')
print(p)
print('⭐⭐⭐⭐⭐')
secretNumber = random.choice(p)
print('🏁 🏁 🏁 🏁 🏁')
for guessTaken in range(1, 6):
    print('⏳ واش تتوقَّع يكون العدد الأوَّلي؟ ⏳')
    print('✍')
    guess = int(input())
    if guess != secretNumber and (guess - secretNumber)>=0 and (guess - secretNumber)>=10 :
        print('🡇 وين راك هارب نقَّص 🡇')
        print('🡇 🡇 🡇 🡇 🡇 🡇 🡇 🡇 🡇 🡇 🡇 🡇 🡇 🡇 🡇 🡇 🡇')
    elif guess != secretNumber and (guess - secretNumber)>=0 and (guess - secretNumber)<10 and guess != secretNumber:
        print(' هذا أكبر من العدد الأوَّلي اللي في بالي')
        print('🡻 🡻 🡻 🡻 🡻 🡻 🡻 🡻 🡻 🡻 🡻 🡻 🡻 🡻 🡻')
    elif guess != secretNumber and (guess - secretNumber)<0 and (guess - secretNumber)<=(-10) and guess != secretNumber:
        print('🡅 راك بعيد ياسر زيد طلَّع 🡅')
        print('🡅 🡅 🡅 🡅 🡅 🡅 🡅 🡅 🡅 🡅 🡅 🡅 🡅 🡅 🡅 🡅 🡅')
    elif guess != secretNumber and (guess - secretNumber)<0 and (guess - secretNumber)>(-10) and guess != secretNumber :
        print(' هذا أقل من العدد الأوَّلي اللي في بالي')
        print('🡹 🡹 🡹 🡹 🡹 🡹 🡹 🡹 🡹 🡹 🡹 🡹 🡹 🡹 🡹')
    else:
        break
print('\n 🕛🕐🕑🕒🕓')
if guess == secretNumber:
    print(' يعطيكم الصحة راكم لڨيتم العدد الأوَّلي الصحيح بعد '+str(guessTaken)+' محاولات ')
    print(' تستاهل 🍉')
    print('\n✔✔✔✔✔')
else:
    print(' ياوو لالالالا، العدد الأوَّلي اللي كان في بالي هو '+str(secretNumber))
    print(' طريڨ الربح ✌ ')
    print('\n❌❌❌❌❌')

#in6days.