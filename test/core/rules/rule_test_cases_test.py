"""Runs the rule test cases."""
import os
import pytest
from sqlfluff.testing.rules import load_test_cases, rules__test_helper

ids, test_cases = load_test_cases(
    test_cases_path=os.path.join(
        os.path.abspath(os.path.dirname(__file__)), "test_cases", "*.yml"
    )
)


@pytest.mark.parametrize("test_case", test_cases, ids=ids)
def test__rule_test_case(test_case):
    """Run the tests."""
    res = rules__test_helper(test_case)
    if res is not None and res != test_case.fail_str:
        cfg = FluffConfig(configs=test_case.configs)
        rule = get_rule_from_set(test_case.rule, config=cfg)
        assert is_fix_compatible(
            rule
        ), f'Rule {test_case.rule} returned fixes but does not specify "@document_fix_compatible".'
