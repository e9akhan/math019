import answer


def is_answered():
    assert answer.answer()


def test_answer():
    assert answer.answer() == 171
