class SwimMixin:
    """
    Mixin class that provides swimming ability.
    This class is intended to be used alongside other classes
    to add the swim() method functionality.
    """
    def swim(self):
        """
        Print a message indicating that the creature can swim.
        """
        print("The creature swims!")


class FlyMixin:
    """
    Mixin class that provides flying ability.
    This class is intended to be used alongside other classes
    to add the fly() method functionality.
    """
    def fly(self):
        """
        Print a message indicating that the creature can fly.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A Dragon class that can swim and fly by inheriting from
    SwimMixin and FlyMixin. It also has its own behavior like roaring.
    """
    def roar(self):
        """
        Print a message indicating that the dragon is roaring.
        """
        print("The dragon roars!")