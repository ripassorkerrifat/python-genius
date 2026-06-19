# Lab Solutions Breakdown

### Lab 1: The Smart Survey Onboarding Engine
For the first lab, I used `input()` to grab the user's name, age, and developer status. Since age needs to be evaluated as a number, I wrapped that input in `int()`. For the logic, it's just a straightforward `if/elif/else` chain:
- If they are under 18, they get "Tier 3".
- If they are 18 or older and typed "yes" for developer, they get "Tier 1".
- Everyone else falls into "Tier 2".
Finally, I used an f-string to plug those variables into the final profile summary so it prints out cleanly.

### Lab 2: The Multi-Cluster IP Audit Tool
Here we needed to calculate cluster utilization. Instead of overcomplicating it with a loop, I just used the built-in `len()` function to count how many IPs were sitting inside the `active_nodes` list. I divided that count by the `total_max_slots` from the dictionary and multiplied by 100 to get the percentage. When printing, I used `:.2f` inside the f-string to make sure the percentage always rounded nicely to two decimal places.

### Lab 3: The Deployment Budget Optimizer
This one was all about tracking a budget. I wrote a function that multiplies the `instance_count`, `hourly_rate`, and 720 hours together to get the total monthly cost. 
If that total went over the `budget_cap`, I returned a rejection alert, showing exactly how much they exceeded the budget. If it was fine, I returned an approval message with the total cost. F-strings made it super easy to format the money amounts directly in the return statements.

### Lab 4: The Profile Text Normalization Pipeline
This was a classic data cleanup task. I set up an empty list called `sanitized_records`. Then, I looped through every messy string in `raw_survey_inputs` and chained two string methods: `.strip().lower()`. This instantly stripped off the weird spaces on the sides and forced all the weird capitalization into lowercase in one fell swoop. I just appended each cleaned item to the new list and printed them both to show the difference.

### Lab 5: System Alert Flag Evaluator
For the final lab, it was just about chaining boolean logic. I created a single `should_alert` variable that evaluates to `True` if:
- The server is down (`not is_active`)
- OR the CPU is melting down in production (`cpu_percent > 90.0 and is_production`).
Then I just passed that `should_alert` flag into a basic `if/else` block to print either a warning or an "[OK]" message.
