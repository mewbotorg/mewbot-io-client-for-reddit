class TestMewbotIOAPI:
    """
    Tests the api for the mewbot-io-client-for-reddit.
    """

    @staticmethod
    def test_reddit_self_io_config_import() -> None:
        """
        Tests importing the RedditSelfIOConfig.

        :return:
        """
        from mewbot.io.client_for_reddit import RedditSelfIOConfig

        assert RedditSelfIOConfig is not None

    @staticmethod
    def test_reddit_bot_password_io_config_import() -> None:
        """
        Tests importing the RedditBotPasswordIOConfig.

        :return:
        """
        from mewbot.io.client_for_reddit import RedditBotPasswordIOConfig

        assert RedditBotPasswordIOConfig is not None

    @staticmethod
    def test_reddit_bot_oauth_io_config_import() -> None:
        """
        Tests importing the RedditBotOauthIOConfig.

        :return:
        """
        from mewbot.io.client_for_reddit import RedditBotOauthIOConfig

        assert RedditBotOauthIOConfig is not None
