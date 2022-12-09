import random
time = ["Many years ago", "today", "1000 years ago", "yesterday"]
p_name = ["Shubhranshu", "Parth", "Novel", "shubh", "yuvraj"]
place = ["hotel", "countryside", "forest"]
food = ["omlettes", "chicken", "burger", "turkey"]
print(random.choice(time)+" "+random.choice(p_name)+" went to " +
      random.choice(place)+" and he ate "+random.choice(food))
