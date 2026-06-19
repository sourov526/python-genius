# Solution Notes for Labs 1-5

## Lab 1: Smart Survey Onboarding Engine

The program collects `name`, `age`, and developer status from the user using `input()`. It converts `age` to an integer and normalizes the developer answer so `"yes"` becomes `True`.

The clearance logic works like this:

- If `age < 18`, the user gets `Tier 3: Guest`.
- If the user is 18 or older and is a developer, they get `Tier 1: Admin Infrastructure Access`.
- If the user is 18 or older and not a developer, they get `Tier 2: Standard Executive Access`.

The final result is displayed with an f-string in a single profile summary line.

## Lab 2: Multi-Cluster IP Audit Tool

This solution uses the provided `cluster_config` dictionary and a function named `calculate_capacity(config)`.

Inside the function, a `for` loop iterates through `active_nodes` and counts how many IP addresses exist. That count is used in the utilization formula:

`(active_node_count / total_max_slots) * 100`

The script then prints a report showing:

- Cluster name
- Number of active nodes
- Total slot capacity
- Utilization percentage

## Lab 3: Deployment Budget Optimizer

The function `estimate_deployment_cost(instance_count, hourly_rate, budget_cap)` calculates the total monthly cost based on 720 hours in a 30-day month.

Formula used:

`instance_count * hourly_rate * 720`

After calculating the cost:

- If the cost is greater than the budget cap, the function returns a rejection message showing how much the budget was exceeded by.
- If the cost is within budget, the function returns an approval message with the total estimated cost.

Dollar values are formatted to two decimal places.

## Lab 4: Profile Text Normalization Pipeline

The program loops through each item in `raw_survey_inputs`, cleans the text, and stores the cleaned version in `sanitized_records`.

The cleanup is done with:

- `strip()` to remove extra spaces from the beginning and end
- `lower()` to convert text to lowercase

Each cleaned string is added to the new list with `append()`. Finally, both the original and cleaned lists are printed so the results can be compared.

## Lab 5: System Alert Flag Evaluator

This solution builds a single boolean condition:

`(not is_active) or (cpu_percent > 90.0 and is_production)`

This means an alert is triggered if:

- The server is not active
- CPU usage is above 90% while running in production

An `if/else` statement then prints either the alert message or the safe-status message based on the result.
