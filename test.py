import pytest
# FLOAT
def float_division(a, b):
    return a / b


def float_pow(a, b):
    return a ** b


@pytest.mark.parametrize("a,b,expected", [(4.4, 2.0, 2.2), (9.0, -3.0, -3.0), (5.6, 2.8, 2.0)])
def test_float_division(a, b, expected):
    assert float_division(a, b) == expected


def test_pow_properties():
    # 2^4 == 2^2 * 2^2 must be equals
    assert float_pow(3, 8) == (float_pow(3, float_division(8, 2)) * float_pow(3, float_division(8, 2)))


# LIST
def list_reverse(l):
    return l.reverse()


def list_sort(l):
    return l.sort()


@pytest.mark.parametrize("l,expected", [([3, 4, 5, 3, 9], [9, 3, 5, 4, 3]), ([3, 4, 5, 3, 9], [9, 3, 5, 4, 3])])
def test_list_reverse(l, expected):
    list_reverse(l)
    assert len(l) == len(expected)
    for i in range(len(l)):
        assert l[i] == expected[i]

def test_list_sort():
    l= [5,7,2,4,9,1,8,3,6,0]
    list_sort(l)
    for i in range(1,len(l)):
        assert l[i] >= l[i-1]

# DICT
def dict_compare(d1, d2):
    if len(d1)!=len(d2):
        return False
    l = len(d1)
    for i in d1.keys():
        if d1.get(i)!=d2.get(i):
            return False
    return True

def dict_add(d, key,value):
    if d.get(key) != None:
        raise KeyError("This key ("+str(key)+ ") is already exist")
    d.update({key, value})

@pytest.mark.xfail(raises=AttributeError)
def test_dict_compare_input_parameters():
    dict_compare([1,2], [3,4])

def test_wrong_dict_add():
    d = {1: "one", 2: "two"}
    with pytest.raises(KeyError) as excinfo:
        dict_add(d, 1, "one")
    assert "This key (1) is already exist" in str(excinfo.value)