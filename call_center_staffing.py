import streamlit as st
import math
from scipy.special import factorial

def erlang_c(traffic, agents):
    """Calculate the Erlang C probability of waiting"""
    numerator = (traffic ** agents / math.factorial(agents)) * (agents / (agents - traffic))
    denominator = sum([(traffic ** n) / math.factorial(n) for n in range(agents)]) + numerator
    return numerator / denominator

def required_agents(call_volume, aht, service_level, shrinkage):
    """Estimate the number of agents needed"""
    traffic = (call_volume * aht) / 60  # Calculate workload in Erlangs
    agents = math.ceil(traffic)  # Start with the minimum required

    while True:
        probability_wait = erlang_c(traffic, agents)
        avg_speed_answer = (probability_wait / (agents - traffic)) * (aht * 60)
        
        if avg_speed_answer <= service_level:
            break
        agents += 1
    
    adjusted_agents = math.ceil(agents / (1 - shrinkage))
    return agents, adjusted_agents

# Streamlit UI
st.title("📞 Call Center Staffing Calculator")

# Inputs
call_volume = st.number_input("📈 Calls per Hour", min_value=1, value=100)
aht = st.number_input("⏳ Average Handling Time (minutes)", min_value=0.1, value=5.0)
service_level = st.number_input("🎯 Service Level Target (Seconds)", min_value=1, value=20)
shrinkage = st.slider("📉 Shrinkage Percentage", min_value=0, max_value=100, value=30) / 100

if st.button("Calculate Agents"):
    fte_agents, total_agents = required_agents(call_volume, aht, service_level, shrinkage)
    
    st.success(f"✅ Required Agents (FTE): {fte_agents}")
    st.warning(f"⚠️ Adjusted Agents (with Shrinkage): {total_agents}")

st.markdown("💡 Uses the **Erlang C model** to estimate staffing needs.")
