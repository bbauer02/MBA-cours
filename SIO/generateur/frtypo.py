# French typography: non-breaking spaces inside numbers, before units and before high punctuation.
import re

NBSP = ' '


def fr(s):
    for _ in range(3):
        s = re.sub(r'(\d) (\d{3})(?!\d)', r'\1' + NBSP + r'\2', s)
    s = re.sub(r' ([:;?!»%])', NBSP + r'\1', s)
    s = s.replace('« ', '«' + NBSP)
    s = re.sub(r'(\d) (k€|M€|€|To|Go|Mbit/s|h\b|k\b)', r'\1' + NBSP + r'\2', s)
    return s
