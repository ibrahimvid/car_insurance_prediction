Simple prediction script for the car insurance model.

This file is intentionally lightweight and focuses on showing a
professional project structure rather than being a full production
pipeline.

Suggested usage (after you add a trained model artifact and loading code):

    python -m src.predict --input data/Test_data.csv --output prediction_results.csv

You can extend this script to:
- Load a serialized model (e.g. from `models/`)
- Apply the same preprocessing used in the training notebook
- Save predictions with the correct submission format
