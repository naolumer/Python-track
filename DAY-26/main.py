# coding exercises related to list and dictionary comprehension

sentence= "What Is The Air speed Velocity Of An Unladen Swallow"
senlis= sentence.split()
# print(senlis)


result={word:len(word) for word in senlis}
# print(result)

weather_c= {"Monday":12,
            "Tuesday":14,
            "Wednesday":15,
            "Thursday":14,
            "Friday":21,
            "Saturday":22,
            "Sunday":24}

weather_f={ days:(int(temp)*9/5)+32 for (days,temp) in weather_c.items()}
# print(weather_f)

# Looping through dictionaries
dict= {"Student": ["Angela","Carla","Jack"],
            "Score": [55,65,78]}

for (key,value) in dict.items():
    print(key,value)

import pandas

student_data_frame= pandas.DataFrame(dict)
# print(student_data_frame)

for (index,row) in student_data_frame.iterrows():
    print(row.Student)


