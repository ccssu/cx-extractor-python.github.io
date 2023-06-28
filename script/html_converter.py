
def convert_html_encoding(input_file, output_file, input_encoding, output_encoding):
    # 读取原始 HTML 文件
    with open(input_file, "r", encoding= input_encoding, errors='ignore') as file:
        html_content = file.read()

    # 移除原始 HTML 文件中的 <meta charset="gb2312">
    html_content = html_content.replace(f'<meta charset="{input_encoding}">', f'<meta charset="{output_encoding}">')

    # 将内容保存为指定编码的 HTML 文件
    with open(output_file, "w", encoding= output_encoding) as file:
        file.write(html_content)

# 得到路径下文件 
def get_file_list(path):
    import os
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

if __name__ == "__main__":
  # 将 gb2312 编码的 HTML 文件转换为 utf-8 编码的 HTML 文件

#   input_path = r'/workspace/cx-extractor-python/RawHtml'

#   for file in get_file_list(input_path):
#     print(f'Converting {file}')
#     convert_html_encoding(file, file, "gb2312", "utf-8")

    arr1 = get_file_list(r'/workspace/cx-extractor-python/bbcnews-html')
    arr2 = get_file_list(r'/workspace/cx-extractor-python/bbcnews-text') 
    arr1.sort()
    arr2.sort()
    zipped = zip(arr1, arr2)
    with open('result.txt', 'w') as f:
        for file1, file2 in zipped:
            print(f'{file1} {file2}')
            file1 = file1.replace('/workspace/cx-extractor-python/', '')
            file2 = file2.replace('/workspace/cx-extractor-python/', '')
            x1=f'<p><a href="{file1}" target="_blank" rel="noopener">{file1}</a></p>'
            x2=f'<p><a href="{file2}" target="_blank" rel="noopener">{file2}</a></p>'
            # 逐行写入

            f.write(x1+'\n'+x2+'\n')
