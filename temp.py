import requests


def api(movie):
    #print(f'Movie:  {movie}')
    response = requests.get((
        f'https://imdb-api.com/API/AdvancedSearch/k_xh28yu6n/?title="{movie}"')).json()
   # print(response['results'][0]['image'])
    imageURLList = [] # list of returned image urls
    for url in response['results']:
        imageURLList.append(url['image'])

    #print(imageURLList)
    return imageURLList[0]
    # print(response)


#print(api("avatar")[0])
# print(api(1))
