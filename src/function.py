# pointless test function to test codecov
import logging

def split_some_parts(item):
    i = 0
    parts = item.split('.')
    if len(parts) >= 1:
        i += 1
    if len(parts) >= 2:
        i += 2
    if len(parts) >= 3:
        i += 3

    result = i

    if result == 1:
        logging.info('you have one part')
    elif result == 2:
        logging.info('you have two parts')
    elif result == 3:
        logging.info('you have three parts')
    else:
        logging.info('you have more than three parts')

    return result
