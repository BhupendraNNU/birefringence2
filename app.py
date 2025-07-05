import os
import cv2
import numpy as np
from skimage import color
from scipy.interpolate import interp1d
from flask import (
    Flask, request, redirect, url_for,
    render_template, session, send_from_directory
)
from werkzeug.utils import secure_filename

import calculate_pretilt_angle  # your pre-tilt logic

# ---------- Configuration ----------
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'bmp'}

app = Flask(__name__)
app.secret_key = 'replace_this_with_a_random_secret'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(fn):
    return '.' in fn and fn.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# ---------- Michel–Levy calibration ----------
michel_levy_data = {
    (236,  72,  8): 0.055,   # Red
    (255, 165,  0): 0.050,   # Orange
    (255, 255,  0): 0.045,   # Yellow
    (  0, 255,  0): 0.040,   # Green
    (  0,   0,255): 0.030    # Blue
}
michel_levy_rgb   = np.array(list(michel_levy_data.keys()))
michel_levy_biref = np.array(list(michel_levy_data.values()))

# Convert RGB values to Lab space for interpolation (perceptual uniformity)
lab_colors = np.array([
    color.rgb2lab(np.array([[rgb]]) / 255.0)[0][0]
    for rgb in michel_levy_rgb
])

def get_mean_rgb(img, center, radius=10):
    """Extracts the mean RGB value from a circular region."""
    mask = np.zeros(img.shape[:2], dtype=np.uint8)
    cv2.circle(mask, center, radius, (255, 255, 255), -1)
    mean_val = cv2.mean(img, mask=mask)[:3]  # BGR
    # Convert to (R, G, B)
    return (int(mean_val[2]), int(mean_val[1]), int(mean_val[0]))

def interpolate_birefringence(rgb):
    """Interpolate the birefringence value for a given RGB using linear interpolation."""
    # Convert RGB to Lab
    lab_color = color.rgb2lab(np.array([[rgb]]) / 255.0)[0][0]
    # Build the 1D interpolator on-the-fly
    interp_func = interp1d(
        lab_colors[:, 0],      # L channel of your Michel–Levy samples
        michel_levy_biref,     # corresponding birefringence values
        kind='linear',
        fill_value='extrapolate'
    )
    # Interpolate based on the L value
    return float(interp_func(lab_color[0]))

# ---------- Routes ----------
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        file = request.files.get('image')
        if not file or file.filename == '' or not allowed_file(file.filename):
            return "Upload a valid image file", 400
        fn = secure_filename(file.filename)
        path = os.path.join(app.config['UPLOAD_FOLDER'], fn)
        file.save(path)
        session['filename'] = fn
        return redirect(url_for('select'))
    return render_template('index.html')

@app.route('/select')
def select():
    fn = session.get('filename')
    if not fn:
        return redirect(url_for('index'))
    return render_template('select.html', filename=fn)

@app.route('/compute', methods=['POST'])
def compute():
    fn = session.get('filename')
    if not fn:
        return redirect(url_for('index'))

    coords = []
    for i in range(3):
        coords.append((
            int(request.form[f'x{i}']),
            int(request.form[f'y{i}'])
        ))

    img = cv2.imread(os.path.join(app.config['UPLOAD_FOLDER'], fn))
    rgb_vals   = [get_mean_rgb(img, pt) for pt in coords]
    biref_vals = [interpolate_birefringence(rgb) for rgb in rgb_vals]

    # compute pre-tilt angles
    pretilt_angles = calculate_pretilt_angle.calculate_pretilt_angle(biref_vals)

    results = list(zip(coords, rgb_vals, biref_vals, pretilt_angles))
    return render_template('result.html', results=results)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
