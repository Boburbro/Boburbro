import time
import os,sys
def first(*a):

    try:
        with open("data/name.txt", "r")as f:
            v = f.read()
            pass
    except:
        os.system("pip install requests")
        os.system("pip install smtp")
        os.system("pip install telethon")
        print("\n\n\n\n© BoburBro ")
        time.sleep(0.5)
        print("Bu tool faqat talim maqsadida!")
        time.sleep(0.5)
        print("Bu tool bilan qilingan harqanday jinoyat uchun BoburBro ayibdor emas")
        time.sleep(0.5)




def update(*a):
    a = input("update qilaymi(y/n)")
    if a == "y":

        try:
            with open("data/name.txt", "r") as file:
                s = file.read()
                if s == "termux":
                    os.system("pkg install git")
                    os.system("rm -rf data")
                    os.system("git clone https://github.com/Boburbro/data")
                    try:
                        with open("data/dir.txt", "r")as file1:
                            d = file1.read()
                            if d == "":
                                print("Bajarildi")
                                exit()
                            else:
                                print("Nimadur xato ketidi qayta urining")
                    except:
                        print("Niadur xato ketdi data fayl topilmadi")
                if s == "linux":
                    os.system("pkg install git")
                    os.system("rm -rf data")
                    os.system("git clone https://github.com/Boburbro/data")
                    try:
                        with open("data/dir.txt", "r") as file1:
                            d = file1.read()
                            if d == "":
                                print("Bajarildi")
                                exit()
                            else:
                                print("Nimadur xato ketidi qayta urining")
                    except:
                        print("Niadur xato ketdi data fayl topilmadi")


                if s == "shell":
                    os.system("rm -Recurse data")
                    os.system("git clone https://github.com/Boburbro/data")
                    try:
                        with open("data/dir.txt", "r") as file1:
                            d = file1.read()
                            if d == "":
                                print("Bajarildi")
                                exit()
                            else:
                                print("Nimadur xato ketidi qayta urining")
                    except:
                        print("Nimdur xato ketdi data fayl topilmadi")
                        print("Sizda git yoq shekili negadir data faylni ololmadim")

        except:
            input("data fayl topilmadi update boshlash uchun istalgan tugmani bosing")
            os.system("git clone https://github.com/Boburbro/data")
            input("Bajarildi")
    else:
        exit()







def analiz():
    first()
    try:
        from data.versia import text,versia,photo
        from data.run import run1
        print(f"{photo}\n{text}\n\tv{versia}")
        a = input()
        if a == "..up":
            update()
        run1()
    except(ImportError):
        update()

    except Exception as e:
        print(e, 'Nimadur xato!\nupdate qiling')


analiz()