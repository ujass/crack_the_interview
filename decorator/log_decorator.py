def my_logger(orginal_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orginal_func.__name__), level=logging.INFO) 

    def wrapper(*args, **kwargs):

        # when i put * & ** ahead of args & kwargs in format,age was considering as keyward arg.
        # when i remove it then both name, age was considering as args.
        logging.info('Run with args: {} and kwargs: {}'.format(args,kwargs)) 
        return orginal_func(*args, **kwargs) # at this point orginal function run

    return wrapper    # return without calling so, we can run it later. 

@my_logger
def display_info(name, age):
    print('Running display info with argument = ({}, {})'.format(name, age))

display_info('jay', 24)   # after running this display_info log has also created.