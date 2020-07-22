
#القليل من المُتعة مع الأعداد الأولية
#لعبة بسيطة مُقتبسةٌ من كتاب
#Automate the Boring Stuff with Python By Al Sweigart
# مع القليل من التحديثات الخاصة بالأعداد الأولية
#من إنجاز حوري مديحة وقد نُشرت في مدونة في ستة أيام
#في كل مرة، سيختار البرنامج عددا أوليا ما بين 1 و100 بشكل عشوائي
#وعلى اللاعب العثور على ذلك العدد في ظرف 5 محاولات فقط
#الهدف هو التسلية وحفظ الأعداد الأولية الأقل من 100 بطريقة مُمتعة

import random
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
print('⭐⭐⭐⭐⭐ القليل من المُتعة مع الأعداد الأولية ⭐⭐⭐⭐⭐')
print('=================================================================================================')
print(''' العدد الأولي هو عدد طبيعي أكبر قطعاً من 1، لا يقبل القسمة إلا على نفسه وعلى واحد فقط''')
print('=================================================================================================')
print('لقد اِخترتُ عددا أوليًّا مُميزا ما بين الـ 1 والـ 100، فهَلْ لـكـ أن تجده؟ في ظرف خمس (5) مُحاولات فقط')
print('=================================================================================================')
print('==================== قائمة جميع الأعداد الأولية ما بين الـ 1 والـ 100 كالآتي ====================')
print(primes)
print('=================================================================================================')
secretNumber = random.choice(primes)
print('🏁 🏁 🏁 🏁 🏁')

for guessTaken in range(1, 6):
    print('⏳ ماالعدد الأوَّلي المٌميز الذي تتوقعه ⏳')
    guess = int(input())
   
    if guess not in primes:
        print('هذاالعدد ليس ضمن القائمة')
        continue 
    if guess != secretNumber and (guess - secretNumber)>=0 and (guess - secretNumber)>=10 :
        print('هذا العدد أكبر بكثير من العدد المطلوب،اِختر عددا أوليًّا أقل بكثير')
        print('🡇 🡇 🡇 🡇 🡇 🡇 🡇 🡇 🡇 🡇 🡇 🡇 🡇 🡇 🡇 🡇')
    elif guess != secretNumber and (guess - secretNumber)>=0 and (guess - secretNumber)<10:
        print('هذا العدد أكبر من العدد المطلوب،اِختر عددا أوليًّا أقل')
        print('🡻 🡻 🡻 🡻 🡻 🡻 🡻 🡻 🡻 🡻 🡻 🡻 🡻 🡻')
    elif guess != secretNumber and (guess - secretNumber)<0 and (guess - secretNumber)<=(-10):
        print('هذا العدد أقل بكثير من العدد المطلوب،اِختر عددا أوليًّا أكبر بكثير')
        print('🡅 🡅 🡅 🡅 🡅 🡅 🡅 🡅 🡅 🡅 🡅 🡅 🡅 🡅 🡅 🡅')
    elif guess != secretNumber and (guess - secretNumber)<0 and (guess - secretNumber)>(-10):
        print('هذا العدد أقل من العدد المطلوب،اِختر عددا أوليًّا أكبر')
        print('🡹 🡹 🡹 🡹 🡹 🡹 🡹 🡹 🡹 🡹 🡹 🡹 🡹 🡹')
    else:
        break            
            
print('\n🕛🕐🕑🕒🕓')
if guess == secretNumber:
    print(' أحسنتم ✔✔✔✔✔ لقد وجدتم العدد الأوليَّ المُميز، بعد '+str(guessTaken)+' من المحاولات')
else:
    print(' للأسف ❌❌❌❌❌ فقد كان العدد الأوليَّ المُميز '+str(secretNumber)+ '. شكراً على المحاولة')   
print('\nكل الأعداد الأوليَّة مُميزة والعدد ⭐ '+str(secretNumber)+' ⭐ واحدٌ منها')

#in6days.
