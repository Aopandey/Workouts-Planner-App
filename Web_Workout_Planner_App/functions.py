FILEPATH = "Workouts.txt"


def get_workouts(filepath=FILEPATH):
    """ Read a text file and return the list of Workouts """
    with open(filepath, 'r') as file_local:
        workouts_local = file_local.readlines()
    return workouts_local


def write_workouts(get_args, filepath=FILEPATH):
    """ Write Workouts in the text file """
    with open(filepath, 'w') as file:
        file.writelines(get_args)

