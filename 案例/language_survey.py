import survey


#定义一个问题，并创建一个表示调查的AnonymousSurvey对象
question="What language did you first learn to speak ?"
my_survey=survey.AnonymousSurvey(question)

#显示问题并存储答案
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    respone=input('Language: ')
    if respone == 'q':
        break
    my_survey.store_response(respone)

print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()