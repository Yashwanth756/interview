from record_analyze import *
from fetch_questions import *
while True:
    text_to_speech('Please tell me the related category you want to train')
    userCategory = listen_and_transcribe()
    if userCategory is None:
        continue

    text_to_speech(f'choose the level for {userCategory} like easy, medium, hard ')
    userLevel=listen_and_transcribe()
    if userLevel is None:
        continue


    gqa = GenerateQuestions(userCategory, userLevel).questions
    questionAnswers = gqa[list(gqa.keys())[0]]
    # print(questionAnswers[list(questionAnswers.keys())[0]])

    score = [0]*len(questionAnswers)
    
    for i, qa in enumerate(questionAnswers):
        question = qa['question']
        solution = qa['solution']
        print('question is \n',question)
        text_to_speech(question)
        userSol = listenTranscribe(str(i))

        if userSol == 'abort':
            print((round(sum(score), 4)/len(questionAnswers))*100)
        elif userSol == 'skip':
            continue
        else:
            score[i]=evaluate2(str(solution), str(userSol))
        
        # print(qa)
        print('*'*50,'\n\n')
    print(score)
    print((round(sum(score), 4)/len(questionAnswers))*100)




