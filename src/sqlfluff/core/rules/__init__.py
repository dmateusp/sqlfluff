"""Register all the rule classes with their corresponding rulesets (just std currently)."""

from .base import RuleSet
from sqlfluff.core.plugin.host import get_plugin_manager
from sqlfluff.core.rules.config_info import get_config_info

std_rule_set = RuleSet(name="standard", config_info=get_config_info())

# Iterate through the rules list and register each rule with the std_rule_set
plugin_manager = get_plugin_manager()
for plugin_rules in plugin_manager.hook.get_rules():
    for rule in plugin_rules:
        std_rule_set.register(rule)


def get_ruleset(name: str = "standard") -> RuleSet:
    """Get a ruleset by name."""
    lookup = {std_rule_set.name: std_rule_set}
    # Return a copy in case someone modifies the register.
    return lookup[name].copy()
