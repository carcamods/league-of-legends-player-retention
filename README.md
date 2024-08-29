# League of Legends Player Retention Project

## Project Description
This project aims to build a predictive model to analyze and predict player retention in League of Legends. By leveraging data from the Riot Games API, the project will identify patterns and factors that influence player retention.

## Directory Structure
The project is organized into the following directories:

- **docs/**: Contains project documentation and reports.
- **data/**: Stores raw and processed data files.
- **src/**: Includes all source code related to data processing, feature engineering, and model development.
- **notebooks/**: Contains Jupyter/Colab notebooks used for data exploration, analysis, and model training.
- **scripts/**: Utility scripts for tasks like data collection and preprocessing.
- **tests/**: Contains test scripts to ensure the reliability of the project code.

## Setup Instructions
Follow these steps to set up the project environment:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/carcamods/league-of-legends-player-retention.git
   cd league-of-legends-player-retention
   ```

2. **Install Dependencies**:

   - If using a local environment, you may want to set up a virtual environment and install the required packages:
     ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows use `venv\Scriptsctivate`
     pip install -r requirements.txt
     ```

   - If using Google Colab, the dependencies can be installed directly in the notebook using:
     ```python
     !pip install -r requirements.txt
     ```

3. **API Setup**:
   - Ensure you have registered for the necessary API keys (Riot Games API).
   - Store API keys securely in environment variables or a `.env` file.

## Usage Instructions
Here’s how to use the project:

1. **Data Collection**:
   - Run the data collection scripts located in the `scripts/` directory to gather data from the specified sources.

2. **Data Processing**:
   - Use the notebooks in the `notebooks/` directory to process and clean the data.
   - Processed data is stored in the `data/` directory.

3. **Model Training**:
   - Train your predictive models using the scripts or notebooks provided in the `src/` and `notebooks/` directories.
   - Evaluate model performance and save results in the appropriate directories.

4. **Deployment**:
   - The model can be deployed using a cloud service or web framework (e.g., Flask, FastAPI). Deployment instructions and scripts will be provided in the `docs/` directory.

## Contribution Guidelines
If you would like to contribute to this project, please follow these guidelines:

1. **Fork the Repository**: Click the "Fork" button at the top right of the GitHub page.
2. **Create a Branch**:
   ```bash
   git checkout -b feature-branch
   ```
3. **Make Changes**: Implement your feature or fix a bug.
4. **Submit a Pull Request**: Once your changes are ready, submit a pull request to the main repository for review.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgments
- Special thanks to the Riot Games API team for providing access to game data.
