import json
import math
from pathlib import Path


def softmax(logits):
    shifted = [x - max(logits) for x in logits]
    exps = [math.exp(x) for x in shifted]
    denom = sum(exps)
    return [x / denom for x in exps]


def load_model(path):
    with open(path) as f:
        return json.load(f)


def compute_scores(model_path, eval_path, bug=True):
    model = load_model(model_path)
    with open(eval_path) as f:
        evaluation = json.load(f)

    scores = {}
    for name, sequence in evaluation.items():
        if len(sequence) <= 1:
            scores[name] = 1.0
            continue

        losses = []
        for pos in range(len(sequence) - 1):
            context_token = sequence[pos]
            target_token = sequence[pos + 1]
            logits = model["token_logits"][str(context_token)]
            probs = softmax(logits)
            if bug:
                target = sequence[pos]
            else:
                target = target_token
            losses.append(-math.log(probs[target] + 1e-12))

        scores[name] = math.exp(sum(losses) / len(losses))

    return scores


if __name__ == "__main__":
    base = Path("/app")
    results = compute_scores(base / "model.json", base / "evaluation.json", bug=True)
    (base / "perplexity_scores.json").write_text(json.dumps(results, indent=2))
    print("wrote /app/perplexity_scores.json")
