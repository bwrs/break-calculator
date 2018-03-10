# Break Calculator

`breakcalc2.py` is where the actual calculations occur. We used to use a Monte Carlo algorithm, and this is kept in the folder `montecarlo`. We now simulate an "ideal" debating competition (effectively, we assume that teams are no longer discrete entities, but rather, we permit fractions of teams, and so care only about proportions) thus:

With a total of t teams, b breaking teams, and r rounds as the parameters:

 - The program initialises itsour list of scores with 1 team on 0 and no others.
 - The program simulates each round by replacing each team with p points with one with p, one with p+1, one with p+2, and one with p+3.
 - The program then looks at the top b/t of the teams, and say that those ones "break". It is possible for a fraction of a team to break.
 - There is then a score s, such that all teams with >s points break, a proportion p of those with s points break, and all with <s do not.
 - The program returns s and p.

This should be interpreted by users thus:

 - If a team has >s points, it will very probably break.
 - If a team has s points, its chance of breaking is roughly p.
 - If a team has <s points, it is unlikely to break.

It is possible, especially in small competitions, for these odds to be somewhat incorrect. However, the output given by the program is usually roughly correct. (However, users should not decide to leave and not see who has broken based onthe output of the program.)

## Tabulation

`tabulator.py` was the first attempt at converting `breakcalc2.py`'s calculations into a portable form, namely a set of tables. It returns a `.tex` ((La)TeX) file, which can be converted into a PDF using the command `pdftex`. `bc2-12-36-6-4.pdf`, a sample output, is provided.

## Plotting

`pyplotter.py` produces, using `matplotlib`, a much more portable readout, namely a chart. Two such charts are provided, namely `optimalchartlog.png` and `optimalchartlogit.png`. They can be read thus:

 - For a competition with r rounds, one should look at the rth coloured line from the bottom (by default, the lowest is 1 round, and the highest is 12). Call this line l.
 - One should then calculate x=(breaking teams)/(total teams). Let the y value of the point on the line l with that x value be y.
 - If line l is vertical with x=(breaking teams)/(total teams), then y is the minimum y value of all the points of that line.
 - The boundary number of points, i.e. s from the description earlier, is then y rounded down to an integer. The chance of those with s points breaking is given by y-s.

This allows data for many possible competitions to be placed readably on one sheet of A4 paper. Settings can be changed, such as the precision with which points are plotted on the graph, the range of values plotted, &c.