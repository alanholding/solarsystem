"""
2021-08-11
MIDI note to Mutable Instruments Plaits drum models

Sol ports output mapping:
- CV A: Mutable Instruments Plaits FM voltage value.
- CV B: Mutable Instruments Plaits Model voltage value.
- CV C: Mutable Instruments Plaits Morph voltage value.
- CV D: Not used in this script.
- Gate 1: Note Trigger.
- Gate 2: 8th clock triggers.
- Gate 3: Not used in this script.
- Gate 4: Not used in this script.
"""

import winterbloom_sol as sol

midi_note_to_model = {
    36: {
        'plaits_model_name': 'Analog bass drum model',
        'plaits_model_cv': 4.00,
        'plaits_fm_cv': 3.00,
        'plaits_morph_cv': 1.00
    },
    38: {
        'plaits_model_name': 'Analog snare drum model',
        'plaits_model_cv': 4.33,
        'plaits_fm_cv': 6.00,
        'plaits_morph_cv': 1.00
    },
    42: {
        'plaits_model_name': 'Analog hi-hat model',
        'plaits_model_cv': 4.66,
        'plaits_fm_cv': 7.00,
        'plaits_morph_cv': 0.5
    },
    46: {
        'plaits_model_name': 'Analog hi-hat model',
        'plaits_model_cv': 4.66,
        'plaits_fm_cv': 7.50,
        'plaits_morph_cv': 6.0
    }
}

def loop(last, state, outputs):

    if state.note in midi_note_to_model:
        outputs.cv_a = midi_note_to_model[state.note]["plaits_fm_cv"]
        outputs.cv_b = midi_note_to_model[state.note]["plaits_model_cv"]
        outputs.cv_c = midi_note_to_model[state.note]["plaits_morph_cv"]

    if sol.was_key_pressed(state):
        outputs.trigger_gate_1()

    if sol.should_trigger_clock(state, 8):
        outputs.trigger_gate_2()

sol.run(loop)
