## make a ceaser cipher program to encrypt text with a key using ascii character
def changing(word,shift_key,what_to_do):
    resulted_text=""
    if what_to_do in ['d','decrypt']:
        shift_key=-shift_key
    for character in word:
        if character.islower():
            result=((ord(character)-97)+shift_key)%26+97
            resulted_text+=chr(result)
        elif character.isupper():
            result=((ord(character)-65)-shift_key)%26+65
            resulted_text+=chr(result)
        else:
            resulted_text+=character               
    return resulted_text

def ceaser_cipher():
    should_cont=True
    while should_cont:
        
        what_to_do=input("'encrypt' to encrypt and 'decrypt' to decypt ").lower()
        if what_to_do in ['encrypt','e','decypt','d']:
            word=input(f"Enter the word you want to {what_to_do}: ")
            shift_key=int(input("Enter the shift key: "))
            print(changing(word,shift_key,what_to_do))

            cont=input("Do you want to continue ? (y/n): ")
            if cont not in ['y','yes']:
                should_cont=False
            
        else:
            print("Enter correct choice ! ")
            
ceaser_cipher()
