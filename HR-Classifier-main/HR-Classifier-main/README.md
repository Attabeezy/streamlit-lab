# HR-Classifier
An interactive Streamlit-based web application designed to assess key entrepreneurial traits
# Trait Assessment Quiz

## Overview
The **Trait Assessment Quiz** is an interactive web application built with **Streamlit**. It is designed to evaluate key entrepreneurial traits, such as *Initiative, Competitiveness, Self-Confidence, Perseverance,* and *Self-Reliance*, through engaging scenario-based questions. Users select responses to presented scenarios and receive tailored feedback, offering insights into their strengths and areas for improvement.

---

## Features
- **Scenario-Based Assessment**: Realistic workplace and entrepreneurial scenarios for a comprehensive trait evaluation.
- **Dynamic Feedback**: Personalized feedback for each selected response, helping users understand their decisions.
- **Randomized Questions**: A new set of questions is selected on each run to ensure variety and engagement.
- **Streamlit Interface**: User-friendly design with dropdowns, progress bars, and detailed instructions.
- **Model Integration**: Loads a pre-trained decision tree model (`decision_tree_model.pkl`) for potential advanced evaluations.

---

## Installation

### Prerequisites
- Python 3.8 or later
- `pip` package manager
- Required Python libraries:
  - `streamlit`
  - `numpy`
  - `pandas`
  - `pickle`

### Steps
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/trait-assessment-quiz.git
   cd trait-assessment-quiz
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   streamlit run app.py
   ```

4. **Open in Browser**: Streamlit will display a URL in the terminal (e.g., `http://localhost:8501/`). Open it in your browser to interact with the application.

---

## Project Structure
```
trait-assessment-quiz/
│
├── app.py                  # Main Streamlit application script
├── decision_tree_model.pkl # Pre-trained decision tree model (required for future features)
├── images/                 # Image assets used in the app
│   ├── business-meeting.jpg
│   └── diversity-hands.jpg
├── requirements.txt        # Dependencies for the project
└── README.md               # Project documentation
```

---

## Usage
1. **Start the app**: Follow the installation steps to launch the application.
2. **Answer questions**: Read each scenario carefully and select the best response using dropdowns.
3. **Receive feedback**: View personalized feedback to understand your strengths and areas for growth.
4. **Randomize questions**: Click the "Randomize Questions" button to start a new session with fresh scenarios.

---

## Future Enhancements
- Use the pre-trained model to provide deeper insights and predictive analysis.
- Add more traits and scenarios for a broader assessment.
- Implement a scoring system to rank entrepreneurial aptitude.

---

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m "Add new feature"`.
4. Push to your branch: `git push origin feature-name`.
5. Open a pull request.

---

## License
This project is licensed under the **MIT License**. See the `LICENSE` file for details.

---

## Credits
Made with ❤️ by **Benjamin Ekow Attabra**. Images and other resources used are credited to their respective owners.
