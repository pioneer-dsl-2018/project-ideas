[diagram]: Physics_Lab_6.eps
[code]: lab6.ipynb
# Idea 1 Physics Circuit Diagram Drawer

## The need, the user, and you
**This section describes whom the project would serve and why you're interested
in the project.**


### What's the need?
_What need is met by your idea? Who are you helping? What is that person's
experience like now? How would their experience improve if you could help 
them?_
Physics students always have the need to draw circuit diagrams. Typically, they will use professional graphics softwares such as photoshops or AutoCAD. However, there are students who are not familiar with those elusive softwares and they will waste a lot of time making a simple diagram with those softwares. They need a light-weight and simple program to help them draw the circuit diagram. A DSL may solve this problem easily.
The user of this DSL will be physics students who are not good at using professional graphing softwares. They now waste a lot of time installing, setting and learning those softwares. With the help of this DSL, they might make a circuit diagram lot more efficiently.

### Why you?
_What excites you about this idea? How did you come up with it?_
I came up this idea when I was writing my physics lab report. I search for ways to draw physics circuit diagrams. At last, I discovered a Python library called ```SchemDraw```, which could draw circuit diagrams easily. So I installed the packages on my computer and successfully drew my [diagram][diagram]. Even though it’s quite convenient to draw diagrams with this library, there are still some annoying features with this library.

[The code to make this diagram][code]

### Domain
_Describe the project's domain in five words._
Circuit Diagrams for new computer users.

## The language
**This section helps you argue that a DSL can serve the need(s) described in
the previous section.**

### Why a language?
_Why is a DSL appropriate for your user(s)? How does it address the need?_
Because my users are not familiar with professional graphic softwares, it is reasonable to assume that they cannot program as well. A DSL with simple syntax may complete this task well. It helps the user by making the syntax simpler and more direct.

### Linguistic pieces
**For each question below, brainstorm a few answers. If a question does not
apply to your project, explain why.**

_What are some likely nouns in this domain? (Nouns correspond to kinds of
data. In our image manipulation DSL, an **image** is a noun.)_
Capacitors, inductors, resistors, LEDs, Voltmeter, Ammeter . . .

_What are some likely adjectives? (Adjectives correspond to values for a
particular kind of data; for example: a **JPEG** image.)_ 
The output may be a **JPEG** or a **PNG** image
The size of some elements, fonts may be **large** or **small**


_What are some likely verbs? (Verbs correspond to behaviors or actions; for
example: **rotating**.)_
Import, add, save, rotates, delete, labeling, reverse, flip, color, customize, extends



_What are some likely adverbs? (Verbs correspond to modifications to a specific
behavior or action; for example: rotating **left**.)_
Add labels/elements on the **left/right**
Elements are connected in series/in parallel

### Expressiveness
_What should be easy to do in this language? What should be possible, but
difficult? What should be impossible or very difficult?_
It should be easy to draw simple circuits that contains a few elements

### Related work
_Are there any other DSLs in this domain? If not, describe how you know there
aren't and conjecture why not. If so, describe them and provide links. How well
do they address the need? What do you like about the language? Are there parts
of the language you think could be improved?_

There should be more related works in this area besides “SchemDraw”. For example the “logisim” introduced in the generating idea file. Different from a language, “logisim” achieve its purpose by creating a GUI, which is better than a language in some features. However, it is quite difficult to connect wires in “logisim”, so I may be able to improve this part in my DSL.


## The Project
**This section examines whether the idea makes for a good project for this
course.**

### Suitability
_If someone were to work on this project, what percentage of their time would be
spent directly engaging in the **language** aspects of this project (e.g.,
making language-design decisions), as opposed to "systems" aspects of the
project (e.g., implementing a complicated visualization that doesn't require a
lot of language design)?_
The user should spend more time directly engaging in the language aspect, because this DSL achieve its purpose solely by user input languages. Therefore, approximately 90 percent of their time will be spent on language aspect.

### Scope
_How ambitious is this project for you? Not very? Somewhat? Very?_
For me, it is quite ambitious to build this project, because I have no previous experience in making a own DSL before. And I am still not very good at writing codes in Scala. Although I knew some general steps in making a DSL in the group meeting, I still don’t know how to achieve each steps. For example, the first step of implementing a DSL is making a Library, but I don’t know how to make a library that can output circuit diagrams.

### Benefits and drawbacks
_Why might this be a good idea for a project?_ 
I will learn many computer science skills through working on this project. The project itself may help me in my future physics courses. 


_Why might this not be a good idea project?_

Designing the syntax maybe difficult, because there are lots of nouns and verbs in this domain. Also, there might be many related work in this domain, so I should avoid making my project too similar to those exists.
