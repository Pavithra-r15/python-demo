def main():
    try:
        a=5//0
        print(a)
    except Exception as error:
        print("error is", error)
    finally:
        print("no error")
        return
main()