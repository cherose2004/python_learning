from django.db.models.signals import pre_save, post_save


def callback(sender, **kwargs):
    print("xxoo_callback")
    print(sender, kwargs)


# post_save.connect(callback)
# post_save.connect(callback1)

from django.dispatch import receiver

#
# @receiver(post_save)
# def callback1(sender, **kwargs):
#     print("xxoo_callback1111111")
#     print(sender, kwargs)


from sg import pizza_done


# @receiver(pizza_done)
# def callback2(sender, **kwargs):
#     print("xxoo_callback2222")
#     print(sender, kwargs)
