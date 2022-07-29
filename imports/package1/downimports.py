# from utils import helper
# from utils.sub_utils.sub_helper import subHelperFun
from package1.utils.sub_utils.sub_helper import subHelperFun
from package1.utils.helper import helperFun
val = helperFun()
print(val)
if __name__ == "__main__":
    val = helperFun()
    print(val)

    val1 = subHelperFun()
    print(val1)
