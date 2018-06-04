# Idea 3

## The need, the user, and you
**This section describes whom the project would serve and why you're interested
in the project.**


### What's the need?
_What need is met by your idea? Who are you helping? What is that person's
experience like now? How would their experience improve if you could help 
them?_

The domains this language would attempt to cater to are information visualization and time management. Essentially, this project will be a calendar visualizer specific for school students. It would, first and foremost, have the ability to take inputs of events, classes, meetings, exams, deadlines, and visualize all of this data on a monthly/weekly/daily calendar. It would have an additional functionality wherein it would give users the ability to generate daily schedules for themselves basis the action items and the fixed events which they input. I believe that there are a variety of needs that such an idea can help meet. For one, it can facilitate efficient time management for students by enabling them to keep track of deadlines, classes, and tasks. Additionally, it can help increase productivity even during holidays by generating daily schedules for users basis their interests, their time commitments, and their action items. Currently, several students often struggle with effective time management, especially during unscheduled times like the holidays. Such a language could greatly help them overcome this predicament.

### Why you?
_What excites you about this idea? How did you come up with it?_

As a student myself and someone who has struggled with time management in the past, I believe that this DSL would be incredible useful. Additionally, the prospect of being able to simply generate daily schedules basis my preferences and action items is something that fascinates and excites me in its potential to significantly improve students’ productivity and time management. This idea is inspired by and partially based on the pre-packaged project idea for a calendar visualizer on the project generation page. The additional idea for a daily-schedule generator is something I came up with as a consequence of speaking to a number of my peers and discovering that because students are accustomed to following a set schedule, thus the lack of one during holidays can often negatively impact their productivity.

### Domain
_Describe the project's domain in five words._

Time management, education, information visualization

## The language
**This section helps you argue that a DSL can serve the need(s) described in
the previous section.**

### Why a language?
_Why is a DSL appropriate for your user(s)? How does it address the need?_

This, to my understanding, would be a DSL for simulation in that it would enable users to save on time and effort. In addition, I have always found it to be time-consuming and thus, to some extent, counterintuitive to use calendar apps which require one to create events under specific months/weeks/days instead of simply being able to input an event and have it be interpreted and visualized by a calendar. I believe that a programming language would be a quicker and more natural way of inputting such events. In addition to this, since a repetitive task is to be performed with set parameters, using custom libraries whose scope is limited to this domain would make much more sense.

### Linguistic pieces
**For each question below, brainstorm a few answers. If a question does not
apply to your project, explain why.**

_What are some likely nouns in this domain? (Nouns correspond to kinds of
data. In our image manipulation DSL, an **image** is a noun.)_

Classes, Exams, Tasks, Subjects, Meetings, Events, Reminders

_What are some likely adjectives? (Adjectives correspond to values for a
particular kind of data; for example: a **JPEG** image.)_

Most of the nouns in this DSL will each have two or three set parameters: dates, times, and optional descriptions

_What are some likely verbs? (Verbs correspond to behaviors or actions; for
example: **rotating**.)_

Add (an event), Edit (an event), Delete (an event), Add Task, Add Reminders

_What are some likely adverbs? (Verbs correspond to modifications to a specific
behavior or action; for example: rotating **left**.)_

The adverbs in this case would be the definition of the event/task/reminder in terms of dates and times where they need to be placed. For instance, a user wishing to add an event would have to input the date it takes place, the time, the location (optional) and a name. For a task, on the other hand, the input parameters would be possible deadline for completion, estimated time commitment, description, subject, etc.

### Expressiveness
_What should be easy to do in this language? What should be possible, but
difficult? What should be impossible or very difficult?_

It should indubitably be easy for users to not only create an intricate calendar through as few inputs as possible but also update it as and when needed. It should, however, be a focussed and specific enough language such that no other operations are possible except calendar manipulation.

### Related work
_Are there any other DSLs in this domain? If not, describe how you know there
aren't and conjecture why not. If so, describe them and provide links. How well
do they address the need? What do you like about the language? Are there parts
of the language you think could be improved?_

I found one DSL in this domain as part of one of the student archives shared with us on the Github project generation page, titled Calendarscript (https://github.com/aputman/project/blob/master/documents/final.md). I found this project very fascinating and comprehensive in terms of addressing the need and found the language design and syntax to be extremely fluent. The only thing which I think could be improved upon is to make the output calendar a little more comprehensible by perhaps removing some degree of host flavour.


## The Project
**This section examines whether the idea makes for a good project for this
course.**

### Suitability
_If someone were to work on this project, what percentage of their time would be
spent directly engaging in the **language** aspects of this project (e.g.,
making language-design decisions), as opposed to "systems" aspects of the
project (e.g., implementing a complicated visualization that doesn't require a
lot of language design)?_

I believe that in working upon this project, at least 60% of the language-implementer’s time would be dedicated to the linguistic design decisions more than the systems parts of the project in terms of trying to best understand how many parameters should be defined so that they are specific enough to feature on a personalized calendar but still generalised enough that a certain definition of an event can fit a variety of types of events.

### Scope
_How ambitious is this project for you? Not very? Somewhat? Very?_

I believe that this project is fairly ambitious for me and is something I would also greatly enjoy working upon.

### Benefits and drawbacks
_Why might this be a good idea for a project?_ 

I believe this might be a good idea for a project since it is something I find interesting and would enjoy working on. Moreover, there exists a need for such a language and its users could greatly benefit from such a DSL. In addition to this, I think the potential that this DSL has for language design would also make it a good project for this course. The level of customization that could be made available to the users might also make it a good project.

_Why might this not be a good idea project?_

This might not be a good project since calendar apps are a popular phenomenon hence people may not be extremely willing to switch to a different medium for maintaining their schedules.
