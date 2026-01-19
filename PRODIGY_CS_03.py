
def pass_complexity_chck(passwd):
    has_upper= False
    has_lower= False
    has_num= False
    has_special= False
    special_ch= "@#$_ /"

    for char in passwd:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_num = True
        elif char in special_ch:
            has_special = True
    leng= 7<len(passwd)<21
    
    criteria = [
        (has_upper, "Uppercase letters (A-Z)"),
        (has_lower, "Lowercase letters (a-z)"),
        (has_num, "Numbers (0-9)"),
        (has_special, f"Special characters ({special_ch})")]
    
    score = sum(1 for met, label in dict if met)
    print("\n--- PASSWORD STRENGTH ---")
    
    if not leng:
        print("Strength: INVALID ")
        print("Please Enter password between 8-20 characters !!")
    else:
        if score == 4:
            print("Strength: STRONG ")
        elif score == 3:
            print("Strength: MEDIUM ")
        else:
            print("Strength: WEAK ")
        if score < 4:
            print("\nTo improve your score, include:")
            for met, label in dict:
                if not met:
                    print(f" [ ] {label}")


password =input("Enter your password between 8-20 characters\nIt should contain atleast one uppercase character\nIt should contain atleast one lowercase character \nIt should contain atleast one number\n \n Pass :")
pass_complexity_chck(password)
