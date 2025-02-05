import requests

class LinkedinApiGateway:
    def getForm(self, form_id, call: requests.Session):
        print(call.cookies)
        url = 'https://www.linkedin.com/voyager/api/graphql?variables=(jobPostingUrn:urn%3Ali%3Afsd_jobPosting%3A4136117673)&queryId=voyagerJobsDashOnsiteApplyApplication.1e0753b642bdc5f84b0d2652f2080958'

        response = call.get(url)

        return response.json()