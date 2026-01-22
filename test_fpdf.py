from fpdf import FPDF
import os

# Test if FPDF can embed images
pdf = FPDF()
pdf.add_page()

img_path = 'analysis_output/score_distribution.png'
print(f'Image path: {img_path}')
print(f'Exists: {os.path.exists(img_path)}')
print(f'Size: {os.path.getsize(img_path)} bytes')

pdf.image(img_path, x=10, w=100)
pdf.output('test_image.pdf')

print(f'Test PDF size: {os.path.getsize("test_image.pdf")} bytes')
print('If test PDF is much larger than a few KB, images work!')
