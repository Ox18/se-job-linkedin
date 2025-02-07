def suggestJobAdapter(data):
    content = data['searchDashReusableTypeaheadByBlended']

    items = []

    elements = content['elements']

    for element in elements:
        item = {
            'name': element['title']['text'],
            'trackingId': element['trackingId'],
            'id': element['trackingUrn'].split(':')[-1],
        }
        items.append(item)

    return items