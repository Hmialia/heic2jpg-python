import os
import pyheif
from PIL import Image

def heic2jpg (base):
  for root, ds, fs in os.walk(base):
    for f in fs:
      if f.endswith('.heic') or f.endswith('.HEIC'):
        fullname = os.path.join(root, f)
        i = pyheif.read_heif(fullname)
        pi = Image.frombytes(mode=i.mode, size=i.size, data=i.data)
        pi.save(fullname[:-5]+".jpg", format="jpeg")
        os.remove(fullname)

if __name__ == "__main__":
    heic2jpg('C:\\pictures')