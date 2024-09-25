def all_variants(text):
    for t in range(len(text) + 1):
        for j in range(t, len(text) + 1):
            yield text[t:j]


a = all_variants("abc")
for i in a:
    print(i)
