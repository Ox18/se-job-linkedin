import requests
from shared.utils.cache import cache

class LinkedinApiGateway:
    def getFormJob(self, jobPostingId, call: requests.Session):
        url = f'https://www.linkedin.com/voyager/api/graphql?variables=(jobPostingUrn:urn%3Ali%3Afsd_jobPosting%3A{jobPostingId})&queryId=voyagerJobsDashOnsiteApplyApplication.1e0753b642bdc5f84b0d2652f2080958'


        exist_in_cache = cache.get(url)

        if exist_in_cache:
            return exist_in_cache

        response = call.get(url)

        cache.set(url, response.json(), timeout=60*60*24)

        data = response.json()

        return data['data']