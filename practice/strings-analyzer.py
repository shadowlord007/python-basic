#######String analyzer##########
user_string = str(input("Enter a string: "))
count_string = len(user_string)
vowels = "aeiouAEIOU"
count_vowels = 0
for char in user_string:
    if char in vowels:
        count_vowels += 1

sub_String = "python"
contain_sub_String = sub_String in user_string


upper_case = user_string.upper()
lower_case = user_string.lower()

print("\n-------String Analyzer-------")
print(f"The string has {count_string} characters.")
print(f"The string has {count_vowels} vowels.")
print(f"The string contains the substring '{sub_String}'? {contain_sub_String}")
print(f"The string in upper case: {upper_case}")
print(f"The string in lower case: {lower_case}")
