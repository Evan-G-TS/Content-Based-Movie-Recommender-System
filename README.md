# ML_Project1 -- Content-Based Movie Recommender System

📊 Project Status
✅ Phase 1: Project Setup and Structure
✅ Phase 2: Data Ingestion Pipeline
🔄 Phase 3: Feature Engineering (In Progress)
⏳ Phase 4: Model Development
⏳ Phase 5: Web Interface
⏳ Phase 6: Testing and Documentation
⏳ Phase 7: Deployment

## Overview

A content-based movie recommendation system that leverages the IMDB dataset to provide personalized movie suggestions based on a user's bookmarked movies. The system analyzes movie metadata including genres, cast, crew, plot keywords, and other features to build a comprehensive user preference profile and generate accurate recommendations.

[Python 3.12](https://www.python.org/downloads/)
[scikit-learn](https://scikit-learn.org/)
[License: MIT](https://opensource.org/licenses/MIT)


steps:
* Created template.py, setup.py, added a virtual environment, set up GitHub repository
* added my csv file to the online database of Supabase and connected it to my DBeaver locally
* creating the Data Ingestion phase.





### Key Features
- **Personalized Recommendations**: Generates suggestions based on user's bookmarked movies
- **Multi-Feature Analysis**: Utilizes genres, cast, directors, plot descriptions, and more
- **Scalable Architecture**: Modular design following industry best practices
- **Interactive Web Interface**: User-friendly frontend for easy interaction
- **Production Ready**: Includes Docker support and configuration management

## 🏗️ Project Architecture

The project follows a modular, production-ready structure inspired by clean architecture principles:

📦 movie-recommender-system
├── 📂 src # Source code root
│ └── 📂 recommender # Main package
│ ├── 📂 components # Core ML components
│ │ ├── init.py
│ │ ├── data_ingestion.py # Data loading module
│ │ ├── data_transformation.py # Feature engineering
│ │ └── model_trainer.py # Recommendation model
│ ├── 📂 utils # Utility functions
│ │ ├── init.py
│ │ └── common.py # Shared utilities
│ ├── 📂 config # Configuration management
│ │ ├── init.py
│ │ └── configuration.py # Config loader
│ ├── 📂 pipeline # ML pipelines
│ │ ├── init.py
│ │ ├── data_ingestion_pipeline.py
│ │ ├── data_transformation_pipeline.py
│ │ └── model_training_pipeline.py
│ ├── 📂 entity # Entity definitions
│ │ ├── init.py
│ │ └── config_entity.py # Configuration entities
│ └── 📂 constants # Project constants
│ └── init.py
├── 📂 config # Configuration files
│ ├── config.yaml # Main configuration
│ └── schema.yaml # Data schema
├── 📂 research # Jupyter notebooks for experimentation
│ └── research.ipynb
├── 📂 templates # Web interface templates
│ └── index.html
├── 📂 tests # Unit tests
│ ├── init.py
│ ├── test_components.py
│ └── test_pipelines.py
├── main.py # Application entry point
├── params.yaml # Model parameters
├── setup.py # Package installation
├── requirements.txt # Dependencies
├── Dockerfile # Docker configuration
├── .gitignore
└── README.md




Author: Evan Tsiotsias

GitHub: 

LinkedIn: Your Profile

Acknowledgments : 
IMDB for providing the dataset
Scikit-learn community for amazing ML tools
