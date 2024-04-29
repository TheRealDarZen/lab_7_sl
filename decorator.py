import logging
import time

#Configuration
logger = logging.getLogger(__name__)
logging.basicConfig(filename='decorator.log',level=logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

def log(level=logging.INFO):
    def decorator(func_or_class):
        logger.setLevel(level)

        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func_or_class(*args, **kwargs)
            end_time = time.time()

            duration = end_time - start_time

            logger.log(level, f'Function {func_or_class.__name__} called with args: {args}, kwargs: {kwargs}.')
            logger.log(level, f'Call time: {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time))}')
            logger.log(level, f'Execution time: {duration:.10f} seconds.')
            logger.log(level, f'Returned: {result}.')

            return result


        if isinstance(func_or_class, type):
            def init_wrapper(*args, **kwargs):
                obj = func_or_class(*args, **kwargs)

                logger.log(level,f'Class {func_or_class.__name__} instantiated with args: {args}, kwargs: {kwargs}.')

                return obj
            return init_wrapper

        return wrapper

    return decorator


@log(level=logging.INFO)
def example_function(x, y):
    return (x + y)

@log(level=logging.INFO)
class ExampleClass:
    def __init__(self, x):
        self.x = x



if __name__ == "__main__":
    f = example_function(3, 4)
    c = ExampleClass(10)
