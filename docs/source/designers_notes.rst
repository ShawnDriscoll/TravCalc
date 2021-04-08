**Designer's Notes**
====================

In the Beginning
----------------
One of the first things I do when learning a new language is to
discovery how it generates random numbers. Older computer languages
from the '70s had their own built-in random number generators. Technically,
they were pseudo-random number generators. But technically, I wanted to
program my Star Trek games anyway no matter what they were called.

In the '80s, I would discover that not all computer languages came
with random number generators built in. Many didn't have such a thing
unless some external software library was installed. Both FORTRAN and C
couldn't do random anything out of the box. A math library had to be picked from
the many that were out there. And if none were available, a computer class on campus
was available to teach you how to program your own random number generator from scratch.

By the '90s, random number generators were pretty much standardized as
for as how accurately random they were. And they were included in standard
libraries for various languages. By the time Python was being developed, the
C language used to write Python had very robust random number generators.
And because Python was written in C, it just made sense for it to make
use of C libraries.

For those that are curious, **diceroll** uses the ``random.randint()`` module that comes
with CPython. There are stronger random generators out there now, with NumPy being one
of them. But at the time of designing **diceroll**, I didn't quite understand how-all
NumPy worked, or what version of it to install. And for rolling dice, the built-in
random number generator would be just fine.

Lessons Learned
---------------
In the past, when I needed a random number from 1 to say 6 (see 6-sided dice), I would use ``INT(RND(1)*6) + 1``.
And I would be used to doing it that way for probably 15 years or so, because that is
how most BASIC languages did things. Other languages like C required me to whip out the
80286 System Developer's 3-ring binder to find out how ``srand()`` and ``rand()`` worked,
and under what circumstances.

Fast-forward 20 years, and I'm learning CPython without knowing the difference between a CPython
or an RPython or any other Python out there. I figured Python was the same all over, even though
I had a feeling Linux did things differently because of its filepath naming and OS commands. And
of course, the first thing I had to try was Python's ``random`` module, as well as its
ugly-looking ``randint()``.

Right away I noticed the way Python "loaded" modules was going to be a learning experience. I
hadn't really programmed anything huge since my TANDY Color Computer 3 days running OS-9 Level II
and programming in BASIC09 (https://en.wikipedia.org/wiki/BASIC09). Python would reveal different
ways of importing modules the more I read about them, and the more code I poured over.

I would soon find that: ::

   import random
   
   print random.randint(1, 6) # roll a 6-sided die

Was the same thing as: ::

   from random import randint
   
   print randint(1, 6) # roll a 6-sided die

Which looked a bit cleaner. But I was debating if I wanted to use ``randint()`` at all in
my normal coding.

So while I was learning how to write my own functions, as well as how to go about importing them, I came up with
an idea for **diceroll**. It would included a ``roll()`` function, and a ``die_rolls()`` function as
a "side effect." Even though ``die_rolls()`` had no error-checking, ``roll()`` would call it after
doing its own error-checking.

I was trying to avoid using: ::

   from diceroll import die_rolls
   
   print die_rolls(6, 2) # roll two 6-sided dice

For my dice rolls, I wanted something more readable. Something like: ::

   from diceroll import roll
   
   print roll('2D6') # roll two 6-sided dice

It was almost less typing, which I thought was great because I was going to be typing this function a lot
for a Python project I had in mind. And it would be a lot easier to spot what kind of rolls were being made in my
code. And the simple addition or subtraction of DMs to such a roll was making the function more appealing: ::

   print roll('2D6+3') # roll two 6-sided dice and add a DM of +3 to it

The Channel 1
-------------
**diceroll** was written years ago. The code is used by both my TravCalc and TravGen apps, and gets looked at
by GitHub visitors who google-by now and again. But not many programmers will use the code because of the simple fact
that Python is now version 3.6+ something. So **diceroll**, along with a slew of other pre-Python 2.6 era modules,
are the Channel 1 stations in the room that no TV can possibly watch.

It really comes down to a philosophy. I waited on learning Python until a version was released where I could say,
*"This is Python."* Or say, *"This is what Python should be."* Something like that.

And for me, it was Classic Python 2.5.4 when I said such things. Python 2.6 books were showing up in stores. And
there were already differences being found between it and the Python that I was using. Python had become this
huge thing. And non-programmers were being attracted to it for their own reasons. And that was all fine.
Python 2.7, 3.0, etc., were seeing lots of new talent joining their mix. They were taking Python to places it
hadn't been to. And more and more people were doing Python because of it.

Python is trying to be all things to all programmers these days. And it has become less of Python in doing so.
I am not a functional programmer. Never have been. But a lot of people are. And Python now serves them very well.
I'm often told, *"Python now does things this way."* But it is ways that I don't see myself using.

People are altering **diceroll** so that it works in their Python, just as I am altering their uploaded code so that it
works in my Python. If I wanted my code to reach more people, of course I would have to program using
the latest greatest Python. But there is a certain individuality lost in doing that.

I believe the next great computer programming language will be the one that remains true to its nature/design as
it grows. And doesn't split the party as it grows.

| *Shawn Driscoll*
| *October 3rd, 2017*
| *US, California*