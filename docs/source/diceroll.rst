**diceroll Module**
===================
.. module:: diceroll

.. method:: roll(number_of_dice + dice_type + dice_roll_modifier)

   | ``roll()`` accepts a string value made up of three concatenated values, then returns an integer.
   |
   | String values comes from *number_of_dice* + *dice_type* + *dice_roll_modifier*
   |
   | Some examples are:
   | '2' + 'D10' + '-2'
   | str(3) + 'D6' + '+2'
   | 'FLUX'
   |
   | *dice_roll_modifier* must include a '+' or '-' with its value.
   |
   | Note that both *number_of_dice* and *dice_roll_modifier* are optional, and may not even be
   | used by some *dice_type* rolls.
