class FromTxtToHtmlAdapter:
    def __init__(self, file_path):
        self.__file_path = file_path

    def from_txt_to_html(self):
        with open(self.__file_path) as file:
            lines = file.readlines()

        header = lines[0].replace('\n', '').split(',')
        data = [item.replace('\n', '').split(',') for item in lines[1:]]
        results = [dict(zip(header, user_data)) for user_data in data]
        my_list = []
        for result in results:
            my_list.append(''.join([f'<{item}>{value}</{item}>\n' for (item, value) in result.items()]))
        return ''.join(my_list)


if __name__ == '__main__':
    html = FromTxtToHtmlAdapter("users.txt").from_txt_to_html()
    print(html)

