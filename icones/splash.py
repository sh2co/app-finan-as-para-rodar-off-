import glob
from PIL import Image
logo = Image.open('icones/logo.png').convert('RGBA')
n = 0
for f in glob.glob('android/app/src/main/res/**/splash.png', recursive=True):
    try:
        w, h = Image.open(f).size
        bg = Image.new('RGBA', (w, h), (255, 255, 255, 255))
        lw = int(min(w, h * 2.5) * 0.5)
        lh = int(lw * logo.height / logo.width)
        bg.alpha_composite(logo.resize((lw, lh), Image.LANCZOS), ((w - lw) // 2, (h - lh) // 2))
        bg.convert('RGB').save(f)
        n += 1
    except Exception as e:
        print('ignorado', f, e)
print('telas de abertura atualizadas:', n)
