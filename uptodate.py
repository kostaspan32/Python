dict = 'Management for the prevention of recurrent gout flares and damage to joints and other tissues from urate crystal deposition includes drug therapy, lifestyle modifications, and other strategies for risk reduction. Gout is monosodium urate (MSU) crystal deposition disease; the symptoms and signs of gout do not occur in the absence of urate saturation of extracellular fluids, which is reflected by hyperuricemia (serum urate levels >6.8 mg/dL [405 micromol/L]), urate crystal deposition, and inflammatory responses to crystal deposition. Long-term maintenance of subsaturating urate levels results in cessation of gout flares, resolution of tophi, and improvement in patient physical function and health-related quality of life.'

my_list = list(dict)


counter = {
}

for letter in my_list:
    counter[letter] = 1

for letter in my_list:
    counter[letter] += 1

counter[' '] = 0

for key in counter.keys():
    if counter[key] == max(list(counter.values())):
        print(key)

print(counter)



