from renamer import Renamer
from arg_parsing import get_args

if __name__ == "__main__":
    args = get_args()
    print(args)
    renamer = Renamer(args)
    renamer.start()