import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    result = []
    if os.path.isfile(path) and path.endswith(suffix):
            result.append(path)
    elif os.path.isdir(path):
        for new_path in os.listdir(path):
            sub_dir = "/".join([path, new_path])
            subdir_output = find_files(suffix=suffix, path=sub_dir)
            for subpath in subdir_output:
                result.append(subpath)
    return result

if __name__ == '__main__':

    test_dir_path = './testdir'

    # Test 1
    result1 = find_files(suffix="c", path=test_dir_path)
    assert result1 == ['./testdir/subdir3/subsubdir1/b.c',
                      './testdir/t1.c',
                      './testdir/subdir5/a.c',
                      './testdir/subdir1/a.c']
    print(result1)

    # Test 2
    result2 = find_files(suffix="h", path=test_dir_path)
    assert result2 == ['./testdir/subdir3/subsubdir1/b.h',
                       './testdir/subdir5/a.h',
                       './testdir/t1.h',
                       './testdir/subdir1/a.h']
    print(result2)

    # Test 3
    result3 = find_files(suffix="b.c", path=test_dir_path)
    assert result3 == ['./testdir/subdir3/subsubdir1/b.c']
    print(result3)