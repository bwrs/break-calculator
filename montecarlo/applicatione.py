# coding=utf-8

import kivy
from numpy.random import shuffle as 𐎣

𐎠𐎶=range
𐎠𐎷=len
#𐎠𐎸
#𐎠𐎹
𐎠𐎺=1
𐎠𐎻=list
𐎠𐎼=set
𐎠𐎽=str
𐎠𐎾=sorted
𐎠𐎿=__name__
#𐎠𐏀
𐎠𐏁=int
𐎠𐏂=bool

from operator import add
from itertools import chain
import decimal as 𐎠
𐎠.getcontext().prec=3
𐎡=𐎠.Decimal

from kivy.app import App as 𐎠𐎤
from kivy.uix.button import Button as 𐎠𐎦
from kivy.uix.gridlayout import GridLayout as 𐎠𐎧
from kivy.uix.label import Label as 𐎠𐎨
from kivy.uix.textinput import TextInput as 𐎠𐎩

class 𐎠𐎮(𐎠𐎤):
    def build(𐎠𐎸):
        𐎠𐎬 = 𐎠𐎬 = 𐎠𐎧(cols=𐎠𐎺+𐎠𐎺,padding=(𐎠𐎺+𐎠𐎺)*((𐎠𐎺+𐎠𐎺)*(𐎠𐎺+𐎠𐎺)+𐎠𐎺))
        𐎨 = ["rooms: ", "rounds: ", "breaking teams: "]
        
        global 𐎦
        𐎦,𐎧 = {},{}
        
        for 𐏃 in 𐎠𐎶(𐎠𐎷(𐎨)):
            𐎧[𐏃] = 𐎠𐎨(text="Number of "+𐎨[𐏃])
            𐎠𐎬.add_widget(𐎧[𐏃])
            𐎦[𐏃] =  𐎠𐎩(text='', multiline=𐎠𐏂(𐎠𐎺-𐎠𐎺))
            𐎠𐎬.add_widget(𐎦[𐏃])
        
        𐎠𐎸.𐎠𐎪 = 𐎠𐎨(text="")
        𐎠𐎬.add_widget(𐎠𐎸.𐎠𐎪)
        𐎠𐎭 = 𐎠𐎦(text="Compute")
        𐎠𐎬.add_widget(𐎠𐎭)
        𐎠𐎭.bind(on_press=𐎠𐎸.𐎠𐏀)
        return 𐎠𐎬

    def 𐎠𐏀(𐎠𐎸,𐎠𐎹):
        𐎠𐎸.𐎠𐎪.text = "\n.".join(𐎥(*[𐎠𐏁(𐎦[𐎠𐎫].text) for 𐎠𐎫 in 𐎠𐎶(𐎠𐎺+𐎠𐎺+𐎠𐎺)]))

def 𐎩(𐎲,𐎱):
    𐎲.sort()
    𐎳=[]
    for 𐎴 in 𐎠𐎶(𐎱):
        𐎳.append(𐎲[(𐎠𐎺+𐎠𐎺)*(𐎠𐎺+𐎠𐎺)*𐎴:(𐎠𐎺+𐎠𐎺)*(𐎠𐎺+𐎠𐎺)*𐎴+(𐎠𐎺+𐎠𐎺)*(𐎠𐎺+𐎠𐎺)])
    return 𐎳

def 𐎰(𐎶,𐎵):
    𐎫=[]
    𐎷=𐎩(𐎶,𐎵)
    for 𐎢 in 𐎠𐎶(𐎠𐎷(𐎷)):
        𐎣(𐎷[𐎢])
        for 𐎪 in 𐎠𐎶((𐎠𐎺+𐎠𐎺)*(𐎠𐎺+𐎠𐎺)):
            𐎫.append(𐎷[𐎢][𐎪]+𐎪)
    return 𐎫

def 𐎬(𐎭,𐎮,𐎯):
    𐎸=[𐎠𐎺-𐎠𐎺 for 𐎹 in 𐎠𐎶(𐎭*(𐎠𐎺+𐎠𐎺)*(𐎠𐎺+𐎠𐎺))]
    for 𐎹 in 𐎠𐎶(𐎮): 𐎸=𐎰(𐎸,𐎭)
    𐎸.sort()
    𐎺=𐎸[-𐎯]
    return (𐎺,𐎸[-𐎯:].count(𐎺),𐎸.count(𐎺))

def 𐎻(𐎼,𐎽,𐎾,𐎿):
    𐏀={}
    for 𐏁 in 𐎠𐎶(𐎿):
        𐏂=𐎬(𐎼,𐎽,𐎾)
        if 𐏂 in 𐏀:
            𐏀[𐏂]+=𐎠𐎺
        else:
            𐏀[𐏂]=𐎠𐎺
    return 𐏀

def 𐏈(𐏉):
    𐏋=𐎠𐎼([𐏊[𐎠𐎺-𐎠𐎺] for 𐏊 in 𐏉])
    𐏍={𐏌:𐎡(𐎠𐎺-𐎠𐎺) for 𐏌 in 𐏋}
    for 𐏎 in 𐎠𐎻(𐏉):
        for 𐏏 in 𐏋:
            if 𐏎[𐎠𐎺-𐎠𐎺]<𐏏:
                𐏍[𐏏]+=𐏉[𐏎]
            elif 𐏎[𐎠𐎺-𐎠𐎺]==𐏏:
                𐏍[𐏏]+=(𐎡(𐏉[𐏎]*𐏎[𐎠𐎺])/𐎡(𐏎[𐎠𐎺+𐎠𐎺]))
    return 𐏍

def 𐎠𐎰(𐎠𐎱,𐎠𐎥):
    𐎠𐎲=𐏈(𐎠𐎱)
    𐎠𐎳=[]
    for 𐎠𐎴 in 𐎠𐎾(𐎠𐎻(𐎠𐎲)):
        𐎠𐎳.append("Teams with "+𐎠𐎽(𐎠𐎴)+" points have a "+𐎠𐎽(𐎡((((𐎠𐎺+𐎠𐎺)*((𐎠𐎺+𐎠𐎺)*(𐎠𐎺+𐎠𐎺)+𐎠𐎺))**(𐎠𐎺+𐎠𐎺))*𐎠𐎲[𐎠𐎴])/𐎡(𐎠𐎥))+"% chance of breaking.")
    return 𐎠𐎳
        
def 𐎥(𐎠𐎠,𐎠𐎡,𐎠𐎢):
    𐎠𐎵=(((𐎠𐎺+𐎠𐎺)*((𐎠𐎺+𐎠𐎺)*(𐎠𐎺+𐎠𐎺)+𐎠𐎺))**(𐎠𐎺+𐎠𐎺+𐎠𐎺))
    𐎠𐎣=𐎻(𐎠𐎠,𐎠𐎡,𐎠𐎢,𐎠𐎵)
    return 𐎠𐎰(𐎠𐎣,𐎠𐎵)

if 𐎠𐎿=='__main__':
    𐎠𐎮().run()
