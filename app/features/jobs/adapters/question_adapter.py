import json
class Question:
    text:str = ""
    required:bool = False
    type:str = ""
    ruler:str = ""
    urn:str = ""
    choices: list[str] = []

def formAdapter(data):

    ## save in json
    with open('data.json', 'w') as f:
        json.dump(data, f)

    post = data.get('jobsDashOnsiteApplyApplicationByJobPosting', {})

    element = post['elements'][0]

    jobApplicationForms = element['jobApplicationForms']


    questions: list[Question] = []

    for form in jobApplicationForms:
        questionGroupings = form['questionGroupings']

        for questionGroup in questionGroupings:

            ## check if formSection is Null
            if not questionGroup.get('formSection'):
                continue

            formSection = questionGroup['formSection']

            formElementGroups = formSection['formElementGroups']

            for formElementGroup in formElementGroups:
                formElements = formElementGroup['formElements']

                for formElement in formElements:
                    # text = formElement['title']['text']
                    # questions.append(text)
                    question = Question()
                    question.text = formElement['title']['text']
                    question.required = formElement['required']
                    question.type = formElement['urn'].split(":")[-1].split("_")[-1].split("(")[-1].split(",")[-1].split(")")[0]
                    question.ruler = formElement['requiredFieldMissingErrorText']['text']
                    question.urn = formElement['urn']

                    if question.type == "multipleChoice":
                        choices = []
                        options = formElement['formComponentResolutionResult']['textEntityListFormComponent']['textSelectableOptions']
                        for option in options:
                            choices.append(option['optionText']['text'])
                        question.choices = choices

                    questions.append(question.__dict__)
                
    return {
        'questions': questions
    }
