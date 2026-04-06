list_of_scores=[5,2,3,6,7]
second_runner_up=list_of_scores[0]
winner=list_of_scores[0]
for x in list_of_scores:
    if x>winner:
       second_runner_up=winner
       winner=x
    elif x>second_runner_up and x!=winner:
     second_runner_up=x
print(second_runner_up)

        