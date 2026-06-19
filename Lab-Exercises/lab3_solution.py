HOURS_PER_MONTH = 30 * 24


def estimate_deployment_cost(instance_count, hourly_rate, budget_cap):
    total_cost = instance_count * hourly_rate * HOURS_PER_MONTH

    if total_cost > budget_cap:
        overage = total_cost - budget_cap
        return f"REJECTED: Budget Exceeded by ${overage:.2f}!"

    return f"APPROVED: Total Estimated Cost is ${total_cost:.2f}."


print(estimate_deployment_cost(instance_count=5, hourly_rate=0.45, budget_cap=1500.00))
print(estimate_deployment_cost(instance_count=12, hourly_rate=0.85, budget_cap=5000.00))
