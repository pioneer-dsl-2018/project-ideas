# Idea 1

## The need, the user, and you
**This section describes whom the project would serve and why you're interested
in the project.**


### What's the need?
_What need is met by your idea? Who are you helping? What is that person's
experience like now? How would their experience improve if you could help 
them?_

The domain this language would aim to cater to is mathematics. This project will essentially be a domain-specific language that will attempt to emulate certain complex functionalities of a scientific calculator (e.g. computing integrands or derivatives) as well as be able to apply more complex theories to solve mathematical problems which can’t be computed directly by most calculators (e.g. employing different theories to find the limit of a function). I believe that the need that could be met through this idea is to simplify the process of checking manual work for students and reducing time spent on arbitrary calculations for professionals. This language would also attempt to bring the inputs for the computation of complex problems closer to natural-language (e.g. a user being able input a request for an implicit differentiation instead of having to convert the equation to a y = form). As a student myself, I have often found myself trying to confirm my solution to a problem online due to the lack of a calculator being able to compute it directly (e.g. find the expression for a derivative rather than the derivative for a particular value of x); I believe that such a DSL could enhance that experience by enabling users to find the answers to otherwise complex problems. In addition to this, since scientific and graphing calculators can often be expensive and intricate to use, in my view, such a DSL might be able to increase access to and simplify the learning process for beginners by providing an enhanced calculator.

### Why you?
_What excites you about this idea? How did you come up with it?_

Mathematics is incontrovertibly a subject I thoroughly enjoy myself however when using a calculator, myself, I often find myself intrigued by the actual computations that go into the building of a sine function or the variety of rules that need to be input for a calculator to be able to compute the derivative, thus the prospect of being able to explore a variety of these in the construction of a DSL scientific calculator greatly fascinates me. In addition to this, I think there is a lot of potential in terms of the language design and bringing it closer natural language and mathematical terms hence I am also extremely enthusiastic at the idea of being able to explore what we learnt about linguistic design and implementation during the course.

I came up with this idea when I was studying for my finals and found myself confirming some of my math answers online. I think that if there existed a DSL to apply some more complex rules and be able to answer such questions, it could be greatly helpful to students.

### Domain
_Describe the project's domain in five words._

Calculus, Functions, Trigonometry, Mathematics, Education

## The language
**This section helps you argue that a DSL can serve the need(s) described in
the previous section.**

### Why a language?
_Why is a DSL appropriate for your user(s)? How does it address the need?_

This, to my understanding, would be a DSL for simulation in that it would enable users to save on time and effort. I think a programming language is appropriate for this purpose because it comes more naturally to the user to simply be able to instruct a computer to use a rule to perform a calculation. In addition to this, I think a DSL, particularly, is needed because of the many specific and complex operations and theorems that many mathematical fields have which thus are typically not functionalities available in general purpose programming languages. Since repetitive tasks can be readily defined and performed by DSLs, I believe this further adds to why it would be the appropriate medium to address this need.

### Linguistic pieces
**For each question below, brainstorm a few answers. If a question does not
apply to your project, explain why.**

_What are some likely nouns in this domain? (Nouns correspond to kinds of
data. In our image manipulation DSL, an **image** is a noun.)_

Number, Equation, Function, Angle, x-coordinate, y-coordinate

_What are some likely adjectives? (Adjectives correspond to values for a
particular kind of data; for example: a **JPEG** image.)_ 

•	Number
    o	Adjectives: Real, Complex, Integer, Positive, Negative
•	Equation
    o	Adjectives: Number of Unknowns
•	Function
    o	Quadratic, Cubic, Piecewise, Polynomial
•	Angle
    o	Degrees, Radians


_What are some likely verbs? (Verbs correspond to behaviors or actions; for
example: **rotating**.)_

To simplify the language design and make it concise, for certain mathematical fields, like functions, I would like to be able to use nouns as verbs, for instance, using the word Inverse to define a method which finds the inverse of a given function, or using the word Limit to find the limit of a function as x approaches a particular value. According to this system, certain examples of verbs the DSL could have are:

Functions: Inverse, Intercepts, Domain, Range
Trigonometry: Sine, Cosine, Tangent, Cosecant, Secant, Cotangent, Arcsin, Arccos, Arctan
Calculus: Differentiate, Integrate, Limit, Implicitly Differentiate


_What are some likely adverbs? (Verbs correspond to modifications to a specific
behavior or action; for example: rotating **left**.)_

•	Limit
    o	Adverbs: (As x approaches) 0, infinity
•	Differentiate
    o	Adverbs: With respect to y, with respect to x, for x=4
•	Range
    o	For domain of -3 < x <0
•	Integrate
    o	From x = 3 to x = 5

### Expressiveness
_What should be easy to do in this language? What should be possible, but
difficult? What should be impossible or very difficult?_

It should most definitely be easy to compute different parameters for a particular field of mathematics using as many as possible existing theories. For instance, if a user wishes to calculate the limit of a piecewise function, or of a function using the l’Hopital rule, or by dividing all the powers of x by another power of x – all of these and more should be possibilities. Ideally, the language should be focused and specific enough that using it for anything other than such calculations and operations is impossible.

### Related work
_Are there any other DSLs in this domain? If not, describe how you know there
aren't and conjecture why not. If so, describe them and provide links. How well
do they address the need? What do you like about the language? Are there parts
of the language you think could be improved?_

I was able to find a research paper written summarizing a DSL in mathematics (https://arxiv.org/pdf/1310.3473.pdf) which to my understanding aims to do something similar for certain fields in discrete mathematics. I found it quite comprehensive and complete in addressing a set of functionalities in set theory, graph theory, number theory, etc. and also think that the presented names for the functions were comprehensible and added fluency to the language. However, I think one improvement that could be made is to the syntax to bring the language closer to a natural language.

## The Project
**This section examines whether the idea makes for a good project for this
course.**

### Suitability
_If someone were to work on this project, what percentage of their time would be
spent directly engaging in the **language** aspects of this project (e.g.,
making language-design decisions), as opposed to "systems" aspects of the
project (e.g., implementing a complicated visualization that doesn't require a
lot of language design)?_

I believe that in working on this project, several of the “systems” aspects would be easier to comprehend and address for the language-implementer due to the widespread existence of examples on how to calculate such values. I believe a majority of the time (60%-70%) would be spent working on the linguistic design part of the product and trying to build something which eases the process of computing complex calculations for users by making it a fluent language and making the kind of calculations it can perform customizable.

### Scope
_How ambitious is this project for you? Not very? Somewhat? Very?_

I believe that this is a fairly ambitious project for me. It might be difficult to implement all of various theories and concepts of all mathematical domains for this project hence I believe what might be better would be for me to focus on one/two specific fields such as calculus and functions, for example, since this would make it easier for me to delve deeper into each field rather than simply scratching the surface.

### Benefits and drawbacks
_Why might this be a good idea for a project?_ 

I think this would be a good idea for a project since it is something which I find extremely interesting and I believe to which there exists a great deal of potential for linguistic design.

_Why might this not be a good idea project?_

This might not be a good project if I attempt to implement too many mathematical fields and hence get carried away from being able to focus the project on a very specific domain. In addition to this, researching all the possible theories and concepts which exist to calculate a particular parameter might take away from the amount of time I dedicate to the language design aspect of it, which is the most essential part of the project.
