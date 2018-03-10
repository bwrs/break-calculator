import breakcalc2 as bc2
from matplotlib import pyplot
import numpy as np
from fractions import Fraction
from matplotlib.ticker import NullFormatter

### NOTA OPTIME: MUST TAKE INPUTS AS int OR Fraction
def optimalchartargs(max_rounds=12,break_proportion_step=Fraction(1,250000),max_break_proportion=Fraction(1,1),min_break_proportion=Fraction(1,1000),per_room=4):
    args=[]
    styles=["b-","r-","g-"]
    for rounds in range(1,max_rounds+1):
        args.append(np.arange(min_break_proportion,max_break_proportion+break_proportion_step,break_proportion_step))
        results=[]
        for prop in args[-1]:
            points,chance=bc2.identify(rounds,1,prop*per_room)
            results.append(float(points+chance))
        args.append(np.array(results))
        args.append(styles[rounds%len(styles)])
    return args

def optimalchartdraw(args,fname="optimalchart.png",typex="log"):
    pyplot.figure(figsize=(8.27,11.69),dpi=600)
    pyplot.plot(*args,linewidth=0.5)
    pyplot.grid(True,"both")
    pyplot.minorticks_on()
    pyplot.xscale(typex)
    if typex=="logit":
        pyplot.gca().xaxis.set_minor_formatter(NullFormatter())
    pyplot.title("Break Calculator with {} x axis".format(typex))
    pyplot.savefig(fname,dpi=600)

### NOTA OPTIME: MUST TAKE INPUTS AS int OR Fraction
def optimalchart(fname="optimalchart.png",max_rounds=12,break_proportion_step=Fraction(1,250000),max_break_proportion=Fraction(1,1),min_break_proportion=Fraction(1,1000),per_room=4,typex="log"):
    args=optimalchartargs(max_rounds,break_proportion_step,max_break_proportion,min_break_proportion,per_room)
    optimalchartdraw(args,fname,typex)

args=optimalchartargs()
optimalchartdraw(args,fname="optimalchartlog.png",typex="log")
optimalchartdraw(args,fname="optimalchartlogit.png",typex="logit")
