
def call_with_retry(no_retries, time_between_retries, enable_retry, logger,
                    no_retry_condition=lambda x:False):
    # Decorator to handle retry mechanism.
    def caller(func):
        def wrapped(*args, **kwargs):
            n_retries = no_retries
            if not enable_retry:
                try:
                    logger.debug('Calling %(func)s with parameters %(args)s and '
                                 '%(nargs)s' % {'func': func.__name__, 'args': args,
                                                'nargs': kwargs})
                    result = func(*args, **kwargs)
                # Catch all exception, and re raise the calling function handle this
                # So we don't need to handle each exception on every level.
                except Exception as e:
                    raise
                else:
                    return result
            else:
                while n_retries > 0:
                    try:
                        logger.debug('Calling [%(func)s]: with %(args)s and %(nargs)s'
                                     %{'func': func.__name__, 'args': args,
                                       'nargs': kwargs})
                        result = func(*args, **kwargs)
                    # Catch all exception, and re raise when we did all retries
                    # the calling function handle this
                    except Exception as e:
                        logger.warn('Error when calling [%(func)s]: with %(args)s and'
                                    ' %(nargs)s - %(exception)s, remaining %(num)s '
                                    'retries' % {'func': func.__name__, 'args': args,
                                                 'nargs': kwargs, 'exception': e,
                                                 'num': n_retries-1})
                        # No need for retry in case of this condition
                        if no_retry_condition(e):
                                raise
                        n_retries -= 1
                        if n_retries == 0:
                            raise
                        else:
                            time.sleep(time_between_retries)
                    else:
                        return result
        return wrapped
    return caller
