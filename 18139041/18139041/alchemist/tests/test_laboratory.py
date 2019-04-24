import yaml
import os
import pytest
from ..laboratory import Laboratory
from pytest import raises
from alchemist import command


def read_fixture():
    with open(os.path.join(os.path.dirname(__file__),
                           'fixtures.yaml')) as fixtures_file:
        fixtures = yaml.load(fixtures_file)
    return fixtures


@pytest.mark.parametrize("fixture", read_fixture())
def test_laboratory(fixture):
    answer = fixture.pop('answer')
    myLab = Laboratory(fixture["lower"], fixture["upper"])
    assert myLab.run_full_experiment(fixture["lower"],
                                     fixture["upper"]) == tuple(answer)


def test_empty_upper():
    myLab = Laboratory([], ['antiA'])
    answer = ([], ['antiA'], 0)
    assert myLab.run_full_experiment([], ['antiA']) == answer


def test_empty_lower():
    myLab = Laboratory(['antiA'], [])
    answer = (['antiA'], [], 0)
    assert myLab.run_full_experiment(['antiA'], []) == answer


def test_empty_both():
    myLab = Laboratory([], [])
    answer = ([], [], 0)
    assert myLab.run_full_experiment([], []) == answer


def test_wrong_input():
    with raises(ValueError):
        command.read_input_file({"shelf1": "yes",
                                 "A": "antiB", "shelf3": "antiC"})
