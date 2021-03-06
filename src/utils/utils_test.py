from utils.encodedecode import encoded, decoded
from utils.dictutils import retrieveKVList
from utils.strutils import strcat, listToString, escapeQuotes
from utils.converterutils import convertStrToInt, convertStrToFloat

def test_encoded_and_decoded():
    example_str = "Hello World!"
    assert encoded(example_str) != example_str, "Encode changes contents of str"
    assert decoded(encoded(example_str)) == example_str, "Decode undos encode"

def test_retrieveKVList():
    # Trivial cases
    assert retrieveKVList({}) == ([], []), "Empty dict gives empty lists"
    assert retrieveKVList({"a": 1}) == (["a"], [1]), "One item gives expected lists"

    # Nontrivial case
    three_keys, three_vals = retrieveKVList({"a": 1, "b": 2, "c": 3})
    assert len(three_keys) == 3, "Expected number of keys"
    assert len(three_vals) == 3, "Expected number of values"

    assert "a" in three_keys
    assert "b" in three_keys
    assert "c" in three_keys

    assert 1 in three_vals
    assert 2 in three_vals
    assert 3 in three_vals

    assert sorted(zip(three_keys, three_vals), key = lambda l: l[0]) ==\
        [("a", 1), ("b", 2), ("c", 3)]

def test_strcat():
    assert strcat("", "") == ""
    assert strcat("", "", "") == ""
    assert strcat("a", "b", "c") == "abc"
    assert strcat("a", "", "c") == "ac"
    assert strcat("", "b", "c") == "bc"
    assert strcat("a", "b") == "ab"
    assert strcat("a", "") == "a"

    assert strcat("a", "b", "c", "d") == "abcd"

def test_listToString():
    assert listToString([]) == ""
    assert listToString(["a"]) == "a"
    assert listToString(["a"], ", ") == "a"
    assert listToString(["a", "b", "c"]) == "a b c"
    assert listToString(["a", "b", "c"], ", ") == "a, b, c"

def test_escapeQuotes():
    assert escapeQuotes("") == "", "Empty string untouched"

    assert escapeQuotes("Hello World!") == "Hello World!", \
        "No quotes in string untouched"

    assert escapeQuotes("\"") == "&quot;",\
        "Double quote is replaced"

    assert escapeQuotes("'") == "&quot;",\
        "Single quote is replaced"

    assert escapeQuotes("\"Hello 'world'\"") == "&quot;Hello &quot;world&quot;&quot;",\
        "Escaping works within word"

    assert escapeQuotes("<p> Hello & World </p>") == "<p> Hello & World </p>", \
        "Other html entities are not inserted"

def test_convertStrToInt():
    assert convertStrToInt("not a number", 1) == 1,\
        "uses default if conversion fails"
    assert convertStrToInt("10", 2) == 10,\
        "Int conversion succeeds"
    assert convertStrToInt("3.12", 2) == 2,\
        "Float conversion fails"

def test_convertStrToFloat():
    assert convertStrToFloat("not a number", 1.0) == 1.0,\
        "uses default if conversion fails"
    assert convertStrToFloat("10", 2.0) == 10.0,\
        "Int conversion succeeds"
    assert convertStrToFloat("3.12", 2.0) == 3.12,\
        "Float conversion succeeds"
