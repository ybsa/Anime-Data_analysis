from fpdf import FPDF
import os

# Simple test with the exact same paths as generate_pdf.py
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
output_dir = os.path.join(project_root, "analysis_output")

print(f"Script dir: {script_dir}")
print(f"Project root: {project_root}")
print(f"Output dir: {output_dir}")

pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)

# Add all images like the main script does
images = [
    'score_distribution.png',
    'trends_over_time.png',
    'top_genres.png',
    'score_vs_popularity_binned.png',
    'top_studios.png'
]

for img in images:
    pdf.add_page()
    img_path = os.path.join(output_dir, img)
    print(f"Adding: {img_path}")
    print(f"  Exists: {os.path.exists(img_path)}")
    if os.path.exists(img_path):
        print(f"  Size: {os.path.getsize(img_path)} bytes")
        pdf.image(img_path, x=25, w=160)

pdf.output('test_multiple.pdf')
final_size = os.path.getsize('test_multiple.pdf')
print(f"\nFinal PDF size: {final_size} bytes ({final_size/1024:.1f} KB)")
print("Expected: Should be > 100 KB if images embedded")
