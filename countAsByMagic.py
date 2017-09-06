import pytest

def countAs(s):
  " count a and A in string s "
  if type(s)!=str:
        raise ValueError \
          ('param to countAs should be of type str, you fool!')
  if len(s)==0:
    return 0
  if len(s)==1:
    if s=="a" or s=="A":
       return 1
    else:
       return 0
  return countAs(s[0]) + countAs(s[1:])    
      
      
def test_countAs_1():
    with pytest.raises(ValueError):
        result = countAs(-42)
        
def test_countAs_2():
    assert countAs("Santa Ana")==4

def test_countAs_3():
    assert countAs("")==0

def test_countAs_4():
    assert countAs("a")==1

def test_countAs_5():
    assert countAs("A")==1

def test_countAs_6():
    assert countAs("X")==0
