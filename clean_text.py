def cleaned(text):
    final_text=[]
    text1=text.split("\n")
    for t in text1:
        if t.strip():
            final_text.append(t)
    return final_text        
