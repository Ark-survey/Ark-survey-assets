from operator import length_hint
import os
from PIL import Image
from imageSizeChange import img_size_change
# from toWebp import to_webp
from utils import make_sprites
from abUnpack import unpack_all_assets


unpack_all_assets('source','destination')

img_size_change('destination','resize&group')

make_sprites('char',['char_'])
make_sprites('uniequip',['uniequip_','default'], "skill_icon_", "uniequipimg")
make_sprites('skill',['skill_icon_skchr_','skill_icon_skcom_'])

# to_webp('css-sprites')