import re


def building_match_apply_functions(pattern, search, replace):

    def match_rule(word)
        return re.search(pattern, word)

    def apply_rule(word):
        return re.sub(search, replace, word)

    return (match_rule, apply_rule)

patterns = (
    ('[sxz]$', '$', 'es'),
    ('[^aeioudgkprt]h$', '$', 'es'),
    ('(qu|[^aeiou])y$', 'y$', 'ies'),
    ('$', '$', 's')
)

rules = [building_match_apply_functions(pattern, search, replace)
         for (pattern, search, replace) in patterns]


def plural(noun):
    for matches_rule, apply_rule in rules:
        if matches_rule(noun):
            return apply_rule(noun)


# print(rules)
print(plural('cat'))
