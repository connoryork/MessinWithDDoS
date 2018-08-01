import requests, time


def send(path):
    requests.get(path)


def send_multiple(path, amount):
    for _ in range(amount):
        send(path)


def send_infinite(path):
    while True:
        send(path)


def send_timed(path, seconds):
    start = time.time()
    while time.time() - start < seconds:
        send(path)


if __name__ == '__main__':
    """
    visit this site to see requests 
    https://webhook.site/#/67dd3ec8-237c-4753-aa9e-94a4dfee4da9/375ec8fb-355a-468a-9a72-2fcf0cd785a3/0
    """
    test_request_url = "https://webhook.site/67dd3ec8-237c-4753-aa9e-94a4dfee4da9"
    send_timed(test_request_url, 10)
