import breakcalc2 as bc

def representation(rounds,rooms,final_rooms,per_room=4):
    if final_rooms>=rooms:
        return "\\(0, 100\\%\\)"
    n,frac=bc.identify(rounds,rooms,final_rooms*per_room)
    return "\\({}, {}\\%\\)".format(n,int(frac*100))

def build_table(rounds,max_rooms,max_final_rooms,per_room=4):
    s="\\begin{tabular}{|c||"+("c|"*max_final_rooms)+"}\\hline\n"
    s+="    "+str(rounds)+"&"+"&".join([str(n) for n in range(1,max_final_rooms+1)])+"\\\\\\hline\\hline\n"
    for rooms in range(1,max_rooms+1):
        s+="    "+str(rooms)+"&"+"&".join([representation(rounds,rooms,i) for i in range(1,max_final_rooms+1)])+"\\\\\\hline\n"
    s+="\\end{tabular}"
    return s

def build_document(max_rounds,max_rooms,max_final_rooms,per_room=4):
    s="\\documentclass{article}\n\n\\begin{document}\n\\setcounter{section}{-1}\n"
    s+="\\section{How to use}\nNumbers in the top row of tables are the number of final rooms for the corresponding columns; numbers in the leftmost column of tables are the number of rooms for the corresponding rows; the section indicates the number of rounds, but this is also put in the top-leftmost cell.. If a cell of a table reads \\(k,x\\%\\), that means that one is very unlikely to break with fewer than \\(k\)) points, very unlikely not to break with more than \\(k\\) points, and has a \\(x\\%\\) chance of breaking with exactly \\(k\\) points.\n"
    s+="\\begin{center}\n"
    for rounds in range(1,max_rounds+1):
        s+="\\section{Debates with "+str(rounds)+" rounds}\n"
        s+=build_table(rounds,max_rooms,max_final_rooms,per_room)
    s+="\\end{center}\n"
    s+="\\end{document}"
    return s

if __name__=="__main__":
    max_rounds=int(input("Maximum number of rounds: "))
    max_rooms=int(input("Maximum number of rooms: "))
    max_final_rooms=int(input("Maximum number of final rooms: "))
    per_room=int(input("Number of teams per room: "))
    filename=str(input("Filename: "))
    f=open(filename,"w")
    f.write(build_document(max_rounds,max_rooms,max_final_rooms,per_room))
    f.close()
