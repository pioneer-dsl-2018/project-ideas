# Idea 1

## The need, the user, and you
**This section describes whom the project would serve and why you're interested
in the project.**


### What's the need?
_What need is met by your idea? Who are you helping? What is that person's
experience like now? How would their experience improve if you could help 
them?_

The domain this language would aim to cater to is computer science education. Essentially, in my experience as a student, most school courses in computer science, when introducing programming, do so through pseudocode rather than a programming language which can be compiled. While this is great and definitely is something which enables beginners to focus more on the logical aspect of programming rather than the syntactical, I believe it also to some extent, hinders the learning process because students are often unable to confirm as to whether or not their logic is correct from lack of being able to actually compile and run the programs they write. I believe something that could significantly improve students’ experience when learning computer science as beginners in school would be to have a domain specific language that essentially functions as a pseudocode translator. This project would be able to comprehend a variety of different ways students write conditional statements, iterators, arithmetic functions, etc. and would then allow them to input values to actually test their functions. This will help school students to get a hands-on experience with beginner programming without having to focus on the syntax of a particular high-level programming language. Their experience would improve in that they will be able to test and detect any logic errors in their programs without having to trace the program step-by-step.

### Why you?
_What excites you about this idea? How did you come up with it?_

For one, I am extremely passionate about learning computer science. However, more importantly, it fascinates me to no end that computer science has led to the creation of systems and innovations which were unimaginable less than a century ago, and is the only science which enables one to create something from nothing: the closest to actual magic we have ever been. Yet the scope of what it can do, of where it can propel humanity, has barely been tapped. For this reason, I think it is more important than ever for students to be taught this incredible subject in the most comprehensive way possible. I believe a DSL which can enable students to focus on the logical aspect of their programs rather than syntax but still enable them to calculate and evaluate the result of a program they write would greatly enhance our learning.

### Domain
_Describe the project's domain in five words._

Computer Science, Education, Programming, Natural-Language Processing

## The language
**This section helps you argue that a DSL can serve the need(s) described in
the previous section.**

### Why a language?
_Why is a DSL appropriate for your user(s)? How does it address the need?_

This, to my understanding, would be a DSL for simulation in that it would enable users to save on time and effort. In addition to this, I think a DSL, particularly, is needed because of its potential to account for linguistic differences to perform the same task which is incontrovertibly crucial to this project. A DSL’s ability to emulate natural languages through enhanced fluency combined with the fact that a DSL would enable such a project to be specific to the modules and methods typically required for beginner programming make a DSL the best possible way to implement this idea.

### Linguistic pieces
**For each question below, brainstorm a few answers. If a question does not
apply to your project, explain why.**

_What are some likely nouns in this domain? (Nouns correspond to kinds of
data. In our image manipulation DSL, an **image** is a noun.)_

The nouns in this domain are likely to be similar to a general-purpose language since the aim of this language would be to create a translator for pseudocode at a beginner level which tends to have the same parameters and methods as a language.
Nouns: variable, constant, number

_What are some likely adjectives? (Adjectives correspond to values for a
particular kind of data; for example: a **JPEG** image.)_ 

Boolean, float, real, integer, string, array

_What are some likely verbs? (Verbs correspond to behaviors or actions; for
example: **rotating**.)_

add, divide, subtract, multiply, loop, if-then-else, while-do-endwhile, repeat-until, switch-case, modulo, int

_What are some likely adverbs? (Verbs correspond to modifications to a specific
behavior or action; for example: rotating **left**.)_

I think the adverbs for this language would ideally be the parameters which define the conditionals and iterators which would most likely be conditions defined in terms of numbers hence I’m not entirely certain language adverbs would be applicable to this DSL.

### Expressiveness
_What should be easy to do in this language? What should be possible, but
difficult? What should be impossible or very difficult?_

Since the purpose of this language is to enable beginners in programming to be able to run and compile their pseudocode without having to focus too much on the syntactical portion of a language, it should be easy for a user to compile their code even if there exist some minor syntactical errors. Since the domain is concentrated to enable users to compile pseudocode, any functionalities beyond that should be impossible to implement.

### Related work
_Are there any other DSLs in this domain? If not, describe how you know there
aren't and conjecture why not. If so, describe them and provide links. How well
do they address the need? What do you like about the language? Are there parts
of the language you think could be improved?_

I was unable to find any DSLs specifically intended for this purpose in this domain when conducting research on the internet for the same. I think the reason as to why this might be is because of the massive number of possibilities which exist when it comes to pseudocode which thus makes the implementation of this language challenging in terms of accounting for all these possibilities.

## The Project
**This section examines whether the idea makes for a good project for this
course.**

### Suitability
_If someone were to work on this project, what percentage of their time would be
spent directly engaging in the **language** aspects of this project (e.g.,
making language-design decisions), as opposed to "systems" aspects of the
project (e.g., implementing a complicated visualization that doesn't require a
lot of language design)?_

I believe that in working on this project, at least 75-80% of the developer’s time would need to be devoted to the language design of this project since the “systems” requirements are typically just pre-existing methods in general-purpose programming languages of combinations of these methods. The majority of this project would instead consist of accounting for as many as different ways of writing out a particular command (for instance, writing a for loop as “Loop from 1 to 4” or “For 1<x<4, loop x” or “For C 1 to 4, do”)  as possible as well as accounting for being able to ignore syntactical problems.

### Scope
_How ambitious is this project for you? Not very? Somewhat? Very?_

I believe this project is somewhat ambitious for me but in terms of its complexity in terms of problem-solving and logic, it is a little limiting as compared to some of the other projects.

### Benefits and drawbacks
_Why might this be a good idea for a project?_

I believe that there is incredible potential for this project to be explored in terms of linguistic features and designs wherein I think I can try to greatly utilise what we have learnt about fluency and language design during the course. Another feature which I think makes this a good potential project is that it is something I am genuinely interested in and care about and hence will certainly enjoy working on.

_Why might this not be a good idea project?_

This project might not be a good idea since it is essentially designing a General-Purpose Programming Language as a DSL which I am not entirely certain fits the ideal definition of a DSL.
