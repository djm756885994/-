#a = "i, am, a, student, in, chengdu"
def foo(arg):
    arg = "student"
def bar(args):
    args = "chengdu"
arg = input("请输入一个名字：")
args = input("请输入一个地名：")
print("i am a %s in %s" % (arg, args))
