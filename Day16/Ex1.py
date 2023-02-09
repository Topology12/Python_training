gold = {"US": 46, "Fiji": 1, "Great Britain": 27, "Cuba": 5, "Thailand": 2, "China": 26, "France": 10}
country = ["Fiji", "Chile", "Mexico", "France", "Norway", "US"]
country_gold = []
value_false = 'Did not get gold'

for x in country:
    try:
      country_gold.append(gold[x])
    except Exception as e:
        country_gold.append(value_false)

print(country_gold)