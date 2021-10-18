depts = {
            "sci": 99,
            "eng": 99,
            "lab": 99
        }

info = input("Department: ")
infos = depts.get(info)
cut_off = int(input("UTME Score: "))
if cut_off < infos:
    print("fail")
else:
    print("pass")

#    dept = depts.get(cut_off)
#    dept *= 2
#    if dept > cut_off:
#        print("fail")
#    else:
#        print("pass")