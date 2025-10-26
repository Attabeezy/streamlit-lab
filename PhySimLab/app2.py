import streamlit as st
import plotly.graph_objects as go
import numpy as np

# Title Section with Introduction
st.title("PhySimLab: Where Physics Becomes Play!")

st.markdown("""
Welcome to PhySimLab, the *coolest* place to tinker with physics! 🚀
Ever wondered how forces, motion, or energy work? Well, wonder no more! Let's jump in and **explore** the beauty of physics with interactive simulations.
""")

# Sidebar for Navigation
st.sidebar.title("Navigate the Lab")
section = st.sidebar.radio(
    "Choose a Lab Section", 
    ["Forces & Motion", "Energy", "Projectile Motion", "Pendulum Motion", 
     "Collision Simulation", "Planetary Motion", "Harmonic Oscillator", 
     "Rotational Dynamics", "Circular Motion", "Light and Waves"]
)

# --- Clear Structure for each Section ---
if section == "Forces & Motion":
    st.header("Forces & Motion: Feel the Push!")
    
    mass = st.slider("Select the mass of the object (kg)", 1, 100, 10)
    force = st.slider("Apply a force (N)", 0, 500, 100)

    # Explanation
    st.markdown("""
    ### Newton's Second Law
    When a force is applied to an object, it accelerates! That's **Newton's Second Law**:
    
    $$ F = ma $$
    
    Let's calculate the acceleration based on your values.
    """)

    acceleration = force / mass
    st.write(f"The acceleration of the object is **{acceleration:.2f} m/s²**")

    # Plotly Visualization
    time = np.linspace(0, 10, 100)
    velocity = acceleration * time
    distance = 0.5 * acceleration * time**2

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=time, y=velocity, mode='lines', name="Velocity (m/s)", line=dict(color='blue')))
    fig.add_trace(go.Scatter(x=time, y=distance, mode='lines', name="Distance (m)", line=dict(color='green')))
    
    fig.update_layout(title="Object's Velocity and Distance Over Time", xaxis_title="Time (s)", yaxis_title="Velocity/Distance")
    st.plotly_chart(fig, use_container_width=True)

elif section == "Energy":
    st.header("Energy: Where the Action's At!")
    
    mass = st.slider("Select the mass of the object (kg)", 1, 100, 10)
    height = st.slider("Select the height (m)", 1, 100, 10)
    
    # Explanation
    st.markdown("""
    ### Gravitational Potential Energy
    The potential energy of an object due to its position is given by:
    
    $$ E_p = mgh $$
    
    Where:
    - \( E_p \) is the potential energy (in joules)
    - \( m \) is the mass (in kilograms)
    - \( g \) is the acceleration due to gravity (\( 9.8 m/s² \))
    - \( h \) is the height (in meters)
    
    Let's calculate the potential energy.
    """)
    
    g = 9.8
    potential_energy = mass * g * height
    st.write(f"The potential energy of the object is **{potential_energy:.2f} J**")

elif section == "Projectile Motion":
    st.header("Projectile Motion: Taking Flight!")
    
    velocity = st.slider("Initial Velocity (m/s)", 10, 100, 50)
    angle = st.slider("Launch Angle (degrees)", 0, 90, 45)
    
    # Explanation
    st.markdown("""
    ### Projectile Motion
    When an object is launched with an initial velocity at a certain angle, it follows a parabolic path. 
    The horizontal and vertical components of the velocity determine how far and high the object will go.
    """)

    angle_rad = np.radians(angle)
    g = 9.8
    time_of_flight = (2 * velocity * np.sin(angle_rad)) / g
    max_height = (velocity**2 * np.sin(angle_rad)**2) / (2 * g)
    range_ = (velocity**2 * np.sin(2 * angle_rad)) / g

    st.write(f"Time of flight: **{time_of_flight:.2f} s**")
    st.write(f"Maximum height: **{max_height:.2f} m**")
    st.write(f"Range: **{range_:.2f} m**")
    
    # Plot trajectory
    time_points = np.linspace(0, time_of_flight, num=500)
    x = velocity * np.cos(angle_rad) * time_points
    y = velocity * np.sin(angle_rad) * time_points - 0.5 * g * time_points**2
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name="Projectile Path", line=dict(color='orange')))
    
    fig.update_layout(title="Projectile Motion", xaxis_title="Distance (m)", yaxis_title="Height (m)")
    st.plotly_chart(fig, use_container_width=True)

elif section == "Pendulum Motion":
    st.header("Pendulum Motion: Swinging with Grace!")
    
    length = st.slider("Pendulum Length (m)", 1.0, 10.0, 5.0)
    initial_angle = st.slider("Initial Angle (degrees)", 1, 90, 30)

    st.markdown("""
    ### Pendulum Motion
    A pendulum exhibits periodic motion, and its period depends on its length and the acceleration due to gravity.
    
    The period of a simple pendulum is given by:
    
    $$ T = 2\pi \sqrt{\\frac{L}{g}} $$
    """)

    g = 9.8
    period = 2 * np.pi * np.sqrt(length / g)
    st.write(f"The period of the pendulum is **{period:.2f} s**")

    # Simulate the pendulum motion (simple visual example)
    theta = np.linspace(0, 2*np.pi, 100)
    x = length * np.sin(theta)
    y = -length * np.cos(theta)

    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=x, y=y, mode='lines', name="Pendulum Motion", line=dict(color='orange')))
    
    fig2.update_layout(title="Pendulum Motion", xaxis_title="Horizontal Displacement (m)", yaxis_title="Vertical Displacement (m)")
    st.plotly_chart(fig2)

elif section == "Collision Simulation":
    st.header("Collision Simulation: Crashes and Bounces!")
    
    mass1 = st.slider("Mass of Object 1 (kg)", 1, 50, 10)
    mass2 = st.slider("Mass of Object 2 (kg)", 1, 50, 20)
    velocity1 = st.slider("Initial Velocity of Object 1 (m/s)", -50, 50, 20)
    velocity2 = st.slider("Initial Velocity of Object 2 (m/s)", -50, 50, -10)
    
    # Explanation
    st.markdown("""
    ### Elastic Collisions
    In an elastic collision, both momentum and kinetic energy are conserved. The final velocities of two objects after a collision are determined by:
    
    $$ v_{1f} = \\frac{(m_1 - m_2)v_{1i} + 2m_2 v_{2i}}{m_1 + m_2} $$
    $$ v_{2f} = \\frac{(m_2 - m_1)v_{2i} + 2m_1 v_{1i}}{m_1 + m_2} $$
    """)
    
    final_velocity1 = ((mass1 - mass2) * velocity1 + 2 * mass2 * velocity2) / (mass1 + mass2)
    final_velocity2 = ((mass2 - mass1) * velocity2 + 2 * mass1 * velocity1) / (mass1 + mass2)
    
    st.write(f"Final velocity of Object 1: **{final_velocity1:.2f} m/s**")
    st.write(f"Final velocity of Object 2: **{final_velocity2:.2f} m/s**")
    
    # Simulate collision
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[0, final_velocity1], y=[0, mass1], mode='markers', name="Object 1", marker=dict(size=15, color='red')))
    fig.add_trace(go.Scatter(x=[0, final_velocity2], y=[0, mass2], mode='markers', name="Object 2", marker=dict(size=15, color='blue')))
    
    fig.update_layout(title="Collision Simulation", xaxis_title="Final Velocity (m/s)", yaxis_title="Mass (kg)")
    st.plotly_chart(fig)

elif section == "Planetary Motion":
    st.header("Planetary Motion: Orbits in Space!")
    
    mass_planet = st.slider("Mass of the planet (kg)", 1e23, 1e25, 5e24)
    distance_from_sun = st.slider("Distance from the Sun (m)", 1e9, 1e11, 1e10)
    
    # Explanation
    st.markdown("""
    ### Planetary Motion
    According to Newton's Law of Gravitation, the force between two masses is:
    
    $$ F = G \\frac{m_1 m_2}{r^2} $$
    """)
    
    G = 6.67430e-11
    sun_mass = 1.989e30
    gravitational_force = G * mass_planet * sun_mass / distance_from_sun**2
    
    st.write(f"The gravitational force between the planet and the Sun is **{gravitational_force:.2e} N**")

    # Plot orbital path (assuming circular orbit)
    theta = np.linspace(0, 2*np.pi, 100)
    x_orbit = distance_from_sun * np.cos(theta)
    y_orbit = distance_from_sun * np.sin(theta)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_orbit, y=y_orbit, mode='lines', name="Planet Orbit", line=dict(color='blue')))
    
    fig.update_layout(title="Planetary Orbit", xaxis_title="X Position (m)", yaxis_title="Y Position (m)")
    st.plotly_chart(fig)
    
elif section == "Harmonic Oscillator":
    st.header("Harmonic Oscillator: Bounce Back!")
    
    k = st.slider("Spring constant (N/m)", 1, 100, 50)
    mass = st.slider("Mass attached to spring (kg)", 1, 10, 5)
    
    # Explanation
    st.markdown("""
    ### Harmonic Oscillator
    The motion of a mass attached to a spring is governed by Hooke's Law:
    
    $$ F = -kx $$
    """)

    omega = np.sqrt(k / mass)
    st.write(f"The angular frequency of the oscillator is **{omega:.2f} rad/s**")

    # Simulate the oscillation (plot position over time)
    time = np.linspace(0, 10, 100)
    amplitude = 1
    position = amplitude * np.cos(omega * time)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=time, y=position, mode='lines', name="Position over Time", line=dict(color='green')))
    
    fig.update_layout(title="Harmonic Oscillator Motion", xaxis_title="Time (s)", yaxis_title="Position (m)")
    st.plotly_chart(fig)

# Add further sections for Rotational Dynamics, Circular Motion, Light, and Waves similarly...
