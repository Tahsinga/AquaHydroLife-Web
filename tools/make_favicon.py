from PIL import Image
import sys

def make_favicon(src='static/images/recent_projects/water.png', dst='static/favicon.ico'):
    img = Image.open(src).convert('RGBA')
    sizes = [(16,16),(32,32),(48,48),(64,64),(128,128),(256,256)]
    img.save(dst, format='ICO', sizes=sizes)

if __name__ == '__main__':
    src = sys.argv[1] if len(sys.argv) > 1 else 'static/images/recent_projects/water.png'
    dst = sys.argv[2] if len(sys.argv) > 2 else 'static/favicon.ico'
    make_favicon(src, dst)
