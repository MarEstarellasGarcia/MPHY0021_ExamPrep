from argparse import ArgumentParser
from .laboratory import Laboratory
import yaml


def process():
    parser = ArgumentParser(description="Input alchemist file location")
    parser.add_argument("ymlLoc", type=str,
                        help="Input the location of your alchemist.yml file")
    parser.add_argument('--reactions', '-r', action="store_true",
                        help="Outputs the total number of reactions")

    args = parser.parse_args()

    ymlFile = yaml.load(open(args.ymlLoc))

    [shelf1, shelf2] = read_input_file(ymlFile)

    myLab = Laboratory(shelf1, shelf2)

    [new_shelf1, new_shelf2, count] = myLab.run_full_experiment(shelf1, shelf2)

    if args.reactions:
        print(count)
    else:
        print("lower: [%s]\nupper: [%s]"
              % (', '.join(map(str, new_shelf1)),
                 ', '.join(map(str, new_shelf2))))


if __name__ == "__main__":
    process()


def read_input_file(ymlFile):
    if len(ymlFile) > 2:
        raise ValueError('Not more than two shelves, please!')
    else:
        shelf1 = ymlFile.get("lower")
        shelf2 = ymlFile.get("upper")
    return shelf1, shelf2
