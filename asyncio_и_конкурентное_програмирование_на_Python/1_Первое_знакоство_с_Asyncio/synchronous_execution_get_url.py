from utilits import timer, URLS, read_headers_url


@timer
def get_synch_url():
    read_headers_url(URLS['Google'])


if __name__ == '__main__':
    get_synch_url()