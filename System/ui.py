from time import sleep


def loadBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='>'):
    # Loading bar from https://www.youtube.com/watch?v=MtYOrIwW1FQ
    percent = ('{0:.' + str(decimals) + 'f}').format(100 * (iteration/float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
    if iteration == total:
        print()

def runLoadbar(duration=3, bar_width=75):
    """
    Create a progress bar that runs for `duration` seconds and is `bar_width` characters wide
    
    :param duration: The total time the loadbar will run for(optional)
    :param bar_width: The width of the bar in characters (optional)
    """
    items = list(range(0, bar_width))
    l = len(items)
    loadBar(0, l, prefix='Progress: ', suffix="Complete", length=l)
    for i, _ in enumerate(items):
        sleep(duration / bar_width)
        loadBar(i + 1, l, prefix="Progress: ", suffix="Complete", length=l)