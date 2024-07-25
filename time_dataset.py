def test():
    dset = EvenDataset(2, 10)
    prefix = "testing EvenDataset(2, 10)..."

    assert len(dset) == 4, prefix + f"len(dset) should equal 4, got {len(dset)}"
    assert dset[0] == 2, prefix + f"dset[0] should equal 2, got {dset[0]}"
    assert dset[2] == 6, prefix + f"dset[2] should equal 6, got {dset[2]}"
    assert dset[:2] == [2, 4], prefix + f"dset[:2] should equal [2, 4], got {dset[:2]}"


def time():
    abs_ = [(2, 2 ** x) for x in range(2, 17)]

    for a, b in abs_:
        dset = EvenDataset(a, b)
        vals = list(dset[a: b])


if __name__ == "__main__":
    import sys
    import timeit
    import importlib
    from argparse import ArgumentParser

    parser = ArgumentParser(description="Test Implementation of EvenDataset")
    parser.add_argument("--module_name", type=str, default="dataset",
                        help="module name that contains EvenDataset, default 'dataset'")
    parser.add_argument("--class_name", type=str, default="EvenDataset",
                        help="class name to import, default 'EvenDataset'")

    args = parser.parse_args()

    _module = importlib.import_module(args.module_name)
    EvenDataset = _module.__getattribute__(args.class_name)

    test()
    t = timeit.timeit("time()", setup="from __main__ import time", number=100)

    dset = EvenDataset(2, 2 ** 16)


    def get_size_of(dset):
        return sum(map(sys.getsizeof, dset.__dict__.values()))


    s = get_size_of(dset)

    print(f"time (s): {t}, size (Bytes): {s: ,}")
