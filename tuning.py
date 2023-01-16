from typing import Union, Tuple


class Tuning(object):
  scale: list[str] = []
  normalized_ratios: list[float] = []
  tonic_directive: float = None
  tonic_hz_raw: float = 440.0

  def __init__(self, scale: list[str], tonic_directive: Union[float, Tuple[float, int]] = None):
    """
    :param scale: A list of notes in the scale. Either a list of ratios or a list of cents. Per the .scl spec,
    if the element contains a decimal "." it is a cent value, otherwise it is a ratio.
    :param tonic_directive: optionally provide a tonic for this tuning, either as a raw frequency for the first semitone or
    as a tuple of (frequency, semitone index) e.g. (440, 9) to peg A4 to 440 Hz in a C major equal temperament scale
    if the tonic is not provided, the first semitone will be pegged to 440 Hz
    """
    self.scale = scale
    self.normalized_ratios = Tuning.normalize_ratios(scale)
    self.tonic_directive = tonic_directive
    self.tonic_hz_raw = Tuning.tonic_hz(tonic_directive, scale)


  @classmethod
  def normalize_ratios(cls, scale: list[str]) -> list[float]:
    """
    :param scale: A list of notes in the scale. Either a list of ratios or a list of cents, per the .scl spec.
    :return: A list of floating point ratios for notes in the scale
    """
    total_cents = len(scale) * 100
    def parse(_val: str):
      val = str(_val)
      if '.' in val:
        cents = float(val)
        return pow(2, cents / total_cents)
      elif '/' in val:
        n, d = val.split('/')
        return int(n) / int(d)
      else:
        return float(val)
    return list(map(parse, scale))

  def ratios(self) -> list[float]:
    """
    Return a list of normalized floating point ratios for the scale
    """
    return self.normalized_ratios

  def frequencies(self, octave_offset: int = 0) -> list[float]:
    """
    Return a list of frequencies for the scale. Optionally provide an integer octave offset to shift the scale
    """
    return [self.frequency(i, octave_offset) for i in range(len(self.normalized_ratios))]

  def frequency(self, semitone_index: int, octave_offset: int = 0) -> float:
    """
    Return the frequency for a given semitone in the scale. Optionally provide an integer octave offset to shift the scale
    """
    dividend = int(semitone_index / len(self.normalized_ratios))
    octave = dividend + octave_offset
    degree = semitone_index % len(self.normalized_ratios)
    ratio = self.normalized_ratios[degree - 1] if degree > 0 else 1
    return ratio * self.tonic_hz_raw * pow(2, octave)

  @classmethod
  def tonic_hz(cls, tonic_directive: Union[float, Tuple[float, int], None], scale: list[str]) -> float:
    """
    Return the frequency of the tonic for this scale
    """
    if tonic_directive is None:
      return 440
    elif isinstance(tonic_directive, float):
      return tonic_directive
    else:
      ratios = Tuning.normalize_ratios(scale)
      freq, idx = tonic_directive
      ratio = ratios[idx - 1]
      return freq / ratio

__all__ = ['Tuning']