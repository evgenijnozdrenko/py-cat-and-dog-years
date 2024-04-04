from app.main import get_human_age
import pytest


def test_for_the_type_of_the_final_object() -> None:
    assert isinstance(get_human_age(14, 14), list)


def test_for_the_length_of_the_final_list() -> None:
    assert len(get_human_age(14, 14)) == 2


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ],
)
def test_for_correct_counting_of_years(
    cat_age: int, dog_age: int, result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == result
