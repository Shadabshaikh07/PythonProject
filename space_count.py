import os

my_dir = 'C:\\Users\\Shadab\\OneDrive\\Desktop\\IMDB'


def sum_space(folder):
    sum = 0
    for f in os.listdir(folder):
        # type = 'd' if os.path.isdir(os.path.join(my_dir, f)) else '-'
        if os.path.isfile(os.path.join(folder, f)):
            size = os.path.getsize(os.path.join(folder, f))
            sum = sum + size
        else:
            sum += sum_space(os.path.join(folder, f))
    return sum


print('Space occupied by {}: {}'.format(my_dir, sum_space(my_dir)))