from pencil_durability import write


def test_writes_text_to_paper_from_provided_text():
    text = "Hello World"
    paper = write(text)
    assert paper == text

