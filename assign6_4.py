animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}   #值都是列表

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')


def biggest(Dict):
    k, v = [], []
    for key, value in Dict.items():
        k.append(key)
        v.append(len(value))
    return k[v.index(max(v))]

print(biggest(animals))
