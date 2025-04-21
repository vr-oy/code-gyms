from typing import Never
import re

class Input_Utils:
    @classmethod
    def get_number_list_interactively(cls,options={}) -> list[int] | None:
        print(options.get('inputText') or 'Enter the comma separated numbers:')
        try:
            nums = cls.get_number_list()
            print(options.get('confirmText') or "List of numbers:", nums)
            return nums
        except ValueError as e:
            print(options.get('errorText') or 'the input is invalid')
            return None

    @staticmethod
    def get_number_list() -> list[int] | Never:
        list_str:str = input()
        if(not list_str or not all(map(lambda item : bool(re.match(r"^[-+]?\d+$", item)),list_str.split(',')))):
            raise ValueError('Invalid input')

        # Create a list 'nums' with specific elements
        nums = list(map(int,list_str.split(',')))

        return nums