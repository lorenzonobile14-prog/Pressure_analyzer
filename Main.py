# This creates a perfect plain text requirements.txt file
with open('requirements.txt', 'w') as f:
    f.write('streamlit')

# This creates a perfect plain text main.py file
with open('main.py', 'w') as f:
    f.write("""
import streamlit as st

def get_clinical_status(sys, dia):
    if sys > 180 or dia > 120:
        return "HYPERTENSIVE CRISIS (Consult a doctor immediately)", "#dc3545"
    elif sys >= 140 or dia >= 90:
        return "Hypertension Stage 2", "#fd7e14"
    elif (130 <= sys <= 139) or (80 <= dia <= 89):
        return "Hypertension Stage 1", "#ffc107"
    elif (120 <= sys <= 129) and dia < 80:
        return "Elevated", "#17a2b8"
    elif sys < 120 and dia < 80:
        return "Normal", "#28a745"
    else:
        return "Mixed/Uncategorized", "#6c757d"

st.set_page_config(page_title="BP Analyzer", page_icon="❤️")
st.markdown("## Blood Pressure Analyzer")

s_val = st.slider('Systolic:', 70, 250, 120)
d_val = st.slider('Diastolic:', 40, 150, 80)

if st.button("Analyze Results"):
    status, color = get_clinical_status(s_val, d_val)
    st.markdown(f'''
        <div style="background: white; padding: 1.5rem; border-radius: 12px;
                    text-align: center; border: 4px solid {color}; margin-top: 10px;">
            <h3 style="color: #666;">Results for {s_val}/{d_val} mmHg</h3>
            <h2 style="color: {color};">{status}</h2>
            <p style="font-size: 12px; color: #888;">Note: This is an educational tool, not medical advice.</p>
        </div>
    ''', unsafe_allow_html=True)
""")
