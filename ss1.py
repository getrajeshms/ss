import streamlit as st
from statsmodels.stats.power import TTestIndPower

# Display the logo at the top of the app

# Title
st.title("Sample Size Determination for Association Study")

# Sidebar for input parameters
st.sidebar.header("Input Parameters")
effect_size = st.sidebar.slider("Effect Size (Cohen's d)", 0.1, 2.0, 0.5, 0.1)
alpha = st.sidebar.slider("Significance Level (α)", 0.01, 0.10, 0.05, 0.01)
power = st.sidebar.slider("Power (1-β)", 0.5, 1.0, 0.8, 0.05)
num_covariates = st.sidebar.slider("Number of Covariates", 0, 10, 1, 1)

# Main content
st.subheader("Sample Size Calculation")
st.write(f"Effect Size (Cohen's d): {effect_size}")
st.write(f"Significance Level (α): {alpha}")
st.write(f"Power (1-β): {power}")
st.write(f"Number of Covariates: {num_covariates}")

# Adjust effect size for the number of covariates
adjusted_effect_size = effect_size / (1 + num_covariates * 0.1)  # Simplified adjustment

# Sample size calculation
analysis = TTestIndPower()
sample_size = analysis.solve_power(effect_size=adjusted_effect_size, alpha=alpha, power=power, alternative='two-sided')

# Display the sample size
st.write(f"Required Sample Size (per group): {int(sample_size)}")

# Adjust for potential dropouts
dropout_rate = st.sidebar.slider("Expected Dropout Rate (%)", 0, 50, 10, 1)
adjusted_sample_size = sample_size / (1 - dropout_rate / 100)
st.write(f"Adjusted Sample Size (per group) for {dropout_rate}% dropout rate: {int(adjusted_sample_size)}")
