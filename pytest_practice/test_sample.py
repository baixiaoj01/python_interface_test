def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 4

def test_function(record_xml_attribute):
    record_xml_attribute("assertions", "REQ-1234")
    record_xml_attribute("classname", "custom_classname")
    print('hello world')
    assert True