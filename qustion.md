Hi Professor,

After the second individual session, I though through the language design and found out that it might be a matter of the user, that whether they are good at programming or not.

For the capacitor discharging diagram, in which a capacitor and a resistor were connected in serives, I come up with two versions of syntax design. The first version is like this: ```CAP + RES``` and the second version is like this ```inSeries(Cap, Res)```. During the session, you said that these two design might cause confusion to my physics teacher who doesnt know computer very much.

However, if the user of this DSL is some physics scientists who do know programming, I still feel that the first verison is quite a good idea.(using ```+```, ```|``` and ```()```denoting how circuits are connected)

Making my physics teacher as the user, I generate the third version of my idea, I hope you could give me some comments:)

I was inspired by SQLs, in which they have synatic keywords like ```From```, ```where```, or ```and```, so I design a syntax as shown below:

```Connect Cap and Res In Series```

similarly, if they are connected in parellel, it would be like:

```Connect Cap and Res In Parellel```

To add another conponent, it would be something like this:

```Add LB to Cap in Series```,
where ```LB``` denotes "light bulbs"

I feel that this design has good readability and can be very scalable. Do you think this is a good design? And I have few more question: for the "motivation for DSL" nwriting, must I write a 5-paragraph essay? Can I write more/less than 5 paragraphs? Is it okay to paraphrase some of Fowler's words in defining a DSL?

Thank you very much ,

Weicheng
