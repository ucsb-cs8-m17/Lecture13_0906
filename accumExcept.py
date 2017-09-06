import pytest

def countAs(s):
  " count a and A in string s "
  if type(s)!=str:
      raise ValueError('parameter to countAs should be of type str')
  count = 0
  for c in s:
      if c=='a' or c=='A':
          count = count + 1
  return count
      
      
def test_countAs_1():
    with pytest.raises(ValueError):
        result = countAs(-42)
        
def test_countAs_2():
    assert countAs("Santa Ana")==4
