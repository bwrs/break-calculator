import fractions
Frac=fractions.Fraction

def generate_data(rounds,per_room=4):
    if rounds==0: return [1]
    else:
        l=generate_data(rounds-1,per_room)
        return [sum(l[max(0,i):i+per_room]) for i in range(1-per_room,len(l))]

def identify(rounds,rooms,breaking_teams,per_room=4):
    if breaking_teams>=per_room*rooms: return (0,Frac(1,1))
    data=generate_data(rounds,per_room)
    breaking_teams=Frac(breaking_teams*sum(data),rooms*per_room)
    while breaking_teams>data[-1]:
        breaking_teams-=data.pop()
    return (len(data)-1,Frac(breaking_teams,data[-1]))

if __name__=="__main__":
    rounds=int(input("How many rounds? "))
    rooms=int(input("How many rooms? "))
    breaking_teams=int(input("How many breaking teams? "))
    per_room=int(input("How many teams per room? "))
    borderline_points,proportion=identify(rounds,rooms,breaking_teams,per_room)
    print("Teams with {} or fewer points are not likely to reach the final.".format(borderline_points-1))
    print("Teams with {} points have (according to estimations) a {}% chance of reaching the final.".format(borderline_points,float(proportion*100)))
    print("Teams with {} or more points are highly likely to reach the final.".format(borderline_points+1))
