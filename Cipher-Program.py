class Cipher:
    
    """Welcome to Cipher-Program"""
    
    def __init__(self, Text):
        self.Text = Text

Doc = Cipher("")
print(Doc.__doc__)
print()
# User Interface for selection of encryption method
Encryption_Method = ("Scytale Cipher", "Caesar Cipher", "Polybius Cipher")

("1", "2", "3") == Encryption_Method

print ("1: ", Encryption_Method[0])
print ("2: ", Encryption_Method[1])
print ("3: ", Encryption_Method[2])
print()
EM = input("Please enter an encryption method: ")
print()
if EM == "3":
    Text = input("Enter considered encrypt/decrypt text: ").upper()
else:
    Text = input("Enter considered encrypt/decrypt text: ")

def Scytale():
    
    Scytale = Cipher(Text)
    
    Cipher_List1 = Text.split(" ")
    print()
    # The question for selection of encryption process or decryption process
    Q = input("Does your text is cipher? (y/n) ")

    # The cipher has been reversed for high security and in this section ...
    # the cipher need to reverse to decrypt
    if Q == "y":
        
        Cipher_List1.reverse()

    Length = len(Cipher_List1)

    Cipher_List2 = []

    Cipher_List3 = []

    Clear_List = []

    j = 0

    for i in range(Length):

        counter = 0
        # To undestand of letter number in every word
        for ch in Cipher_List1[i]:

            counter += 1

        for j in Cipher_List1[i]:

            Cipher_List2.append(j)
        # We will not chnage the word with capital letter in first of it
        if Cipher_List2[0].islower() == True:

            for p in range(counter):

                Cipher_List3.append(Cipher_List2.pop())

        elif Cipher_List2[0].isupper() == True:
            
            for p in range(counter):

                Cipher_List3.append(Cipher_List2.pop())

            # Cipher_List3 = Cipher_List2.copy()

        Str = "".join(Cipher_List3)

        Clear_List.append(Str)
        
        Cipher_List2.clear()

        Cipher_List3.clear()

    # Reverse of cipher for high security
    if Q == "n":

        Clear_List.reverse()

    Decrypt = " ".join(Clear_List)
    print()
    return Decrypt

def Caesar():
    
    Dict1 = {"A":"D", "B":"E", "C":"F", "D":"G", "E":"H", "F":"I",
             "a":"d", "b":"e", "c":"f", "d":"g", "e":"h", "f":"i",
             "G":"J", "H":"K", "I":"L", "J":"M", "K":"N", "L":"O",
             "g":"j", "h":"k", "i":"l", "j":"m", "k":"n", "l":"o",
             "M":"P", "N":"Q", "O":"R", "P":"S", "Q":"T", "R":"U",
             "m":"p", "n":"q", "o":"r", "p":"s", "q":"t", "r":"u",
             "S":"V", "T":"W", "U":"X", "V":"Y", "W":"Z", "X":"A",
             "s":"v", "t":"w", "u":"x", "v":"y", "w":"z", "x":"a",
             "Y":"B", "Z":"C", ".":".", ",":",", ";":";", "0":"3",
             "y":"b", "z":"c", "1":"4", "2":"5", "3":"6", "4":"7",
             "5":"8", "6":"9", "7":"0", "8":"1", "9":"2"}

    Dict2 = {"D":"A", "E":"B", "F":"C", "G":"D", "H":"E", "I":"F",
             "d":"a", "e":"b", "f":"c", "g":"d", "h":"e", "i":"f",
             "J":"G", "K":"H", "L":"I", "M":"J", "N":"K", "O":"L",
             "j":"g", "k":"h", "l":"i", "m":"j", "n":"k", "o":"l",
             "P":"M", "Q":"N", "R":"O", "S":"P", "T":"Q", "U":"R",
             "p":"m", "q":"n", "r":"o", "s":"p", "t":"q", "u":"r",
             "V":"S", "W":"T", "X":"U", "Y":"V", "Z":"W", "A":"X",
             "v":"s", "w":"t", "x":"u", "y":"v", "z":"w", "a":"x",
             "B":"Y", "C":"Z", ".":".", ",":",", ";":";", "3":"0",
             "b":"y", "c":"z", "4":"1", "5":"2", "6":"3", "7":"4",
             "8":"5", "9":"6", "0":"7", "1":"8", "2":"9"}

    Caesar = Cipher(Text)
        
    Cipher_List1 = Text.split(" ")
    print()
    Q = input("Does your text is cipher? (y/n) ")

    # The cipher has been reversed for high security and in this section ...
    # the cipher need to reverse to decrypt

    if Q == "y":
        
        Cipher_List1.reverse()

    Length = len(Cipher_List1)

    Cipher_List2 = []

    Clear_List = []

    if Q == "y":
        
        for i in range(Length):
        
            for ch in Cipher_List1[i]:
                
                Cipher_List2.append(Dict2.get(ch))
        
            Str1 = "".join(Cipher_List2)
            
            Clear_List.append(Str1)
            
            Cipher_List2.clear()
            
    elif Q == "n":
        
        for i in range(Length):
        
            for ch in Cipher_List1[i]:
                
                Cipher_List2.append(Dict1.get(ch))
        
            Str1 = "".join(Cipher_List2)
            
            Clear_List.append(Str1)
            
            Cipher_List2.clear()

    # Reverse of cipher for high security
    if Q == "n":
        
        Clear_List.reverse()

    Decrypt = " ".join(Clear_List)
    print()
    return Decrypt

def Polybius(): # 180 bytes
    
    Dict1 = {"1115!":"A", "1124@":"F", "1133#":"E", "1142$":"D", "1151%":"M",
             "1215^":"P", "1224&":"B", "1233*":"C", "1242(":"L", "1251)":"N",
             "1315[":"Q", "1324]":"G", "1333{":"J", "1342}":"K", "1351|":"O",
             "1415;":"R", "1424:":"H", "1433,":"I", "1442<":"S", "1451.":"T",
             "1515>":"W", "1524/":"V", "1533?":"U", "1542`":"X", "1551~":"Y",
             "1335+":"Z", "!!!!!":"1", "@@@@@":"2", "#####":"3", "$$$$$":"4",
             "%%%%%":"5", "^^^^^":"6", "&&&&&":"7", "*****":"8", "(((((":"9",
             ")))))":"0"}

    Dict2 = {"A":"1115!", "F":"1124@", "E":"1133#", "D":"1142$", "M":"1151%",
             "P":"1215^", "B":"1224&", "C":"1233*", "L":"1242(", "N":"1251)",
             "Q":"1315[", "G":"1324]", "J":"1333{", "K":"1342}", "O":"1351|",
             "R":"1415;", "H":"1424:", "I":"1433,", "S":"1442<", "T":"1451.",
             "W":"1515>", "V":"1524/", "U":"1533?", "X":"1542`", "Y":"1551~",
             "Z":"1335+", "1":"!!!!!", "2":"@@@@@", "3":"#####", "4":"$$$$$",
             "5":"%%%%%", "6":"^^^^^", "7":"&&&&&", "8":"*****", "9":"(((((",
             "0":")))))"}
    
    Polybius = Cipher(Text)
    
    Cipher_List1 = Text.split(" ")

    Cipher_List2 = []

    Cipher_List3 = []

    Cipher_List4 = []

    Cipher_List5 = []

    Clear_List = []

    print()
    Q = input("Does your text is cipher? (y/n) ").lower()

    Length = len(Cipher_List1)

    if Q == "y":
        
        for i in range(Length):
        
            for ch in Cipher_List1[i]:
                
                Cipher_List2.append(ch)
            # print(Cipher_List2)
            while True:
        
                Cipher_List3 = Cipher_List2[0:6]
        
                f = Cipher_List3[0] + Cipher_List3[1] + Cipher_List3[2] + Cipher_List3[3] + Cipher_List3[4]
                
                Cipher_List4.append(f)
                
                for j in range(5):
                
                    Cipher_List2.pop(0)
                
                if Cipher_List2 == []:
                    
                    break
            
            # The cipher has been reversed for high security and in this section ...
            # the cipher need to reverse to decrypt
            Cipher_List4.reverse()
            
            for k in Cipher_List4:
                
                Cipher_List5.append(Dict1.get(k))
                
            Str1 = "".join(Cipher_List5)
            
            Clear_List.append(Str1)
            
            Cipher_List4.clear()
            
            Cipher_List5.clear()
            
    elif Q == "n":
        
        for i in range(Length):
            
            for ch in Cipher_List1[i]:
                
                Cipher_List2.append(ch)
            
            for k in Cipher_List2:
                
                Cipher_List3.append(Dict2.get(k))
            
            Cipher_List3.reverse()
            
            Str1 = "".join(Cipher_List3)
            
            Clear_List.append(Str1)
            
            Cipher_List2.clear()
            
            Cipher_List3.clear()
            
    Decrypt = " ".join(Clear_List)
    print()
    return Decrypt
    
if EM == "1":
    
    print("Your clear/cipher text is:", Scytale())

elif EM == "2":
    
    print("Your clear/cipher text is:", Caesar())
    
elif EM == "3":
    
    print("Your clear/cipher text is:", Polybius())