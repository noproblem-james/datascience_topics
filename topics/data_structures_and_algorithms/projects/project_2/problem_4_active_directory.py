
class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    seen_groups = set()
    if user in set(group.users):
        return True
    elif len(group.groups) < 1:
        return False
    else:
        for child in group.groups:
            if child in seen_groups:
                pass
            else:
                seen_groups.add(child)
            return is_user_in_group(user, child)


if __name__  == '__main__':
    # Test 1
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")
    sub_child_user = "sub_child_user"

    parent.add_group(child)
    child.add_group(sub_child)
    sub_child.add_user(sub_child_user)
    print(is_user_in_group(sub_child_user, parent))

    # Test 2
    fake_child_user = "fake_child_user"
    print(is_user_in_group(fake_child_user, parent))

    # Test 3
    child_user = "child_user"
    child.add_user(child_user)
    print(is_user_in_group(child_user, sub_child))
