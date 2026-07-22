A causal language model checkpoint and an evaluation set are available at /app/model.json and /app/evaluation.json. The model stores per-token logits for a small vocabulary, and the evaluation file contains several token sequences.

Write a JSON object to /app/perplexity_scores.json containing one perplexity score per sequence. Each score must be the mean negative log-likelihood of the next token under the model, computed from the correct next-token target for each position.

Success criteria:
1. /app/perplexity_scores.json exists and contains valid JSON.
2. The JSON object contains one entry for each sequence in /app/evaluation.json.
3. Each score matches the reference values for the provided model and evaluation data.

You have 120 seconds to complete this task. Do not cheat by using online solutions or hints specific to this task.
