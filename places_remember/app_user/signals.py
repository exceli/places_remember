from allauth.socialaccount.models import SocialAccount


def get_extra_data(user, provider, **kwargs):
    if not user or not provider:
        return None

    try:
        social_account = user.socialaccount_set.filter(provider='google')[0].extra_data
    except SocialAccount.DoesNotExist:
        return None
    else:
        return social_account.extra_data