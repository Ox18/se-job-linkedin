import requests
from shared.utils.cache import cache
from shared.adapters.linkedin.geo_adapter import geoAdapter
from shared.adapters.linkedin.suggest_job_adapter import suggestJobAdapter

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
    
    def geo(self, keywords, call: requests.Session):
        url = f'https://www.linkedin.com/voyager/api/graphql?variables=(keywords:{keywords},query:(typeaheadFilterQuery:(geoSearchTypes:List(POSTCODE_1,POSTCODE_2,POPULATED_PLACE,ADMIN_DIVISION_1,ADMIN_DIVISION_2,COUNTRY_REGION,MARKET_AREA,COUNTRY_CLUSTER)),typeaheadUseCase:JOBS),type:GEO)&queryId=voyagerSearchDashReusableTypeahead.54529a68d290553c6f24e28ab3448654'
        key = f'geo_search_{keywords}'

        exist_in_cache = cache.get(key)

        if exist_in_cache:
            return exist_in_cache
        
        response = call.get(url)

        response = response.json()

        data = geoAdapter(response['data'])

        cache.set(key, data, timeout=60*60*24)

        return data
    
    def suggestJob(self, keywords, call: requests.Session):
        url = f'https://www.linkedin.com/voyager/api/graphql?variables=(keywords:{keywords},query:(typeaheadUseCase:JOBS))&queryId=voyagerSearchDashReusableTypeahead.898e3049ac3b133a04b5748430261aae'
        key = f'suggest_job_{keywords}'

        exist_in_cache = cache.get(key)

        if exist_in_cache:
            return exist_in_cache

        response = call.get(url)

        response = response.json()

        data = suggestJobAdapter(response['data'])

        cache.set(key, data, timeout=60*60*24)
        
        return data