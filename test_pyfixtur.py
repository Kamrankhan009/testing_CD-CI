

def test_with_example_fixture(example_fixture):
    assert example_fixture == 1
    
def format_data_for_display(people):
    return [
        {"Kamran khan : Senior python developer"}
    ]

def test_format_data_for_display(group_of_people):
    assert format_data_for_display(group_of_people) == [
        {"Kamran khan : Senior python developer"}
    ]