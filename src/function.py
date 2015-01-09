# pointless test function to test codecov
import logging

def split_some_parts(item):
    i = 0
    if len(item):
        parts = item.split('.')
        i += 1
        if len(parts) >= 2:
            i += 1
        if len(parts) >= 3:
            i += 1
        if len(parts) >= 4:
            i = len(parts)

    result = i

    if result == 0:
        logging.error('you must have parts')
    if result == 1:
        logging.info('you have one part')
    elif result == 2:
        logging.info('you have two parts')
    elif result == 3:
        logging.info('you have three parts')
    else:
        logging.warn('you have more than three parts')

    return result
