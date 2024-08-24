import qrcode
from PIL import Image,ImageDraw,ImageFont



qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

qr.add_data("2134")
qr.make(fit=True)
img = qr.make_image(fill_color='green', back_color="white")

# 创建一个新的图像，用于放置二维码和文字
width, height = img.size
new_width = width + 100  # 增加宽度以容纳文字
new_height = height + 30
imgnew = Image.new('RGB', (new_width, new_height), color='white')
# 将二维码粘贴到新图像上剧中
setimg_x = (new_width - width) // 2
setimg_y = (new_height - height) // 2
imgnew.paste(img, (setimg_x, setimg_y))

imgnew.save("./Pic/test.png")

############################################################
import qrcode

# data = 'https://www.baidu.com/'
# img_file = r'./Pic/code.png'
# # 实例化QRCode生成qr对象
# qr = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_H,
#     box_size=10,
#     border=4
# )
# # 传入数据
# qr.add_data(data)
# qr.make(fit=True)
# # 生成二维码
# img = qr.make_image()
# # 保存二维码
# img.save(img_file)
# # 展示二维码
# img.show()



