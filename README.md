# CallCenter_Staffing_Calculator

Determining the required number of agents for a call center involves analyzing call volume, handling time, and service level targets.

1. Collect Key Metrics
Call Volume (λ): Number of incoming calls per hour.
Average Handling Time (AHT): Average time (in minutes) to handle one call, including talk time and after-call work.
Service Level (SL): Target percentage of calls answered within a specified time (e.g., 80% of calls answered within 20 seconds).
Shrinkage Factor (S): Percentage of time agents are unavailable (e.g., breaks, training, absenteeism).

2. Estimate Required Workload (Traffic Intensity)
  
   Traffic Load = (Calls per hour * AHT (in minutes))/60
   
This gives the number of Full-Time Equivalents (FTEs) required to handle the workload without considering wait times.

3. Apply Erlang C Model (For Queueing Consideration)

Erlang C considers: Queue formation when all agents are busy.Probability of waiting time exceeding SL target.
Tools like an Erlang C Calculator or Python packages (pyworkforce) can be used to compute this accurately.

4. Adjust for Service Level and Occupancy
Use an Erlang C calculator to get the actual required agents.
Factor in occupancy (the percentage of time agents spend on calls vs. idle time).

Example Calculation - Assume: 
Call volume = 100 calls/hour
AHT = 6 minutes
Service level = 80% within 20 sec
Shrinkage = 30%

5. Account for Shrinkage
Total Required Agents = Calculated Agents/( 1−Shrinkage (%))

To follow further and get the results use the calculator.










