import nltk
from nltk.tree import Tree, ParentedTree
import itertools
from itertools import permutations


def check_for_pattern(subtree):
    if subtree.label() != "NP":
        return False

    for item in subtree:
        if not (
            item.label() in ("NP", ",")
            or item.label() == "CC" and item[0].lower() == "and"
        ):
            return False

    return True


def find_matching_patterns(tree, result_indexes_list, parent_position=None):
    if parent_position is None:
        parent_position = []

    for node_index, branch in enumerate(tree):
        if isinstance(branch, str):
            continue

        group_indexes = []
        current_position = parent_position + [node_index]

        if check_for_pattern(branch):
            for index, sub_branch in enumerate(branch):
                if sub_branch.label() == "NP":
                    group_indexes.append(current_position + [index])

        if group_indexes:
            result_indexes_list.append(group_indexes)

        find_matching_patterns(branch, result_indexes_list, current_position)

    return


def create_combinations(indexes_list):
    combinations = permutations(indexes_list)
    return combinations


def generate_new_trees(parent_tree, groups, results, limit=None):
    group = groups[0]
    combinations = create_combinations(group)

    for combination in combinations:
        new_tree = parent_tree.copy(deep=True)
        for i, index_in_tree in enumerate(combination):
            combination_value = parent_tree[index_in_tree]
            position_to_insert = group[i]
            new_tree[position_to_insert] = combination_value

        try:
            generate_new_trees(new_tree, groups[1:], results, limit)
        except IndexError:
            if limit and len(results) == limit + 1:
                return results
            else:
                results.append(new_tree)

