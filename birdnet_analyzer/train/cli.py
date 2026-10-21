from birdnet_analyzer.utils import runtime_error_handler


@runtime_error_handler
def main():
    from birdnet_analyzer import cli
    from birdnet_analyzer.train.core import train # SH 18-Sep-2025: imports the train function explicitly, if not the train function and the train module will be confused and throw a "module object is not callable" error.

    # Parse arguments
    parser = cli.train_parser()

    args = parser.parse_args()

    train(**vars(args))
