import streamlit as st
import streamlit.components.v1 as components  # Import the correct components module

# Title
st.title("Circuit Builder Challenge")

# Component definitions with educational content
components_info = {
    "Resistor": {
        "description": "A resistor limits the current flowing in a circuit.",
        "symbol": "🟫"
    },
    "Capacitor": {
        "description": "A capacitor stores and releases electrical energy.",
        "symbol": "🟡"
    },
    "Transistor": {
        "description": "A transistor acts as a switch or amplifier for electrical signals.",
        "symbol": "🟠"
    },
    "Battery": {
        "description": "A battery provides the necessary voltage for the circuit.",
        "symbol": "🔋"
    },
    "LED": {
        "description": "An LED emits light when current flows through it.",
        "symbol": "💡"
    },
}

# Sidebar for component selection
st.sidebar.header("Select Components")
selected_components = st.sidebar.multiselect(  # Renamed to avoid conflict
    "Choose components to build your circuit:",
    list(components_info.keys()),
)

# Circuit area (placeholder for demonstration)
st.header("Circuit Area")
if selected_components:  # Updated reference
    st.write("You have selected:")
    for component in selected_components:  # Updated reference
        st.write(f"- {components_info[component]['symbol']} {component}")
        st.write(f"  * {components_info[component]['description']}")
    
    # Validate circuit components (basic logic)
    valid_circuit = False
    if "Battery" in selected_components:  # Updated reference
        if "Resistor" in selected_components or "LED" in selected_components:  # Updated reference
            valid_circuit = True
    
    # Show validation result
    if valid_circuit:
        st.success("Your circuit is valid!")
    else:
        st.warning("Your circuit is invalid. Make sure to include a battery and at least one load (Resistor or LED).")
else:
    st.write("Select components from the sidebar to start building your circuit.")

# Example circuit description
st.subheader("Circuit Example")
st.write(
    "Try building a simple series circuit with a Battery and a Resistor or LED."
)

# HTML for Circuit Simulation (optional enhancement)
circuit_html = """
<html>
  <body>
    <h3>Interactive Circuit Simulation (Placeholder)</h3>
    <div id="circuit-area" style="width: 100%; height: 400px; border: 1px solid black;">
      <!-- JavaScript Circuit Simulation could go here -->
    </div>
  </body>
</html>
"""

# Display the circuit area
components.html(circuit_html, height=600)  # This now refers to the correct components module
