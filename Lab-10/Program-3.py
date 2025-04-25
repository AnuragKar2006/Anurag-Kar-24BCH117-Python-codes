def create_vcard():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email (optional): ")
    org = input("Enter Organization (optional): ")

    vcard = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL;TYPE=CELL:{phone}"""

    if email:
        vcard += f"\nEMAIL:{email}"
    if org:
        vcard += f"\nORG:{org}"

    vcard += "\nEND:VCARD"

    filename = name.replace(" ", "_") + ".vcf"
    try:
        with open(filename, "w") as f:
            f.write(vcard)
        print(f"V-card '{filename}' created successfully.")
        print(f"You can import this file into your mobile contacts.")
    except Exception as e:
        print(f"Error creating v-card file: {e}")

create_vcard()