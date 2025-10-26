import streamlit as st
import plotly.graph_objects as go
import numpy as np

# Set Streamlit page config
st.set_page_config(page_title="PhySimLab 🌌", layout="wide")

# Global Constants
GRAVITY = 9.8  # m/s² 🌎
GRAVITATIONAL_CONSTANT = 6.674e-11  # Nm²/kg² 🌠
SPEED_OF_LIGHT = 3e8  # m/s ⚡

# Title and Welcome Message
st.title("Welcome to PhySimLab! 🎉")
st.write("An interactive lab for exploring the wonders of physics! From forces that drive motion to the waves of light, PhySimLab makes the invisible visible. 🌠 Ready to dive in?")

# Sections for various simulations
sections = {
    "Force & Motion 🚀": "force_motion",
    "Energy 💡": "energy",
    "Projectile Motion 🏹": "projectile_motion",
    "Pendulum Motion 🕰️": "pendulum_motion",
    "Collision Simulation 💥": "collision_simulation",
    "Planetary Motion 🌍": "planetary_motion",
    "Harmonic Oscillator 🎸": "harmonic_oscillator",
    "Rotational Dynamics 🔄": "rotational_dynamics",
    "Circular Motion 🌀": "circular_motion",
    "Light and Waves 💡": "light_waves",
    "Wave Motion 🌊":"wave_motion",
    "Optics Refraction 🌈":"optics_refraction",
    "Doppler Effect  🚗":"doppler_effect",
    "Diffraction 🧲":"diffraction"
}

# Sidebar for navigation
st.sidebar.title("Select a Simulation 🧭")
choice = st.sidebar.selectbox("Choose a topic:", list(sections.keys()))

# Function Definitions for Each Section

def force_motion_simulation():
    st.markdown(r"""
    ### Newton's Second Law 🚀
    When a force acts on an object, it accelerates! That's **Newton's Second Law**:

    $$ F = ma $$

    Feel the need for speed? Calculate how force and mass create acceleration!
    """)
    with st.form(key='force_motion_form'):
        mass = st.number_input("Enter the mass (kg): 🏋️", min_value=0.1)
        force = st.number_input("Enter the force (N): 💥", min_value=0.1)
        calculate = st.form_submit_button("Calculate Acceleration 💫")
        if calculate:
            acceleration = force / mass
            st.success(f"The acceleration is {acceleration:.2f} m/s² 🚀")

            mass_values = np.linspace(0.1, mass, 50)
            force_values = force * np.ones_like(mass_values)
            acceleration_values = force_values / mass_values

            fig = go.Figure()
            fig.add_trace(go.Scatter(x=mass_values, y=acceleration_values, mode='lines+markers', name='Acceleration vs Mass'))
            fig.update_layout(title="Force and Acceleration Relationship 📊", xaxis_title="Mass (kg)", yaxis_title="Acceleration (m/s²)")
            st.plotly_chart(fig)

def energy_simulation():
    st.markdown(r"""
    ### Gravitational Potential Energy 🏔️
    Lifting objects takes energy, and the higher you go, the more energy you gain! 🌌

    $$ E_p = mgh $$

    Calculate how high you can go before potential energy hits the max!
    """)
    with st.form(key='energy_form'):
        mass = st.number_input("Enter the mass (kg): 🏋️", min_value=0.1)
        height = st.number_input("Enter the height (m): 📏", min_value=0.1)
        calculate = st.form_submit_button("Calculate Potential Energy ⚡")
        if calculate:
            energy = mass * GRAVITY * height
            st.success(f"The gravitational potential energy is {energy:.2f} J ⚡")

            height_values = np.linspace(0.1, height, 50)
            energy_values = mass * GRAVITY * height_values

            fig = go.Figure()
            fig.add_trace(go.Scatter(x=height_values, y=energy_values, mode='lines+markers', name='Potential Energy'))
            fig.update_layout(title="Potential Energy vs Height 📊", xaxis_title="Height (m)", yaxis_title="Energy (J)")
            st.plotly_chart(fig)

def projectile_motion_simulation():
    st.markdown(r"""
    ### Projectile Motion 🏹
    Ever wondered why a ball follows a curved path? That’s projectile motion!

    🌠 Launch at an angle, and watch the magic of parabolic paths.
    """)
    with st.form(key='projectile_motion_form'):
        initial_velocity = st.number_input("Enter the initial velocity (m/s): 🚀", min_value=0.1)
        angle = st.number_input("Enter the angle of projection (°): 🔄", min_value=0.0, max_value=90.0)
        simulate = st.form_submit_button("Simulate Projectile Motion 🌠")
        if simulate:
            angle_rad = np.radians(angle)
            time_of_flight = (2 * initial_velocity * np.sin(angle_rad)) / GRAVITY
            max_height = (initial_velocity**2 * np.sin(angle_rad)**2) / (2 * GRAVITY)
            range_of_projectile = (initial_velocity**2 * np.sin(2 * angle_rad)) / GRAVITY

            st.write(f"Time of flight: {time_of_flight:.2f} s ⏱️")
            st.write(f"Maximum height: {max_height:.2f} m 🏔️")
            st.write(f"Range: {range_of_projectile:.2f} m 🛤️")

            t = np.linspace(0, time_of_flight, num=500)
            x = initial_velocity * np.cos(angle_rad) * t
            y = initial_velocity * np.sin(angle_rad) * t - 0.5 * GRAVITY * t**2
            fig = go.Figure(data=[go.Scatter(x=x, y=y, mode='lines', name='Trajectory')])
            fig.update_layout(title="Projectile Motion Path 🎯", xaxis_title="Distance (m)", yaxis_title="Height (m)")
            st.plotly_chart(fig)

def pendulum_motion_simulation():
    st.markdown(r"""
    ### Pendulum Motion ⏰
    Back and forth! This rhythm depends on gravity and length.

    $$ T = 2\pi \sqrt{\frac{L}{g}} $$

    Swing along and calculate the period of your pendulum!
    """)
    with st.form(key='pendulum_form'):
        length = st.number_input("Enter the length of the pendulum (m): 🔄", min_value=0.1)
        calculate = st.form_submit_button("Calculate Period 🔄")
        if calculate:
            period = 2 * np.pi * np.sqrt(length / GRAVITY)
            st.success(f"The period of the pendulum is {period:.2f} s ⏲️")

            length_values = np.linspace(0.1, length, 50)
            period_values = 2 * np.pi * np.sqrt(length_values / GRAVITY)

            fig = go.Figure()
            fig.add_trace(go.Scatter(x=length_values, y=period_values, mode='lines+markers', name='Period vs Length'))
            fig.update_layout(title="Pendulum Period vs Length 🕰️", xaxis_title="Length (m)", yaxis_title="Period (s)")
            st.plotly_chart(fig)


def pendulum_motion_simulation():
    st.markdown(r"""
    ### 🎯 Pendulum Motion
    Watch gravity do its magic! 🌍 The period of a simple pendulum depends on its length and the gravitational pull:

    $$ T = 2\pi \sqrt{\frac{L}{g}} $$
    """)
    with st.form(key='pendulum_form'):
        length = st.number_input("🌐 Enter the length of the pendulum (in meters):", min_value=0.1)
        calculate = st.form_submit_button("💡 Calculate Period")
        if calculate:
            period = 2 * np.pi * np.sqrt(length / GRAVITY)
            st.success(f"⏳ The period of the pendulum is {period:.2f} seconds! 🎉")

            # Visualization of pendulum period vs length
            length_values = np.linspace(0.1, length, 50)
            period_values = 2 * np.pi * np.sqrt(length_values / GRAVITY)

            fig = go.Figure()
            fig.add_trace(go.Scatter(x=length_values, y=period_values, mode='lines+markers', name='Period vs Length'))
            fig.update_layout(title="Pendulum Period vs Length 📐", xaxis_title="Length (m)", yaxis_title="Period (s)")
            st.plotly_chart(fig)

def collision_simulation():
    st.markdown(r"""
    ### 🚗💥 Collision Simulation
    It's crash time! 🤯 In an elastic collision, momentum and kinetic energy get a new spin. Ready for the impact?

    """)
    with st.form(key='collision_form'):
        m1 = st.number_input("🚗 Enter the mass of object 1 (in kg):", min_value=0.1)
        v1i = st.number_input("💨 Enter the initial velocity of object 1 (in m/s):", min_value=0.1)
        m2 = st.number_input("🚙 Enter the mass of object 2 (in kg):", min_value=0.1)
        v2i = st.number_input("💨 Enter the initial velocity of object 2 (in m/s):", min_value=0.1)
        calculate = st.form_submit_button("💥 Simulate Collision")
        if calculate:
            v1f = ((m1 - m2) * v1i + 2 * m2 * v2i) / (m1 + m2)
            v2f = ((m2 - m1) * v2i + 2 * m1 * v1i) / (m1 + m2)
            st.success(f"🚗 Final velocity of object 1: {v1f:.2f} m/s")
            st.success(f"🚙 Final velocity of object 2: {v2f:.2f} m/s")

            # Visualization of velocity changes
            fig = go.Figure()
            fig.add_trace(go.Bar(name='Initial Velocity', x=['Object 1', 'Object 2'], y=[v1i, v2i]))
            fig.add_trace(go.Bar(name='Final Velocity', x=['Object 1', 'Object 2'], y=[v1f, v2f]))
            fig.update_layout(title="Initial vs Final Velocities 🏁", barmode='group', xaxis_title="Objects", yaxis_title="Velocity (m/s)")
            st.plotly_chart(fig)

def planetary_motion_simulation():
    st.markdown(r"""
    ### 🌌 Planetary Motion
    Explore the dance of celestial bodies! 🪐 The gravitational force between two masses is:

    $$ F = G \frac{m_1 m_2}{r^2} $$
    """)
    with st.form(key='planetary_form'):
        m1 = st.number_input("🌍 Enter the mass of the first object (in kg):", min_value=0.1)
        m2 = st.number_input("🌕 Enter the mass of the second object (in kg):", min_value=0.1)
        r = st.number_input("🔭 Enter the distance between the objects (in meters):", min_value=0.1)
        calculate = st.form_submit_button("🚀 Calculate Gravitational Force")
        if calculate:
            force = GRAVITATIONAL_CONSTANT * (m1 * m2) / r**2
            st.success(f"🌠 The gravitational force between the objects is {force:.2e} N.")

            # Visualization of gravitational force vs distance
            r_values = np.linspace(0.1, r, 50)
            force_values = GRAVITATIONAL_CONSTANT * (m1 * m2) / r_values**2

            fig = go.Figure()
            fig.add_trace(go.Scatter(x=r_values, y=force_values, mode='lines+markers', name='Gravitational Force'))
            fig.update_layout(title="Gravitational Force vs Distance 🧲", xaxis_title="Distance (m)", yaxis_title="Force (N)")
            st.plotly_chart(fig)

def harmonic_oscillator_simulation():
    st.markdown(r"""
    ### 🔄 Harmonic Oscillator
    Oscillate your way to discovery! 🎶 The restoring force in a spring is governed by Hooke's Law:

    $$ F = -kx $$
    """)
    with st.form(key='harmonic_form'):
        k = st.number_input("🎛️ Enter the spring constant (in N/m):", min_value=0.1)
        displacement = st.number_input("↔️ Enter the displacement (in meters):", min_value=0.1)
        calculate = st.form_submit_button("🔄 Calculate Restoring Force")
        if calculate:
            force = -k * displacement
            st.success(f"🔧 The restoring force is {force:.2f} N!")

            # Visualization of restoring force vs displacement
            displacement_values = np.linspace(0, displacement, 50)
            force_values = -k * displacement_values

            fig = go.Figure()
            fig.add_trace(go.Scatter(x=displacement_values, y=force_values, mode='lines+markers', name='Restoring Force'))
            fig.update_layout(title="Restoring Force vs Displacement 🌊", xaxis_title="Displacement (m)", yaxis_title="Force (N)")
            st.plotly_chart(fig)

def rotational_dynamics_simulation():
    st.markdown(r"""
    ### ⚙️ Rotational Dynamics
    Spin to win! 🌀 The rotational equivalent of Newton's Second Law is:

    $$ \tau = I\alpha $$
    """)
    with st.form(key='rotational_form'):
        torque = st.number_input("📏 Enter the torque (in Nm):", min_value=0.1)
        inertia = st.number_input("⚖️ Enter the moment of inertia (in kgm²):", min_value=0.1)
        calculate = st.form_submit_button("⚡ Calculate Angular Acceleration")
        if calculate:
            angular_acceleration = torque / inertia
            st.success(f"💫 The angular acceleration is {angular_acceleration:.2f} rad/s²!")

            # Visualization of angular acceleration vs torque
            torque_values = np.linspace(0.1, torque, 50)
            angular_acceleration_values = torque_values / inertia

            fig = go.Figure()
            fig.add_trace(go.Scatter(x=torque_values, y=angular_acceleration_values, mode='lines+markers', name='Angular Acceleration'))
            fig.update_layout(title="Angular Acceleration vs Torque 🧭", xaxis_title="Torque (Nm)", yaxis_title="Angular Acceleration (rad/s²)")
            st.plotly_chart(fig)

def circular_motion_simulation():
    st.markdown(r"""
    ### 🔄 Circular Motion
    Keep it in orbit! 🌕 The centripetal force needed for circular motion is:

    $$ F_c = \frac{mv^2}{r} $$
    """)
    with st.form(key='circular_motion_form'):
        mass = st.number_input("🌐 Enter the mass (in kg):", min_value=0.1)
        velocity = st.number_input("💨 Enter the velocity (in m/s):", min_value=0.1)
        radius = st.number_input("🔄 Enter the radius of the circular path (in m):", min_value=0.1)
        calculate = st.form_submit_button("💥 Calculate Centripetal Force")
        if calculate:
            force = (mass * velocity**2) / radius
            st.success(f"🚀 The centripetal force is {force:.2f} N!")

            # Visualization of centripetal force vs velocity
            velocity_values = np.linspace(0.1, velocity, 50)
            force_values = (mass * velocity_values**2) / radius

            fig = go.Figure()
            fig.add_trace(go.Scatter(x=velocity_values, y=force_values, mode='lines+markers', name='Centripetal Force'))
            fig.update_layout(title="Centripetal Force vs Velocity 🔄", xaxis_title="Velocity (m/s)", yaxis_title="Force (N)")
            st.plotly_chart(fig)

def light_and_waves_simulation():
    st.markdown(r"""
    ### 💡 Light and Waves
    Light travels at different speeds depending on the medium it passes through. This speed is determined by the medium's refractive index (n) and follows the equation:

    $$ v = \frac{c}{n} $$

    where:
    - **v** is the speed of light in the medium,
    - **c** is the speed of light in a vacuum (~3.00 x 10⁸ m/s),
    - **n** is the refractive index of the medium.
    """)
    SPEED_OF_LIGHT = 3.0e8  # Speed of light in a vacuum (m/s)

    with st.form(key='light_waves_form'):
        refractive_index = st.number_input("🔍 Enter the refractive index of the medium:", min_value=1.0, step=0.1, value=1.0)
        calculate = st.form_submit_button("📏 Calculate Speed of Light in Medium")

        if calculate:
            speed = SPEED_OF_LIGHT / refractive_index
            st.success(f"🌠 The speed of light in the medium is approximately {speed:.2e} m/s.")

            # Generate data for speed vs. refractive index visualization
            refractive_indices = np.linspace(1.0, refractive_index, 50)
            speed_values = SPEED_OF_LIGHT / refractive_indices

            # Plotting speed vs. refractive index
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=refractive_indices, y=speed_values, mode='lines+markers', name='Speed of Light'))
            fig.update_layout(
                title="Speed of Light vs Refractive Index 🌈",
                xaxis_title="Refractive Index (n)",
                yaxis_title="Speed of Light (m/s)",
                showlegend=True
            )
            st.plotly_chart(fig)

def wave_motion_simulation():
    st.markdown(r"""
    ### 🌊 Wave Motion
    Ride the wave! 🌊 Waves are all about moving energy through space. For a simple harmonic wave, the wave equation is:

    $$ y(x, t) = A \sin(kx - \omega t) $$

    where:
    - **A** = Amplitude of the wave (height)
    - **k** = Wave number, which relates to wavelength
    - **ω** = Angular frequency, related to the period

    Let's see how different frequencies and wavelengths affect the wave's shape!
    """)
    with st.form(key='wave_form'):
        amplitude = st.number_input("🌊 Enter the amplitude (in meters):", min_value=0.1)
        frequency = st.number_input("🔄 Enter the frequency (in Hz):", min_value=0.1)
        wavelength = st.number_input("📏 Enter the wavelength (in meters):", min_value=0.1)
        calculate = st.form_submit_button("💥 Generate Wave")
        if calculate:
            k = 2 * np.pi / wavelength
            omega = 2 * np.pi * frequency

            # Time array
            x_values = np.linspace(0, 4 * wavelength, 100)
            y_values = amplitude * np.sin(k * x_values)

            fig = go.Figure()
            fig.add_trace(go.Scatter(x=x_values, y=y_values, mode='lines', name='Wave'))
            fig.update_layout(title="Wave Motion 🌊", xaxis_title="Position (m)", yaxis_title="Displacement (m)")
            st.plotly_chart(fig)

def optics_refraction_simulation():
    st.markdown(r"""
    ### 🌈 Optics - Refraction
    Let's bend some light! 🌈 When light passes through different media, its speed changes, causing it to bend. This is refraction, and it follows Snell's Law:

    $$ n_1 \sin(\theta_1) = n_2 \sin(\theta_2) $$

    where:
    - **n₁** and **n₂** are the refractive indices of the media,
    - **θ₁** and **θ₂** are the angles of incidence and refraction.
    """)
    with st.form(key='optics_form'):
        n1 = st.number_input("🔍 Refractive index of medium 1:", min_value=1.0)
        theta1 = st.slider("📐 Angle of incidence (degrees):", min_value=0, max_value=90)
        n2 = st.number_input("🔍 Refractive index of medium 2:", min_value=1.0)
        calculate = st.form_submit_button("🌈 Calculate Refraction Angle")
        if calculate:
            theta1_rad = np.radians(theta1)
            theta2_rad = np.arcsin((n1 / n2) * np.sin(theta1_rad))
            theta2 = np.degrees(theta2_rad)
            st.success(f"📐 Angle of refraction: {theta2:.2f}°")

            # Visualization of refraction angles
            fig = go.Figure()
            fig.add_trace(go.Scatterpolar(r=[1, np.cos(theta1_rad)], theta=[0, theta1], mode='lines', name='Incident Ray'))
            fig.add_trace(go.Scatterpolar(r=[1, np.cos(theta2_rad)], theta=[0, theta2], mode='lines', name='Refracted Ray'))
            fig.update_layout(title="Refraction of Light 🌈", polar=dict(radialaxis=dict(visible=True, range=[0, 1])))
            st.plotly_chart(fig)

def doppler_effect_simulation():
    st.markdown(r"""
    ### 🚗 Doppler Effect
    Speeding sound waves! 🚗🔊 When a wave source moves toward or away from an observer, the wave frequency changes, producing the Doppler effect:

    $$ f' = f \left(\frac{v \pm v_o}{v \mp v_s}\right) $$

    where:
    - **f'** is the observed frequency,
    - **f** is the source frequency,
    - **v** is the speed of the wave,
    - **vₒ** is the observer's speed (relative to the wave),
    - **vₛ** is the source speed (relative to the wave).
    """)
    with st.form(key='doppler_form'):
        source_frequency = st.number_input("🔊 Enter the source frequency (in Hz):", min_value=1.0)
        speed_of_sound = st.number_input("🚀 Speed of sound (in m/s):", min_value=1.0, value=343.0)
        observer_speed = st.number_input("🏃 Observer's speed (in m/s):", min_value=0.0)
        source_speed = st.number_input("🚗 Source's speed (in m/s):", min_value=0.0)
        calculate = st.form_submit_button("📣 Calculate Observed Frequency")
        if calculate:
            # If source moves toward observer (negative source speed), and observer moves toward source (positive observer speed)
            observed_frequency = source_frequency * ((speed_of_sound + observer_speed) / (speed_of_sound - source_speed))
            st.success(f"👂 Observed frequency: {observed_frequency:.2f} Hz")

            # Visualization of frequency change
            speed_range = np.linspace(0, source_speed, 50)
            observed_freqs = source_frequency * ((speed_of_sound + observer_speed) / (speed_of_sound - speed_range))

            fig = go.Figure()
            fig.add_trace(go.Scatter(x=speed_range, y=observed_freqs, mode='lines+markers', name='Observed Frequency'))
            fig.update_layout(title="Doppler Effect on Frequency 📈", xaxis_title="Source Speed (m/s)", yaxis_title="Observed Frequency (Hz)")
            st.plotly_chart(fig)

def diffraction_simulation():
    st.markdown(r"""
    ### 🧲 Diffraction
    Bending waves around corners! 🧲 In single-slit diffraction, light bends as it passes through a narrow opening. The width of bright and dark fringes is described by:

    $$ a \sin(\theta) = m\lambda $$

    where:
    - **a** = slit width,
    - **θ** = angle of the diffraction fringe,
    - **m** = fringe order,
    - **λ** = wavelength.
    """)
    with st.form(key='diffraction_form'):
        slit_width = st.number_input("📏 Enter the slit width (in meters):", min_value=0.000001, format="%e")
        wavelength = st.number_input("🔆 Enter the wavelength of light (in meters):", min_value=0.000001, format="%e")
        calculate = st.form_submit_button("💫 Calculate Diffraction Angles")
        if calculate:
            # First few orders of diffraction
            orders = np.arange(1, 5)
            angles = np.degrees(np.arcsin(orders * wavelength / slit_width))

            st.success("📐 Diffraction angles calculated for orders m=1 to m=4")

            # Visualization of diffraction pattern
            fig = go.Figure()
            fig.add_trace(go.Bar(x=[f"Order {m}" for m in orders], y=angles, name='Diffraction Angles'))
            fig.update_layout(title="Diffraction Angles by Order 🔆", xaxis_title="Order of Diffraction (m)", yaxis_title="Angle (°)")
            st.plotly_chart(fig)


# Call the selected function
if choice == "Force & Motion 🚀":
    force_motion_simulation()
elif choice == "Energy 💡":
    energy_simulation()
elif choice == "Projectile Motion 🏹":
    projectile_motion_simulation()
elif choice == "Pendulum Motion 🕰️":
    pendulum_motion_simulation()
elif choice == "Collision Simulation 💥":
    collision_simulation()
elif choice == "Planetary Motion 🌍":
    planetary_motion_simulation()
elif choice == "Harmonic Oscillator 🎸":
    harmonic_oscillator_simulation()
elif choice == "Rotational Dynamics 🔄":
    rotational_dynamics_simulation()
elif choice == "Circular Motion 🌀":
    circular_motion_simulation()
elif choice == "Light and Waves 💡":
    light_and_waves_simulation()
elif choice == "Wave Motion 🌊":
    wave_motion_simulation()
elif choice == "Optics Refraction 🌈":
    optics_refraction_simulation()
elif choice == "Doppler Effect  🚗":
    doppler_effect_simulation()
elif choice == "Diffraction 🧲":
    diffraction_simulation()
