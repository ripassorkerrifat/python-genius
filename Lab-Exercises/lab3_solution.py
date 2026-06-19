def estimate_deployment_cost(instance_count, hourly_rate, budget_cap):
    total_cost = instance_count * hourly_rate * 720
    if total_cost > budget_cap:
        return f"REJECTED: Budget Exceeded by ${total_cost - budget_cap:.2f}!"
    else:
        return f"APPROVED: Total Estimated Cost is ${total_cost:.2f}."

# Test Cases to verify your execution:
print(estimate_deployment_cost(instance_count=5, hourly_rate=0.45, budget_cap=1500.00))
print(estimate_deployment_cost(instance_count=12, hourly_rate=0.85, budget_cap=5000.00))
