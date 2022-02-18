def test_simple():
	list=[1,2,3,4,5]
	dict={a: a ** 2 for a in range(5)}

	assert 3 in list
	assert 9 == dict[3]

import pytest

@pytest.mark.parametrize("num, output",[(1,1),(-1,1),(0,0),(5,25)])
def test_multiplication_11(num, output):
   assert num*num == output

def test_simple2():
	list2=[2,4,-1]
	dict2={'a':1,'c':3}
	
	try:
		assert dict2[3]
	except KeyError:
		pass
	try: 
		assert list2[1]<0
	except AssertionError:
		pass
