import qrcode
from PIL import Image,ImageDraw,ImageFont

def ReadTxt(file_name):
    dict = {}
    file = open(file_name,'r')
    lines = file.readlines()
    for line in lines:
        parts = line.strip().split(',')
        dict[parts[0]] = (parts[1],parts[2])
    return dict

def CreatePicsCode(dict):

    for dict_Key in dict.keys():
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(dict_Key)
        # img = qrcode.make(dict_Key)
        qr.make(fit=True)
        img_qr = qr.make_image(fill_color="black", back_color="white")

        # 创建一个新的图像，用于放置二维码和文字
        qrwidth, qrheight = img_qr.size
        outputPicwidth = qrwidth +100 # 增加宽度以容纳文字
        outputPicheight = qrheight + 20
        outputPic = Image.new('RGB', (outputPicwidth, outputPicheight), color='white')
        # 将二维码粘贴到新图像上剧中
        pasteqr_x=(outputPicwidth-qrwidth)//2
        pasteqr_y =(outputPicheight-qrheight)//2
        outputPic.paste(img_qr, (pasteqr_x, pasteqr_y))

        #在新图像上添加文字
        drawText = ImageDraw.Draw(outputPic)
        font = ImageFont.truetype('msyh.ttc', 30)  # 选择字体和大小
        text = f"板长:{dict[dict_Key][0]},板宽:{dict[dict_Key][1]}"
        (text_left, text_top,text_right,text_bottom) = drawText.textbbox((0,0),text, font=font)
        text_x =(outputPicwidth - (text_right-text_left) ) //2 # 计算文字位置
        text_y = (outputPicheight-(text_bottom-text_top) )-20
        drawText.text((text_x, text_y), text, font=font, fill='black')

        outputPic.save(f"./Pic/{dict_Key}.png")

if __name__ =="__main__":
    CreatePicsCode(ReadTxt("./PanelInfo.txt"))
