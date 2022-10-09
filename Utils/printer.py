class Bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    INFO = "\033[95m"
    FAIL = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    ENDC = "\033[0m"

    # Method that returns a message with the desired color
    @staticmethod
    def colored(message, color):
        print(color + message + Bcolors.ENDC)

    # Method that returns an orange info
    @staticmethod
    def info(message):
        print(Bcolors.INFO + message + Bcolors.ENDC)

    # Method that returns a yellow warning
    @staticmethod
    def warning(message):
        print(Bcolors.WARNING + message + Bcolors.ENDC)

    # Method that returns a red fail
    @staticmethod
    def fail(message):
        print(Bcolors.FAIL + message + Bcolors.ENDC)

    # Method that returns a green ok
    @staticmethod
    def ok(message):
        print(Bcolors.OKGREEN + message + Bcolors.ENDC)

    # Method that returns a blue ok
    @staticmethod
    def okblue(message):
        print(Bcolors.OKBLUE + message + Bcolors.ENDC)

    # Method that returns a header in some purple-ish color
    @staticmethod
    def header(message):
        print(Bcolors.HEADER + message + Bcolors.ENDC)

