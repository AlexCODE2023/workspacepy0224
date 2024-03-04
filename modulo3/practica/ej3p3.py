import re
def busueda(text:str,pat):
    #hola = r("hola")
    if pat in text:
        return (text.count(pat),re.findall(pat,text))
    else:
        return (0,[])

def cortar (text:str,a:int,b:int):
    return text[a:b]

def cortarOrac(text:str):
    text2 = text.strip().split(".")
    text2.remove("")
    return text2

def contarPalabras(text:str):
    arr = text.split(" ")
    return dict(enumerate(arr))
text = """
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
"""

print(contarPalabras(text))
print(cortarOrac(text))
print(busueda(text,"Lorem"))
print(cortar(text,0,10))