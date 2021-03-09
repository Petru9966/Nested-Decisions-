#Ask user  what to do
print("What activity should I do (play/study)?")
activity=input()
#decide if beep should play or study
if(activity=="play"):
  #ask user what to play with
  print("What should I play with(toy/friend)?")
  play_with=input()
#decide if beep should playwith toys or friends
  if(play_with=="toy"):
    print("I will play with my toys")
  else:
    print("I will play with my friend")
else:
  print("I will study")



