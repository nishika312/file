f= open("nishika.txt","w")
f.write("my name is nishika""\n""I am from delhi""\n""I am persuing graduation in B.A. program from delhi university""\n"
        "IMy hobby is watchin web series,reading books,photography""\n""My mother is housewife""\n""My father has his own work" )


l=[]
f=open("nishika.txt","r")
l.append(f.readlines())
print(l)