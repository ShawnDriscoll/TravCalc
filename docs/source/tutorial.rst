**TravCalc Tutorial**
=====================

The GUI
-------
After the program starts, there should be a screen that looks like:

.. figure:: program_start_screen.png

The screen contains various outlined areas that are labeled as:

   | **Task:**
   | Choose the difficulty and die-modifiers for a task.
   |
   | **Roll:**
   | Choose the roll type to perform.
   |
   | **Damage:**
   | Calculate a damage roll.
   |
   | **Outcome:**
   | Displays a plotted graph of the roll chances, and of the roll result if a difficulty is chosen.

.. note::

   Plotted graphs are generated only when difficulties are selected. **D66** rolls will never generate graphs.
   

Making a Task Roll
------------------
Typically, task rolls will have a difficulty chosen by the game's referee. The player simply clicks the **Task Difficulty** button and clicks on the difficulty level. This will unlock the rest of the **Task** area that the player can fill in as well. It's pretty much self-explanatory how the rest is filled in. It is assumed that the player has a characteristic and a skill in mind when changing these values.

.. note::

   The default **Characteristic** value is **7**. Be sure to input your character's own value in its place before rolling any dice. The same goes for the **Skill Level**, which has a default of **0**. Give it the value of your character's skill level for the task being done.
   
   Don't worry about the characteristic **Mod** amount. Its value is calculated automatically, as well as the DM **Total**.

Once the DM is calculated, a roll is then made (determined by the referee). The dice will be shown. The roll **Result** and **Effect** will be calculated. And the **Task Time** will be calculated if a **Timeframe** was chosen.

A graph of the **Outcome** will then be displayed.


Making a Damage Roll
--------------------
The **D** and **DD** rolls calculate the "soaking" of damage against armor. **Armor** amount is entered, along with hidden **Cover** amount (*which is new in v3.0.6b*) and **AP** amount. The number of dice is selected. And a **DM** can be added before clicking either the **D** or **DD** roll buttons. The effect will be added to **D** rolls.

The **Clear** button will reset the damage area.
The **Clear All** button will reset all the areas.


Settings Menu
-------------
Dice styles can be selected from the **Dice** menu.
Voice styles (yes, voice styles) can be selected from the **Audio** menu.

.. note::
   
   Only the **female voice** works with general die rolls (rolls made without a **Task Difficulty**).
