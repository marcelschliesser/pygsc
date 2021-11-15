import json
from fuzzywuzzy import fuzz

def load_json_data(filename):
    """Die Funktion lädt die Datei input.json in den Arbeitsspeicher."""
    json_data = open(filename)
    data = json.load(json_data)
    json_data.close()
    return data

def calc_threshold(data):
    """Diese Funktion berechnet den Brand-Schwellwert."""
    words = []
    data = load_json_data('input.json')
    for i in data['rows']:
        words_i = i['keys'][0].split(' ')
        for x in words_i:
            words.append(x)
    words = sorted(set(words))
    for y in words:
        result = fuzz.ratio(y, 'tchibo')
        print('{},{},{}'.format(y, result, result - 67))

def determine_brand(data):
    """Diese Funktion interiert über den Datensatz und bestimmt pro Zeile den Brandcharakter."""
    out = []
    data = load_json_data('input.json')
    for i in data['rows']:
        res = []
        for x in i['keys'][0].split(' '):
            res.append(fuzz.ratio(x, 'tchibo') -67)
        i['brand'] = max(res) >= 0
        print(i)
        out.append(i)
    return out

def calc_non_brand_ratio(data):
    """Diese Funktion berechnet das NonBrand-Verhältnis des Datensatz."""
    nonbrand_clicks = 0
    brand_clicks = 0
    for i in data:
        if i['brand']:
            brand_clicks += i['clicks']
        else:
            nonbrand_clicks += i['clicks']
    return (brand_clicks, nonbrand_clicks, (nonbrand_clicks/(nonbrand_clicks + brand_clicks)))

def main():
    data = load_json_data('input.json')
    calc_threshold(data)
    data = determine_brand(data)
    ratio = calc_non_brand_ratio(data)
    print(ratio)

if __name__ == '__main__':
    main()