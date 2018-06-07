# Idea 3 --- Grapher

## The need, the user, and you
**This section describes whom the project would serve and why you're interested
in the project.**


### What's the need?
_What need is met by your idea? Who are you helping? What is that person's
experience like now? How would their experience improve if you could help 
them?_
Many scientists, from economists to mathamaticians, they have a need to graph there data out in a plot, so that they could present their research visually. In many cases, they will be troubled by the graphers in common softwares such as Microsoft Excel and Numbers. These softwares are either too difficult to use or limited in functions. And many of these scientists or researchers will waste time in simply graphing data out. For those who have the need to present data viusally while have difficulties using these common softwares, it would be best for them to use a DSL to graph data out. With the help of this DSL, they will improve their efficiency greatly.

### Why you?
_What excites you about this idea? How did you come up with it?_
I came up this idea when I was completing my caculus projects, which requires me to draw a diagram with two sets of data. I thought,_it would be lot more convenient if i can draw a grph using simpler tools._ At last, I plot the diagram with the help of a Python library --- matplotlib.

### Domain
_Describe the project's domain in five words._
A Graphing tool for researchers.

## The language
**This section helps you argue that a DSL can serve the need(s) described in
the previous section.**

### Why a language?
_Why is a DSL appropriate for your user(s)? How does it address the need?_
For researchers that wants to make diagrams, a DSL will be appropriate for them because it provides a simpler syntax. A DSL may address the need by improving the efficiency of typing codes.

### Linguistic pieces
**For each question below, brainstorm a few answers. If a question does not
apply to your project, explain why.**

_What are some likely nouns in this domain? (Nouns correspond to kinds of
data. In our image manipulation DSL, an **image** is a noun.)_
graph, color, trigonometry, logistics, labels, axis, units, limits, maximum/minimum

_What are some likely adjectives? (Adjectives correspond to values for a
particular kind of data; for example: a **JPEG** image.)_ 
- a **cartisian/polar** form
- a **PNG** image
- **red/green/blue** color
- **two/three dimensional**
- **infinite** range

_What are some likely verbs? (Verbs correspond to behaviors or actions; for
example: **rotating**.)_
- plot, add/delete, rotate, intersect, truncate, move, equate, extend

_What are some likely adverbs? (Verbs correspond to modifications to a specific
behavior or action; for example: rotating **left**.)_
- zoom in/zoom out
- 


### Expressiveness
_What should be easy to do in this language? What should be possible, but
difficult? What should be impossible or very difficult?_
It should be quite easy to draw the diagram for some equations such as ```y = sinx```,```y = 1/x```,```y = x```, ``` y = e^x```. It would be more difficult to plot more complex equtions. It would be nearly impossible to plot some 3D equations such as ``` x^3 + y^3 + z^3 = 0```

### Related work
_Are there any other DSLs in this domain? If not, describe how you know there
aren't and conjecture why not. If so, describe them and provide links. How well
do they address the need? What do you like about the language? Are there parts
of the language you think could be improved?_
- Mathamatica and Wolfram languages. I think this is the best DSL now because it can convert natural languages into commands. However, it is quite expensive to get a complete version of this software
- matlab
-Python Library, matplotlib. I think I can improve this library becasue it involves some annoying language features.

## The Project
**This section examines whether the idea makes for a good project for this
course.**

### Suitability
_If someone were to work on this project, what percentage of their time would be
spent directly engaging in the **language** aspects of this project (e.g.,
making language-design decisions), as opposed to "systems" aspects of the
project (e.g., implementing a complicated visualization that doesn't require a
lot of language design)?_


### Scope
_How ambitious is this project for you? Not very? Somewhat? Very?_
This is quite ambitious for me because I don't know how a grapher work. How could it transfer a equation to a plot? Also, I have little knowledge in designing the syntax for this DSL.

### Benefits and drawbacks
_Why might this be a good idea for a project?_ 
- I will probably learn a lot of things through implementing this DSL
- I might be able to gain help from this DSL if I successfully create it

_Why might this not be a good idea project?_
- There are so many related works, and it is quite difficult to make this DSL creative from existing works.
- I will probably meet many difficulties in making this DSL
