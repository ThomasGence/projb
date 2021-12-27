import argparse
import numpy as np


def evaluate(predicted, gold):

    precisions = {"total": 0}
    recalls = {"total": 0}
    accuracies = {"total": 0}

    precision_counts = {"total": 0}
    recall_counts = {"total": 0}
    accuracy_counts = {"total": 0}

    for q in question_types:
        precisions[q] = 0
        recalls[q] = 0
        accuracies[q] = 0

        precision_counts[q] = 0
        recall_counts[q] = 0
        accuracy_counts[q] = 0

    assert len(predicted) == len(gold)

    for key, predicted_value in predicted.items():

        gold_value = gold[key]
        q = key[-1]
        equal = value == gold_value

        accuracy_counts["total"] += 1
        accuracy_counts[q] += 1

        if equal:
            accuracies["total"] += 1
            accuracies[q] += 1

        if predicted_value:
            precision_counts["total"] += 1
            precision_counts[q] += 1

            if equal:
                precisions["total"] += 1
                precisions[q] += 1

        if gold_value:
            recall_counts["total"] += 1
            recall_counts[q] += 1

            if equal:
                recalls["total"] += 1
                recalls[q] += 1

    final_recalls = {"total": recalls["total"] / recall_counts["total"]}
    final_precisions = {"total": precisions["total"] / precision_counts["total"]}
    final_accuracies = {"total": accuracies["total"] / accuracy_counts["total"]}

    f1s = {}

    for q in question_types:
        final_recalls[q] = recalls[q] / recall_counts[q]
        final_precisions[q] = precisions[q] / precision_counts[q]
        final_accuracies[q] = accuracies[q] / accuracy_counts[q]

        f1s[q] = (2 * final_recalls[q] * final_precisions[q] /
                  (final_recalls[q] + final_precisions[q]))

    f1s["micro"] = (2 * final_recalls['total'] * final_precisions['total'] /
                    (final_recalls["total"] + final_precisions["total"]))

    f1s["macro"] = np.mean([f1s[q] for q in question_types])

    print("Total Precision:    {}".format(final_precisions["total"]))
    print("Total Recall:       {}".format(final_recalls["total"]))
    print("F1 Micro-average:   {}".format(f1s["micro"]))
    print("F1 Macro-average:   {}".format(f1s["macro"]))

    for q in question_types:
        print("\n" + ("="*60) + "\n")
        print(q + "\n")
        print("Precision:          {}".format(final_precisions[q]))
        print("Recall:             {}".format(final_recalls[q]))
        print("F1:                 {}".format(f1s[q]))


if __name__ == "main":

    parser = argparse.ArgumentParser()

    args = parser.parse_args()


    if args.split == "test":
        print("WARNING: you're evaluating on the test data.")

    with open(args.predictions_file, "r") as f:
        predictions = json.load(f)

    with open(args.data_file, "r") as f:
        data_file = json.load(f)
        labels = {i["example_id"]: i["answer"] for i in data_file}

    evaluate(predictions, gold)

