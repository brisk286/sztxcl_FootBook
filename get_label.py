import os
os.environ["KMP_DUPLICATE_LIB_OK"]  =  "TRUE"
import pandas as pd
import easyocr


def getOcr(image_path):
    """
    调用OCR
    :param image_path: 要识别的图片地址 （String）
    :return: ocr的识别结果 （String）
    """
    reader = easyocr.Reader(['en'])  #
    result = str(reader.readtext(image_path, detail=0, allowlist=["0", "1", "2", "3", "4", "5", "6",
                                                                  "7", "8", "9"]))
    result = result.replace(' ', '').replace('[', '').replace(']', '').replace('\'', '').replace(',', '')  # 去除一些符号拼合字符串

    return result


if __name__ == '__main__':

    path = r"C:\"
    labelPath = r"C:\"

    images = os.listdir(path)
    labels = []

    for each in images:
        result = getOcr(path + "\\" + each)
        labels.append(result)

        print(each + '\n' + result + '\n')

    pd.DataFrame({"name": images, "label": labels}).to_csv(labelPath + "\\" + "data_csv.csv", index=False)

    result = getOcr(r'C:\')

    print(result)