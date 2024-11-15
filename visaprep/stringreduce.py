input_string=input().strip()
reduced_string=""
current_char=input_string[0]
count=1
for i in range(1,len(input_string)):
    if input_string[i]==current_char:
         count+=1
    else:
        reduced_string+=f"{current_char}{count}"
        current_char=input_string[i]
        count=1
reduced_string+=f"{current_char}{count}"
print(reduced_string)
