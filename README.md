# Birefringence Analysis Web App

A simple web-based tool to estimate birefringence and calculate pre-tilt angles from uploaded optical images using Michel–Levy chart interpolation.

---

## 🚀 Features

- Upload microscope images  
- Select 3 points of interest on the image  
- Estimate birefringence from RGB values using Michel–Levy interpolation  
- Compute pre-tilt angles using physical formulas  

---

## 🧰 Requirements

- Python 3.7 or later  

Install dependencies:

```bash
pip install -r requirements.txt

Or manually:

bash
Copy
Edit
pip install Flask opencv-python numpy scikit-image scipy gunicorn
