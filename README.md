# Solar System

My evolving list of scripts for the [Winterbloom Sol Eurorack module](https://winterbloom.com/store/winterbloom-sol).

## 01 Plaits MIDI Drum Machine

Use MIDI notes to switch between and trigger the analog bass drum, analog snare drum and analog hi-hat models of Mutable Instruments Plaits.

### How to use

Copy the code in `01_plaits_midi_drum_machine.py3` to the `code.py` file on the Sol and save it to send the code to the Sol.

Patch…

* Sol CV A to Mutable Instruments Plaits FM port. Play with the attenuvertor to taste.
* Sol CV B to Mutable Instruments Plaits Model port. Ensure that you manually set the model to first green one in order for the voltage values to work so that the various drum models can be triggered.
* Sol CV C to Mutable Instruments Plaits Morph port. Play with the attenuvertor to taste.
* Sol CV D: Not used in this script.

* Sol Gate 1 to Mutable Instruments Plaits Trig port.
* Sol Gate 2 provides 8th clock triggers for use elsewhere in your patch.
* Sol Gate 3: Not used in this script.
* Sol Gate 4: Not used in this script.

Send the following MIDI notes to trigger the different drum sounds on the Plaits:

* 36: Analog bass drum
* 38: Analog snare drum
* 42: Analog hi-hat ("closed")
* 46: Analog hi-hat ("open")

If you send a note that is not recognised by the script, the previous drum model is played.

You may need to stop / restart the MIDI clock on your DAW / controller to get the clock triggers to work correctly if you're sending a clocked MIDI sequence to this script.

### Tips

* Change the voltages in the `midi_note_to_model` dictionary to change the baseline sounds.
* Use other modulation into the Plaits to really get crazy.

## 02 Rainfall Triggers

Every sixteenth MIDI clock note, four integers countdown by one from random starting values. When a countdown's value is less than zero, Sol sends a trigger from the countdown's associated output (1, 2, 3 or 4) and sets a new random starting value for that countdown.

This happens forever until the power runs out.
