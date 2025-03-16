import call_site_logging as cslogging

module_logger = cslogging.getLogger()


def my_function():
    function_logger = cslogging.getLogger()
    function_logger.info("Message from function")


class MyClass:
    def __init__(self):
        self.class_logger = cslogging.getLogger()
        self.class_logger.info("Message from Class")

    def my_method(self):
        method_logger = cslogging.getLogger()
        method_logger.info("Message from Class method")


def main():
    cslogging.basicConfig(
        level=cslogging.INFO, format="%(levelname)s - %(name)s - %(message)s"
    )

    module_logger.info("Message from module level")
    my_function()
    instance = MyClass()
    instance.my_method()


if __name__ == "__main__":
    main()
