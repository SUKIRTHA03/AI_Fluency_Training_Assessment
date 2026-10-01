BYTES_PER_PARAM = {
    "FP16": 2.00,
    "Q8_0": 1.00,
    "Q6_K": 0.81,
    "Q5_K_M": 0.68,
    "Q4_K_M": 0.57,
    "Q3_K_M": 0.43
}


def estimate(params_b, context_k, precision):
    weights = params_b * BYTES_PER_PARAM[precision]
    kv_cache = params_b * context_k * 0.02
    total = (weights + kv_cache) * 1.10

    return weights, kv_cache, total


configs = [
    (1.5, 8, "Q4_K_M"),
    (8, 8, "Q4_K_M"),
    (8, 8, "FP16"),
    (30, 8, "Q4_K_M"),
    (70, 8, "Q4_K_M")
]


print("Day 4 Memory Estimator")
print("-" * 70)
print(f"{'Model':<12}{'Precision':<12}{'Weights':<12}{'KV Cache':<12}{'Total':<12}")

for params, context, precision in configs:
    weights, kv, total = estimate(params, context, precision)

    print(
        f"{str(params) + 'B':<12}"
        f"{precision:<12}"
        f"{weights:.2f} GB     "
        f"{kv:.2f} GB      "
        f"{total:.2f} GB"
    )


print("\nContext length experiment - 8B Q4_K_M")

for context in [4, 8, 16, 32]:
    weights, kv, total = estimate(8, context, "Q4_K_M")
    print(
        f"{context}K context: "
        f"Weights={weights:.2f} GB, "
        f"KV={kv:.2f} GB, "
        f"Total={total:.2f} GB"
    )


print("\nQuantization experiment - 8B model at 8K context")

for precision in ["FP16", "Q8_0", "Q6_K", "Q5_K_M", "Q4_K_M", "Q3_K_M"]:
    weights, kv, total = estimate(8, 8, precision)
    print(
        f"{precision}: "
        f"Weights={weights:.2f} GB, "
        f"KV={kv:.2f} GB, "
        f"Total={total:.2f} GB"
    )