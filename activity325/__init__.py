import check50
import check50.c

@check50.check()
def exists():
    """python files exist"""
    check50.exists("main.py")
    check50.exists("psrock.py")
    check50.exists("strategy.py")

@check50.check(exists)
def test1():
    """main.py runs without error"""
    check50.run("python3 main.py").stdout("*Win-loss-tie*", timeout=5).exit()
