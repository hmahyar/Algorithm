def palindromes(text):
    text = text.lower()
    results = []

    for i in range(len(text)):
        for j in range(i):
            chunk = text[j:i + 1]
            if chunk == chunk[::-1]:
                results.append(chunk)
    
    return text.index(max(results, key=len)), results

a,b= palindromes('123443265')
print a
print b 