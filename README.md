# birefringence2

## Overview

**birefringence2** is a Python-based web application designed for **birefringence analysis** of microscope images. It allows users to upload images, select points of interest, and estimate birefringence values using the Michel–Levy chart interpolation. Additionally, it computes pre-tilt angles based on physical formulas, making it a useful tool for researchers and students working with optical microscopy.

---

## Live Demo

The latest version of this project is **deployed and available online** at:  
**[https://birefringence-web.onrender.com/](https://birefringence-web.onrender.com/)**

---
## Features

- Upload microscope images for analysis.
- Select three points of interest on the image.
- Estimate birefringence from RGB values using Michel–Levy chart interpolation.
- Calculate pre-tilt angles from the analyzed data.
- Web-based interface powered by Flask.

---

## Requirements

- Python 3.7 or higher
- Packages:
  - Flask
  - OpenCV (`opencv-python`)
  - NumPy
  - SciPy
  - scikit-image
  - gunicorn

---

## Installation and Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/BhupendraNNU/birefringence2.git
   cd birefringence2
   ```

2. **Create and activate a virtual environment (optional but recommended):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

---

## Running the Application Locally

1. **Start the Flask development server:**

   ```bash
   python app.py
   ```

   This will start the server, usually accessible at `http://127.0.0.1:5000` or `http://localhost:5000`.

2. **Open your web browser and navigate to the above URL.**

3. **Upload your microscope image and follow the on-screen instructions to perform birefringence analysis.**

---

## Usage

1. **Upload Image:** Click the upload button to select a microscope image from your computer.
2. **Select Points:** Click on three points of interest on the uploaded image.
3. **Analyze:** The application will process the RGB values at the selected points and estimate birefringence using Michel–Levy chart interpolation.
4. **Results:** View the calculated birefringence values and pre-tilt angles.

---

## Technical Details

- **Backend:** Flask web framework
- **Image Processing:** OpenCV and scikit-image for image manipulation
- **Scientific Computing:** NumPy and SciPy for numerical calculations
- **Birefringence Estimation:** Michel–Levy chart interpolation method
- **Pre-tilt Calculation:** Physical formulas for angle computation

---

## Notes

- Ensure you have the required Python version and packages installed.
- The app uses image processing libraries, so large images may take longer to process.
- For production deployment, consider using a production-ready server like Gunicorn.
- The accuracy of birefringence estimation depends on image quality and lighting conditions.

---

## License

This project is licensed under the Apache-2.0 license - see the LICENSE file for details.

---

## Contact

For questions, suggestions, or contributions, please:
- Open an issue on GitHub
- Submit a pull request
- Contact the repository owner

---

## Acknowledgments

- Michel–Levy chart for birefringence color reference
- OpenCV community for image processing tools
- Flask framework for web application development
