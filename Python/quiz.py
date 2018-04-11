import pandas as pd
import numpy as np

#### A simple quiz program
question_dict={"What's the current year?":"2018","Who is the current president of the USA?":"Donald Trump/Trump","Where's the headquarters of UN located?":"New York","Name the biggest slum in the world":"Dharavi"}

result_status={"Success":"Congratulations!! You got it right!!","Failure":"Oops! You got it wrong!! Better luck next time"}
print("It's quizz time!!")

score=0;

for q in question_dict:
	status=None
	print (q,question_dict[q])
	ans=input()
	if ans.lower()==question_dict[q].lower():
		status="Success"
		print ("*****",result_status[status],"******")
		score+=1
	else :
		status="Failure"
		print ("*****",result_status[status],"******")		
print ("Your final score :",score)