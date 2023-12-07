import os


def dashes_before_after_text(func):
    def func_with_decorator(*args, pre_pause_text="Lista słów w słowniku", post_pause_text="KONIEC", **kwargs):
        if os.getenv("ENABLE_DECORATOR", "True") == "True":
            os.system('cls')
            print(f"---------- {pre_pause_text} ----------")
            func(*args, **kwargs)
            print(f"---------- {post_pause_text} ----------\n")
        else:
            func(*args, **kwargs)

    return func_with_decorator
