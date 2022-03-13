<!DOCTYPE html>
<html>
<head>
    <title>Necesito un titulo para esto</title>
</head>

<body>
    %print(aQuestions)
    %if(len(aQuestions) > 0):
        %for i in aQuestions:
            %number = i["question_number"]
            %question = i["question"]
            %answer = i["answer"]
            <p>{{number}}.- ¿{{question}}?</p>
            <p>  - {{answer}}</p>
        %end
    %else:
        <p>Parece que no hay respuestas actualmente, ¿que tal si contestas una?</p>
    %end
</body>

</html>
    