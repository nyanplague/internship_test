from flask import Flask, request, jsonify
from parser import check_for_pattern, find_matching_patterns, create_combinations, generate_new_trees
import nltk
from nltk.tree import Tree


app = Flask(__name__)


@app.route("/paraphrase", methods =["GET"])
def paraphrase():
    original_tree = request.args.get("tree")
    original_tree.replace('% ', '')

    limit = None
    if request.args.get("limit"):
        limit = int(request.args.get("limit"))

    tree_to_parse = Tree.fromstring(original_tree)

    groups = []
    find_matching_patterns(tree_to_parse, groups)
    results = []
    generate_new_trees(tree_to_parse, groups, results, limit)

    del results[0]  # remove original tree from results

    response_list = []
    for result in results:
        tree_strs = str(result)
        response_list.append({"tree": " ".join(tree_strs.split())})

    return jsonify(paraphrases=response_list)


if __name__ == '__main__':
    app.run(debug=True)
