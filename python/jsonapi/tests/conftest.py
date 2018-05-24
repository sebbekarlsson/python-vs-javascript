from jsonapi.facades.UserFacade import UserFacade


def pytest_configure():
    UserFacade.delete_all()
