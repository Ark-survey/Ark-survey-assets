from operator import length_hint
import os
from PIL import Image
from imageSizeChange import img_size_change
from utils import make_sprites
from abUnpack import unpack_all_assets


unpack_all_assets('source','destination')

img_size_change('destination','resize&group')

make_sprites(['char_'])
make_sprites(['uniequip_','default'])
make_sprites(['skill_icon_'])