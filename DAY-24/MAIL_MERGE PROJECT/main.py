SAMPLE= "[name]"

with open("./DAY-24/MAIL_MERGE PROJECT/INPUT/NAMES/invited_names.txt") as name_list:
    list_name= name_list.readlines()

with open("./DAY-24/MAIL_MERGE PROJECT/INPUT/LETTERS/Starting_letter.txt") as letter:
    letter_str= letter.read()
    for name in list_name:
        stripped_name= name.strip()
        new_letter=letter_str.replace(SAMPLE, stripped_name)
        
        with open(f"./DAY-24/MAIL_MERGE PROJECT/OUTPUT/READY_TO_SEND/letter_for_{stripped_name}.txt",mode="w") as final_letter:
            final_letter.write(new_letter)
        
