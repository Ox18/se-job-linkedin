import json
class Question:
    text:str = ""
    required:bool = False
    type:str = ""
    ruler:str = ""
    urn:str = ""
    choices: list = []

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
            if questionGroup['questionGroupingType'] == 'RESUME':
                question = Question()
                question.text = questionGroup['customizedFormSection']['fileUploadFormSection']['title']
                question.required = True
                question.type = 'resume'
                question.urn = questionGroup['customizedFormSection']['fileUploadFormSection']['fileUploadFormElement']['formElementUrn']
                choices = []
                for resume in questionGroup['usedResumesResolutionResults']:
                    # choices.append(resume['resume']['resumeName'])
                    choice = {
                        'filename': resume['fileName'],
                        'urn': resume['entityUrn'],
                        # 'download_url': resume['downloadUrl']
                    }
                    choices.append(choice)
                question.choices = choices

                questions.append(question.__dict__)
                continue

            if not questionGroup.get('formSection'):
                continue

            formSection = questionGroup['formSection']

            formElementGroups = formSection['formElementGroups']

            for formElementGroup in formElementGroups:
                formElements = formElementGroup['formElements']

                for formElement in formElements:
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
