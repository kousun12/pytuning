import unittest

from tuning import Tuning

ETCents = ["100.", "200.", "300.", "400.", "500.", "600.", "700.", "800.", "900.", "1000.", "1100.", "1200."]
LMYRatioStrings = [
  "567/512", "9/8", "147/128", "21/16", "1323/1024", "189/128", "3/2", "49/32", "7/4", "441/256",
  "63/32", "2/1"
]
LMYRatios = [1.107421875, 1.125, 1.1484375, 1.3125, 1.2919921875, 1.4765625, 1.5, 1.53125, 1.75, 1.72265625, 1.96875, 2]
ETRatios = [1.05946, 1.12246, 1.18921, 1.25992, 1.33484, 1.41421, 1.49831, 1.5874, 1.68179, 1.7818, 1.88775, 2]


class TestTuning(unittest.TestCase):
  def test_basic_ratios(self):
    basic = Tuning(['5/4', '233.9850002884625', '375.', '2'])
    assert basic.ratios() == [1.25, 1.5, 1.9152065613971474, 2.0]

    et = Tuning(ETCents)
    assert [round(x, 5) for x in et.ratios()] == ETRatios

    lmy = Tuning(LMYRatioStrings)
    assert lmy.ratios() == LMYRatios

  def test_basic_frequencies(self):
    basic = Tuning(['5/4', '233.9850002884625', '375.', '2'])
    assert basic.frequencies() == [440.0, 550.0, 660.0, 842.6908870147448]

    et = Tuning(ETCents)
    exp_et = [round(x, 2) for x in et.frequencies()]
    assert exp_et == [440.0, 466.16, 493.88, 523.25, 554.37, 587.33, 622.25, 659.26, 698.46, 739.99, 783.99, 830.61]

    lmy = Tuning(LMYRatioStrings)
    exp_lmy = [round(x, 2) for x in lmy.frequencies()]
    assert exp_lmy == [440, 487.27, 495.0, 505.31, 577.5, 568.48, 649.69, 660.0, 673.75, 770.0, 757.97, 866.25]

  def test_pinned_freq(self):
    lmy = Tuning(LMYRatioStrings, (440, 6))
    exp_lmy = [round(x, 2) for x in lmy.frequencies()]
    expect_tonic = 297.99
    assert exp_lmy == [expect_tonic, 330.0, 335.24, 342.22, 391.11, 385.0, 440.0, 446.98, 456.3, 521.48, 513.33, 586.67]
    octave = round(lmy.frequency(len(LMYRatioStrings)), 2)
    assert octave == expect_tonic * 2


if __name__ == '__main__':
  unittest.main()
