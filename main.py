def create_formatted_receipt(products, width_of_receipt):
    receipt_lines = []
    for product in products:
        name, price = product
        string_price = ' ' + str(price) + ' руб.'
        full_name = name + string_price
        short_name_len = (width_of_receipt - 2) - len(full_name)
        if short_name_len > 0:
            line = name + ' ' * short_name_len + string_price
        else:
            line = name[:short_name_len-3] + '...' + string_price
        receipt_lines.append(line)
    return receipt_lines


def print_all_lines(lines, width_of_receipt):
    print(' ' + '_' * (width_of_receipt-2))
    print('|' + ' ' * (width_of_receipt-2) + '|')
    for line in lines:
        print('|' + str(line) + '|')
    print('|' + '_' * (width_of_receipt-2) + '|')


if __name__ == '__main__':
    PRODUCTS = [
        ['яблоки', 100],
        ['швейцарский сыр', 1500],
        ['красная рыба', 450],
        ['морской окунь холодного копчения', 1000]
        ]
    WIDTH_OF_RECEIPT = 30
    print_all_lines(
        create_formatted_receipt(PRODUCTS, WIDTH_OF_RECEIPT),
        WIDTH_OF_RECEIPT)
