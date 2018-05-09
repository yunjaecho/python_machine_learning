import math

# duck typing
#   - 타입을 미리 정하는게 아니라 실행이 되었을 때 해당 Method들을 확인하여 타입을 정한다.
def example_function(name: str, radius: float) -> str:
    area = math.pi * radius * 2
    return "The area of {} is {}".format(name, area)

print(example_function("Bob" , 5))
