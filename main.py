# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

player_0 = 'Ruud Gullit'
player_1 = 'Marco van Basten'

goal_0 =  32
goal_1 =  54

a = player_0 + " " + str(goal_0) + ","
b = player_1 + " " + str(goal_1)

scorers = (a + " " + b)
print (scorers)

c = player_0 + " scored in the " + str(goal_0) + "nd minute"
d = player_1 + " scored in the " + str(goal_1) + "th minute"

report = c + '\n' + d
print (report)

player = 'Jan Wouters'

s = player.find(" ")
o = slice(s)
first_name = (player[o])
print (first_name)


l = len(player)
last_n = slice(s+1,l)
last_name = (player[last_n])
print (last_name)

last_name_len = len((player[last_n]))
print (last_name_len)

name_short = (player[slice(1)]) + "." + " " + last_name
print (name_short)


first_name_len = len((player[o]))
chant_a = (first_name + "!" + " " ) * first_name_len 
chant = chant_a [:-1]


print (chant) 

good_chant = (chant[-1] is not " ")


print (good_chant)
