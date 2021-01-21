"""Register all the rule classes with their corresponding rulesets (just std currently)."""

<<<<<<< HEAD
from sqlfluff.core.rules.base import RuleSet
from sqlfluff.core.rules.config_info import STANDARD_CONFIG_INFO_DICT
from sqlfluff.core.rules.std import (
    get_rules,
)
from sqlfluff.core.plugin.plugin_manager import get_plugin_manager
=======
from .base import RuleSet
from .config_info import STANDARD_CONFIG_INFO_DICT
from sqlfluff.core.plugin.plugin_manager import plugin_manager
>>>>>>> 3f745388... Add plugin default config

std_rule_set = RuleSet(name="standard", config_info=STANDARD_CONFIG_INFO_DICT)

# Iterate through the rules list and register each rule with the std_rule_set
for plugin_rules in plugin_manager.hook.get_rules():
    for rule in plugin_rules:
        std_rule_set.register(rule)


def get_ruleset(name: str = "standard") -> RuleSet:
    """Get a ruleset by name."""
    lookup = {std_rule_set.name: std_rule_set}
    # Return a copy in case someone modifies the register.
    return lookup[name].copy()
