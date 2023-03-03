 # 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lower_name1 = name1.lower()
lower_name2 = name2.lower()

name_t_count = lower_name1.count("t") +  lower_name2.count("t")
name_r_count = lower_name1.count("r") +  lower_name2.count("r")
name_u_count = lower_name1.count("u") + lower_name2.count("u")
name_e_count = lower_name1.count("e") + lower_name2.count("e")
true_count = name_t_count + name_r_count + name_u_count + name_e_count

name_l_count = lower_name1.count("l") + lower_name2.count("l")
name_o_count = lower_name1.count("o") + lower_name2.count("o")
name_v_count = lower_name1.count("v") + lower_name2.count("v")
name_e_count = lower_name1.count("e") + lower_name2.count("e")
love_count = name_l_count + name_o_count + name_v_count + name_e_count

score = str(true_count) + str(love_count)

if int(score) < 10 or int(score) > 90:
    print (f"Your score is {score}, you go together like coke and mentos.")
elif int(score) >= 40 and int(score) <= 50:
    print (f"Your score is {score}, you are alright together.")
else:
    print (f"Your score is {score}.")