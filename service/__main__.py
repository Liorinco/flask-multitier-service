from service import config


if __name__ == "__main__":
    application = config.configure_application()
    application.run()
