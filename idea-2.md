# Idea 2 --- A Guitar DSL

## The need, the user, and you
**This section describes whom the project would serve and why you're interested
in the project.**

### What's the need?
_What need is met by your idea? Who are you helping? What is that person's
experience like now? How would their experience improve if you could help 
them?_
Chords are commonly used in guitar. In many cases, performing chords with a guitar is simple and repetitive: it is a permutation of left land(chords) and right hand(strings). I want to make a DSL that produces guitar music by programming. Currently, music producers have to make music with real guitars, and it takea much time in rehearsing and practicing with music scores. One way to solve this problem is using a DSL that can maniuplate the notes, chords, and the way to play guitar(tapping, sweeping, bending). I believe the person's experience will be greatly improved by this DSL. With the help of this DSL, they will be able to play without a real guitar, and perform pieces of music that human can hardly do. Also, this DSL allows looping and recursion, even conditions, so music producer's efficiency will be greatly improved.

### Why you?
_What excites you about this idea? How did you come up with it?_
I came up this idea on a rainy day. I was listening to my sister practicing her piano. I heard lots of repetition of notes and beats in her performance. Suddenly, I thought, _Why aren't there people make programming language in piano performing?_ However, I cannot play piano, so I further integrate my idea into a guitar DSL.

### Domain
_Describe the project's domain in five words._
Guitar, performing, music, beginners, functional

## The language
**This section helps you argue that a DSL can serve the need(s) described in
the previous section.**

### Why a language?
_Why is a DSL appropriate for your user(s)? How does it address the need?_
A DSL will be appropriate for my users because most of the users have little experience with programming. It would be best for them to start with a simple syntax and a failiar domain. This DSL will address the need very well. When a human is performing with guitar, he might make the wrong note or fail to play in a specific tempo. For a DSL, all those data, notes, pitches, tempos are manipulated in numerical values, and since a computer never make mistakes, technically a computer will surpass human performers in all aspects, except for emotions.

### Linguistic pieces
**For each question below, brainstorm a few answers. If a question does not
apply to your project, explain why.**

_What are some likely nouns in this domain? (Nouns correspond to kinds of
data. In our image manipulation DSL, an **image** is a noun.)_
notes, tempos, frequencies, strings, chords

_What are some likely adjectives? (Adjectives correspond to values for a
particular kind of data; for example: a **JPEG** image.)_ 
a **MP3** music piece, 


_What are some likely verbs? (Verbs correspond to behaviors or actions; for
example: **rotating**.)_
Sliding, pulling, tapping, bending, sweeping picking, slapping

_What are some likely adverbs? (Verbs correspond to modifications to a specific
behavior or action; for example: rotating **left**.)_
sweep **quickly/slowly**
play **happlily/lively/solemnly/lightly**


### Expressiveness
_What should be easy to do in this language? What should be possible, but
difficult? What should be impossible or very difficult?_
Ideally, it should be quite easy to play simple guitar chords. It may be more difficult to play complicated guitar notes involving changing tempos and playing types(tapping, bending, sweeping). It will be almost very difficult to play songs like a real human, which will put emphasis on some notes or extend some notes.

### Related work
_Are there any other DSLs in this domain? If not, describe how you know there
aren't and conjecture why not. If so, describe them and provide links. How well
do they address the need? What do you like about the language? Are there parts
of the language you think could be improved?_
One Well known DSL for music programming is ```Sonic Pi``` by Sam Aaron. Although it is also a music DSL, it focus more on manipulating sounds like DJ. Unlike ```Sonic Pi```, this DSL focus more on music playing itself

Another DSL is ```GuitarPro 7```. It is a powerful tool for professional guitar users. However, it only provides a GUI instead of a language implementation.

## The Project
**This section examines whether the idea makes for a good project for this
course.**

### Suitability
_If someone were to work on this project, what percentage of their time would be
spent directly engaging in the **language** aspects of this project (e.g.,
making language-design decisions), as opposed to "systems" aspects of the
project (e.g., implementing a complicated visualization that doesn't require a
lot of language design)?_
Still I believe more than 90 percent of their time would be spent directly engaging in the language aspect, since this is a language implementation instead of a user interface.

### Scope
_How ambitious is this project for you? Not very? Somewhat? Very?_
I think this is a **very ambitious** project. There hasn't anyone made a guitar music DSL before. So I am very excited to achieve this project.

### Benefits and drawbacks
_Why might this be a good idea for a project?_ 
- I am quite good at playing guitar, 
- there aren't many similar projects on the internet now
- I might be able to make good music with this DSL

_Why might this not be a good idea project?_
- there will be many difficulties implementing this DSL, such as importing sound samples
(I can't think of a disadvantage anymore because I really think it's a good idea)
